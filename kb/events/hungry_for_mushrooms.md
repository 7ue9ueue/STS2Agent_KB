---
title: Hungry for Mushrooms
source: https://spire-codex.com/api/events
id: HUNGRY_FOR_MUSHROOMS
type: Event
act: Act 3 - Glory
preconditions: []
stub: false
---

# Hungry for Mushrooms

## Sources

- https://spire-codex.com/api/events

## Structured Fields

| Field | Value |
|---|---|
| ID | HUNGRY_FOR_MUSHROOMS |
| Type | Event |
| Act | Act 3 - Glory |
| Epithet | — |
| Image URL | — |

## Preconditions

_None in source record._

## Initial Options

| ID | Title | Effect |
|---|---|---|
| BIG_MUSHROOM | Big Mushroom | Obtain Big Mushroom. Upon pickup, raise your Max HP by 20. At the start of each combat, draw 2 fewer cards. |
| FRAGRANT_MUSHROOM | Fragrant Mushroom | Obtain Fragrant Mushroom. Upon pickup, lose 15 HP and Upgrade 2 random cards. |

## Page Transition Options

| Page ID | Option ID | Title | Effect |
|---|---|---|---|
| INITIAL | BIG_MUSHROOM | Big Mushroom | Obtain Big Mushroom. Upon pickup, raise your Max HP by 20. At the start of each combat, draw 2 fewer cards. |
| INITIAL | FRAGRANT_MUSHROOM | Fragrant Mushroom | Obtain Fragrant Mushroom. Upon pickup, lose 15 HP and Upgrade 2 random cards. |

## Relics

_No relic list in source record._

---
<!-- META-AGENT NOTES — do not edit above this line -->
## Strategy Notes

<!-- Reserved for the meta-agent. Append lessons, combos, and heuristics here.
     Wiki facts live above the divider. -->
- In late Act 3, Big Mushroom's -2 opening draw is a severe boss-consistency penalty; prefer Fragrant Mushroom when current HP and upcoming recovery can absorb the 15 HP loss.
- If using save/load to inspect Fragrant Mushroom, verify upgraded cards from live save/deck data before valuing the branch; do not assume the upgrade text produced useful upgrades.
