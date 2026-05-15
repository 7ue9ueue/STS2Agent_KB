---
title: Punch Off
source: https://spire-codex.com/api/events
id: PUNCH_OFF
type: Event
act: Underdocks
preconditions: []
stub: false
---

# Punch Off

## Sources

- https://spire-codex.com/api/events

## Structured Fields

| Field | Value |
|---|---|
| ID | PUNCH_OFF |
| Type | Event |
| Act | Underdocks |
| Epithet | — |
| Image URL | — |

## Preconditions

_None in source record._

## Initial Options

| ID | Title | Effect |
|---|---|---|
| NAB | Nab | Add Injury to your Deck. Obtain a random Relic. |
| I_CAN_TAKE_THEM | I Can Take Them | Fight them for Greater Rewards. |

## Page Transition Options

| Page ID | Option ID | Title | Effect |
|---|---|---|---|
| INITIAL | NAB | Nab | Add Injury to your Deck. Obtain a random Relic. |
| INITIAL | I_CAN_TAKE_THEM | I Can Take Them | Fight them for Greater Rewards. |
| I_CAN_TAKE_THEM | FIGHT | Fight | — |

## Relics

_No relic list in source record._

---
<!-- META-AGENT NOTES — do not edit above this line -->
## Strategy Notes

<!-- Reserved for the meta-agent. Append lessons, combos, and heuristics here.
     Wiki facts live above the divider. -->
- Fight option can be lethal at mid-low HP unless the deck can block 14+ or kill one Punch Construct before Fast Punch applies Weak.
