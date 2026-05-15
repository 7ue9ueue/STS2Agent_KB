---
title: Colossal Flower
source: https://spire-codex.com/api/events
id: COLOSSAL_FLOWER
type: Event
act: Act 2 - Hive
preconditions: [Requires 19+ HP]
stub: false
---

# Colossal Flower

## Sources

- https://spire-codex.com/api/events

## Structured Fields

| Field | Value |
|---|---|
| ID | COLOSSAL_FLOWER |
| Type | Event |
| Act | Act 2 - Hive |
| Epithet | — |
| Image URL | — |

## Preconditions

- Requires 19+ HP

## Initial Options

| ID | Title | Effect |
|---|---|---|
| EXTRACT_CURRENT_PRIZE_1 | Extract Nectar | Gain 35 Gold. |
| REACH_DEEPER_1 | Reach Deeper | Enter deeper. Lose 5 HP. |

## Page Transition Options

| Page ID | Option ID | Title | Effect |
|---|---|---|---|
| INITIAL | EXTRACT_CURRENT_PRIZE_1 | Extract Nectar | Gain 35 Gold. |
| INITIAL | REACH_DEEPER_1 | Reach Deeper | Enter deeper. Lose 5 HP. |
| REACH_DEEPER_1 | EXTRACT_CURRENT_PRIZE_2 | Extract Nectar | Gain 75 Gold. |
| REACH_DEEPER_1 | REACH_DEEPER_2 | Reach Deeper | Enter even deeper. Lose 6 HP. |
| REACH_DEEPER_2 | EXTRACT_INSTEAD | Extract Nectar | Gain 135 Gold. |
| REACH_DEEPER_2 | POLLINOUS_CORE | Enter the Center | Lose 7 HP. Obtain Pollinous Core. |

## Relics

_No relic list in source record._

---
<!-- META-AGENT NOTES — do not edit above this line -->
## Strategy Notes

<!-- Reserved for the meta-agent. Append lessons, combos, and heuristics here.
     Wiki facts live above the divider. -->
