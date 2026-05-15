# Ironclad A10 Win Analysis

Source: `runs/data/*.json`, 161 Ironclad Ascension 10 wins exported from `sts2.fun`.

Important bias: this is a winning-run corpus. It shows what winning decks contained and when cards entered those decks. It cannot by itself prove win rate, because failed runs and skipped reward options are not present.

## Run Shape

| Metric | Value |
| --- | --- |
| Runs analyzed | 161 |
| Results | 161 wins, 0 losses |
| Average deck size | 32.29 |
| Median deck size | 31 |
| Deck size range | 16-91 |
| Deck size p25/p75 | 27.0 / 34.0 |
| Average total damage taken | 381.2 |
| Median total damage taken | 384 |
| Average final HP fraction | 0.515 |
| Average combat turns | 117.7 |
| Average elites killed | 6.42 |

The normal winning deck size is around 30-35 cards. The mean is pulled upward by two very large outliers: 4014b177 (91 cards), fbce63fe (90 cards). Excluding decks above 50 cards, the average deck size is 30.4.

## Deck Size By Act

The site does not expose exact deck state at each floor. The table below uses visible card pickups from floor rewards: starter deck size 11 plus cards shown as selected through the end of each act. It does not fully account for shop/event buys, transforms, or removals, so final deck size remains the exact endpoint and act-end values are best treated as visible growth estimates.

| Act | Visible Deck Median | Visible Deck Avg | P25/P75 | Visible Adds | Known Final Cards By Act | Damage | Turns |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 19 | 18.77 | 18.0 / 20.0 | 7.77 | 14.98 | 120.1 | 41.7 |
| 2 | 24 | 24.41 | 22.0 / 26.0 | 5.64 | 20.61 | 125.3 | 36.2 |
| 3 | 27 | 27.98 | 25.0 / 31.0 | 3.57 | 24.17 | 135.8 | 39.8 |

Visible growth is front-loaded: winners add about 7.77 visible cards in Act 1, 5.64 in Act 2, and 3.57 in Act 3. Median visible deck size is 19 after Act 1, 24 after Act 2, and 27 after Act 3, while exact final median is 31.

The reconciliation gap matters: final decks average 8.12 cards that were not matched to visible reward-card pickups, and exact final deck size averages 4.32 cards above the simple visible-growth estimate. That is mostly shop/event/transform noise plus removals, so use this section for pacing, not exact card count auditing.

## Act Mix And Campfires

| Act | Top Node Mix | Card Type Mix | Rest Nodes/Run | Smiths/Run | Heals/Run | Smith Share |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | monster 4.6/run, rest 3.27/run, unknown 3.0/run, elite 2.34/run | Attack 44.0%, Skill 41.2%, Power 14.7% | 3.27 | 2.5 | 0.83 | 75.0% |
| 2 | monster 3.91/run, rest 3.07/run, unknown 2.76/run, elite 2.32/run | Skill 46.6%, Attack 28.4%, Power 20.7% | 3.07 | 2.09 | 1.02 | 67.1% |
| 3 | monster 3.66/run, rest 2.69/run, unknown 2.66/run, boss 2.0/run | Skill 53.0%, Attack 30.1%, Power 16.2% | 2.69 | 1.75 | 0.87 | 66.8% |

This matches `GUIDE.md`: campfire default is smith. Across the expanded win set, smithing is 75.0% of Act 1 campfire actions, 67.1% in Act 2, and 66.8% in Act 3. Healing is still common enough to matter, but it is the exception used to stabilize pathing, not the baseline plan.

Card mix shifts by act. Act 1 is balanced between attacks and skills, which fits the need to build damage plus draw/block immediately. Acts 2 and 3 skew more heavily toward skills, which suggests winners spend later picks on consistency, block, exhaust, and utility rather than raw attacks.

Most common smith targets:

