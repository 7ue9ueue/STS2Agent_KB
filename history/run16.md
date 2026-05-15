# Run 16 - Ironclad A10

- Date: 2026-04-30
- Character: Ironclad
- Ascension: 10
- Outcome: In progress
- Floor reached: 46

## Starting Rules Read

- Read updated pathing rules in `kb/strategies/pathing.md`: inspect the full visible route tree to the boss, prioritize rest-site count, and prefer question marks over regular enemies when the deck is not desperate for card rewards.
- Read `kb/strategies/_index.md`, `ironclad.md`, `pathing.md`, `archetypes.md`, and `card_impressions.md` before starting.
- Carry-forward lessons: current HP matters more than small max-HP preservation; save potions for elites/bosses by default, but spend them before hallway damage becomes lethal; plan both turns of known two-turn enemy damage checks.

## Floor 1 - Neow

- State: Ironclad A10, 64/80 HP, 99 gold, Burning Blood.
- Options: Neow's Talisman, Small Capsule, Cursed Pearl.
- KB read: `kb/enemies/ancients/neow.md`, `kb/events/neow.md`, `kb/relics/neow_s_talisman.md`, `kb/cards/status/greed.md`, `kb/relics/burning_blood.md`; created `kb/relics/small_capsule.md` from live text.
- Decision: take Small Capsule.
- Reason: Small Capsule gives a random relic with no downside. Neow's Talisman is only two starter upgrades, and Cursed Pearl adds Eternal Greed; 333 gold can be strong with early shops, but the map is not visible before choosing and the permanent unplayable draw tax is a real cost.
- Result: Small Capsule offered Molten Egg. Created `kb/relics/molten_egg.md`; Molten Egg upgrades future Attack cards when added, making upcoming attack rewards and shop attacks more attractive without justifying unsupported filler.

## Floor 1 - Pathing

- Boss: Ceremonial Beast.
- Strategy read: `kb/strategies/pathing.md`, `kb/strategies/bosses.md`.
- Boss KB read: `kb/enemies/bosses/ceremonial_beast.md`.
- Boss plan: build enough damage to cross the Plow threshold during a Plow turn, and save the Ringing turn after Beast Cry for the single highest-impact card.
- Full-route comparison:
  - Left Monster `(0,1)`: best routes can reach 4 rests, but require 4 forced monsters before first rest.
  - Middle Monster `(2,1)`: best routes can reach 4 rests with only 3 forced monsters before first rest and early question marks.
  - Right Monster `(4,1)`: best routes reach 3 rests and usually require 4-5 forced monsters before first rest.
- Decision: take middle Monster `(2,1)`.
- Reason: it follows the updated pathing rule: maximize full-route rest access, prefer early question marks over extra regular enemies, and avoid excess forced hallway damage before the first rest.

## Floor 2 - Fuzzy Wurm Crawler

- Enemy KB read: `kb/enemies/overgrowth/fuzzy_wurm_crawler.md`.
- KB point: Fuzzy Wurm Crawler attacks for 6, buffs with Inhale for +7 Strength, then attacks for 13 on A10.
- Combat: opened with three Strikes, accepting the first 6 damage because Burning Blood could refund it. On the buff turn, played Bash then Strike to set Vulnerable and push damage. On the 13-damage turn, three Vulnerable Strikes killed before the attack.
- Result: won at 64/80 after Burning Blood. Claimed 7 gold and Attack Potion.
- Card reward options: Molten Fist+, Bludgeon+, Infernal Blade.
- Strategy read: `kb/strategies/card_impressions.md`; card KB read: `molten_fist.md`, `bludgeon.md`, `infernal_blade.md`.
- Decision: take Bludgeon+.
- Reason: Molten Egg makes Bludgeon enter upgraded at 42 damage. That is decisive Act 1 frontload, strong with Bash Vulnerable, and directly supports the Ceremonial Beast plan of crossing the Plow threshold on a key turn. Molten Fist+ is good but less decisive; Infernal Blade is random and has a weak data signal.

## Floor 2 - Pathing

- Strategy read: `kb/strategies/pathing.md`.
- Options: Unknown `(2,2)` or Monster `(3,2)`.
- Full-route comparison: both branches can reach 4 rest sites, but Unknown has 2 forced monsters before the first rest on the best branch, while Monster has 3. Unknown also gives an extra question mark and less expected hallway damage.
- Decision: take Unknown `(2,2)`.
- Reason: follows the updated rule: same rest count, fewer forced combats, and question mark preferred over regular enemy.

## Floor 3 - Tablet of Truth

- Event KB read: `kb/events/tablet_of_truth.md`.
- Options: Decipher for -3 max HP and a random upgrade, or Smash for +20 HP; later Decipher tiers cost 6, 12, 24 max HP, then all-in.
- Decision: Decipher twice, then Give Up.
- Reason: at 64/80 HP, Smash would waste most of the heal. Losing 9 total max HP for two random upgrades is acceptable early, especially because small max-HP loss is not a major cost. Stopped before the 12 max-HP tier because the deck already has Bludgeon+ and the next price is much steeper for one random upgrade.
- Result: 64/71 HP.

## Floor 3 - Pathing

- Options: only Unknown `(2,3)`.
- Decision: take forced Unknown.

## Floor 4 - Self-Help Book

- Event KB read: `kb/events/self_help_book.md`; enchant KB read: `kb/cards/enchants/sharp.md`, `kb/cards/enchants/nimble.md`.
- Options: Sharp 2 on an Attack, Nimble 2 on a Skill, Power option locked.
- Decision: choose Sharp 2 and enchant Bludgeon+.
- Reason: Sharp is best on repeat-hit attacks, but the deck does not have one. Bludgeon+ is the highest-impact available Attack, and Sharp applies before Vulnerable, making it a strong Ceremonial Beast threshold card.

## Floor 4 - Pathing

- Options: only Monster `(2,4)`.
- Decision: take forced Monster.

## Floor 5 - Shrinker Beetle

- Enemy KB read: `kb/enemies/overgrowth/shrinker_beetle.md`.
- KB point: Shrinker Beetle opens with Shrink, making player Attacks deal 30% less while it is alive, then alternates 8 and 14 damage attacks.
- Combat: opening hand contained Sharp Bludgeon+ for 44 damage into 40 HP, so killed immediately before Shrink.
- Result: won at 70/71 after Burning Blood. Attack Potion preserved.
- Reward: 10 gold and card reward.
- Card reward options: Forgotten Ritual, Blood Wall, Juggling.
- Strategy read: `kb/strategies/card_impressions.md`; card KB read: `forgotten_ritual.md`, `blood_wall.md`, `juggling.md`.
- Decision: take Blood Wall.
- Reason: the deck's damage is already strong with Sharp Bludgeon+, while Blood Wall adds a one-card 16 block answer for elite/boss attack turns. Forgotten Ritual is conditional without enough natural Exhaust, and Juggling is weak until the deck can regularly play three Attacks in one turn.

## Floor 5 - Pathing

- Strategy read: `kb/strategies/pathing.md`.
- Options: Monster `(1,5)` or Monster `(2,5)`.
- Full-route comparison: `(1,5)` can branch to RestSite `(0,6)` immediately after the next fight; `(2,5)` forces Elite `(3,6)` before rest.
- Decision: take Monster `(1,5)`.
- Reason: preserve first rest-site access and avoid a forced elite while the deck is strong but still thin on block/draw.

## Floor 6 - Slimes

