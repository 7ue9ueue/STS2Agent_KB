---
title: Inferno
sources: [https://spire-codex.com/api/cards/INFERNO, https://slaythespire.wiki.gg/wiki/Slay_the_Spire_2:Inferno]
character: Ironclad
type: Power
rarity: Uncommon
cost: 1
target: Self
keywords: []
api_tags: []
wiki_stub: true
---

# Inferno

## Sources

- https://spire-codex.com/api/cards/INFERNO
- https://slaythespire.wiki.gg/wiki/Slay_the_Spire_2:Inferno

## Card Text

- Cost: 1
- Type/Rarity: Power / Uncommon
- Target: Self
- Base: At the start of your turn, lose 1 HP. Whenever you lose HP on your turn, deal 6 damage to ALL enemies.
- Upgraded: At the start of your turn, lose 1 HP. Whenever you lose HP on your turn, deal 9 damage to ALL enemies.

## Structured Fields

| Field | Value |
|---|---|
| ID | INFERNO |
| Color | ironclad |
| Type key | Power |
| Rarity key | Uncommon |
| Target | Self |
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
| Powers applied | `[{"amount": 6, "power": "Inferno", "power_key": "Inferno"}]` |

## Upgrade And Generation Data

| Field | Value |
|---|---|
| Spawns cards | — |
| Vars | `{"Inferno": 6, "InfernoPower": 6}` |
| Upgrade | `{"infernopower": "+3"}` |
| Can be generated in combat | — |
| Compendium order | 42 |

---
<!-- META-AGENT NOTES — do not edit above this line -->
## Strategy Notes

<!-- Reserved for the meta-agent. Append lessons, combos, and heuristics here.
     Wiki facts live above the divider. -->
- Blood Wall's HP loss triggers Inferno, turning the block card into extra damage while still covering the attack; useful in elite races when Burning Blood can refund chip.
- In low-HP boss gauntlets, count every future start-turn HP loss before playing Inferno; it can be worse than skip if the fight is already a survival check.
- Do not accept a line that survives the current attack but enters the next boss turn at 1-4 HP from Inferno ticks unless lethal or deterministic full block is already planned.