| Card | Smiths | Pct Runs |
| --- | --- | --- |
| Pommel Strike | 102 | 63.4% |
| Bash | 46 | 28.6% |
| True Grit | 44 | 27.3% |
| Armaments | 44 | 27.3% |
| Uppercut | 44 | 27.3% |
| Bloodletting | 37 | 23.0% |
| Vicious | 33 | 20.5% |
| Battle Trance | 32 | 19.9% |
| Pyre | 28 | 17.4% |
| Feel No Pain | 25 | 15.5% |
| Expect A Fight | 24 | 14.9% |
| Stoke | 24 | 14.9% |
| Burning Pact | 22 | 13.7% |
| Dominate | 20 | 12.4% |
| Stampede | 18 | 11.2% |

`Pommel Strike` is the standout upgrade target in the larger set. That lines up with the card-frequency data: winners not only take it often, they spend campfires making it draw two.

## Encounters And Relics

Hardest common encounters by average damage taken:

| Encounter | Runs | Avg Damage | Median Damage | Avg Turns |
| --- | --- | --- | --- | --- |
| Waterfall Giant (Boss) | 31 | 39.4 | 38 | 10.1 |
| Kaiser Crab (Boss) | 44 | 38.9 | 36.5 | 7.1 |
| Vantom (Boss) | 22 | 36.1 | 39.0 | 8 |
| The Kin (Boss) | 24 | 35.9 | 33.0 | 8.1 |
| Test Subject (Boss) | 115 | 34.9 | 31 | 8.9 |
| Doormaker (Boss) | 100 | 31.3 | 29.5 | 7.3 |
| Queen (Boss) | 107 | 30.6 | 25.5 | 7.0 |
| Knowledge Demon (Boss) | 62 | 30.4 | 29 | 6.7 |
| The Insatiable (Boss) | 55 | 28.9 | 27 | 6.7 |
| Ceremonial Beast (Boss) | 23 | 26.5 | 27.5 | 7.8 |
| Soul Fysh (Boss) | 31 | 25.5 | 22 | 8.9 |
| Skulking Colony (Elite) | 64 | 24.1 | 22.0 | 6.5 |
| Lagavulin Matriarch (Boss) | 30 | 23.5 | 25.0 | 8.3 |
| Decimillipede (Elite) | 121 | 22.7 | 20.5 | 4.5 |
| Byrdonis (Elite) | 53 | 21.5 | 20 | 3.8 |

Most frequent relic rewards:

| Relic | Runs | Pct Runs |
| --- | --- | --- |
| Bag Of Preparation | 54 | 33.5% |
| Centennial Puzzle | 51 | 31.7% |
| Happy Flower | 50 | 31.1% |
| Vajra | 47 | 29.2% |
| Strike Dummy | 47 | 29.2% |
| Pendulum | 46 | 28.6% |
| Anchor | 46 | 28.6% |
| Oddly Smooth Stone | 46 | 28.6% |
| Strawberry | 42 | 26.1% |
| Lantern | 41 | 25.5% |
| Gorget | 40 | 24.8% |
| Bronze Scales | 40 | 24.8% |
| War Paint | 38 | 23.6% |
| Whetstone | 38 | 23.6% |
| Blood Vial | 37 | 23.0% |

## Most Chosen Cards And Timing

| Card | Picks | Runs | Avg Floor | Act 1 | Act 2 | Act 3 |
| --- | --- | --- | --- | --- | --- | --- |
| Pommel Strike | 189 | 117 (72.7%) | 22.49 | 70 | 69 | 50 |
| Shrug It Off | 132 | 94 (58.4%) | 23.2 | 45 | 44 | 43 |
| Bloodletting | 115 | 91 (56.5%) | 20.86 | 50 | 35 | 30 |
| Battle Trance | 76 | 63 (39.1%) | 20.71 | 35 | 23 | 18 |
| True Grit | 71 | 60 (37.3%) | 21.56 | 31 | 18 | 22 |
| Blood Wall | 69 | 60 (37.3%) | 19.46 | 35 | 18 | 16 |
| Tremble | 69 | 59 (36.6%) | 21.86 | 28 | 23 | 18 |
| Colossus | 67 | 51 (31.7%) | 23.27 | 26 | 21 | 20 |
| Headbutt | 67 | 64 (39.8%) | 18.07 | 39 | 14 | 14 |
| Dominate | 63 | 56 (34.8%) | 23.02 | 23 | 23 | 17 |
| Feel No Pain | 59 | 49 (30.4%) | 23.8 | 16 | 31 | 12 |
| Burning Pact | 58 | 54 (33.5%) | 27.24 | 17 | 19 | 22 |
| Uppercut | 58 | 54 (33.5%) | 18.5 | 31 | 12 | 15 |
| Taunt | 51 | 47 (29.2%) | 19.73 | 22 | 18 | 11 |
| Vicious | 49 | 38 (23.6%) | 24.39 | 16 | 20 | 13 |
| Offering | 49 | 44 (27.3%) | 25.84 | 20 | 27 | 2 |
| Evil Eye | 47 | 40 (24.8%) | 24.13 | 13 | 22 | 12 |
| Molten Fist | 47 | 37 (23.0%) | 18.21 | 24 | 17 | 6 |