- Enemy KB read: `kb/enemies/overgrowth/slimes.md`; status KB read: `kb/cards/status/slimed.md`.
- Combat: used Bludgeon+ to kill Leaf Slime (M) immediately, preventing two Slimed, while accepting 5 from Twig Slime. Next turn killed Twig with two Strikes and blocked Leaf Slime's 4. Final turn killed Leaf Slime before another status.
- Result: won at 71/71 after Burning Blood. Attack Potion preserved.
- Reward: 14 gold, Energy Potion, and card reward.
- Card reward options: Second Wind, Ashen Strike+, Inferno.
- Strategy read: `kb/strategies/card_impressions.md`; card KB read: `second_wind.md`, `ashen_strike.md`, `inferno.md`.
- Decision: take Inferno.
- Reason: the deck already has premium single-target damage with Sharp Bludgeon+ and needs AoE/repeat damage. Inferno pairs with Blood Wall's turn-HP loss and Burning Blood can offset the chip. Second Wind is powerful but risky this early because most non-Attacks are still Defends/Blood Wall, and Ashen Strike+ is extra damage without enough exhaust support yet.

## Floor 6 - Pathing

- Strategy read: `kb/strategies/pathing.md`, `kb/strategies/elites.md`.
- Options: RestSite `(0,6)` or Monster `(1,6)`.
- Full-route comparison: RestSite route can reach 4 rest sites with immediate rest access and no forced monster before the first rest; Monster route reaches only 3 rest sites and still can path into elites later.
- Decision: take RestSite `(0,6)`.
- Reason: updated pathing rule prioritizes full-path rest count. The deck is full HP with Bludgeon+, Blood Wall, Inferno, Attack Potion, and Energy Potion, so smithing before the elite is better than taking another hallway first.

## Floor 7 - Rest Site

- Options: Rest for 21 HP or Smith.
- Decision: Smith Blood Wall.
- Reason: full HP makes Rest worthless. Tablet already upgraded two Defends, and Bludgeon+ is already upgraded; Blood Wall+ gives 20 one-card block for the forced elite and future Ceremonial Beast turns.

## Floor 7 - Pathing

- Strategy read: `kb/strategies/elites.md`; elite KB read: `byrdonis.md`, `bygone_effigy.md`, `phrog_parasite.md`.
- Options: only Elite `(0,7)`, then RestSite `(0,8)`.
- Decision: take forced Elite.
- Reason: full HP, Attack Potion, Energy Potion, Bludgeon+, Blood Wall+, and Inferno meet the Act 1 elite readiness check, with immediate rest access afterward.

## Floor 8 - Elite: Bygone Effigy

- Enemy KB read: `kb/enemies/elites/bygone_effigy.md`.
- KB point: Bygone Effigy gives two setup turns, then attacks for 25 every turn at A10; defense is usually worse than racing unless it enables lethal next turn.
- Combat: installed Inferno on turn 1, then played two Strikes. Turn 2 used Energy Potion for Bash + Sharp Bludgeon+, dropping Effigy to 33 before its first attack. Turn 3 used Blood Wall+ to block most of the 25 and trigger Inferno, then Strike pushed it to 12. Took 5 from the first attack, then Inferno plus Strike killed on turn 4.
- Result: won at 67/71. Used Energy Potion; preserved Attack Potion. Reward: 27 gold, Regal Pillow, and card reward.
- KB update: added an Inferno note that Blood Wall's HP loss triggers Inferno damage while covering the attack.
- Relic KB read/updated: `kb/relics/regal_pillow.md`.
- Decision: take Regal Pillow, 27 gold, and Pommel Strike+ from Pommel Strike+ / Setup Strike+ / Thunderclap+.
- Reason: Regal Pillow adds 15 HP to each Rest and reinforces the current rest-site-rich path. Pommel Strike+ is the cleanest card reward because the deck needs draw and cycle more than another generic attack; Thunderclap+ is useful AoE Vulnerable but lower signal and partially overlaps Bash/Inferno, while Setup Strike+ is short-term damage that dilutes faster.

## Floor 9 - Rest Site

- Options: Rest for 21 + 15 from Regal Pillow, or Smith.
- Card KB read: `kb/cards/ironclad/bash.md`, `kb/cards/ironclad/inferno.md`.
- Decision: Smith Inferno+.
- Reason: at 67/71, Rest would waste almost all of Regal Pillow's healing. Among remaining upgrades, Inferno+ adds 3 damage to every trigger and all enemies, scaling with Blood Wall's HP-loss trigger; Bash+ is good but less urgent with Sharp Bludgeon+ and Pommel Strike+ already carrying the attack plan.

## Floor 10 - Treasure

- Relic KB created: `kb/relics/the_courier.md`.
- Decision: take The Courier.
- Reason: chest reward. The Courier discounts shops by 20% and makes shop inventories not run out, which is especially valuable with 195 gold and a visible shop option later in the act.

## Floor 10 - Pathing

- Strategy read: `kb/strategies/pathing.md`, `kb/strategies/elites.md`.
- Options: Unknown `(0,10)` or Elite `(1,10)`.
- Full-route comparison: both branches preserve RestSite on floor 11, Elite on floor 12, Shop/Monster on floor 13, Elite on floor 14, RestSite on floor 15, then boss.
- Decision: take Unknown `(0,10)`.
- Reason: rest count and later elite access are equal, and the current path already contains two forced elites before the boss. Updated pathing guidance prefers question marks over extra enemies/elites when the deck is not desperate for rewards.

## Floor 11 - Slippery Bridge

- Event KB read: `kb/events/slippery_bridge.md`.
- Initial offer: remove Inferno+.
- Decision: Hold On once for 3 HP, then Overcome to remove an unupgraded Defend.
- Reason: Inferno+ was just upgraded and is a core AoE/scaling card with Blood Wall+. An unupgraded Defend is acceptable to remove because the deck still has Blood Wall+ and two upgraded Defends; paying another 4+ HP to chase a Strike removal before forced elites was not worth it.

## Floor 12 - Rest Site

- Options: Rest for 21 + 15 from Regal Pillow, or Smith.
- Card KB read: `kb/cards/ironclad/bash.md`.
- Decision: Smith Bash+.
- Reason: Rest would heal only 7 missing HP and waste 29 potential healing. Bash+ extends Vulnerable to 3 turns, improving Sharp Bludgeon+, Pommel Strike+, and Ceremonial Beast threshold planning.

## Floor 13 - Elite: Byrdonis

- Enemy KB read: `kb/enemies/elites/byrdonis.md`.
- KB point: Byrdonis alternates 19 Swoop and 4x3 Peck on A10 while gaining Strength every turn; later Peck turns scale very quickly.
- Combat: installed Inferno+ and Bash+ on turn 1, accepting 19. Turn 2 used Pommel Strike+ into Blood Wall+, blocking Peck fully while triggering Inferno. Turn 3 used Bash+ and Strike to set lethal, accepting the 21 Swoop. Turn 4 Inferno left Byrdonis at 5, and Strike killed.
- Result: won at 25/71 after Burning Blood. Preserved Attack Potion. Reward: 27 gold, Liquid Bronze, Bag of Marbles, and card reward.
- Relic/potion KB read or updated: `kb/relics/bag_of_marbles.md`, `kb/potions/liquid_bronze.md`.
- Card reward options: Uppercut+, Setup Strike+, Molten Fist+.
- Strategy read: `kb/strategies/card_impressions.md`; card KB read: `uppercut.md`, `setup_strike.md`, `molten_fist.md`.
- Decision: take Uppercut+.
- Reason: the deck needs damage mitigation before another forced elite. Uppercut+ adds Weak plus Vulnerable, which is more valuable at 25 HP than Molten Fist+'s Vulnerable doubling or Setup Strike+'s short-term damage.

## Floor 13 - Pathing

- Strategy read: `kb/strategies/pathing.md`.
- Options: Monster `(1,13)` or Shop `(2,13)`.
- Full-route comparison: both branches go to Elite `(2,14)`, then RestSite `(2,15)`, then Ceremonial Beast.
- Decision: take Shop `(2,13)`.
- Reason: same rest/elite structure, but Shop avoids hallway damage at 25 HP and is high value with The Courier plus 222 gold.

