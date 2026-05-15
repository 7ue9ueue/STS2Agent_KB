---
title: Sword Boomerang
sources: [https://spire-codex.com/api/cards/SWORD_BOOMERANG]
character: Ironclad
type: Attack
rarity: Common
cost: 1
target: RandomEnemy
keywords: []
api_tags: []
wiki_stub: false
---

# Sword Boomerang

## Sources

- https://spire-codex.com/api/cards/SWORD_BOOMERANG

## Card Text

- Cost: 1
- Type/Rarity: Attack / Common
- Target: RandomEnemy
- Base: Deal 3 damage to a random enemy 3 times.
- Upgraded: Deal 3 damage to a random enemy 4 times.

## Structured Fields

| Field | Value |
|---|---|
| ID | SWORD_BOOMERANG |
| Color | ironclad |
| Type key | Attack |
| Rarity key | Common |
| Target | RandomEnemy |
| Keywords | `[]` |
| API tags | `[]` |

## Numeric Fields

| Field | Value |
|---|---|
| Damage | 3 |
| Block | — |
| Hit count | 3 |
| Cards drawn | — |
| Energy gain | — |
| HP loss | — |
| Powers applied | — |

## Upgrade And Generation Data

| Field | Value |
|---|---|
| Spawns cards | — |
| Vars | `{"Damage": 3, "Repeat": 3}` |
| Upgrade | `{"repeat": "+1"}` |
| Can be generated in combat | — |
| Compendium order | 18 |

---
<!-- META-AGENT NOTES — do not edit above this line -->
## Strategy Notes

<!-- Reserved for the meta-agent. Append lessons, combos, and heuristics here.
     Source facts live above the divider. -->
- Akabeko/Vigor applies to each hit; saving 8 Vigor for base Sword Boomerang adds +24 total damage (3 hits), far better than spending it on a single Strike.
- Upgrading adds a fourth hit; with Akabeko this is +32 Vigor total and 44 single-target opening damage before Vulnerable.
- Beware Strength loss: repeated Lagavulin Matriarch Soul Siphons can reduce Sword Boomerang+ to 0-damage hits, and The Boot did not rescue those 0-damage hits in live A10.
