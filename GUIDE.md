# STS2 Agent Guide

This file is the **router**. It contains the agent's non-negotiable priors and points to the playbook/reference file for every decision. Detailed rules live in `kb/`. Read the playbook for the decision you are about to make.

---

## Default Run Posture

These are the highest-priority defaults. The precise decision rules live in the linked KB files.

- **Smaller deck by default.** Use the Ironclad targets from [`kb/strategies/reward_choice.md`](kb/strategies/reward_choice.md): End Act 1 around 20 cards, End Act 2 around 26, End Act 3 around 30. [`kb/strategies/deck_size.md`](kb/strategies/deck_size.md) says a card can be good and still be wrong if it delays the deck's specific answers by one turn.
- **Save/load every battle at least once when possible.** Use `save_and_quit` plus `continue` to compare at least one materially different combat line before accepting the battle outcome. [`kb/mechanics/save_and_load.md`](kb/mechanics/save_and_load.md) says to actively compare branches for HP, potion retention, and path equity; [`kb/strategies/meta_play.md`](kb/strategies/meta_play.md) says "won, but barely" is a retry signal.
- **Draft by act.** Act 1: choose more real Attack cards and frontloaded damage. Exception: if the Act 1 boss is [`Waterfall Giant`](kb/enemies/bosses/waterfall_giant.md), also draft/upgrade real defense because its KB calls it the hardest common Act 1 boss by damage and warns to plan the Steam Eruption explosion block. Act 2: complete the plan with scaling, exhaust, reliable block, energy, or boss-specific answers. Act 3: refine, skip medium cards, and take only premium or boss-solving cards. See [`kb/strategies/reward_choice.md`](kb/strategies/reward_choice.md) and [`kb/strategies/ironclad.md`](kb/strategies/ironclad.md).

---

## Core Principles (always-loaded priors)

1. **HP is a resource, not a score.** Take calculated damage to deal more. Don't waste energy on block when enemies aren't attacking.
2. **Smaller deck by default; answer density beats card count.** Skip card rewards if they do not improve access to the cards that solve the next elite/boss. A large deck of good cards can still miss Impervious, Apparition, Second Wind, Feel No Pain, or the kill package on a scripted danger turn.
3. **Act 1 front-loads damage; Waterfall Giant also demands defense; Acts 2/3 look for scaling and refinement.** Killing enemies faster means less total damage taken early, but Waterfall Giant needs real block for Steam Eruption and Death Blow planning. Later acts need scaling, exhaust, reliable block, energy, or boss-specific answers more than another medium attack.
4. **Read intents carefully.** Sleep/Buff = all-out offense. Attack = balance block and damage. Debuff = usually no damage, offense turn.
5. **Drawing cards matters.** Cycle to find key cards. Draw pile reshuffles with discard when empty.
6. **Exhausting bad cards is often good.** Removes them only for the current combat — shrinks the live deck and cycles the best cards faster.
7. **Path safety compounds.** A no-damage shop/rest branch can beat an elite branch when the deck has enough relic power. Trace the whole visible route to the boss.
8. **Smith is the default campfire action.** Rest is a survival purchase that needs concrete lethal/pathing math. Extra HP does not improve scaling; a key upgrade can shorten boss fights, improve block/draw output, and prevent more damage than the heal would restore.
9. **Function first, scarcity second.** Pick cards because they solve the deck's current act plan or scaling problem.
10. **Check the act boss.** At the start of each act, read the boss KB before pathing and card choices.
11. **Potion preservation has a floor.** Save for elites/bosses by default, but spend in hallway fights when a near-lethal sequence threatens.
12. **Current HP beats small max-HP preservation.** Losing 1–3 max HP is acceptable if it buys tempo, prevents current HP loss, kills a scaler, or turns on a key setup.
13. **Use save-and-load every battle when possible, before damage snowballs.** Compare at least one materially different line before accepting the battle outcome, especially when a line causes avoidable HP loss, spends a key potion, or harms path equity. Write the lesson to KB and replay with a corrected plan. Ancients are the exception: the harness cannot save/load branch-inspect them, so choose from visible value.
14. **HP-cost engines need a boss-entry budget.** Bloodletting, Blood Wall, Crimson Mantle, curses, and similar effects can win tempo but still lose long boss fights if the route leaves no HP margin for upkeep or forced chip.
15. **Forced elite paths need a real HP buffer.** A single strong potion can be insufficient if the deck lacks the burst/AoE/block density for the worst elite in the pool; path as if that elite appears.

---

## Decision Router

| When you need to decide... | Read this first | Then look up |
|---|---|---|
| What card to take/skip/upgrade | [`kb/strategies/reward_choice.md`](kb/strategies/reward_choice.md) | the offered cards in `kb/cards/<color>/<card>.md`; use [`kb/strategies/card_winrates.md`](kb/strategies/card_winrates.md) only as a secondary close-call signal |
| Whether the deck is getting too large | [`kb/strategies/deck_size.md`](kb/strategies/deck_size.md) | draw/exhaust/removal cards and the next elite/boss file |
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

Ironclad-specific draft shape, archetype lanes, card win-rate signals, and starter-deck nuance: [`kb/strategies/ironclad.md`](kb/strategies/ironclad.md), [`kb/strategies/reward_choice.md`](kb/strategies/reward_choice.md), and [`kb/strategies/card_winrates.md`](kb/strategies/card_winrates.md).

## Run History And Corrections

Run-specific analysis, retry lines, and correction context: `history/run<N>.md`. Reusable lessons from those runs should be promoted into the relevant playbook or entity KB Strategy Notes — do not leave run-specific evidence sprinkled in the playbooks.
