---
title: Spite
sources: [https://spire-codex.com/api/cards/SPITE]
character: Ironclad
type: Attack
rarity: Uncommon
cost: 0
target: AnyEnemy
keywords: []
api_tags: []
wiki_stub: false
---

# Spite

## Sources

- https://spire-codex.com/api/cards/SPITE

## Card Text

- Cost: 0
- Type/Rarity: Attack / Uncommon
- Target: AnyEnemy
- Base: Deal 5 damage. If you lost HP this turn, hits 2 times.
- Upgraded: Deal 5 damage. If you lost HP this turn, hits 3 times.

## Structured Fields

| Field | Value |
|---|---|
| ID | SPITE |
| Color | ironclad |
| Type key | Attack |
| Rarity key | Uncommon |
| Target | AnyEnemy |
| Keywords | `[]` |
| API tags | `[]` |

## Numeric Fields

| Field | Value |
|---|---|
| Damage | 5 |
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
| Vars | `{"Damage": 5, "Repeat": 2}` |
| Upgrade | `{"repeat": "+1"}` |
| Can be generated in combat | — |
| Compendium order | 50 |

---
<!-- META-AGENT NOTES — do not edit above this line -->
## Strategy Notes

<!-- Reserved for the meta-agent. Append lessons, combos, and heuristics here.
     Wiki facts live above the divider. -->
- "Lost HP this turn" means HP lost during the **current player turn** only — damage taken on the enemy's turn does NOT count for the next player turn. Spite will not double-hit on T2 from damage taken on T1 enemy phase.
- Best used after same-player-turn HP loss from cards such as Breakthrough, Brand, Blood Wall, Bloodletting, or Corrupted attacks.
- Breakthrough is a reliable same-turn enabler for Spite because its HP loss happens before Spite is played.
