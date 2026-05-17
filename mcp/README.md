# MCP Tools

## Tool Transcript Logging

The MCP bridge can write a JSONL transcript of every HTTP request it sends to
the STS2 mod, including read-only `get_game_state` calls and mutating actions.
Enable it with environment variables when starting the MCP server:

```bash
STS2_TOOL_LOG=1 STS2_TOOL_LOG_RUN=run20 uv run --directory /path/to/STS2_MCP/mcp python server.py
```

By default, logs are written under `history/tool_logs/`:

```text
history/tool_logs/<local-run-or-run-id-or-session>.jsonl
```

Each line contains a timestamp, session id, sequence number, inferred MCP tool
name, optional run linkage fields, request params/body, status, duration, and
response text. For live local runs, set `STS2_TOOL_LOG_RUN=run<N>` so the log
pairs with `history/run<N>.md` and `history/run<N>_strategy.md`:

```bash
STS2_TOOL_LOG=1 \
STS2_TOOL_LOG_RUN=run20 \
STS2_TOOL_LOG_DETAIL=summary \
STS2_TOOL_LOG_MAX_RESPONSE_BYTES=50000 \
uv run --directory /path/to/STS2_MCP/mcp python server.py
```

`STS2_TOOL_LOG_DETAIL=full` logs raw responses. `STS2_TOOL_LOG_DETAIL=summary`
keeps mutating action responses full, but replaces singleplayer/multiplayer
`get_game_state` responses with compact `response_summary` objects plus the
original response byte count.

The playing agent can also set or change the active log name at runtime:

```text
set_tool_log_run(local_run="run21")
set_tool_log_detail(detail="summary")
```

After that call, subsequent transcript events are written to:

```text
history/tool_logs/run21.jsonl
```

Useful variables:

| Variable | Description |
|---|---|
| `STS2_TOOL_LOG` | Set to `1`, `true`, `yes`, or `on` to enable logging |
| `STS2_TOOL_LOG_RUN` | Optional local run key such as `run20`; used in events and default file name |
| `STS2_TOOL_LOG_RUN_ID` | Optional secondary run id; used in events and default file name if `STS2_TOOL_LOG_RUN` is unset |
| `STS2_TOOL_LOG_PATH` | Optional explicit JSONL output path |
| `STS2_TOOL_LOG_SESSION` | Optional session id written into each event |
| `STS2_TOOL_LOG_DETAIL` | `full` for raw responses, or `summary`/`thin` for compact state-read responses |
| `STS2_TOOL_LOG_MAX_RESPONSE_BYTES` | Optional response truncation limit; `0` or unset means full response |
| `STS2_TOOL_LOG_MAX_REQUEST_BYTES` | Optional request truncation limit; `0` or unset means full request |

The MCP process must be restarted after changing these variables. Existing game
runs can continue because the logger only changes the bridge process, not the
game mod.

## Singleplayer

| Tool | Scope | Description |
|---|---|---|
| `set_tool_log_run(local_run, run_id?)` | Logger | Set the active transcript log target, e.g. `history/tool_logs/run20.jsonl` |
| `get_tool_log_status()` | Logger | Show whether transcript logging is enabled and where it writes |
| `set_tool_log_detail(detail)` | Logger | Switch between `full` and `summary`/`thin` transcript detail |
| `get_game_state(format?)` | General | Get current game state (`markdown` or `json`) |
| `menu_select(option, seed?)` | General | Select a visible menu/game-over option |
| `save_and_quit()` | General | Save the current singleplayer run and return to the main menu |
| `get_profile()` | Profiles | Get active profile progress |
| `list_profiles()` | Profiles | List profile slots and active slot |
| `switch_profile(profile_id)` | Profiles | Switch to a profile slot through the game UI |
| `delete_profile(profile_id)` | Profiles | Delete an inactive profile slot |
| `use_potion(slot, target?)` | General | Use a potion (works in and out of combat) |
| `discard_potion(slot)` | General | Discard a potion to free up the slot |
| `proceed_to_map()` | General | Proceed from rewards/rest site/shop/treasure to the map |
| `combat_play_card(card_index, target?)` | Combat | Play a card from hand |
| `combat_end_turn()` | Combat | End the current turn |
| `combat_select_card(card_index)` | Combat Selection | Select a card from hand during exhaust/discard prompts |
| `combat_confirm_selection()` | Combat Selection | Confirm the in-combat card selection |
| `rewards_claim(reward_index)` | Rewards | Claim a reward from the post-combat screen |
| `rewards_pick_card(card_index)` | Rewards | Select a card from the card reward screen |
| `rewards_skip_card()` | Rewards | Skip the card reward |
| `map_choose_node(node_index)` | Map | Choose a map node to travel to |
| `rest_choose_option(option_index)` | Rest Site | Choose a rest site option (rest, smith, etc.) |
| `shop_purchase(item_index)` | Shop | Purchase an item from the shop |
| `event_choose_option(option_index)` | Event | Choose an event option (including Proceed) |
| `event_advance_dialogue()` | Event | Advance ancient event dialogue |
| `deck_select_card(card_index)` | Card Select | Pick/toggle a card in the selection screen |
| `deck_confirm_selection()` | Card Select | Confirm the current card selection |
| `deck_cancel_selection()` | Card Select | Cancel/skip card selection |
| `bundle_select(bundle_index)` | Bundle Select | Open a bundle preview |
| `bundle_confirm_selection()` | Bundle Select | Confirm the current bundle preview |
| `bundle_cancel_selection()` | Bundle Select | Cancel the current bundle preview |
| `relic_select(relic_index)` | Relic Select | Choose a relic from the selection screen |
| `relic_skip()` | Relic Select | Skip relic selection |
| `treasure_claim_relic(relic_index)` | Treasure | Claim a relic from the treasure chest |
| `crystal_sphere_set_tool(tool)` | Crystal Sphere | Switch the active divination tool |
| `crystal_sphere_click_cell(x, y)` | Crystal Sphere | Click a hidden cell in the grid |
| `crystal_sphere_proceed()` | Crystal Sphere | Continue after the minigame finishes |

