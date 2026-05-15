---
title: Vicious
sources: [https://spire-codex.com/api/cards/VICIOUS]
character: Ironclad
type: Power
rarity: Uncommon
cost: 1
target: Self
keywords: []
api_tags: []
wiki_stub: false
---

# Vicious

## Sources

- https://spire-codex.com/api/cards/VICIOUS

## Card Text

- Cost: 1
- Type/Rarity: Power / Uncommon
- Target: Self
- Base: Whenever you apply Vulnerable, draw 1 card.
- Upgraded: Whenever you apply Vulnerable, draw 2 cards.

## Structured Fields

| Field | Value |
|---|---|
| ID | VICIOUS |
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
| Cards drawn | 1 |
| Energy gain | — |
| HP loss | — |
| Powers applied | — |

## Upgrade And Generation Data

| Field | Value |
|---|---|
| Spawns cards | — |
| Vars | `{"Cards": 1}` |
| Upgrade | `{"cards": "+1"}` |
| Can be generated in combat | — |
| Compendium order | 57 |

---
<!-- META-AGENT NOTES — do not edit above this line -->
## Strategy Notes

<!-- Reserved for the meta-agent. Append lessons, combos, and heuristics here.
     Source facts live above the divider. -->
- 161-win signal: appears in 31.1% of final decks and is upgraded in 81.8% of final copies.
- High-priority upgrade when the deck has repeated Vulnerable applications; otherwise do not force the Vul-chain package.
- Core engine of the **Vul-Chain archetype** (20% of A10 wins). Draws 2 per Vul *application* (once per card, not per stack). Two copies = draw 4 per Vul card.
- Featured in 4 of the 5 lowest-damage Test Subject kills among A10 winners — the multi-hit + damage-mult + Vicious pattern is the sub-20-damage Test Subject formula.
- Upgraded copy is a strong Act 2 pickup when the deck already has Bash+, Thunderclap+, and Tremble.
- Do not force from zero support; Vicious becomes a centerpiece when the deck can repeatedly apply Vulnerable and use the extra draw with energy/damage payoffs.
