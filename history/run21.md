# Run 21

- Date: 2026-05-15
- Character: Ironclad
- Ascension: 10
- Outcome: In progress

## Pre-run Reads

- Read `GUIDE.md`.
- Read all strategy playbooks in `kb/strategies/`: `_index.md`, `archetypes.md`, `bosses.md`, `card_impressions.md`, `combat.md`, `elites.md`, `ironclad.md`, `meta_play.md`, `pathing.md`, and `reward_choice.md`.

## Floor 1 - Neow

- Current HP/status: 64/80 HP, 99 gold, no potions, Burning Blood.
- Entity KB read: `kb/enemies/ancients/neow.md`, `kb/relics/hefty_tablet.md`, `kb/relics/phial_holster.md`, `kb/cards/colorless/neow_s_fury.md`, `kb/cards/status/injury.md`.
- Decision: chose Hefty Tablet over Neow's Torment and Phial Holster.
- Reason: Hefty Tablet gives a controlled rare choice with higher run-defining upside than one Neow's Fury or two unknown potions, despite adding Injury.
- Card KB read: `kb/cards/ironclad/primal_force.md`, `kb/cards/ironclad/pacts_end.md`, `kb/cards/ironclad/stoke.md`.
- Decision: picked Primal Force over Pact's End and Stoke.
- Reason: Primal Force immediately converts starter Attacks into 16-damage Giant Rocks for Act 1. Pact's End KB says it is a bad Neow rare for a plain starter deck without exhaust, and Stoke is too random for the opening fights.

## Floor 1 - Pathing

- Current HP/status: 64/80 HP, 99 gold, no potions, Burning Blood + Hefty Tablet.
- Strategy files read: `kb/strategies/pathing.md`, live `history/run21_strategy.md`.
- Entity KB read: `kb/enemies/bosses/vantom.md`.
- Boss note: Vantom has 9 Slippery stacks, fixed attacks into a T3 30-damage Dismember at A10, and adds Wounds; the deck needs early hits plus block/draw before the boss.
- Decision: chose next node [0], Monster at (1,1).
- Reason: left route gives early card rewards and broad branches to rest sites while avoiding a forced elite. The right route forces four early combats into a rest and then an elite, too risky with no potion and an Injury.

## Floor 2 - Slimes

- Current HP/status: entered at 64/80 HP, no potions.
- Strategy file read: `kb/strategies/combat.md` was part of pre-run reads; combat followed one-action polling.
- Entity KB read: `kb/enemies/overgrowth/slimes.md`.
- Combat: killed Twig Slime (S) first to stop immediate damage, then used Primal Force to convert two Strikes into Giant Rocks and kill Twig Slime (M). Blocked the remaining Leaf Slime attack, then finished with Bash + Strike.
- Result: took 0 damage and healed to 70/80 from Burning Blood.
- Reward strategy read: `kb/strategies/reward_choice.md`, live `history/run21_strategy.md`.
- Card KB read: `kb/cards/ironclad/bloodletting.md`, `kb/cards/ironclad/setup_strike.md`, `kb/cards/ironclad/feel_no_pain.md`.
- Decision: picked Bloodletting over Setup Strike and Feel No Pain; claimed 10 gold.
- Reason: Bloodletting fits the high-frequency draw/energy shell and helps pay for Primal Force turns. Feel No Pain needs more exhaust support first, while Setup Strike is medium frontload and can be overwritten by Primal Force.

## Floor 2 - Pathing

- Current HP/status: 70/80 HP, 109 gold, no potions.
- Strategy files read: `kb/strategies/pathing.md`, live `history/run21_strategy.md`.
- Entity KB read: `kb/enemies/bosses/vantom.md`.
- Decision: chose next node [0], Monster at (0,2).
- Reason: the deck still needs early Act 1 card rewards, and the left branch preserves rest-site access without forcing the floor-6 elite.

## Floor 3 - Shrinker Beetle

- Current HP/status: entered at 70/80 HP, 109 gold, no potions.
- Entity KB read: `kb/enemies/overgrowth/shrinker_beetle.md`.
- Combat: used Bloodletting on the opening debuff turn to play Bash + two Strikes before Shrink reduced attack damage. On turn 2, Primal Force turned three Strikes into Giant Rocks; one Vulnerable Giant Rock finished the Beetle.
- Result: Bloodletting cost 3 HP, took no attack damage, ended at 73/80 after Burning Blood.
- Reward strategy read: `kb/strategies/reward_choice.md`, live `history/run21_strategy.md`.
- Card KB read: `kb/cards/ironclad/shrug_it_off.md`, `kb/cards/ironclad/cinder.md`, `kb/cards/ironclad/true_grit.md`.
- Potion KB read: `kb/potions/speed_potion.md`.
- Decision: picked True Grit over Shrug It Off and Cinder; claimed Speed Potion and 11 gold.
- Reason: True Grit directly answers Injury and Vantom's future Wounds once upgraded, and it opens the exhaust/block lane. Shrug It Off was strong but less specific to the run's curse/status problem; Cinder added damage but random exhaust risk.

