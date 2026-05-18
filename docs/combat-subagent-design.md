# Combat Subagent Design

This design lets the main gameplay agent delegate a combat playout to a child
agent, then terminates that child when the fight reaches a terminal state. It is
designed around the current STS2 MCP bridge, which controls one live game
instance through `localhost:15526`.

## Goal

Use a subagent to answer one bounded question:

> From the current combat state, can this policy/line beat the enemy, and with
> what HP/potion/card-cost outcome?

The subagent must not own route, reward, shop, event, or run-history decisions.
It returns a combat result and an action trace. The supervisor decides whether to
replay, keep, or discard the line.

## Key Constraint

The current mod exposes the live game, not an in-memory cloned combat simulator.
Two agents cannot safely play the same live combat at the same time.

That means the default implementation should be **supervised exclusive control**:

1. The supervisor creates or verifies a room-start checkpoint.
2. The supervisor grants a combat lease to one combat subagent.
3. The subagent may use `save_and_quit` plus menu `continue` inside that lease
   to test multiple lines from the room start.
4. During search, the subagent must stop before terminal actions: no confirmed
   lethal card/play, no end turn that is expected to kill the player, and no
   irreversible reward/map/event actions.
5. The supervisor watches state until ready-to-commit, win/loss, abort, timeout,
   or reload-budget exhaustion.
6. The supervisor terminates the subagent and either accepts the proposed trace,
   replays it in commit mode, or starts a new lease.

True parallel playout requires separate game processes with copied save data and
different MCP ports. That is a later mode, not the safe default.

## Components

### Combat Supervisor

Host-side orchestrator owned by the main agent.

Responsibilities:

- Acquire an exclusive gameplay lock before delegation.
- Capture the initial state signature: run id if available, floor, room type,
  player HP, potions, relics, deck count, enemy ids, enemy HP, hand, draw/discard
  counts, and combat round.
- Start the child agent with a bounded prompt, maximum action budget, maximum
  reload budget, and terminal-boundary policy.
- Poll `get_game_state(format="json")` after each child action.
- Detect terminal states.
- Kill or close the child agent at terminal state, no-progress timeout, invalid
  state, or action budget exhaustion.
- Release the gameplay lock.
- Persist the child action trace into `history/run<N>.md` or a sidecar log.

### Combat Subagent

The child agent gets narrow authority:

- It may call combat and reload tools only:
  `get_game_state`, `combat_play_card`, `combat_select_card`,
  `combat_confirm_selection`, `use_potion`, `combat_end_turn`,
  `save_and_quit`, and `menu_select("continue")`.
- It may read relevant KB files if the platform supports repository access.
- It must play one action, wait/poll, then decide the next action.
- In search mode, it must stop before actions that would intentionally win,
  lose, or commit irreversible non-combat decisions.
- It must stop immediately when the supervisor reports terminal state.
- It must return a compact result object.

It should not call map, reward, shop, rest, event, profile, or menu tools other
than `continue` after save/load. Those remain supervisor-owned.

## Terminal Detection

The supervisor, not the child, is authoritative.

Win against the enemy:

- `state_type` changes from `monster`, `elite`, or `boss` to `rewards`,
  `card_reward`, `treasure`, `map`, `event`, or another non-combat post-room
  state.
- Or all enemies in `battle.enemies` are absent/dead and the next poll confirms
  a non-combat state.

Loss:

- `state_type == "game_over"`.
- Or player HP is `0` and the next poll confirms game over.

Abort:

- `state_type` becomes `unknown` for more than a small grace window.
- A blocking overlay appears that is outside the allowed combat tools.
- No state signature changes after repeated actions/polls.
- Action budget, reload budget, turn budget, or wall-clock budget is exceeded.
- The child tries a forbidden action.

## Result Contract

The subagent returns data in this shape:

```json
{
  "status": "win | loss | abort",
  "reason": "terminal state or abort cause",
  "final_hp": 42,
  "hp_delta": -8,
  "potions_spent": ["Fire Potion"],
  "turns": 3,
  "actions": [
    {"tool": "combat_play_card", "args": {"card_index": 4, "target": "ENEMY_0"}},
    {"tool": "combat_end_turn", "args": {}}
  ],
  "notes": [
    "Killed scaler before second buff turn",
    "Potion prevented 18 damage"
  ]
}
```

The supervisor may normalize tool names and append observed state summaries after
each action.

## Search And Commit Modes

Combat delegation has two modes.

Search mode:

- The subagent may reload the room-start checkpoint and test multiple lines.
- It may mark a card, potion, or end-turn as a candidate terminal action, but
  should not execute that action.
- It returns `ready_to_commit` with the best trace and expected result.

Commit mode:

- The supervisor or subagent replays the selected trace.
- Lethal actions are allowed.
- Save/load is disabled unless the commit diverges from the expected room
  signature and must abort.

## Live Retry Flow

Use this for the current single-game setup.

1. Main agent reaches combat and reads the relevant strategy/enemy/card KB.
2. Supervisor creates or verifies a room-start checkpoint.
3. Supervisor starts child A with a prompt such as:

   ```text
   You are a combat-only STS2 subagent. Play the current fight to win with max
   HP and potion preservation. You may use save_and_quit plus continue to retry
   from room start. In search mode, stop before terminal lethal/death actions and
   return the best commit trace.
   ```

4. Child A searches lines, reloading when needed and staying before terminal
   actions.
5. Supervisor records result A.
6. If another policy is worth testing, supervisor starts child B with a
   different policy hint and a fresh reload budget.
7. Main agent chooses the best line, reloads the checkpoint if needed, and
   replays the selected action trace itself or lets a final commit child run
   under supervision.

This intentionally serializes playouts. It is slower than parallel search but
does not corrupt the live run.

## Parallel Playout Mode

For true simultaneous child agents:

1. Create one worker profile/save directory per playout.
2. Copy the current run save into each worker directory.
3. Launch one STS2 process per worker with a distinct MCP port.
4. Start one MCP server instance per port.
5. Assign each child agent one port and one save clone.
6. Kill the child agent and worker game process on terminal state.
7. Keep only the action trace/result. Never merge worker save files back into
   the real run.

This needs additional process/profile tooling and should be treated as a separate
feature because STS2 save paths and mod port configs must be isolated.

## Safety Rules

- Only one actor may send gameplay actions to a live MCP endpoint at a time.
- The supervisor owns the combat lease, reward handling, and history/KB writes.
- The child may own `save_and_quit` and menu `continue` only inside the combat
  lease.
- The child gets a hard maximum action count, reload count, turn count, and
  wall-clock timeout.
- The child is closed even after a clean win; terminal state means its authority
  is over.
- Every action must be followed by a fresh state poll. Hand indices are never
  reused across actions without re-reading state.
- A child result is advice until the supervisor commits it on the main run.

## Minimal Implementation Plan

1. Add an orchestration layer outside the game mod, preferably in the agent host
   or MCP wrapper, because subagent lifecycle is a host concern.
2. Implement a `CombatSession` state machine with states:
   `idle`, `checkpointing`, `delegated`, `terminal`, `reloading`, `committing`,
   and `aborted`.
3. Add an action gateway that rejects forbidden child actions and enforces the
   exclusive lock.
4. Add terminal and pre-terminal predicates over `get_game_state(format="json")`.
5. Add trace capture as JSONL so run-history analysis can compare tested lines.
6. Add optional cloned-process workers later for parallel playout.
