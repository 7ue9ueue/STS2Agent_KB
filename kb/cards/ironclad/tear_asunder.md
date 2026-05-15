---
title: Tear Asunder
sources: [https://spire-codex.com/api/cards/TEAR_ASUNDER]
character: Ironclad
type: Attack
rarity: Rare
cost: 2
target: AnyEnemy
keywords: []
api_tags: []
wiki_stub: false
---

# Tear Asunder

## Sources

- https://spire-codex.com/api/cards/TEAR_ASUNDER

## Card Text

- Cost: 2
- Type/Rarity: Attack / Rare
- Target: AnyEnemy
- Base: Deal 5 damage. Hits an additional time for each time you lost HP this combat.
- Upgraded: Deal 7 damage. Hits an additional time for each time you lost HP this combat.

## Structured Fields

| Field | Value |
|---|---|
| ID | TEAR_ASUNDER |
| Color | ironclad |
| Type key | Attack |
| Rarity key | Rare |
| Target | AnyEnemy |
| Keywords | `[]` |
| API tags | `[]` |

## Numeric Fields

| Field | Value |
|---|---|
| Damage | 5 |
| Block | — |
| Hit count | 1 |
| Cards drawn | — |
| Energy gain | — |
| HP loss | — |
| Powers applied | — |

## Upgrade And Generation Data

| Field | Value |
|---|---|
| Spawns cards | — |
| Vars | `{"CalculationBase": 0, "CalculationExtra": 1, "Damage": 5, "Repeat": 1}` |
| Upgrade | `{"damage": "+2"}` |
| Can be generated in combat | — |
| Compendium order | 82 |

---
<!-- META-AGENT NOTES — do not edit above this line -->
## Strategy Notes

<!-- Reserved for the meta-agent. Append lessons, combos, and heuristics here.
     Source facts live above the divider. -->
- The live tooltip's "Hits N times" is the total hit count, not extra hits beyond the base; calculate damage as displayed hit count times current damage.
- In Knowledge Demon, self-damage can make Tear Asunder a major late burst card, but it may still lose to the boss's heal/upkeep clock if the deck cannot pair it with enough block and follow-up damage.