## Floor 3 - Pathing

- Current HP/status: 73/80 HP, 120 gold, Speed Potion.
- Strategy files read: `kb/strategies/pathing.md`, live `history/run21_strategy.md`.
- Decision: chose the only next node [0], Unknown at (0,3).
- Reason: forced path; the branch reaches a rest site soon and current HP plus Speed Potion is sufficient for the next hallway.

## Floor 4 - Jungle Maze Adventure

- Current HP/status: 73/80 HP, 120 gold, Speed Potion.
- Entity KB read: `kb/events/jungle_maze_adventure.md`.
- Decision: chose Solo Quest for 137 gold and -18 HP over Join Forces for 46 gold.
- Reason: paying 18 HP is acceptable with a rest site soon and Burning Blood after the next combat; the extra 91 gold can fund future Injury removal or a shop answer.

## Floor 4 - Pathing

- Current HP/status: 55/80 HP, 257 gold, Speed Potion.
- Strategy files read: `kb/strategies/pathing.md`, live `history/run21_strategy.md`.
- Decision: chose the only next node [0], Monster at (1,4).
- Reason: forced path; preserve Speed Potion unless the fight threatens severe HP loss before the upcoming rest site.

## Floor 5 - Fuzzy Wurm Crawler

- Current HP/status: entered at 55/80 HP, 257 gold, Speed Potion.
- Entity KB read: `kb/enemies/overgrowth/fuzzy_wurm_crawler.md`.
- Combat: T1 played Strike then True Grit to block; True Grit randomly exhausted Injury, the ideal outcome. T2 used Bash + Strike during Inhale. T3 used Primal Force to convert two Strikes into Giant Rocks and killed through Vulnerable before the 13-damage attack.
- Result: took 0 damage, ended at 61/80 after Burning Blood.
- Reward strategy read: `kb/strategies/reward_choice.md`, live `history/run21_strategy.md`.
- Card KB read: `kb/cards/ironclad/sword_boomerang.md`, `kb/cards/ironclad/breakthrough.md`, `kb/cards/ironclad/headbutt.md`.
- Decision: picked Sword Boomerang over Breakthrough and Headbutt; claimed 15 gold.
- Reason: Vantom has 9 Slippery stacks, so Sword Boomerang's three cheap hits are a boss-specific answer. Headbutt is generally useful but less urgent; Breakthrough is AoE the deck does not currently need.

## Floor 5 - Pathing

- Current HP/status: 61/80 HP, 272 gold, Speed Potion.
- Strategy files read: `kb/strategies/pathing.md`, live `history/run21_strategy.md`.
- Decision: chose the only next node [0], Unknown at (0,5).
- Reason: forced path into a rest site; current HP and Speed Potion make the branch stable.

## Floor 6 - Treasure

- Current HP/status: 61/80 HP, 304 gold after chest gold, Speed Potion.
- Relic KB read: `kb/relics/miniature_cannon.md`.
- Decision: claimed Miniature Cannon.
- Reason: only relic offered; improves upgraded Attacks, making future attack upgrades and any Armaments-style effects more valuable.

## Floor 7 - Rest Site

- Current HP/status: 61/80 HP, 304 gold, Speed Potion.
- Strategy files read: `kb/strategies/reward_choice.md`, `kb/strategies/pathing.md`, live `history/run21_strategy.md`.
- Card/relic KB read: `kb/cards/ironclad/true_grit.md`, `kb/cards/ironclad/sword_boomerang.md`, `kb/relics/miniature_cannon.md`.
- Decision: Smith over Rest; upgrade Sword Boomerang.
- Reason: 61 HP is stable with Burning Blood, Speed Potion, and another rest site ahead. Sword Boomerang+ adds a fourth hit for Vantom Slippery and should trigger Miniature Cannon's upgraded-Attack damage bonus on each hit.

## Floor 7 - Pathing

- Current HP/status: 61/80 HP, 304 gold, Speed Potion.
- Strategy files read: `kb/strategies/pathing.md`, live `history/run21_strategy.md`.
- Decision: chose the only next node [0], Monster at (0,7).
- Reason: forced route; next branch includes another rest site or Unknown, so the hallway is acceptable.