High-confidence staples from this corpus:

- `Pommel Strike`: 189 visible picks, 117 pick-runs, 125 final decks, avg pick floor 22.49. It remains the default repeatable attack/draw card.
- `Bloodletting`: 115 visible picks, 91 pick-runs, 120 final decks, avg pick floor 20.86. It is still a top-tier energy/tempo card, but the larger sample puts it behind `Pommel Strike` and `Shrug It Off` in visible pick count.
- `Shrug It Off`: 132 visible picks, 94 pick-runs, 109 final decks, avg pick floor 23.2. The expanded sample makes this look even more important than the first 40-run read.
- `True Grit`, `Battle Trance`, `Burning Pact`, `Blood Wall`, `Tremble`, `Uppercut`, `Dominate`, and `Headbutt` round out the repeated core. The pattern is draw/energy plus efficient block, not pure damage.

## Final Deck Frequency

| Card | Runs | Copies | Avg Copies | Upgraded Copies |
| --- | --- | --- | --- | --- |
| Pommel Strike | 125 (77.6%) | 223 | 1.78 | 170 (76.2%) |
| Bloodletting | 120 (74.5%) | 165 | 1.38 | 89 (53.9%) |
| Shrug It Off | 109 (67.7%) | 181 | 1.66 | 68 (37.6%) |
| True Grit | 75 (46.6%) | 94 | 1.25 | 82 (87.2%) |
| Battle Trance | 74 (46.0%) | 95 | 1.28 | 53 (55.8%) |
| Burning Pact | 70 (43.5%) | 79 | 1.13 | 43 (54.4%) |
| Tremble | 69 (42.9%) | 86 | 1.25 | 28 (32.6%) |
| Uppercut | 67 (41.6%) | 76 | 1.13 | 61 (80.3%) |
| Dominate | 67 (41.6%) | 81 | 1.21 | 34 (42.0%) |
| Headbutt | 67 (41.6%) | 76 | 1.13 | 27 (35.5%) |
| Blood Wall | 64 (39.8%) | 79 | 1.23 | 26 (32.9%) |
| Colossus | 62 (38.5%) | 87 | 1.4 | 25 (28.7%) |
| Feel No Pain | 56 (34.8%) | 74 | 1.32 | 39 (52.7%) |
| Taunt | 56 (34.8%) | 63 | 1.12 | 37 (58.7%) |
| Armaments | 56 (34.8%) | 64 | 1.14 | 59 (92.2%) |
| Vicious | 50 (31.1%) | 66 | 1.32 | 54 (81.8%) |
| Offering | 47 (29.2%) | 55 | 1.17 | 22 (40.0%) |
| Evil Eye | 46 (28.6%) | 58 | 1.26 | 17 (29.3%) |
| Flame Barrier | 46 (28.6%) | 49 | 1.07 | 30 (61.2%) |
| Expect A Fight | 45 (28.0%) | 56 | 1.24 | 41 (73.2%) |

This is the most practical draft signal: cards that remain in final winning decks after removals, shops, events, and upgrades. The top tier is very stable: `Pommel Strike`, `Bloodletting`, and `Shrug It Off` appear in at least two thirds of wins.

## Combos That Look Good

Common three-card packages:

