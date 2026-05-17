---
title: Thrash
sources: [https://spire-codex.com/api/cards/THRASH]
character: Ironclad
type: Attack
rarity: Rare
cost: 1
target: AnyEnemy
keywords: []
api_tags: []
wiki_stub: false
---

# Thrash

## Sources

- https://spire-codex.com/api/cards/THRASH

## Card Text

- Cost: 1
- Type/Rarity: Attack / Rare
- Target: AnyEnemy
- Base: Deal 4 damage twice. Exhaust a random Attack in your Hand and add its damage to this card.
- Upgraded: Deal 6 damage twice. Exhaust a random Attack in your Hand and add its damage to this card.

## Structured Fields

| Field | Value |
|---|---|
| ID | THRASH |
| Color | ironclad |
| Type key | Attack |
| Rarity key | Rare |
| Target | AnyEnemy |
| Keywords | `[]` |
| API tags | `[]` |

## Numeric Fields

| Field | Value |
|---|---|
| Damage | 4 |
| Block | — |
| Hit count | 2 |
| Cards drawn | — |
| Energy gain | — |
| HP loss | — |
| Powers applied | — |

## Upgrade And Generation Data

| Field | Value |
|---|---|
| Spawns cards | — |
| Vars | `{"Damage": 4}` |
| Upgrade | `{"damage": "+2"}` |
| Can be generated in combat | — |
| Compendium order | 83 |

---
<!-- META-AGENT NOTES — do not edit above this line -->
## Strategy Notes

<!-- Reserved for the meta-agent. Append lessons, combos, and heuristics here.
     Source facts live above the divider. -->
- Boss burst payoff when the hand has a high-damage expendable Attack, but random Attack exhaust can remove key one-copy attacks; sequence after deciding which attacks are safe to lose.
- Scales with Strength and Vulnerable as a two-hit attack, so it fits Inflame/Bash/Tremble burst turns when the random exhaust target is acceptable.
- Re-check resolved damage after playing; in Doormaker Hunger/Scrutiny branches, the random exhaust can fail to create the expected burst even when the exhausted-pile tooltip later shows added damage.
