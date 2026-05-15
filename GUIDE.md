# STS2 Agent Guide

This file is the **router**. It contains the agent's non-negotiable priors and points to the playbook/reference file for every decision. Detailed rules live in `kb/`. Read the playbook for the decision you are about to make.

---

## Core Principles (always-loaded priors)

1. **HP is a resource, not a score.** Take calculated damage to deal more. Don't waste energy on block when enemies aren't attacking.
2. **Deck quality > deck size.** Skip card rewards if nothing synergizes. A lean deck draws key cards more often.
3. **Front-load damage.** Killing enemies faster means less total damage taken.
4. **Read intents carefully.** Sleep/Buff = all-out offense. Attack = balance block and damage. Debuff = usually no damage, offense turn.
5. **Drawing cards matters.** Cycle to find key cards. Draw pile reshuffles with discard when empty.
6. **Exhausting bad cards is often good.** Removes them only for the current combat — shrinks the live deck and cycles the best cards faster.
7. **Path safety compounds.** A no-damage shop/rest branch can beat an elite branch when the deck has enough relic power. Trace the whole visible route to the boss.
8. **Rest vs Smith is math, not instinct.** Count guaranteed heals, boss relics, Fairy, potions, and the exact remaining path.
9. **Function first, scarcity second.** Pick cards because they solve the deck's current act plan or scaling problem.
10. **Check the act boss.** At the start of each act, read the boss KB before pathing and card choices.
11. **Potion preservation has a floor.** Save for elites/bosses by default, but spend in hallway fights when a near-lethal sequence threatens.
12. **Current HP beats small max-HP preservation.** Losing 1–3 max HP is acceptable if it buys tempo, prevents current HP loss, kills a scaler, or turns on a key setup.
13. **Use save-and-load before the damage snowballs.** Reload proactively when an early combat line causes giant avoidable HP loss or an event branch has high-impact unknown outcomes; write the lesson to KB and replay with a corrected plan.
14. **HP-cost engines need a boss-entry budget.** Bloodletting, Blood Wall, Crimson Mantle, curses, and similar effects can win tempo but still lose long boss fights if the route leaves no HP margin for upkeep or forced chip.

---

## Decision Router

| When you need to decide... | Read this first | Then look up |
|---|---|---|
| What card to take/skip/upgrade | [`kb/strategies/reward_choice.md`](kb/strategies/reward_choice.md) | the offered cards in `kb/cards/<color>/<card>.md` |
| What route to take on the map | [`kb/strategies/pathing.md`](kb/strategies/pathing.md) | the visible boss in `kb/enemies/bosses/<boss>.md` |
| How to play this combat turn | [`kb/strategies/combat.md`](kb/strategies/combat.md) | enemy file in `kb/enemies/`, card files in `kb/cards/` |
| Whether to fight an elite | [`kb/strategies/elites.md`](kb/strategies/elites.md) | the candidate elite in `kb/enemies/elites/` |
| How to prep for / play a boss | [`kb/strategies/bosses.md`](kb/strategies/bosses.md) | the specific boss in `kb/enemies/bosses/<boss>.md` |
| What archetype to commit to | [`kb/strategies/archetypes.md`](kb/strategies/archetypes.md) | core cards/relics in their KB files |
| Whether to reload / how to use save-and-load | [`kb/mechanics/save_and_load.md`](kb/mechanics/save_and_load.md) | [`kb/strategies/meta_play.md`](kb/strategies/meta_play.md) |
| What an event does | `kb/events/<event>.md` | — |
| What a relic / potion / status does | `kb/relics/<relic>.md`, `kb/potions/<potion>.md`, `kb/cards/status/<status>.md` | — |
| A buff/debuff/keyword | `kb/mechanics/buffs.md`, `debuffs.md`, `keywords.md` | — |

---

## Hero-Specific Notes

Ironclad-specific draft shape, archetype lanes, and starter-deck nuance: [`kb/strategies/ironclad.md`](kb/strategies/ironclad.md) and [`kb/strategies/reward_choice.md`](kb/strategies/reward_choice.md).

## Run History And Corrections

Run-specific analysis, retry lines, and correction context: `history/run<N>.md`. Reusable lessons from those runs should be promoted into the relevant playbook or entity KB Strategy Notes — do not leave run-specific evidence sprinkled in the playbooks.