| Package | Runs | Avg Damage | Damage vs All Wins | Avg Final HP | Avg Turns |
| --- | --- | --- | --- | --- | --- |
| Bloodletting + Pommel Strike + Shrug It Off | 68 | 381.3 | 0.1 | 0.528 | 114.4 |
| Battle Trance + Bloodletting + Pommel Strike | 47 | 391.3 | 10.1 | 0.465 | 114.2 |
| Bloodletting + Colossus + Pommel Strike | 44 | 384.4 | 3.2 | 0.544 | 116.2 |
| Bloodletting + Headbutt + Pommel Strike | 44 | 399.8 | 18.6 | 0.493 | 117.1 |
| Bloodletting + Dominate + Pommel Strike | 43 | 378.0 | -3.2 | 0.522 | 116 |
| Bloodletting + Pommel Strike + True Grit | 43 | 387.4 | 6.3 | 0.525 | 118.5 |
| Bloodletting + Shrug It Off + True Grit | 43 | 387.9 | 6.7 | 0.527 | 117.0 |
| Bloodletting + Pommel Strike + Uppercut | 42 | 391.3 | 10.1 | 0.523 | 117.5 |
| Bloodletting + Pommel Strike + Tremble | 42 | 397.2 | 16.1 | 0.52 | 118.2 |
| Bloodletting + Blood Wall + Pommel Strike | 41 | 386.3 | 5.1 | 0.496 | 114.8 |
| Battle Trance + Bloodletting + Shrug It Off | 41 | 391.3 | 10.1 | 0.494 | 113.2 |
| Headbutt + Pommel Strike + Shrug It Off | 40 | 376.1 | -5.1 | 0.506 | 114.7 |
| Bloodletting + Burning Pact + Pommel Strike | 40 | 377.4 | -3.7 | 0.481 | 116.6 |
| Battle Trance + Pommel Strike + Shrug It Off | 40 | 382.7 | 1.5 | 0.49 | 113.7 |

Efficient repeated two-card pairs with at least 20 runs:

| Pair | Runs | Avg Damage | Damage vs All Wins | Avg Final HP | Avg Turns |
| --- | --- | --- | --- | --- | --- |
| Shrug It Off + Unmovable | 22 | 344.7 | -36.5 | 0.569 | 115.6 |
| Burning Pact + Colossus | 22 | 351.5 | -29.7 | 0.58 | 114.9 |
| Anger + Burning Pact | 20 | 352.1 | -29.1 | 0.607 | 115.6 |
| Dominate + Evil Eye | 23 | 352.2 | -29.0 | 0.563 | 107.3 |
| Burning Pact + Taunt | 27 | 353.7 | -27.5 | 0.545 | 119.7 |
| Colossus + Taunt | 24 | 355.6 | -25.6 | 0.588 | 114.2 |
| Burning Pact + Feel No Pain | 28 | 355.8 | -25.4 | 0.56 | 118.6 |
| Burning Pact + True Grit | 33 | 356.9 | -24.2 | 0.548 | 125.5 |
| Dominate + Feel No Pain | 28 | 357.5 | -23.7 | 0.543 | 115.3 |
| Bloodletting + Drum Of Battle | 20 | 358.7 | -22.5 | 0.592 | 115 |
| Battle Trance + Evil Eye | 22 | 358.9 | -22.3 | 0.562 | 114.9 |
| Armaments + Dominate | 22 | 359.7 | -21.5 | 0.543 | 111.7 |
| Colossus + Expect A Fight | 20 | 360.7 | -20.5 | 0.533 | 120.2 |
| Burning Pact + Forgotten Ritual | 25 | 361.0 | -20.1 | 0.585 | 116.5 |

The cleanest repeated shell is draw plus block plus cheap damage:

- The most repeated packages are no longer just attack shells; the larger sample heavily favors `Bloodletting`, `Pommel Strike`, and `Shrug It Off` combinations.
- `Bloodletting + Pommel Strike + Shrug It Off` is the highest-frequency three-card package. It is the practical baseline: energy/draw, attack/draw, and block/draw.
- `Headbutt` still pairs well with the common shell because it recycles the best upgraded attacks and draw cards.
- Exhaust/value packages show up through `True Grit`, `Burning Pact`, `Feel No Pain`, `Second Wind`, and `Fiend Fire`, but they are less universal than the Pommel/Bloodletting/block shell.