## Floor 14 - Shop

- Strategy read: `kb/strategies/card_impressions.md`; relic/potion KB read or updated: `kb/relics/anchor.md`, `kb/potions/blood_potion.md`, `kb/potions/fysh_oil.md`.
- Relevant stock: Anchor, Pommel Strike+ on sale, Ultimate Defend, Feel No Pain, Blood Potion, Fysh Oil.
- Decision: discard Liquid Bronze, buy Blood Potion and use it immediately, buy Anchor, buy Fysh Oil.
- Reason: at 25/71 before a forced elite, Blood Potion's 14 HP was more important than saving Liquid Bronze. Anchor gives 10 opening Block for the elite and boss, and Fysh Oil is a flexible elite/boss potion. The discounted Pommel+ was attractive but lost to immediate survival after buying Anchor.

## Floor 15 - Elite: Phrog Parasite

- Enemy KB read: `kb/enemies/elites/phrog_parasite.md`.
- KB point: Phrog alternates Infect and 5x4 Lash; killing it by attack spawns 4 stunned Wrigglers for the immediate enemy turn, then they begin acting.
- Combat: used Fysh Oil immediately. Installed Inferno+ and used two Strikes on the Infect turn. Turn 2 played Bash+ plus Defend+ into Lash, taking 11. Turn 3 Bludgeon+ killed Phrog before another Infect. Inferno softened all Wrigglers; killed the attacking Wrigglers first and let Inferno finish the remaining status/buff Wrigglers.
- Result: won at 27/71 after Burning Blood. Used Fysh Oil; preserved Attack Potion. Reward: 33 gold, Blood Vial, and card reward.
- Relic KB read: `kb/relics/blood_vial.md`.
- Card reward options: Bloodletting, Perfected Strike+, Flame Barrier.
- Strategy read: `kb/strategies/card_impressions.md`; card KB read: `bloodletting.md`, `perfected_strike.md`, `flame_barrier.md`.
- Decision: take Flame Barrier.
- Reason: Bloodletting is a strong general energy card, but at low HP before Ceremonial Beast the deck needs reliable block more than HP-cost acceleration. Perfected Strike+ is additional frontload in a deck already carrying Bludgeon+, Bash+, Uppercut+, and Bag of Marbles.

## Floor 16 - Rest Site

- Options: Rest for 21 + 15 from Regal Pillow, or Smith.

- Decision: Rest.
- Reason: entering at 27/71 before Ceremonial Beast makes 36 healing worth more than another upgrade. Result: 63/71.

## Floor 17 - Boss: Ceremonial Beast

- Boss KB read: `kb/enemies/bosses/ceremonial_beast.md`.
- Boss plan: cross the 160 Plow threshold during a Plow turn to stun and cancel the attack; use Ringing turn on the best single card.
- Combat: opened Inferno+ plus Bash+. Turn 2 used Pommel Strike+ into Blood Wall+ to deal damage and fully block the first Plow. Turn 3 Bludgeon+ under Vulnerable crossed the 160 Plow threshold, stunning Beast and canceling the 22 attack. On the Ringing attack turn, used Uppercut+ as the single card to apply Weak/Vulnerable and reduce incoming. Finished with Bludgeon+ after Inferno tick.
- Result: won at 45/71 after Burning Blood. Attack Potion preserved. Reward: 75 gold and rare card reward.
- Card reward options: Dark Embrace, Hellraiser, Brand.
- Strategy read: `kb/strategies/card_impressions.md`; card KB read: `dark_embrace.md`, `hellraiser.md`, `brand.md`.
- Decision: take Brand.
- Reason: Brand gives 0-cost Strength and controlled exhaust, and its 1 HP loss triggers Inferno damage. Dark Embrace lacks enough exhaust support by itself, and Hellraiser is random Strike automation in a deck that needs more control going into Act 2.
- KB update: added Brand + Inferno interaction note to `kb/cards/ironclad/brand.md`.

## Act 2 Start

- Boss: Knowledge Demon.
- Strategy read: `kb/strategies/pathing.md`, `kb/strategies/bosses.md`.
- Boss KB read: `kb/enemies/bosses/knowledge_demon.md`.
- Boss plan: preserve tempo for a fast fight; avoid curse choices that cripple draw/energy unless the HP clock from Disintegration is worse. Brand gives controlled exhaust for statuses/junk, and Attack Potion should be held for elite/boss burst if possible.

## Floor 18 - Ancient: Tezcatara

- Ancient/relic KB read: `kb/enemies/ancients/tezcatara.md`, `kb/relics/very_hot_cocoa.md`, `kb/relics/golden_compass.md`; created `kb/relics/biiig_hug.md`.
- Options: Very Hot Cocoa, Biiig Hug, Golden Compass.
- Decision: take Very Hot Cocoa.
- Reason: +4 opening energy every combat is premium with Inferno+, Brand, Bludgeon+, Uppercut+, Blood Wall+, and Flame Barrier. Biiig Hug removes four cards but adds recurring Soot on reshuffle, and Golden Compass gives rest-rich structure but locks into mandatory pathing and late elites.

## Floor 18 - Pathing

- Strategy read: `kb/strategies/pathing.md`.
- Options: Monster `(1,1)` or Monster `(6,1)`.
- Full-route comparison: both sides can reach three rest sites before Knowledge Demon. The left branch has early Unknowns after the first fight and can route through RestSite `(0,6)`, RestSite `(1,10)`, and a final RestSite at row 14. The right branch has early shop access and several rest options, but tends to require more regular combats or shop stops before the first recovery point.
- Decision: take left Monster `(1,1)`.
- Reason: equal practical rest count, better early question-mark access, and no need to prioritize an immediate shop with only 108 gold.

## Floor 19 - Monster: Tunneler

- Enemy KB read: `kb/enemies/hive/tunneler.md`.
- KB point: Tunneler opens with 15 Bite, then Burrow for 37 Block; fully breaking Burrow block prevents the 26 Attack from Below and stuns it.
- Combat: Very Hot Cocoa enabled Pommel Strike+, Uppercut+, and two Strikes on turn 1 while Anchor plus Defends covered Bite. Turn 2 used Strike plus Bash+ during the non-attacking Burrow setup, leaving Tunneler at 16 HP before it gained 37 Block. Turn 3 Bludgeon+ under Vulnerable dealt enough to kill through all Burrow block.
- Result: won at 71/71 after Burning Blood and Blood Vial healing; preserved Attack Potion. Reward: 9 gold and card reward.
- Card reward options: Breakthrough+, Bully+, Pommel Strike+.
- Strategy read: `kb/strategies/card_impressions.md`; card KB read: `breakthrough.md`, `bully.md`, `pommel_strike.md`.
- Decision: take Pommel Strike+.
- Reason: Pommel Strike+ is premium attack/draw and improves access to Inferno+, Bludgeon+, Uppercut+, and block. Breakthrough+ has AoE/Inferno synergy but poor general signal and another HP cost; Bully+ is free Vulnerable payoff but narrower than a second draw attack.
- KB update: corrected Tunneler strategy notes to use A10 Burrow and Attack from Below values.

## Floor 20 - Event: Symbiote

- Event/enchantment KB read: `kb/events/symbiote.md`, `kb/cards/enchants/corrupted.md`.
- Options: enchant an Attack with Corrupted, or transform a card.
- Decision: choose Approach, then enchant Uppercut+ with Corrupted.
- Reason: at 71/71 with Burning Blood and Blood Vial, the deck can afford occasional 2 HP costs for stronger elite/boss turns. Bludgeon+ was not eligible because it already has Sharp. Uppercut+ is a strong target because it is a key debuff attack that benefits from more frontload without making a repeated draw card like Pommel Strike+ cost HP every cycle.
- KB update: added Symbiote/Corrupted notes that already-enchanted attacks are ineligible and that high-impact non-spam attacks are good Corrupted targets when sustain is strong.