## Floor 8 - Cubex Construct

- Current HP/status: entered at 61/80 HP, 304 gold, Speed Potion.
- Entity KB read: `kb/enemies/overgrowth/cubex_construct.md`.
- Combat: T1 played two Strikes on Charge Up. T2 played two Strikes plus True Grit, leaking 3 damage while preserving tempo. T3 used Primal Force into two Giant Rocks and Defend, taking 7. T4 Sword Boomerang+ dealt 6x4 with Miniature Cannon and killed before 12x2.
- Result: took 10 total combat damage, healed 6, ended at 57/80.
- KB update: added `kb/relics/miniature_cannon.md` note that the +3 damage applies per hit on Sword Boomerang+.
- Reward strategy read: live `history/run21_strategy.md`; card KB read `kb/cards/ironclad/setup_strike.md`, `kb/cards/ironclad/spite.md`, `kb/cards/ironclad/thunderclap.md`; potion KB read `kb/potions/potion_of_binding.md`.
- Decision: picked Spite over Setup Strike and Thunderclap; claimed Potion of Binding and 8 gold.
- Reason: Bloodletting enables Spite on the player turn, and 0-cost multi-hit damage helps Vantom's Slippery without energy strain. Potion of Binding is a strong boss/elite potion paired with Speed Potion.

## Floor 8 - Pathing

- Current HP/status: 57/80 HP, 312 gold, Speed Potion + Potion of Binding.
- Strategy files read: `kb/strategies/pathing.md`, live `history/run21_strategy.md`.
- Decision: chose RestSite [0] over Unknown [1].
- Reason: guaranteed campfire is better than event variance because the deck has high-value smith targets, especially True Grit+ for controlled exhaust before Vantom.

## Floor 9 - Rest Site

- Current HP/status: 57/80 HP, 312 gold, Speed Potion + Potion of Binding.
- Strategy/card KB read: `kb/strategies/reward_choice.md`, `kb/cards/ironclad/true_grit.md`, live `history/run21_strategy.md`.
- Decision: Smith over Rest; upgrade True Grit.
- Reason: HP is stable with two potions and another rest site soon. True Grit+ changes random exhaust into controlled exhaust, directly solving Injury, Vantom Wounds, and starter filler.

## Floor 9 - Pathing

- Current HP/status: 57/80 HP, 312 gold, Speed Potion + Potion of Binding.
- Strategy files read: `kb/strategies/pathing.md`, live `history/run21_strategy.md`.
- Decision: chose the only next node [0], Treasure at (0,9).
- Reason: forced route; afterward the path has Monster into RestSite and later an option to avoid elites.

## Floor 10 - Treasure

- Current HP/status: 57/80 HP, 348 gold after chest gold, Speed Potion + Potion of Binding.
- Relic KB read: `kb/relics/vexing_puzzlebox.md`.
- Decision: claimed Vexing Puzzlebox.
- Reason: only relic offered; a free random start-of-combat card improves opening tempo and can offset Injury/Puzzlebox draw variance.

## Floor 10 - Pathing

- Current HP/status: 57/80 HP, 348 gold, Speed Potion + Potion of Binding.
- Strategy files read: `kb/strategies/pathing.md`, live `history/run21_strategy.md`.
- Decision: chose the only next node [0], Monster at (0,10).
- Reason: forced route; next node is a rest site, so the hallway is acceptable with two preserved potions.

## Floor 11 - Shrinker Beetle + Fuzzy Wurm Crawler

- Current HP/status: entered at 57/80 HP, 348 gold, Speed Potion + Potion of Binding.
- Entity KB read: live combat state plus prior Act 1 strategy context; Shrinker applied player Shrink while alive and Fuzzy scaled to 7 Strength.
- Combat: T1 used Vexing Puzzlebox's free Unmovable, attacked Shrinker, and blocked. T2 attacked Shrinker twice and used True Grit+ to exhaust a Defend, taking 0. T3 faced 27 incoming with no block cards, used Potion of Binding to reduce attacks to 10+9 and apply Vulnerable, then used Primal Force. One Giant Rock killed Shrinker and removed Shrink; two Vulnerable Giant Rocks killed Fuzzy before it attacked.
- Result: took 0 damage, spent Potion of Binding, healed to 63/80 after Burning Blood.
- Reward strategy read: live `history/run21_strategy.md`, `kb/strategies/card_impressions.md`, `kb/strategies/archetypes.md`, `kb/strategies/ironclad.md`.
- Card KB read: `kb/cards/ironclad/headbutt.md`, `kb/cards/ironclad/iron_wave.md`, `kb/cards/ironclad/havoc.md`.
- Decision: picked Headbutt over Iron Wave and Havoc; claimed 9 gold.
- Reason: Headbutt adds real 1-cost damage and can redraw Bloodletting, True Grit+, Sword Boomerang+, or key Primal Force setup turns. Iron Wave is medium despite possible Miniature Cannon upside when upgraded; Havoc is too random with Injury/status risk.

