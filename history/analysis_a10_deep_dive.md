---
title: Ironclad A10 Deep Dive — Archetypes, Synergies, HP Curves
source: runs/data/ (40 successful Ironclad A10 runs from sts2.fun)
date: 2026-04-29
---

# Ironclad A10 Deep Dive

Second-pass analysis of the same 40 winning runs. Focus: archetype clustering, card co-occurrence, HP trajectory, rest-site placement, early picks, relic-archetype correlation, boss damage variance.

## A. Deck Archetype Clustering

A run can match multiple archetypes (most do). Signals:
- **Vul-Chain**: Vicious + (Bash/Tremble/Thunderclap/Squash/Molten Fist) + (Bully/Dismantle/Uppercut)
- **Strength-Snowball**: Inflame OR Limit Break OR Demon Form OR Vajra relic
- **Exhaust**: Feel No Pain OR Fiend Fire OR Sever Soul OR Dark Embrace OR Corruption
- **Block-Heavy**: Barricade OR Entrench OR Body Slam OR 3+ Defends
- **Powers Stack**: 6+ Power-type cards
- **Card-Draw**: Battle Trance OR Burning Pact OR Headbutt OR 2+ upgraded Pommel Strikes

| Archetype | Count | Avg Final HP% | Avg Deck Size |
|---|---|---|---|
| Card-Draw | 36 | 51.5% | 33.3 |
| Strength-Snowball | 20 | 46.0% | 34.0 |
| Exhaust | 17 | 44.1% | 34.3 |
| Vul-Chain | 8 | 55.0% | 32.2 |
| Block-Heavy | 7 | 59.9% | 31.9 |
| Powers Stack (≥6 Powers) | 4 | 63.1% | 51.5 |

**Overlap distribution**: 2 runs match no archetype, 5 match one, 18 match two, 9 match three, 6 match four.

**Vul-Chain breakdown** (8 runs): all 8 are also Card-Draw, 5 also Strength, 2 also Exhaust, 1 also Block. **Zero pure Vul-Chain wins.**

Interpretation:
- Card-Draw is near-universal (90% of wins).
- Powers Stack is rare but the highest-HP archetype — Power-heavy decks scale better but require larger decks (~50 cards).
- Vul-Chain is always layered on Card-Draw — it's a finisher pattern, not a complete deck.

## B. Card Co-Occurrence (Top 20 Pairs)

Among the 15 most common cards. `Co-occur` = runs containing both. `Lift` = P(both) / (P(A)×P(B)) — values >1 indicate true synergy beyond base popularity.

| # | Co-occur | Lift | Pair |
|---|---|---|---|
| 1 | 26 | 1.02 | Pommel Strike + Bloodletting |
| 2 | 26 | 0.98 | Pommel Strike + Bash |
| 3 | 26 | 0.98 | Bash + Bloodletting |
| 4 | 21 | 1.02 | Bash + Shrug It Off |
| 5 | 20 | 1.00 | Bloodletting + Shrug It Off |
| 6 | 19 | 1.03 | Pommel Strike + Colossus |
| 7 | 19 | 1.03 | Bloodletting + Colossus |
| 8 | 19 | 1.03 | Bloodletting + Tremble |
| 9 | 19 | 0.95 | Pommel Strike + Shrug It Off |
| 10 | 18 | **1.07** | Bloodletting + Dominate |
| 11 | 18 | 0.95 | Bash + Colossus |
| 12 | 18 | 0.95 | Bash + Tremble |
| 13 | 17 | **1.18** | Shrug It Off + Colossus |
| 14 | 17 | **1.12** | Bloodletting + Uppercut |
| 15 | 17 | 1.01 | Pommel Strike + Dominate |
| 16 | 17 | 0.98 | Bash + Dominate |
| 17 | 16 | **1.11** | Shrug It Off + Tremble |
| 18 | 16 | 1.05 | Pommel Strike + Uppercut |
| 19 | 16 | 1.02 | Bash + Uppercut |
| 20 | 16 | 1.00 | Pommel Strike + True Grit |

