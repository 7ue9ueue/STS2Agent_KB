---
title: Blood Wall
sources: [https://spire-codex.com/api/cards/BLOOD_WALL, https://slaythespire.wiki.gg/wiki/Slay_the_Spire_2:Blood_Wall]
character: Ironclad
type: Skill
rarity: Common
cost: 2
target: Self
keywords: []
api_tags: []
wiki_stub: false
---

# Blood Wall

## Sources

- https://spire-codex.com/api/cards/BLOOD_WALL
- https://slaythespire.wiki.gg/wiki/Slay_the_Spire_2:Blood_Wall

## Card Text

- Cost: 2
- Type/Rarity: Skill / Common
- Target: Self
- Base: Lose 2 HP. Gain 16 Block.
- Upgraded: Lose 2 HP. Gain 20 Block.

## Structured Fields

| Field | Value |
|---|---|
| ID | BLOOD_WALL |
| Color | ironclad |
| Type key | Skill |
| Rarity key | Common |
| Target | Self |
| Keywords | `[]` |
| API tags | `[]` |

## Numeric Fields

| Field | Value |
|---|---|
| Damage | — |
| Block | 16 |
| Hit count | — |
| Cards drawn | — |
| Energy gain | — |
| HP loss | 2 |
| Powers applied | — |

## Upgrade And Generation Data

| Field | Value |
|---|---|
| Spawns cards | — |
| Vars | `{"Block": 16, "HpLoss": 2}` |
| Upgrade | `{"block": "+4"}` |
| Can be generated in combat | — |
| Compendium order | 6 |

---
<!-- META-AGENT NOTES — do not edit above this line -->
## Strategy Notes

<!-- Reserved for the meta-agent. Append lessons, combos, and heuristics here.
     Wiki facts live above the divider. -->
- Large block option for elite/boss turns; its player-turn HP loss can also enable Spite.
- 161-win signal: appears in 39.8% of final decks, but direct smiths are rare (1.9% of runs); base copy is usually enough.
- An upgraded second copy is reasonable near the Act 3 boss when the deck has enough energy and needs more one-card block.
- Corruption+ removes Blood Wall's energy cost, making it a high-value free block skill; sequence it as the first block card when Vambrace is unused.
- At lethal or near-lethal HP, include the 2 HP loss in block math. Into Doormaker Scrutiny, Blood Wall plus another block card can still fail if the HP loss happens before incoming damage.