## Floor 12 - Rest Site

- Current HP/status: 63/80 HP, 357 gold, Speed Potion.
- Strategy/card KB read: `kb/strategies/pathing.md`, `kb/strategies/reward_choice.md`, live `history/run21_strategy.md`, `kb/cards/ironclad/headbutt.md`, `kb/cards/ironclad/bash.md`, `kb/cards/ironclad/primal_force.md`.
- Decision: Smith over Rest; upgraded Primal Force.
- Reason: HP is above the Act 1 boss checkpoint with Burning Blood and a final rest site before Vantom. Primal Force+ upgrades the whole transformed-attack turn into Giant Rock+ and is the deck's strongest hallway/boss burst plan.

## Floor 12 - Pathing

- Current HP/status: 63/80 HP, 357 gold, Speed Potion.
- Strategy files read: `kb/strategies/pathing.md`, live `history/run21_strategy.md`.
- Decision: chose the only next node [0], Monster at (0,12).
- Reason: forced route; afterward the branch can avoid the first visible elite through Unknown and has a final rest site before Vantom.

## Floor 13 - Mawler

- Current HP/status: entered at 63/80 HP, 357 gold, Speed Potion.
- Entity KB read: `kb/enemies/overgrowth/mawler.md`.
- Combat: Vexing Puzzlebox generated free Juggernaut. Played Juggernaut, then Primal Force+ converted Sword Boomerang+, Bash, and Strike into Giant Rock+. Miniature Cannon made each upgraded token show 23 damage. Played all three rocks, took Mawler's 5x2, then killed with Defend's Juggernaut trigger plus Spite before Roar applied.
- Result: took 10 damage, healed 6, ended at 59/80.
- KB update: added `kb/relics/miniature_cannon.md` note that it applies to upgraded token Attacks generated by Primal Force+.
- Reward strategy read: live `history/run21_strategy.md`; card KB read `kb/cards/ironclad/anger.md`, `kb/cards/ironclad/blood_wall.md`, `kb/cards/ironclad/bloodletting.md`.
- Decision: picked Blood Wall over Anger and second Bloodletting; claimed 7 gold.
- Reason: Blood Wall fixes a real defensive hole for Vantom's 30-damage Dismember and pairs with Speed Potion. A second Bloodletting adds output but not block; Anger is late Act 1 damage with copy-pollution risk.

## Floor 13 - Pathing

- Current HP/status: 59/80 HP, 364 gold, Speed Potion.
- Strategy files read: `kb/strategies/pathing.md`, `kb/strategies/elites.md`, live `history/run21_strategy.md`.
- Elite/entity KB read: `kb/enemies/elites/bygone_effigy.md`, `kb/enemies/elites/byrdonis.md`, `kb/enemies/elites/phrog_parasite.md`.
- Decision: chose Unknown [1] over immediate Elite [0].
- Reason: the deck is elite-capable, but the Unknown branch preserves the option to take a later elite after seeing the event result; if the event costs HP, the monster branch remains available before the final rest.

## Floor 14 - Room Full of Cheese

- Current HP/status: 59/80 HP, 364 gold, Speed Potion.
- Event/relic KB read: `kb/events/room_full_of_cheese.md`, `kb/relics/the_chosen_cheese.md`, live `history/run21_strategy.md`.
- Decision: chose Search, losing 14 HP for The Chosen Cheese, over Gorge.
- Reason: the event KB says Search is strong when a rest site can heal the cost, and avoiding two random common cards protects draw quality before Vantom. The max HP relic should pay off over the rest of the run.

## Floor 14 - Pathing

- Current HP/status: 45/80 HP, 364 gold, Speed Potion, The Chosen Cheese.
- Strategy files read: `kb/strategies/pathing.md`, `kb/strategies/elites.md`, live `history/run21_strategy.md`.
- Decision: chose Monster [0] over Elite [1].
- Reason: after the event HP cost, 45/80 is below the pathing file's 60% before-elite rest threshold. Take the safer combat into the final rest site, then prepare for Vantom.