## Cards To Treat Carefully

Because the corpus contains only wins, this section means `weaker or more conditional signal among wins`, not `proven bad card`.

| Card | Runs | Avg Damage | Damage vs All Wins | Avg Final HP | Avg Turns |
| --- | --- | --- | --- | --- | --- |
| Dramatic Entrance | 6 | 444.3 | 63.1 | 0.635 | 120.7 |
| Feed | 17 | 431.4 | 50.2 | 0.539 | 123 |
| Wish | 9 | 427.1 | 45.9 | 0.315 | 118.2 |
| Not Yet | 16 | 422.1 | 40.9 | 0.642 | 119.1 |
| Rampage | 9 | 420.4 | 39.3 | 0.415 | 131 |
| Apotheosis | 8 | 414.2 | 33.1 | 0.577 | 121.6 |
| Bludgeon | 19 | 412.8 | 31.6 | 0.516 | 116.7 |
| Pyre | 40 | 411.9 | 30.7 | 0.461 | 123.8 |
| Flame Barrier | 46 | 410.4 | 29.2 | 0.463 | 124.2 |
| Pacts End | 17 | 408.1 | 26.9 | 0.545 | 124.9 |
| Sword Boomerang | 17 | 407.4 | 26.2 | 0.411 | 116.7 |
| Breakthrough | 24 | 406.7 | 25.5 | 0.369 | 112 |
| Tear Asunder | 17 | 406.5 | 25.3 | 0.479 | 109.3 |
| Master Of Strategy | 6 | 406.3 | 25.1 | 0.409 | 118.2 |

Cautions from the win set:

- Cards in this table are not automatically bad. Many are chosen when a deck is already under pressure or needs a specific answer.
- `Perfected Strike` remains the cleanest example of an Act 1 bridge: it is picked much more often than it survives as a central endgame card.
- Damage-only attacks with weaker draw/block contribution should be treated as context picks unless the deck has clear relic or Vulnerable support.

## Draft Rules Suggested By These Wins

1. Prioritize `Pommel Strike` early and accept duplicates. Winning decks averaged 1.78 copies when present.
2. Take `Bloodletting` highly. It appears in 74.5% of final decks and supports larger decks without losing tempo.
3. Build block with cantrip/scaling pieces instead of pure defense only: `Shrug It Off`, `Blood Wall`, `True Grit`, `Dominate`, `Tremble`, and `Colossus` are repeated names.
4. Add draw/exhaust once the deck has enough payoff. `Battle Trance`, `Offering`, `Burning Pact`, `Feel No Pain`, `Second Wind`, and `Fiend Fire` are the package to watch.
5. Treat Act 1 as the main deck-building window. The visible growth estimate adds roughly eight cards in Act 1, then slows each act. By Act 3, winners are much more selective.

## Data Limitations

- The run exports include chosen cards and final decks, but not the full reward screens. A card missing from the data may have been offered and skipped.
- Shop purchases and event transforms are imperfectly observable from floor rewards; final deck frequency is therefore more reliable than pick source for those cards.
- All runs are wins. The next useful comparison is a matched loss/failure set to identify overpicked cards, failed archetypes, and deck-size thresholds that stop working.

## Generated Tables

- `run_summary.csv`: one row per run.
- `card_pick_timing.csv`: chosen-card counts and floor/act timing.
- `final_deck_card_frequency.csv`: final-deck card frequency and upgrade rates.
- `card_performance_winset.csv`: present-card averages within the win corpus.
- `card_pair_cooccurrence.csv`: common final-deck card pairs.
- `card_package_cooccurrence.csv`: common final-deck three-card packages.
- `act_summary.csv`: act-level visible deck growth, damage, turns, elites, rests, smiths, heals, relics.
- `act_card_type_mix.csv`: visible picked-card type mix by act.
- `node_mix_by_act.csv`: node distribution by act.
- `campfire_usage.csv`: smith/heal split by act.
- `smith_targets.csv`: most common cards upgraded at campfires.
- `relic_frequency.csv`: relic appearance frequency in the win set.
- `encounter_summary.csv`: damage and turns by encounter.
