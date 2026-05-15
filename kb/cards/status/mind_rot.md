---
title: Mind Rot
source: https://spire-codex.com/api/cards/MIND_ROT
character: Status/Curse
type: Status
rarity: Status
cost: —
target: None
keywords: []
stub: false
---

# Mind Rot

## Sources

- https://spire-codex.com/api/cards/MIND_ROT

## Card Text

- Cost: —
- Type/Rarity: Status / Status
- Target: None
- Base: Draw 1 fewer card each turn.

## Structured Fields

| Field | Value |
|---|---|
| ID | MIND_ROT |
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
| Powers applied | `[{"amount": 1, "power": "Mind Rot", "power_key": "MindRot"}]` |

## Upgrade And Generation Data

| Field | Value |
|---|---|
| Spawns cards | — |
| Vars | `{"MindRot": 1, "MindRotPower": 1}` |
| Upgrade | — |
| Can be generated in combat | False |
| Compendium order | 573 |

---
<!-- META-AGENT NOTES — do not edit above this line -->
## Strategy Notes

<!-- Reserved for the meta-agent. Append lessons, combos, and heuristics here.
     Source facts live above the divider. -->
- Reduces draw by 1 each turn. This attacks the Ironclad win condition directly because draw/cycle is the baseline engine.
- Prioritize removing or ending the fight before the draw penalty makes block/damage turns unreliable.
- Against Knowledge Demon, Mind Rot may be preferable to early Disintegration when HP is the limiting resource, but it still makes later block and lethal windows less reliable.