**True synergies (lift > 1.05)**:
- Shrug It Off + Colossus (1.18) — block backbone
- Bloodletting + Uppercut (1.12) — energy → big attack
- Shrug It Off + Tremble (1.11) — block + Vul setup
- Bloodletting + Dominate (1.07) — energy → control

Bash/Pommel/Bloodletting pairs are high-volume but lift ~1.0 (just both being staples).

## C. HP Curve Over Run

| Checkpoint | N | Mean HP% | Median HP% |
|---|---|---|---|
| Just before Act 1 boss | 40 | 63.0% | 63.1% |
| Start of Act 2 (post-A1-boss) | 40 | 86.6% | 86.1% |
| Start of Act 3 (post-A2-boss) | 40 | 88.9% | 88.1% |
| Just before any elite | 271 | 72.5% | 73.3% |
| Just before A3 boss #1 | 40 | 90.7% | **98.5%** |
| Just before A3 boss #2 (final) | 40 | 70.0% | 70.8% |

Key observations:
- Big jump A1-boss-prep (63%) → Act-2 start (87%): post-boss heal.
- A3 boss #1 entered near-full HP (median 98.5%) — universal pattern.
- A3 boss #1 → final boss costs ~20pp HP on average.
- **Fragile checkpoint isn't the final boss; it's between A3 boss #1 and #2.**

## D. Rest Site Placement

- Act 1 rest mode: **floor 16** (40/40 runs); top 3: 16, 11, 7
- Act 2 rest mode: **floor 32** (40/40 runs); top 3: 32, 24, 29
- Act 3 rest mode: **floor 47** (39/40 runs); top 3: 47, 40, 44
- Avg distance from any rest to next boss: 4.75 floors

Distance from LAST rest before each boss to that boss:
- Within 1 floor: 120 cases (75%)
- Within 2 floors: 40 (25%)
- 3+ floors: 0

**Rule**: Pre-boss resting is universal. The final pre-boss rest (floors 16/32/47) is taken 100% in Acts 1–2 and 97.5% in Act 3.

## E. Early Build Direction (First 5 Cards Added)

Top cards picked in first 5 non-starter additions, by frequency:

| Card | First-5 picks | Avg floor when picked-early |
|---|---|---|
| Pommel Strike | 16 | 7.9 |
| Bloodletting | 12 | 4.8 |
| Battle Trance | 9 | 6.2 |
| Anger | 8 | 4.8 |
| Blood Wall | 8 | 8.6 |
| Headbutt | 7 | 6.0 |
| Uppercut | 7 | 7.3 |
| Colossus | 6 | 3.2 |
| True Grit | 6 | 3.8 |
| Thunderclap | 6 | 4.5 |

Early picks favor cheap utility + draw (Pommel, Bloodletting, Battle Trance, Anger). Colossus and True Grit are picked extremely early (floors 3–4) — likely Neow boons or first reward.

## F. Relic-to-Archetype Correlation

For relics in ≥25% of runs (Burning Blood excluded — 100% starter):

| Relic | Overall | Vul-Chain | Strength | Exhaust | Block | Powers | Card-Draw |
|---|---|---|---|---|---|---|---|
| Vajra | 38% | 38% | **75%** | 59% | 43% | 25% | 36% |
| Potion Belt | 35% | 12% | 30% | 35% | **71%** | 50% | 39% |
| Centennial Puzzle | 35% | 38% | 25% | 47% | **71%** | 50% | 39% |
| Happy Flower | 35% | **62%** | 30% | 12% | 43% | 50% | 33% |
| Oddly Smooth Stone | 32% | 0% | 20% | 35% | 43% | **75%** | 33% |
| Bag of Marbles | 32% | **50%** | 25% | 35% | 43% | 0% | 33% |
| Red Mask | 28% | **50%** | 20% | 35% | 29% | 25% | 28% |

