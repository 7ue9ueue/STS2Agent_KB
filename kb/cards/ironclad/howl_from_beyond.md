---
title: Howl from Beyond
sources: [https://spire-codex.com/api/cards/HOWL_FROM_BEYOND]
character: Ironclad
type: Attack
rarity: Uncommon
cost: 3
target: AllEnemies
keywords: []
api_tags: []
wiki_stub: false
---

# Howl from Beyond

## Sources

- https://spire-codex.com/api/cards/HOWL_FROM_BEYOND

## Card Text

- Cost: 3
- Type/Rarity: Attack / Uncommon
- Target: AllEnemies
- Base: Deal 16 damage to ALL enemies. At the start of your turn, if this is in your Exhaust Pile, play it.
- Upgraded: Deal 21 damage to ALL enemies. At the start of your turn, if this is in your Exhaust Pile, play it.

## Structured Fields

| Field | Value |
|---|---|
| ID | HOWL_FROM_BEYOND |
| Color | ironclad |
| Type key | Attack |
| Rarity key | Uncommon |
| Target | AllEnemies |
| Keywords | `[]` |
| API tags | `[]` |

## Numeric Fields

| Field | Value |
|---|---|
| Damage | 16 |
| Block | — |
| Hit count | — |
| Cards drawn | — |
| Energy gain | — |
| HP loss | — |
| Powers applied | — |

## Upgrade And Generation Data

| Field | Value |
|---|---|
| Spawns cards | — |
| Vars | `{"Damage": 16}` |
| Upgrade | `{"damage": "+5"}` |
| Can be generated in combat | — |
| Compendium order | 40 |

---
<!-- META-AGENT NOTES — do not edit above this line -->
## Strategy Notes

<!-- Reserved for the meta-agent. Append lessons, combos, and heuristics here.
     Source facts live above the divider. -->
- **Does NOT exhaust when played from hand** — goes to discard pile. Auto-replay only triggers when the card is in the Exhaust pile, so you must get it there via another effect (Sever Soul, Corruption-style, exhaust events).
- The combat UI may still show an Exhaust keyword; trust the observed behavior and exhaust it with another card if you need the replay engine.
- 23% pick rate among A10 winners (33% upgraded when taken). Strong AoE finisher in builds that can place it into Exhaust.
- Upgraded copies are attractive in decks with Burning Pact, True Grit+, or Fiend Fire because those cards can place Howl in Exhaust without spending 3 energy to play it first.
- When an exhaust-selection card offers Howl beside a key long-fight power, consider exhausting Howl: it preserves the power and turns on automatic AoE next turn.
- After the automatic start-of-turn play, Howl moves to discard rather than staying in Exhaust for repeated every-turn replay.
- Under Hunger/Ethereal-style effects, playing Howl from hand can place it into Exhaust, causing one automatic start-of-next-turn play.