## Floor 20 - Pathing

- Strategy read: `kb/strategies/pathing.md`.
- Options: Unknown `(0,3)` or Monster `(1,3)`.
- Full-route comparison: both branches rejoin the same visible structure, including access to RestSite `(0,6)`, RestSite `(1,10)`, and a final RestSite before Knowledge Demon.
- Decision: take Unknown `(0,3)`.
- Reason: equal rest-site structure, full HP, and the deck is no longer desperate for regular hallway rewards; the pathing KB prefers question marks over regular enemies in this case.

## Floor 21 - Shop

- Strategy read: `kb/strategies/card_impressions.md`; card/potion KB read: `kb/cards/ironclad/spite.md`, `kb/cards/ironclad/evil_eye.md`, `kb/potions/flex_potion.md`.
- Relevant stock: Spite+, Evil Eye on sale, Blood Wall, Restlessness, Strength Potion, Flex Potion, remove service.
- Decision: buy Spite+ and Flex Potion.
- Reason: Spite+ is a 0-cost triple-hit payoff for same-turn HP loss from Brand, Blood Wall, Inferno turn-start loss, and Corrupted Uppercut+. Flex Potion is reserved for elite/boss burst and scales strongly with Spite+, Vulnerable, and the deck's attacks. Removal was good but less immediate than adding a strong synergy card plus a boss/elite potion.
- KB update: corrected Spite strategy notes so only same-player-turn HP loss enables the bonus hits; enemy-turn damage does not count.

## Floor 22 - Monster: Bowlbug (Rock) + Bowlbug (Egg)

- Enemy KB read: `kb/enemies/hive/bowlbugs.md`.
- KB point: Bowlbug (Rock) attacks every turn for 16 on A10 and becomes stunned if its Headbutt is fully prevented; Bowlbug (Egg) attacks for 8 and gains 8 Block.
- Combat: Very Hot Cocoa and Bag of Marbles made the fight trivial. Bludgeon+ killed Rock immediately through Vulnerable, then Corrupted Uppercut+ killed Egg. The 2 HP loss from Corrupted was fully recovered by Burning Blood.
- Result: won at 71/71. Preserved Attack Potion and Flex Potion. Reward: 7 gold, Block Potion, and card reward; skipped Block Potion because potion slots were full with stronger elite/boss potions.
- Card reward options: Setup Strike+, True Grit, Expect a Fight.
- Strategy read: `kb/strategies/card_impressions.md`; card KB read: `setup_strike.md`, `true_grit.md`, `expect_a_fight.md`.
- Decision: take True Grit.
- Reason: True Grit is a high-value block/exhaust card once upgraded. Base random exhaust is risky, so it should be upgraded before relying on it and sequenced last when preserving key cards matters.

## Floor 23 - Monster: The Obscura

- Strategy/entity KB read: `kb/enemies/hive/the_obscura.md`, `kb/strategies/meta_play.md`, `GUIDE.md`.
- KB point: Parafright revives every turn while Obscura lives, so preventing every Slam can become a strategic trap. Kill Parafright only when it prevents a major unblocked hit; otherwise race Obscura.
- Reload lesson: the first replay drifted into repeated Parafright kills and let Obscura scale. Stopped, updated `kb/enemies/hive/the_obscura.md`, `kb/strategies/meta_play.md`, and `GUIDE.md`, then reloaded the room and replayed with explicit leader-focus.
- Corrected combat: turn 1 used Strike on Vulnerable Obscura. Turn 2 used Brand to exhaust unupgraded True Grit, then Bash+ and Pommel Strike+ on Obscura, accepting Parafright's hit. Turn 3 played Inferno+ and more attacks into Obscura, accepting the second hit to push the leader to 67 HP. Turn 4 used Flex Potion plus Bludgeon+ under Vulnerable to kill Obscura, causing Parafright to leave.
- Result: won at 28/71 after Burning Blood; spent Flex Potion as lethal/survival conversion, preserved Attack Potion, gained Fire Potion and 14 gold.
- Card reward options: Taunt+, Rupture, Havoc.
- Strategy read: `kb/strategies/card_impressions.md`; card KB read: `taunt.md`, `rupture.md`, `havoc.md`.
- Decision: take Rupture.
- Reason: the deck already has repeated player-turn HP loss from Inferno+, Brand, Blood Wall+, and Corrupted Uppercut+, plus Spite+ payoff. Rupture turns that package into Strength scaling for the Knowledge Demon fight; Taunt+ was solid but less synergistic, and Havoc is too random.
- KB update: added Rupture note for Inferno/Brand/Blood Wall/Corrupted attack packages.

## Floor 24 - Rest Site

- Strategy read: `GUIDE.md` rest vs smith rule.
- Decision: Rest.
- Reason: entered at 28/71 after the corrected Obscura race. Regal Pillow made Rest heal 36 to 64/71, which is more valuable than a smith before a route that includes an elite and the Knowledge Demon boss.

## Floor 25 - Event: Colossal Flower

- Event/relic KB read: `kb/events/colossal_flower.md`, `kb/relics/pollinous_core.md`.
- Options: take 35 gold; pay 5 HP to see 75 gold; pay 6 more HP to see 135 gold or Pollinous Core; pay 7 more HP for Pollinous Core.
- Decision: pay 18 HP total and take Pollinous Core.
- Reason: entered at 64/71 with two potions, a treasure before the forced elite, and a rest immediately after the elite. Pollinous Core's every-4-turn draw supports the deck's setup and burst plan: Rupture, Inferno, Brand, Bludgeon+, Uppercut+, Blood Wall+, and Pommel Strike+.
- KB update: added Pollinous Core note that the full HP payment is worthwhile when HP is stable and a rest follows the next danger.

## Floor 26 - Treasure

- Relic KB read/created: `kb/relics/bag_of_preparation.md`.
- Reward: Bag of Preparation.
- Decision: claim it.
- Reason: +2 starting cards pairs extremely well with Very Hot Cocoa's opening energy and improves access to Rupture, Inferno+, Brand, Bludgeon+, Uppercut+, Blood Wall+, and early block before the forced elite.

## Floor 27 - Elite: Infested Prism

- Strategy/enemy KB read: `kb/strategies/elites.md`, `kb/enemies/elites/infested_prism.md`.
- KB point: Infested Prism cycles Jab, Radiate, Whirlwind, then Pulsate; Vital Spark only refunds energy after HP damage, and Radiate adds block before the Whirlwind turn.
- Combat: opened with Corrupted Uppercut+ to convert Bag of Marbles Vulnerable into 29 damage, Weak the Jab, and extend Vulnerable. Pommel Strike+ drew Bludgeon+, which hit for 66 under Vulnerable; Flame Barrier fully covered the weakened Jab. Turn 2 set Inferno+, used Brand to exhaust a Strike, then played Strike plus True Grit to reduce Radiate chip. Turn 3 Bash+ extended Vulnerable and Blood Wall+ blocked most of Whirlwind while triggering Inferno. Turn 4 Inferno, Uppercut+, and Spite+ killed before Pulsate could add Strength.
- Result: won at 29/71 after Burning Blood; preserved Attack Potion and Fire Potion. Rewards: 27 gold, War Paint, and card reward.
- Relic KB read: `kb/relics/war_paint.md`.
- Decision: claim War Paint.
- Reason: normal positive relic; random Skill upgrades are especially valuable with Blood Wall, Flame Barrier, True Grit, and Defends before Knowledge Demon.
- Card reward options: Uppercut+, Headbutt+, Shrug It Off.
- Strategy read: `kb/strategies/card_impressions.md`; card KB read: `uppercut.md`, `headbutt.md`, `shrug_it_off.md`.
- Decision: take Shrug It Off.
- Reason: the deck already has strong Vulnerable and attacks. Shrug It Off is high-signal cantrip block that reduces the main remaining risk: failing to draw enough defense while setting up Inferno/Rupture or racing Knowledge Demon.

