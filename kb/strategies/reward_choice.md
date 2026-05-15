# Reward Choice Playbook

How to decide on card rewards, shop buys, and smith targets. For per-card behavior, look up the card in `kb/cards/<color>/<card>.md` (its Strategy Notes contain pick-rate, upgrade-rate, and synergy data).

**Always read the relevant card KB files before picking, skipping, or upgrading.**

## The Core Question

For every offered card, ask: **does this solve the deck's current problem (damage, draw, energy, block, scaling, or a known boss/elite answer)?** If not, skip.

- Function first; rarity/scarcity is only a tiebreaker when function is close.
- Skipping is good when the offered cards do not improve the deck's jobs.
- Don't take a card just because it is upgraded, rare, or individually playable.

## Deck-Size Targets (Ironclad)

Practical default targets. These are the **act-end** sizes you should plan around:

| Checkpoint | Target deck size | Draft posture |
|---|---:|---|
| End Act 1 | 22 | Attack-heavy survival package online; frontload over filler |
| End Act 2 | 27 | Scaling, exhaust, block, or energy plan mostly complete |
| End Act 3 | 30 | Refine with premium cards, removals, upgrades, relics, potions |


**Above the targets:** 35+ cards needs a concrete reason — innate Apotheosis, heavy draw, transforms that replaced basics, or multiple energy tools. A 38-card winning deck is an exception, not a template.

**Letting the deck drift above the low-30s without enough draw/removal is a common mistake.** Late speculative cards can be worse than seeing Barricade, Unmovable, Body Slam, or the key draw card one turn earlier.

## Act Plan

### Act 1 — Survive

- Bias toward Attack cards and frontloaded damage. Take attacks that end fights, apply Vulnerable, provide AoE, or carry draw/tempo.
- Add Powers/draw/energy as **support**, not as substitutes for damage.
- Strong Act 1 transition picks: Pommel Strike, Anger, Tremble, Shrug It Off, Taunt.
- Skip filler even in Act 1 — the deck needs frontload and boss answers, not raw card count.

### Act 2 — Complete The Plan

- Layer in scaling, exhaust, reliable block, energy, or boss-specific answers.
- Start skipping medium cards that only duplicate jobs already covered.

### Act 3 — Refine, Skip Aggressively

- **Skip is the default for medium cards.** Once standard enemies are easy, most card rewards are liabilities because they delay drawing the deck's best engine pieces.
- A late card must scale the deck's best cards, improve access to them, or answer a boss script.
- Late-reward skip rule: ask "does this card make my best turns better or my boss engine more reliable?" Take cards that amplify existing output (Vicious for repeated Vulnerable, Body Slam for large block, Dark Embrace/Feel No Pain for exhaust, a one-card boss defense). Skip cards that merely add another medium attack/block, even if upgraded.
- In shops, compare every late card purchase against removal; if the deck already has a complete engine, removal or potion support is often better than another medium synergy card.

## Archetypes (Pick One Lane)

**Card draw/cycle is the baseline.** Pommel Strike appears in 77.6% of final winning decks, Shrug It Off 67.7%, Battle Trance 46.0%, Burning Pact 43.5%. All other archetypes layer on top.

| Archetype | Core cards | Win-set signal | Key relics |
|---|---|---|---|
| **Draw/Energy Core** | Pommel Strike, Bloodletting, Shrug It Off, Battle Trance | Highest-frequency shell: Pommel 77.6%, Bloodletting 74.5%, Shrug 67.7% | Bag of Preparation, Centennial Puzzle, Happy Flower, Lantern |
| **Exhaust / Block Value** | True Grit, Burning Pact, Feel No Pain, Fiend Fire, Second Wind | True Grit 46.6%, Burning Pact 43.5%, Feel No Pain 34.8% | Centennial Puzzle, Oddly Smooth Stone, Anchor |
| **Vul-Chain** | Vicious + Bash/Tremble/Thunderclap + Bully/Dismantle/Uppercut | Vicious 31.1%, Tremble 42.9%, Uppercut 41.6% | Bag of Marbles, Red Mask, Akabeko, Pen Nib, Strike Dummy |
| **Strength-Snowball** | Inflame, Limit Break, Demon Form, multi-hit attacks | Less universal; strong with relic support | Vajra, Akabeko, Strike Dummy |
| **Powers Stack** | Pyre, Feel No Pain, Vicious, Rupture, Dark Embrace | More conditional; often larger/slower decks | Ice Cream, War Paint, Miniature Cannon |

Vul-Chain and Strength-Snowball **sit on top of** the draw/cycle baseline — they don't replace it. Draft draw and energy first, then choose the payoff lane. See [archetypes.md](archetypes.md) for full templates.

## Smith Priorities

- **Most common smith targets** (from 161 A10 wins): Pommel Strike (102 smiths / 63.4%), Bash, True Grit, Armaments, Uppercut, Bloodletting.
- **High upgrade-rate when present**: Armaments (92.2%), True Grit (87.2%), Vicious (81.8%), Pyre (81.0%), Uppercut (80.3%), Pommel Strike (76.2%).
- **Usually lower upgrade priority**: Shrug It Off, Colossus, Blood Wall, Tremble, Headbutt. Take for base value; spend Smith charges elsewhere unless the deck has excess campfires.
- **Conditional late smiths**: Blood Wall and other base-value cards become legitimate final upgrades when boss math says the extra block crosses a multi-hit or Body Slam threshold.

## Removal And Starter Cleanup

- Act 1 removal should be balanced and synergy-aware. Do not blindly erase only Strikes or only Defends:
  - Perfected Strike or Hellraiser can make Strike density valuable.
  - Tighten-style Defend payoffs can make Defend density valuable.
- In Acts 2/3, default to erasing Strikes first (starter Attack stats fall off) unless a Strike payoff still pays for them.

## Shop Buying

- Inspect colorless and rare cards early — wide choice sets make scarcity easier to exploit.
- Still buy the card, potion, removal, or relic that best solves the run. **Card stats matter most.**
- Late shops are valid pathing defense: a boss-specific card or potion can be worth more than another random reward.

## Boss Prep Influence

At the start of each act, read the visible boss file (`kb/enemies/bosses/<boss>.md`) **before** valuing close card choices. The boss changes which packages are worth taking:

- Boss adds bad cards → exhaust tools rise in value.
- Boss taxes draw or card plays → prioritize efficient energy, retained block, packages that turn the tax into upside.
- Boss has a known one-turn check → hold defensive potions and one-card answers for that turn.

See [bosses.md](bosses.md) for the start-of-act checklist.

## Documented Synergy Pairs

- **Bloodletting + Pommel Strike + Shrug It Off** — most common three-card package.
- **Burning Pact + Feel No Pain / True Grit** — exhaust-block.
- **Shrug It Off + Colossus** — block backbone.
- **Break+ / Vulnerable burst** — Archaic Tooth turns Bash+ into Break+, makes Dominate/Bully much stronger, gives Music Box a premium first Attack.
- **Block-to-damage pivot** — Unmovable+ + Blood Wall/Anchor/Shrug enables Body Slam+ as 0-cost damage on defensive turns.
- **Retained-block engine** — Barricade + Unmovable turns Blood Wall, Impervious, Shrug It Off into a banked damage source for Body Slam.

See per-card KB files for full synergy data.

## Documented Card Warnings

Do **not** take in the wrong context (read the card KB):

- Drum of Battle
- Howl from Beyond