## Floor 15 - Ruby Raiders

- Current HP/status: entered at 45/80 HP, 364 gold, Speed Potion.
- Entity KB read: `kb/enemies/overgrowth/ruby_raiders.md`.
- Combat: Vexing Puzzlebox generated free Setup Strike. Used Setup Strike plus two Strikes and Spite to kill Tracker before Track, then blocked 5 and leaked 3 from Brute. Used Primal Force+ on Strike and Headbutt to make two 23-damage Giant Rock+ tokens; killed Crossbow through 3 Block, damaged Brute, and finished with Sword Boomerang+ before the next attack connected.
- Result: took 3 damage, healed 6, gained 1 Max HP from The Chosen Cheese, ended at 49/81.
- Reward strategy read: live `history/run21_strategy.md`; card KB read `kb/cards/ironclad/perfected_strike.md`, `kb/cards/ironclad/armaments.md`, `kb/cards/ironclad/howl_from_beyond.md`.
- Decision: took Energy Potion, picked Armaments over Perfected Strike and Howl from Beyond, and claimed 9 gold.
- Reason: Energy Potion supports Primal Force+/Blood Wall turns. Armaments is a high-upgrade-rate card that can become Armaments+ at the final rest site and upgrade whole hands, improving Miniature Cannon attacks, Blood Wall, Bash, and starter cards. Perfected Strike is mostly an Act 1 bridge and Howl needs exhaust support to become more than expensive AoE.

## Floor 16 - Rest Site

- Current HP/status: 49/81 HP, 373 gold, Speed Potion + Energy Potion.
- Strategy/boss KB read: `kb/strategies/bosses.md`, `kb/enemies/bosses/vantom.md`, `kb/strategies/pathing.md`, live `history/run21_strategy.md`.
- Card KB read earlier: `kb/cards/ironclad/armaments.md`.
- Decision: Smith over Rest; upgraded Armaments.
- Reason: Vantom's T3 Dismember is the main check, but 49 HP plus Speed Potion, Energy Potion, Blood Wall, True Grit+, and Burning Blood leaves enough survival room. Armaments+ improves whole hands for the boss and is a higher long-term win upgrade than entering with more HP but a weaker deck.

## Floor 17 - Vantom

- Current HP/status: entered at 49/81 HP, 373 gold, Speed Potion + Energy Potion.
- Strategy/boss KB read: `kb/strategies/bosses.md`, `kb/enemies/bosses/vantom.md`, live `history/run21_strategy.md`.
- Boss plan: clear Slippery with Vexing Puzzlebox's free Howl from Beyond, Spite, Strikes, and Sword Boomerang+; use Speed Potion on the first Dismember; use Energy Potion to compress early attacks and Armaments+.
- Retry 1: preserved Energy Potion until T5 and got Vantom to 50 HP, but entered second Dismember at 12 HP with only True Grit+ plus Defend available and died.
- Retry 2: used Energy Potion on T2 for faster Slippery removal and more early damage, but Wounds plus Injury left insufficient T7 block; Bloodletting damage pushed HP too low.
- Retry 3: tried putting Blood Wall into discard on Prepare so Headbutt could fetch it for T7, but the reshuffle moved Blood Wall into the draw pile, making it unavailable to Headbutt. Headbutt could only fetch True Grit+, which still left 14 block against 32 incoming at 11 HP.
- Result: died to Vantom's second Dismember on floor 17. Steam run log `1778880954.run` confirms `win: false`, `was_abandoned: false`, `killed_by_encounter: ENCOUNTER.VANTOM_BOSS`.
- KB update: added a `kb/enemies/bosses/vantom.md` note that T7 needs guaranteed block after Wounds, and that Headbutt cannot fetch a planned card if it reshuffles into the draw pile.

## Post-run Reflection

- What worked: early Primal Force+ plus Miniature Cannon produced strong hallway burst, and Sword Boomerang+ was excellent at clearing Slippery.
- What cost equity: taking The Chosen Cheese and then smithing Armaments+ left the boss entry at 49 HP with only one premium block card and no draw. The deck could handle the first Dismember but not the second after Wounds entered the shuffle.
- Next change: against Vantom, Rest at the final campfire or draft another real block/draw card before the boss unless the deck can kill before T7. Blood Wall was not enough as a single copy without draw.
- Harness/mechanic lesson: current-room retries are useful for deterministic sequencing, but reshuffles can move planned Headbutt targets out of the discard pile; verify the actual discard before relying on a top-deck plan.