## Floor 28 - Rest Site

- Strategy read: `GUIDE.md` rest vs smith rule.
- Decision: Rest.
- Reason: entered at 29/71 after the forced elite. Regal Pillow healed 36 HP to 65/71, which is better than a smith before a forced hallway, an optional shop/unknown branch, and the Knowledge Demon route.

## Floor 29 - Monster: Mytes

- Enemy KB read: `kb/enemies/hive/myte.md`.
- KB point: one Myte opens with Toxic Cornucopia while the other uses Suck; killing the Suck Myte early prevents Strength scaling, and Toxic should be played/exhausted before ending turn when possible.
- Combat: opened with Inferno+, then Brand exhausted Ascender's Bane and triggered Inferno AoE. Focused the Suck Myte with Uppercut+ and Bash+, leaving it at 5 HP while Anchor/Shrug block covered its weakened attack. Inferno killed it at the next turn start, and Bludgeon+ killed the remaining Toxic Myte before Toxic could deal end-turn damage.
- Result: won at 69/71 after Burning Blood; preserved Attack Potion, replaced Fire Potion with Fysh Oil, gained 13 gold.
- Potion KB read: `fysh_oil.md`, `fire_potion.md`, `attack_potion.md`.
- Decision: discard Fire Potion and claim Fysh Oil.
- Reason: Fysh Oil's +1 Strength/+1 Dexterity should outvalue 20 fixed damage across the upcoming boss route while still saving Attack Potion for burst.
- Card reward options: Pommel Strike+, Sword Boomerang+, Feed+.
- Strategy read: `kb/strategies/card_impressions.md`; card KB read: `pommel_strike.md`, `sword_boomerang.md`, `feed.md`.
- Decision: take Pommel Strike+.
- Reason: Feed+ is late max-HP farming and Sword Boomerang+ lacks draw/random-targets; a third Pommel Strike+ improves consistency for Inferno/Rupture setup, block access, and boss burst turns.

## Floor 30 - Event: Brain Leech

- Strategy/event KB read: `kb/strategies/pathing.md`, `kb/events/brain_leech.md`.
- Pathing decision: chose Unknown over Shop.
- Reason: both routes preserve the final RestSite, but Shop forced an optional Act 2 elite. Unknown kept a non-elite branch, matching the pathing rule to avoid optional Act 2 elites unless needed.
- Event options: Share Knowledge for 1 of 5 random cards, or lose 5 HP for a Colorless card reward.
- Decision: Rip the Leech Off.
- Reason: at 69/71 with a final rest ahead, 5 HP is cheap; the deck wants high-impact utility more than another random Ironclad card.
- Colorless reward options: Fisticuffs+, Restlessness, Flash of Steel+.
- Card KB read: `fisticuffs.md`, `restlessness.md`, `flash_of_steel.md`.
- Decision: take Flash of Steel+.
- Reason: 0-cost damage plus draw improves the deck's fast-cycle plan and scales with Strength/Vulnerable without adding a slow setup condition.

## Floor 31 - Monster: Ovicopter

- Enemy KB read: `kb/enemies/hive/ovicopter.md`.
- KB point: Ovicopter summons Tough Eggs that hatch into minions; focus the leader when possible because minions abandon combat when it dies.
- Combat: used Brand to exhaust a Defend+ and gain Strength, then focused Ovicopter with Uppercut+, Bash+, and Strikes while ignoring eggs. Turn 2 Bludgeon+ under extended Vulnerable killed Ovicopter before the eggs could matter.
- Result: won at 69/71 after Burning Blood; preserved Attack Potion and Fysh Oil. Rewards: 10 gold and card reward.
- Card reward options: Blood Wall, Tremble+, Headbutt+.
- Strategy read: `kb/strategies/card_impressions.md`; card KB read: `blood_wall.md`, `tremble.md`, `headbutt.md`.
- Decision: take Tremble+.
- Reason: it exhausts after use and gives a large Vulnerable window for boss burst. A second Blood Wall is lower value without Corruption, and late Headbutt is less important than clean boss Vulnerable setup.

## Floor 32 - Rest Site

- Strategy/boss KB read: `kb/strategies/bosses.md`, `kb/enemies/bosses/knowledge_demon.md`, `true_grit.md`, `rupture.md`, `shrug_it_off.md`.
- Decision: Smith Rupture+.
- Reason: entered at 69/71 with a boss next, so Rest was low value. Knowledge Demon is a tempo race, and Rupture+ doubles Strength gained from Inferno turn-start loss, Brand, Blood Wall, and Corrupted Uppercut+.

## Floor 33 - Boss: Knowledge Demon

- Boss/status/potion KB read: `kb/strategies/bosses.md`, `kb/enemies/bosses/knowledge_demon.md`, `kb/cards/status/disintegration.md`, `kb/potions/attack_potion.md`.
- Boss plan: preserve draw and burst, take Disintegration over draw/card-play limits if the HP clock remains raceable, and use boss potions only for meaningful burst.
- Combat: opened with Fysh Oil, Rupture+, Corrupted Uppercut+, Spite+, Pommel Strike+, Bash+, and Attack Potion. Attack Potion offered Body Slam / Fiend Fire / Mangle; Fiend Fire was chosen for burst, but its live result was lower than theoretical hand-size math, so future potion choices should use the current card text/result rather than assumptions. Chose Disintegration over Mind Rot to preserve draw. Turn 2 used Bludgeon+ under Vulnerable, accepting HP loss because the next hand was block-heavy. Turn 3 used Flash of Steel+, Brand exhausting Ascender's Bane, Blood Wall+, and Defend+ to cover the 9x3 attack while converting HP loss into Strength. Turn 4 used Flash into Bludgeon+ before Ponder healed. Turn 5 Brand enabled Spite+ triple-hit lethal before the second curse.
- Result: won at 30/71 after Burning Blood and Blood Vial; used Fysh Oil and Attack Potion.
- KB update: added notes to `kb/cards/status/disintegration.md` that Rupture converts the end-of-turn HP loss into Strength, and to `kb/potions/attack_potion.md` that generated attacks must be evaluated from live text/modifiers.
- Rare reward options: Feed+, Unmovable, Hellraiser.
- Strategy read: `kb/strategies/card_impressions.md`; card KB read: `feed.md`, `unmovable.md`, `hellraiser.md`.
- Decision: take Unmovable, claim Blood Potion and use it immediately, claim 75 gold.
- Reason: Unmovable is defensive scaling for Act 3 and pairs with Blood Wall+, Flame Barrier+, Shrug/Defends, Very Hot Cocoa, and the deck's draw. Feed+ is late scaling with awkward fatal setup, and Hellraiser is random and lower value with few remaining Strike cards. Blood Potion healed 14 immediately to enter Act 3 at 44/71 instead of risking a low-HP opener.

## Act 3 Start

- Bosses: Doormaker into Queen.
- Strategy read: `kb/strategies/pathing.md`, `kb/strategies/bosses.md`.
- Boss KB read: `kb/enemies/bosses/doormaker.md`, `kb/enemies/bosses/queen.md`.
- Boss plan: preserve HP and potions for the double boss, install Unmovable early when possible, respect Doormaker Scrutiny blocking extra draw, and avoid optional elites that risk entering Queen depleted.

## Floor 34 - Ancient: Darv