Top-lift relics per archetype (most over-represented):
- **Vul-Chain**: Akabeko (3.00), Pen Nib (2.00), Parrying Shield (2.00), Blood Vial (1.88), Red Mask (1.82)
- **Strength-Snowball**: Vajra (2.00), Parrying Shield (2.00), Akabeko (2.00), Meal Ticket (1.75), Amethyst Aubergine (1.75)
- **Exhaust**: Akabeko (1.88), Horn Cleat (1.76), Yummy Cookie (1.68), Venerable Tea Set (1.65), Vajra (1.57)
- **Block-Heavy**: Precarious Shears (3.43), The Chosen Cheese (2.29), Silver Crucible (2.29), Potion Belt (2.04), Centennial Puzzle (2.04)
- **Powers Stack**: Ice Cream (3.33), War Paint (2.86), Juzu Bracelet (2.86), Miniature Cannon (2.50), Oddly Smooth Stone (2.31)
- **Card-Draw**: ~1.0 lift across the board (uninformative — 36/40 runs are Card-Draw)

Interpretation:
- **Vajra** is the strongest single relic→archetype signal (75% of Strength wins).
- **Bag of Marbles** + **Red Mask** signal Vul-Chain commitment.
- **Block-Heavy** correlates with health-tools (Potion Belt, Centennial Puzzle).
- **Powers Stack** uses Ice Cream / War Paint to compensate for slow setup.

## G. Boss Damage Variance (Act 3 Bosses)

| Boss | N | Min | p25 | Median | p75 | Max |
|---|---|---|---|---|---|---|
| Test Subject | 31 | 8 | 20.0 | 34.0 | 47.0 | 70 |
| Doormaker | 25 | 6 | 22.0 | 29.0 | 47.0 | 69 |
| Queen | 21 | 3 | 15.0 | 18.0 | 32.0 | 51 |

Queen is easiest (median 18 dmg). Test Subject has highest variance — runs either crush it or take 50+.

### 5 Lowest-Damage Test Subject Kills
1. **8 dmg** (edf260f): Vicious×2, Blood Wall×2, Shrug It Off×2, Headbutt×2, Brand+Brightest Flame, Colossus, Bloodletting. Relics: Strike Dummy, Pen Nib, Juzu Bracelet, Ice Cream, Big Mushroom, Red Skull. (Vul-Chain + Powers)
2. **9 dmg** (740c555): Vicious×2, Defend×2, Taunt×2, Unrelenting×2, Cruelty, Drum of Battle, Pyre, Battle Trance, Blood Wall. Relics: Self-Forming Clay, Sand Castle, Gremlin Horn, Crossbow, Strike Dummy, Potion Belt, Kusarigama. (Power/Strength + Strike Dummy)
3. **14 dmg** (5b95dd4): Impervious×2, Shrug It Off×2, Headbutt×2, Thunderclap×2, Inflame, Pyre, Vicious, Blood Wall. Relics: Vajra, Bronze Scales, Parrying Shield, Meat Cleaver, Nunchaku. (Strength + Block)
4. **16 dmg** (e5da4a3): Battle Trance×2, Expect A Fight×2, Shrug It Off×2, Iron Wave×2, Pommel Strike×2, Setup Strike×2, Crimson Mantle, Cruelty, Vicious. Relics: Shuriken, Bag of Marbles, Pocketwatch, War Paint, Astrolabe, Kusarigama, Bread. (Multi-attack + draw)
5. **18 dmg** (53d8666): Wish×3, Defend×2, Ashen Strike×2, Inferno, Stone Armor, Unmovable. Relics: Vajra, Black Star, Sparkling Rouge, Game Piece, Centennial Puzzle. (Wish-stack)

Common thread:
- **Vicious in 4/5** of low-damage runs.
- **Strike Dummy / Pen Nib / Vajra** (damage multipliers) in 3/5.
- Multi-hit + damage-mult relic = sub-20-damage Test Subject formula.

## H. Card Reward Skip Patterns — Data Limitation

The dataset's `rewards.cards` field logs only the *picked* card per floor, not the full 3-card offering. True skip rates aren't recoverable from this JSON. Naive computation showed every offered card almost always ends up in the final deck (confirming `rewards.cards` is the take-log, not the offer-log).

To measure skip rates properly would require either:
- An `offers` field listing all 3 reward choices per floor, or
- Per-floor deck snapshots.

The boss-skip rate (53%) referenced in earlier analysis comes from `node_type=boss` floors with empty `rewards.cards` — these are floors where rewards were either skipped, were potion/gold-only, or weren't logged. The 53% is therefore an upper bound on true skip rate.
