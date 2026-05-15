---
title: Disintegration
source: https://spire-codex.com/api/cards/DISINTEGRATION
character: Status/Curse
type: Status
rarity: Status
cost: —
target: None
keywords: []
stub: false
---

# Disintegration

## Sources

- https://spire-codex.com/api/cards/DISINTEGRATION

## Card Text

- Cost: —
- Type/Rarity: Status / Status
- Target: None
- Base: At the end of your turn, take 6 damage.

## Structured Fields

| Field | Value |
|---|---|
| ID | DISINTEGRATION |
| Color | token |
| Type key | Status |
| Rarity key | Status |
| Target | None |
| Keywords | `[]` |
| API tags | `[]` |

## Numeric Fields

| Field | Value |
|---|---|
| Damage | — |
| Block | — |
| Hit count | — |
| Cards drawn | — |
| Energy gain | — |
| HP loss | — |
| Powers applied | `[{"amount": 6, "power": "Disintegration", "power_key": "Disintegration"}]` |

## Upgrade And Generation Data

| Field | Value |
|---|---|
| Spawns cards | — |
| Vars | `{"Disintegration": 6, "DisintegrationPower": 6}` |
| Upgrade | — |
| Can be generated in combat | False |
| Compendium order | 572 |

---
<!-- META-AGENT NOTES — do not edit above this line -->
## Strategy Notes

<!-- Reserved for the meta-agent. Append lessons, combos, and heuristics here.
     Source facts live above the divider. -->
- End-of-turn damage status; unlike hand-only punishers, the listed effect does not require it to remain in hand.
- Treat repeated copies as a clock: block does not solve all status pressure if the deck cannot end the fight.
- Multiple Disintegration choices stack additively as one end-of-turn damage amount.
- Disintegration damage is blockable; Rupture only gains Strength if the end-of-turn damage actually removes HP.
- With Rupture active, unblocked Disintegration HP loss becomes recurring Strength; this can justify taking the damage curse when racing Knowledge Demon, but do not rely on it behind block.