- Ancient/relic/card KB read: `kb/enemies/ancients/darv.md`, `kb/relics/astrolabe.md`, `kb/relics/dusty_tome.md`, `kb/cards/ironclad/corruption.md`, `kb/relics/snecko_eye.md`.
- Options: Snecko Eye, Astrolabe, Dusty Tome.
- Decision: take Astrolabe and transform three unupgraded Strikes.
- Reason: Astrolabe improves deck quality without adding combat-side randomness. Snecko Eye would randomize several important 0-1 cost cards, and Dusty Tome/Corruption+ is strong but risks over-exhausting Skills before Doormaker + Queen, which conflicts with the current Unmovable block plan.
- KB update: created `kb/relics/astrolabe.md`.

## Floor 34 - Pathing

- Strategy read: `kb/strategies/pathing.md`.
- Options: Monster `(2,1)`, Monster `(3,1)`, Monster `(5,1)`.
- Full-route comparison: left and middle branches can reach three rest sites without forcing an elite; the right branch has an earlier rest but routes through a forced elite at row 9. The middle branch also reaches an early Shop at row 2, which is valuable with 194 gold and The Courier.
- Decision: take middle Monster `(3,1)`.
- Reason: keeps high rest-site access, avoids the forced-elite branch, and uses the early shop to buy recovery, potion support, removal, or boss tech before the double-boss route.

## Floor 35 - Monster: Scrolls of Biting

- Enemy KB read: `kb/enemies/glory/scroll_of_biting.md`.
- KB point: fully block or kill attacking Scrolls first because even 1 unblocked damage triggers Paper Cuts max-HP loss.
- Combat: Astrolabe results were visible in the starting deck: Cascade+, Twin Strike+, and Pact's End+. Opened with three Pommel Strike+ plus Flash/Bash/Twin Strike lines to kill both attacking Scrolls before they could deal Paper Cuts. Used Unmovable + Defend+ to block the final Scroll's 8x2 exactly, then killed with Bludgeon+.
- Result: won at 71/71 with no max-HP loss. Claimed 7 gold, Strength Potion, and True Grit+ from True Grit+ / Havoc / Perfected Strike+.
- Strategy read: `kb/strategies/card_impressions.md`; card KB read: `true_grit.md`, `havoc.md`, `perfected_strike.md`.
- Reason: True Grit+ is controlled block/exhaust and pairs with Unmovable and status/junk cleanup. Havoc was too random, and Perfected Strike+ is mostly a bridge damage card despite remaining Strike-tag density.

## Floor 36 - Shop

- Strategy read: `kb/strategies/card_impressions.md`.
- Entity KB/read: `kb/cards/ironclad/burning_pact.md`; live shop text read for Automation and Potion of Binding because KB entries were missing.
- Decision: bought Burning Pact, Automation, and Potion of Binding; left with 9 gold.
- Reason: Burning Pact gives controlled exhaust plus draw, Automation converts the deck's heavy draw package into energy in long boss fights, and Potion of Binding is a high-value saved boss potion for Doormaker/Queen because it applies both Weak and Vulnerable to all enemies.
- KB update: created `kb/cards/ironclad/automation.md` and `kb/potions/potion_of_binding.md`.

## Floor 36 - Pathing

- Strategy read: `kb/strategies/pathing.md`.
- Options: Monster `(4,3)` or Monster `(5,3)`.
- Full-route comparison: left branch can route through Unknown at row 8, Rest at row 9, avoid the row 11/12 elites, then Rest before Doormaker. Right branch includes a forced elite at row 9 before its later rest options.
- Decision: take Monster `(4,3)`.
- Reason: the left route preserves the most relevant recovery points and avoids forced Act 3 elite exposure before the double boss.

## Floor 37 - Monster: Devoted Sculptor

- Enemy KB read: `kb/enemies/glory/devoted_sculptor.md`.
- KB point: it opens with Ritual setup, then attacks every turn while damage ramps; kill before the scaling becomes dangerous.
- Combat: used turn 1 for Brand on a Strike, Unmovable, and heavy Vulnerable damage while saving potions. Turn 2 applied Tremble+ and blocked with Unmovable-doubled Defend+. Turn 3 used Pommel draw into Flame Barrier+ rather than spending a boss potion; Flame Barrier blocked the 24 attack and reflected 6. Turn 4 Pollinous Core drew into Pact's End+, which killed through Vulnerable.
- Result: won at 71/71 after Burning Blood; preserved Strength Potion and Potion of Binding.
- Reward options: Taunt, Havoc, Molten Fist+.
- Strategy read: `kb/strategies/card_impressions.md`; card KB read: `taunt.md`, `havoc.md`, `molten_fist.md`.
- Decision: take Molten Fist+ and 15 gold.
- Reason: upgraded 1-cost damage that exhausts and doubles Vulnerable is useful boss tech with Bash+, Tremble+, Uppercut+, and Potion of Binding. Taunt was low-impact block/debuff filler, and Havoc remained too random for a boss-facing deck.

## Floor 38 - Monster: Frog Knight

- Enemy KB read: `kb/enemies/glory/frog_knight.md`.
- KB point: opens Tongue Lash for damage plus Frail, then Strike Down Evil, then For the Queen; if below half it can use Beetle Charge.
- Combat: installed Rupture+ and Inferno+, used Blood Wall+ after Rupture for Strength and block, then used Pommel/Brand/Spite/Cascade to push damage while preserving both potions. Cascade unexpectedly played more of the draw pile than the visible top expectation, including Uppercut+ and Unmovable, so I accepted some HP loss instead of spending boss potions. On the buff turn, Bludgeon+ put Frog Knight at 24 HP; Twin Strike+ killed before the 45-damage Beetle Charge turn.
- Result: won at 57/71 after Burning Blood; preserved Strength Potion and Potion of Binding.
- KB update: added a Frog Knight note to kill before the post-buff Beetle Charge if pushing it below half.
- Reward options: Fight Me!+, Blood Wall, Iron Wave+.
- Strategy read: `kb/strategies/card_impressions.md`; card KB read: `fight_me.md`, `blood_wall.md`, `iron_wave.md`.
- Decision: take Blood Wall and 11 gold.
- Reason: a second Blood Wall improves one-card boss block, doubles well with Unmovable, and converts HP loss into Strength with Rupture. Fight Me!+ gives enemy Strength before the boss gauntlet, and Iron Wave+ is low-impact late.

## Floor 39 - Shop

- Strategy read: `kb/strategies/card_impressions.md`; card KB read: `headbutt.md`.
- Decision: bought sale Headbutt+ for 19 gold; no other affordable purchases.
- Reason: Headbutt+ can redraw Pommel Strike+, Uppercut+, Flame Barrier+, Blood Wall+, Bludgeon+, or other boss-turn tools. The API purchase message incorrectly reported the replacement item's 62-gold price, but gold changed from 35 to 16, confirming Headbutt+ was bought.

## Floor 40 - Event: The Round Tea Party

- Event KB read: `kb/events/the_round_tea_party.md`.
- Options: Enjoy Your Tea for full heal plus Royal Poison, or Pick a Fight for 11 HP and a random relic.
- Decision: Pick a Fight; received Meal Ticket and dropped to 46/71.
- Reason: Royal Poison would cost 4 HP at the start of every remaining combat, including Doormaker and Queen. Paying 11 HP once for a relic is safer with a treasure, rest-site access, and Burning Blood recovery still ahead.
- KB update: created `kb/relics/meal_ticket.md` and added a Round Tea Party note to avoid Royal Poison before boss gauntlets unless the full heal is mandatory.

## Floor 40 - Pathing

- Strategy read: `kb/strategies/pathing.md`.
- Options after event: Treasure `(2,7)` or Treasure `(3,7)`.
- Decision: take Treasure `(3,7)`.
- Reason: the left treasure path forces an elite and misses the row 9 rest. The right treasure path goes through Unknown into RestSite, preserving recovery before the boss route.