## Multiplayer

All multiplayer tools are prefixed with `mp_`. They route through `/api/v1/multiplayer` and are only available during multiplayer (co-op) runs. The endpoints automatically guard against cross-mode calls.

| Tool | Scope | Description |
|---|---|---|
| `mp_get_game_state(format?)` | General | Get multiplayer game state (all players, votes, bids) |
| `mp_combat_play_card(card_index, target?)` | Combat | Play a card from the local player's hand |
| `mp_combat_end_turn()` | Combat | Submit end-turn vote (turn ends when all players submit) |
| `mp_combat_undo_end_turn()` | Combat | Retract end-turn vote |
| `mp_use_potion(slot, target?)` | General | Use a potion from the local player's slots |
| `mp_discard_potion(slot)` | General | Discard a potion from the local player's slots |
| `mp_proceed_to_map()` | General | Proceed from current screen to the map |
| `mp_map_vote(node_index)` | Map | Vote for a map node (travel when all agree) |
| `mp_event_choose_option(option_index)` | Event | Vote for / choose an event option |
| `mp_event_advance_dialogue()` | Event | Advance ancient event dialogue |
| `mp_rest_choose_option(option_index)` | Rest Site | Choose a rest site option (per-player, no vote) |
| `mp_shop_purchase(item_index)` | Shop | Purchase an item (per-player inventory) |
| `mp_rewards_claim(reward_index)` | Rewards | Claim a post-combat reward |
| `mp_rewards_pick_card(card_index)` | Rewards | Select a card from the card reward screen |
| `mp_rewards_skip_card()` | Rewards | Skip the card reward |
| `mp_deck_select_card(card_index)` | Card Select | Pick/toggle a card in the selection screen |
| `mp_deck_confirm_selection()` | Card Select | Confirm the current card selection |
| `mp_deck_cancel_selection()` | Card Select | Cancel/skip card selection |
| `mp_bundle_select(bundle_index)` | Bundle Select | Open a bundle preview |
| `mp_bundle_confirm_selection()` | Bundle Select | Confirm the current bundle preview |
| `mp_bundle_cancel_selection()` | Bundle Select | Cancel the current bundle preview |
| `mp_combat_select_card(card_index)` | Combat Selection | Select a card during in-combat selection prompts |
| `mp_combat_confirm_selection()` | Combat Selection | Confirm in-combat card selection |
| `mp_relic_select(relic_index)` | Relic Select | Choose a relic from the selection screen |
| `mp_relic_skip()` | Relic Select | Skip relic selection |
| `mp_treasure_claim_relic(relic_index)` | Treasure | Bid on a relic (relic fight if contested) |
| `mp_crystal_sphere_set_tool(tool)` | Crystal Sphere | Switch the active divination tool |
| `mp_crystal_sphere_click_cell(x, y)` | Crystal Sphere | Click a hidden cell in the grid |
| `mp_crystal_sphere_proceed()` | Crystal Sphere | Continue after the minigame finishes |
