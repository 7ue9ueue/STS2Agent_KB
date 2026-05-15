---
title: The Round Tea Party
source: https://spire-codex.com/api/events
id: ROUND_TEA_PARTY
type: Event
act: Act 3 - Glory
preconditions: [Requires 12+ HP]
stub: false
---

# The Round Tea Party

## Sources

- https://spire-codex.com/api/events

## Structured Fields

| Field | Value |
|---|---|
| ID | ROUND_TEA_PARTY |
| Type | Event |
| Act | Act 3 - Glory |
| Epithet | — |
| Image URL | — |

## Preconditions

- Requires 12+ HP

## Initial Options

| ID | Title | Effect |
|---|---|---|
| ENJOY_TEA | Enjoy Your Tea | Obtain Royal Poison. Heal to full HP. |
| PICK_FIGHT | Pick a Fight | Lose 11 HP. Obtain a random Relic. |

## Page Transition Options

| Page ID | Option ID | Title | Effect |
|---|---|---|---|
| INITIAL | ENJOY_TEA | Enjoy Your Tea | Obtain Royal Poison. Heal to full HP. |
| INITIAL | PICK_FIGHT | Pick a Fight | Lose 11 HP. Obtain a random Relic. |
| PICK_FIGHT | CONTINUE_FIGHT | Continue | — |

## Relics

_No relic list in source record._

---
<!-- META-AGENT NOTES — do not edit above this line -->
## Strategy Notes

<!-- Reserved for the meta-agent. Append lessons, combos, and heuristics here.
     Wiki facts live above the divider. -->
- Avoid Royal Poison before a boss gauntlet unless the full heal is mandatory; the repeated 4 HP loss at each combat start can cost more than the one-time 11 HP relic option.
