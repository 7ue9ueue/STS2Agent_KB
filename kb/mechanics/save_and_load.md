# Save And Load As A Strategic Tool

`save_and_quit` followed by main-menu `continue` reloads the current room from its starting state. In combat, this restarts the fight from turn 1 — not from the middle of the turn. Use it deliberately when a fight has lethal risk, a major potion question, a missed target-order line, an unclear sequencing puzzle, or an early line is about to create a giant HP loss.

## Properties

- **Deterministic RNG.** The same action sequence gives the same draws, generated cards, targets, and results.
- **Full room reset.** Rewards, events, shops, rest sites, and other room decisions are also revisitable; mid-room choices are not persisted after reload.
- **Event branches are inspectable.** If an event has unclear outcomes, random rewards, or high-impact costs, save/load can reveal the different possibilities before committing to the final branch.
- **Brief unstable window.** After `continue`, poll until the game state stabilizes — a brief `state_type: unknown` can appear during reload.
- **Misleading first poll.** After combat reloads, one poll can briefly report a stale "combat ended / waiting for rewards" message before the room-start combat state appears; poll again before acting on contradictory reload output.
- **Reward screen boundary.** Once combat has ended and the reward screen is active, save/load can resume the reward state rather than the fight start; branch before lethal if the goal is to improve combat HP loss or potion use.

## When To Reload

- Likely death in a fight that could have been winnable with a different plan.
- A combat line is trending toward a huge preventable HP loss, even if death is not immediate.
- An event branch has unknown or random outcomes that could materially affect HP, potions, deck quality, relics, gold, or path equity.
- Wasted rare potion or first-debuff effect.
- Wrong target order discovered after enemy intent reveals.
- Major sequencing mistake (block/offense balance, draw timing, card order).

## When NOT To Reload

- Random fishing for better RNG. RNG is deterministic — only retry **distinct lines** that change the sequence before the important random or tactical point.
- Bypassing a known bad strategic line just because it's technically survivable. If the line demonstrates a repeatable mistake (wrong target priority, overblocking, potion timing, stalling against scaling), reload **and correct the plan** before more resources are lost.

## The Correction Loop

When a strategic issue is identified mid-room:

1. Stop. Name the failed assumption out loud.
2. Reload if the room can still be restarted.
3. Write the reusable fix to the relevant KB or strategy file (and exact retry context to `history/run<N>.md`).
4. Replay with an explicit plan that prevents the same mistake.

Reusable tactical rules go in the relevant entity's KB Strategy Notes; exact retry lines and run context go in `history/run<N>.md`.

## Proactive Use

- In each battle, use save/load at least once when possible; the comparison branch should be materially different and should happen before lethal/rewards so combat HP and potion outcomes can still be improved.
- Do not wait until a line is technically dead if the current branch is already burning too much HP for the visible route or boss.
- Actively compare materially different branches for resource quality: prefer the line that exits with more HP, better potion retention, or stronger path equity, not merely the first line that wins the room.
- When comparing branches, score HP saved against potion value and future route pressure; a small HP gain is usually not worth spending a premium potion before an elite or boss unless it prevents dangerous snowballing.
- In events, inspect high-impact branches when the result is uncertain, then choose the branch that best preserves the run plan.
- Ancients cannot be save/load branch-inspected in this harness; evaluate their visible options and commit without relying on room restart.
- Still limit retries to materially different branches or action sequences; deterministic RNG means repeating the same line is not new information.