## Floor 41 - Treasure

- Relic KB read: `kb/relics/vambrace.md`.
- Decision: claim Vambrace.
- Reason: it doubles the first block card each combat and is excellent with Blood Wall, Flame Barrier, Defend+, True Grit+, and the Unmovable block plan.

## Floor 42 - Event: Potion Courier

- Event KB read: `kb/events/potion_courier.md`.
- Options: three Foul Potions, or one random Uncommon Potion.
- Decision: chose Ransack; skipped Powdered Demise because potion slots were full.
- Reason: Strength Potion and Potion of Binding are better boss resources than slow end-of-turn damage, and three Foul Potions would be awkward because they damage the player too.

## Floor 43 - Rest Site

- Strategy/card KB read: `kb/strategies/card_impressions.md`, `kb/cards/ironclad/unmovable.md`, `kb/cards/ironclad/blood_wall.md`.
- Decision: Smith Unmovable+ instead of Rest.
- Reason: there is one hallway before the final pre-boss rest, and 46/71 plus saved potions is enough to attempt it. Unmovable+ dropping to 1 energy is high leverage for Doormaker and Queen because it can be installed while still playing major block.

## Floor 44 - Monster: Punch Construct + Cubex Constructs

- Enemy KB read: no existing KB files for `Punch Construct` or `Cubex Construct`; created `kb/enemies/glory/punch_construct.md` and `kb/enemies/glory/cubex_construct.md` from live observations.
- Observed point: Punch Construct opened Defensive at 60 HP. Cubex Constructs opened Empower, then attacked while gaining Strength, reaching dangerous multi-hit patterns by turn 4.
- Combat: used Burning Pact on a spare Defend+ without spending Vambrace, drew Bash+/Headbutt+, and killed Punch Construct turn 1 before it could block. Saved the one-time Vambrace for Flame Barrier+ on the first real attack turn, fully blocking the two 10-damage hits and reflecting damage. Later used Rupture+ plus Brand for Strength, but the Cubex pair scaled to 12x2 each and became dangerous at 30 HP. Used Potion of Binding to reduce both enemies to 9x2 and make Bludgeon+ kill the healthier Cubex through Vulnerable. Cascade at 0 energy played Flash of Steel+ from the draw pile, helping set up the final kill.
- Result: won at 18/71 after Burning Blood. Used Potion of Binding; preserved Strength Potion. Rewards offered: 7 gold, Lucky Tonic, and a card reward.
- Lesson: saving Vambrace for a real attack turn was correct, but paired Cubex Constructs punish slow lines sharply; remove one Cubex before the turn-4 multi-hit or spend Weak/Vulnerable if the fight becomes lethal.
- Reward decision: took Lucky Tonic and 7 gold. Card reward was Setup Strike+ / Rage+ / True Grit+; read `kb/strategies/card_impressions.md`, `kb/cards/ironclad/setup_strike.md`, `kb/cards/ironclad/rage.md`, and `kb/cards/ironclad/true_grit.md`.
- Reward reason: took Rage+ because it gives 0-cost block on attack-heavy boss turns. Skipped another True Grit+ to avoid over-exhausting key block/draw in the final gauntlet, and skipped Setup Strike+ as late filler.

## Floor 45 - Elite: Mecha Knight

- Strategy read: `kb/strategies/pathing.md`, `kb/strategies/elites.md`; elite KB read: `kb/enemies/elites/mecha_knight.md`, `kb/enemies/elites/knights.md`, `kb/enemies/elites/soul_nexus.md`.
- Pathing correction: after the floor 44 fight, both visible branches forced exactly one elite and one hallway before the rest. The earlier floor 43 smith assumed only one hallway before the rest, so entering this elite at 18/71 was a pathing-risk mistake; with no branch avoiding the elite, elite-first was chosen to face the hardest room before another hallway could lower HP further.
- Combat: spent Strength Potion on the elite at 18 HP, used Burning Pact and True Grit+ to exhaust Burns, stripped Artifact with Tremble+, and used Blood Wall/Shrug/Unmovable to survive the 45 Heavy Cleave. Cascade produced a strong mid-fight line with Flame Barrier+, Uppercut+, Rupture+, and Spite+, dropping Mecha Knight into kill range. On the 50-damage Heavy Cleave turn, Brand exhausted the remaining Burn before Lucky Tonic so Buffer would absorb the attack instead of end-turn Burn damage. Pact's End+ plus Bludgeon+ left Mecha Knight at 2 HP; Buffer prevented the attack, and Twin Strike+ killed next turn.
- Result: won at 14/71 after Burning Blood. Used Strength Potion and Lucky Tonic.
- KB update: added Mecha Knight notes that Burns can consume Buffer before Heavy Cleave, and that Artifact should be stripped before Weak/Vulnerable setup. Created `kb/relics/ornamental_fan.md` from the elite reward.
- Lesson: the Brand-before-Buffer sequence was correct and reusable. The larger issue was reaching the forced elite at 18 HP because the floor 43 route/rest assumption was wrong; when a branch is not fully visible in the current API state, re-check the whole map before smithing at low HP.
- Reward decision: claimed Ornamental Fan, 32 gold, and Uppercut+ from Bloodletting / Uppercut+ / Stomp+.
- Reward reason: read `kb/strategies/card_impressions.md`, `bloodletting.md`, `uppercut.md`, and `stomp.md`. Uppercut+ gives no-HP-cost Weak/Vulnerable for the forced hallway and boss gauntlet, while Bloodletting is strong but risky at 14 HP with no potions and several existing HP-loss cards; Stomp+ is late AoE filler with Inferno/Pact's End already covering that job.

## Floor 46 - Owl Magistrate

- Enemy KB read: `kb/enemies/glory/owl_magistrate.md`.
- KB point: fixed cycle of 17, 4x6, Judicial Flight, then 36 plus 4 Vulnerable; Weak 2 or draw control should be set up before Verdict.
- Combat: entered at 14/71 after the elite and Blood Vial started the fight at 16. Used opening energy to install Inferno+ and push damage while blocking. Cascade+ on turn 2 behaved less predictably than the visible draw preview and only left 16 block into Peck, dropping to 5 HP. On Judicial Flight, used Flash of Steel+, Molten Fist+, Pact's End+, then Headbutt+ to put Flame Barrier+ on top for Verdict and Twin Strike+ for damage. On Verdict, chose Flame Barrier+ plus True Grit+ instead of gambling Bludgeon through Soar, fully blocking the hit. Headbutt+ killed next turn.
- Result: won at 9/71 after Burning Blood. Took Liquid Memories and 10 gold.
- KB updates: added `kb/potions/liquid_memories.md`; added Owl Magistrate note to use Judicial Flight as the setup turn for Verdict; added Cascade note to re-read state after it resolves.
- Card reward options: Blood Wall, Dominate, True Grit.
- Strategy read: `kb/strategies/card_impressions.md`; card KB read: `blood_wall.md`, `dominate.md`, `true_grit.md`.
- Decision: take Dominate.
- Reason: the deck already has multiple Vulnerable sources and needs boss scaling. A third Blood Wall adds more HP-cost pressure at low HP, and another unupgraded True Grit adds random exhaust risk.

## Floor 47 - Rest Site

- Decision: Rest.
- Reason: entered at 9/71 before the two-boss gauntlet; Regal Pillow made Rest heal 36, far higher value than any remaining upgrade. Result: 45/71.

## Floor 48 - Doormaker, attempt 1 reload

