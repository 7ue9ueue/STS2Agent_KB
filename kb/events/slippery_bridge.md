---
title: Slippery Bridge
source: https://spire-codex.com/api/events
id: SLIPPERY_BRIDGE
type: Shared
act: null
preconditions: [Floor 7+, Requires removable cards in deck]
stub: false
---

# Slippery Bridge

## Sources

- https://spire-codex.com/api/events

## Structured Fields

| Field | Value |
|---|---|
| ID | SLIPPERY_BRIDGE |
| Type | Shared |
| Act | — |
| Epithet | — |
| Image URL | — |

## Preconditions

- Floor 7+
- Requires removable cards in deck

## Initial Options

| ID | Title | Effect |
|---|---|---|
| OVERCOME | Overcome | a random Card is removed from your Deck. |
| HOLD_ON_0 | Hold On | Lose 3 HP. The card in the above option is randomized. |

## Page Transition Options

| Page ID | Option ID | Title | Effect |
|---|---|---|---|
| HOLD_ON_0 | HOLD_ON_1 | Hold On | Lose 4 HP. The card in the above option is randomized. |
| HOLD_ON_1 | HOLD_ON_2 | Hold On | Lose 5 HP. The card in the above option is randomized. |
| HOLD_ON_2 | HOLD_ON_3 | Hold On | Lose 6 HP. The card in the above option is randomized. |
| HOLD_ON_3 | HOLD_ON_4 | Hold On | Lose 7 HP. The card in the above option is randomized. |
| HOLD_ON_4 | HOLD_ON_5 | Hold On | Lose 8 HP. The card in the above option is randomized. |
| HOLD_ON_5 | HOLD_ON_6 | Hold On | Lose 9 HP. The card in the above option is randomized. |
| HOLD_ON_6 | HOLD_ON_LOOP | Hold On | Lose 10 HP. The card in the above option is randomized. |
| HOLD_ON_LOOP | HOLD_ON_LOOP | Hold On | Lose 11+ HP. The card in the above option is randomized. |
| INITIAL | OVERCOME | Overcome | a random Card is removed from your Deck. |
| INITIAL | HOLD_ON_0 | Hold On | Lose 3 HP. The card in the above option is randomized. |

## Relics

_No relic list in source record._

---
<!-- META-AGENT NOTES — do not edit above this line -->
## Strategy Notes

<!-- Reserved for the meta-agent. Append lessons, combos, and heuristics here.
     Wiki facts live above the divider. -->
- Reroll premium removals, but accept duplicate/heavy-card removals once HP costs escalate; Hold On can quickly cost more than a normal hallway hit.