- Boss KB read: `kb/enemies/bosses/doormaker.md`; card/relic KB updated after failure: `inferno.md`, `cascade.md`, `ornamental_fan.md`.
- Line: skipped attacks into the infinite-HP Door; installed Unmovable+, Blood Wall, Inferno+, Rupture+, and used Liquid Memories on Flame Barrier+ to survive an otherwise blockless Grasp turn. Blood Wall+ into Spite+ correctly converted HP loss into a strong triple-hit turn.
- Failure point: at 15 HP on a Grasp turn, Cascade+ produced only 16 block and did not give the expected Ornamental Fan block from automatically played attacks. Incoming 30 would leave 1 HP, then Inferno's next start-turn HP loss would kill before any action.
- Reload lesson: at low HP, Inferno is not free scaling in the final boss gauntlet; count future automatic HP losses before playing it. Also do not rely on Cascade-played attacks for Ornamental Fan when exact block math is lethal.

## Floor 48 - Doormaker, attempt 2 reload

- Line: skipped Inferno to preserve HP, installed Unmovable and Rupture, used Headbutt to set up Flame Barrier for Grasp, and saved Liquid Memories until a later 43-damage Hunger turn.
- Failure point: preserving HP without enough damage let Doormaker reach 327 HP on round 10 with 8 Strength. At 6 HP, Flame Barrier+ blocked only 32 into 19x2, exactly lethal.
- Reload lesson: the corrected plan is not "skip all self-damage scaling"; it is "play enough scaling and burst to shorten Doormaker while avoiding automatic start-turn HP loss when it creates exact lethal." Need earlier damage from Inferno/Automation/Cascade/attacks or a faster Vulnerable burst line, with Liquid Memories reserved for the first truly lethal block gap.

## Floor 48 - Doormaker, attempt 3 reload

- Line: skipped the Door turn, installed Unmovable+, then tried a Cascade+ plan expecting Bash+ and Defend+ cards from the visible draw pile. Cascade instead resolved a draw-changing line, installing Inferno+ and leaving 0 block into Hunger; Liquid Memories had to recover Flame Barrier+ immediately. Dominate plus Molten Fist+ and Twin Strike+ gave strong Vulnerable/Strength scaling, but the early potion spend and Inferno HP ticks left the run at 3 HP on round 7 with 15x2 incoming and no survival line.
- Failure point: the Cascade plan treated the visible draw pile as static even though a Cascade-played Pommel Strike+ could draw and alter later Cascade resolutions. That wrong assumption forced the potion too early and made the rest of the fight fail despite better damage scaling.
- Reload lesson: Cascade can be a damage/scaling tool, but do not use it as exact block planning when it may play draw cards. For the next attempt, avoid early Cascade unless the first resolves are safe without assuming later top-deck order; prioritize deterministic Unmovable+ plus Blood Wall/Flame Barrier block, then scale with Dominate/Rupture/Inferno only when the next HP thresholds remain survivable.

## Floor 48 - Doormaker, attempt 4 reload

- Line: installed Unmovable+ and Blood Wall on the first Hunger, then used Inferno+, Tremble+, Dominate, and Molten Fist+ to build the damage clock. Liquid Memories retrieved Flame Barrier+ for the next Hunger; True Grit+ controlled its exhaust target, Rupture+ was installed, and Pommel Strike+ pushed damage. On Scrutiny, Rage+ plus Defends, Spite+, and Headbutt+ produced enough block and damage, but the following Grasp hand could not survive 15x2 at 9 HP under the energy-loss rule.
- Failure point: the line entered the second Grasp too low and without compact defense. Defend+ alone was not enough, and Grasp made Defend+ plus Uppercut+ impossible because each played card also lost energy.
- Reload lesson: before ending a Scrutiny turn at low HP, check the next Grasp hand plan explicitly. It needs a single large block source, Weak already applied, retained/banked block, or enough HP cushion; otherwise the energy-loss tax can make a hand with cards in it functionally unable to defend.

## Floor 48 - Doormaker, attempt 5 reload

- Line: avoided Inferno/Rupture self-damage early and used deterministic Unmovable+ block, Blood Wall, Flame Barrier+, Defends, True Grit+, and Liquid Memories on Defend+ to survive the first several attacks. Took only small damage chunks but dealt too little damage; Doormaker was still 386 HP on round 10.
- Failure point: the line reached a 19x2 Grasp at 6 HP with only True Grit for 14 block. Grasp's energy-loss rule made the remaining attacks and self-damage cards irrelevant to survival.
- Reload lesson: pure preservation is also losing. The next line must keep deterministic block for Hunger/Grasp while using earlier burst/scaling windows, especially Vulnerable plus high-damage attacks and controlled HP-loss synergies, so the second Grasp is reached with either much lower boss HP or a clearly planned compact defense.

## Floor 48 - Doormaker, attempt 6 reload

- Line: used Brand to exhaust Cascade+, installed Unmovable+, Blood Wall, Tremble+, and Inferno+, then used Liquid Memories on Bludgeon+ under Vulnerable for a large burst. Rage+/Spite+/Molten Fist+/Headbutt+ gave a strong Scrutiny turn, and Flame Barrier+ covered the following Grasp.
- Failure point: entering the next Hunger at 19 HP with only Defend+ plus Uppercut+ meant taking 16, then Inferno dropped HP to 2 on the following Scrutiny. The live hand could not produce 25 block without lethal HP loss; three attacks plus Defend+ still fell short.
- Reload lesson: the burst plan was closer, but Inferno plus Blood Wall HP loss must leave enough cushion for the post-Hunger Scrutiny hand. Do not accept a line that enters that Scrutiny below about 6 effective HP unless the next hand has deterministic full block or lethal damage.

## Floor 48 - Doormaker, attempt 7 stopped reflection

- Line: used Flash of Steel+ on the Door to change the draw sequence, then installed Unmovable+ and Blood Wall on the first Hunger. On the first Scrutiny, Liquid Memories retrieved Flame Barrier+ so the turn could both full block and play Tremble+, Dominate, and Inferno+. Later, Uppercut+ before Scrutiny pre-applied Weak/Vulnerable and reduced the next Grasp to 11x2. Headbutt+ set Flame Barrier+ for the following Scrutiny.
- Current stopped state: HP 3/71, no potions, Doormaker 263 HP, Scrutiny 34 incoming fully blocked by Flame Barrier+ plus Defend+. This is technically alive, but strategically still losing or near-losing because Inferno will keep taxing HP and the boss has too much health left.
- What worked: changing the Door turn with Flash of Steel+ found a stronger draw path; Liquid Memories on Flame Barrier+ was correct when it prevented the first Scrutiny leak while still allowing scaling; pre-applying Weak before Grasp materially improved the next turn; Headbutt+ setup for Flame Barrier+ bought one more exact block turn.
- What failed: the line still reached the second Hunger/Scrutiny cycle at 3 HP with no potion cushion. Spending Liquid Memories early solved the first block gap but left no late emergency tool. Cascade at 0 energy also proved unsafe in this fight because it can open draw/exhaust chains and selection prompts; it should not be treated as free when exact HP math matters.
- Strategic reflection: the deeper mistake was entering the two-boss gauntlet at only 45/71 after a forced elite and hallway consumed all potions. Once Doormaker required repeated exact low-HP threading, the combat was no longer the main problem; the pre-boss path/rest/resource plan had already failed. Future Act 3 final routes should preserve more HP, rest earlier when the next branch can force an elite/hallway, and treat a potionless first boss entry below roughly 70% HP as an emergency plan, not a normal boss setup.
- Next-run changes: before the final campfire, re-check the full route tree and forced elite exposure before smithing. In the final gauntlet, do not install Inferno or spend Blood Wall HP if the next two turns project below 6 effective HP without deterministic full block or lethal. If a boss line reaches 1-4 HP with no potion and no imminent lethal, reload earlier if possible and change the underlying setup rather than continuing to solve one turn at a time.
