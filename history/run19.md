# Run 19

- Date: 2026-05-15
- Character: Ironclad A10
- Outcome: Loss on Act 2 floor 33 to Knowledge Demon (`win: false`, `was_abandoned: false`, `killed_by_encounter: ENCOUNTER.KNOWLEDGE_DEMON_BOSS` in Steam run log `1778855698.run`).

## Required Reads

- Read `GUIDE.md`, `kb/strategies/_index.md`, `kb/strategies/ironclad.md`, `kb/strategies/pathing.md`, `kb/strategies/archetypes.md`, and `kb/strategies/card_impressions.md` before starting.

## Floor 1 - Neow

- HP/status: 64/80, 99 gold, no potions, Burning Blood.
- Entity KB read: `kb/events/neow.md`, `kb/enemies/ancients/neow.md`, `kb/relics/lava_rock.md`, `kb/relics/scroll_boxes.md`, `kb/relics/new_leaf.md`.
- Options: New Leaf transform 1 card; Lava Rock delayed Act 1 boss extra relic; Scroll Boxes lose all gold and add one forced 3-card pack.
- Decision: take New Leaf.
- Reason: Immediate starter-deck improvement is more useful than Lava Rock's delayed value at A10 starting HP, and preserving 99 gold is better than forced early deck growth from Scroll Boxes.

## Floor 1 - Act 1 Route

- Strategy file read: `kb/strategies/pathing.md`, `kb/strategies/bosses.md`, `history/run19_strategy.md`.
- Entity KB read: `kb/enemies/bosses/ceremonial_beast.md`.
- Current HP/status: 64/80, 99 gold, no potions.
- Boss plan: build enough frontload to cross Ceremonial Beast's Plow threshold on a dangerous Plow turn; respect Beast Cry's one-card limit.
- Decision: start on the middle Monster at (3,1).
- Reason: Compared with left/right combat-heavy starts, the middle branch gives early combat reward plus an immediate unknown and later shop/rest/elite flexibility.

## Floor 2 - Shrinker Beetle

- Strategy file read: `kb/strategies/combat.md`, `history/run19_strategy.md`.
- Entity KB read: `kb/enemies/overgrowth/shrinker_beetle.md`, `kb/cards/ironclad/molten_fist.md`.
- Current HP/status: entered 64/80, no potions.
- Combat notes: New Leaf transform was Molten Fist. Shrinker Beetle opened with Shrink, then 8/14 attacks. Used Bash before Molten Fist so Molten doubled Vulnerable from 2 to 4.
- Outcome: won at 58/80 after Burning Blood.

## Floor 2 - Card Reward

- Strategy file read: `kb/strategies/reward_choice.md`, `kb/strategies/card_impressions.md`, `history/run19_strategy.md`.
- Entity KB read: `kb/cards/ironclad/vicious.md`, `kb/cards/ironclad/shrug_it_off.md`, `kb/cards/ironclad/uppercut.md`.
- Current HP/status: 58/80, 99 gold before claiming gold, no potions.
- Options: Vicious, Shrug It Off, Uppercut.
- Decision: take Uppercut; claim 11 gold.
- Reason: Uppercut is immediate Act 1 frontload and mitigation, supports Molten Fist/Vulnerable lines, and is a stronger Ceremonial Beast prep card than speculative Vicious or defensive Shrug before damage is secured.

## Floor 3 - Morphic Grove

- Strategy file read: `history/run19_strategy.md`, `kb/strategies/reward_choice.md`.
- Entity KB read: `kb/events/morphic_grove.md`.
- Current HP/status: 58/80, 110 gold, no potions.
- Options: lose all gold and transform 2 cards; gain 5 max HP.
- Decision: choose Group; transform two Defends.
- Reason: Two starter-card transforms are immediate deck-quality improvement and can solve damage/draw/block better than +5 max HP. Defends are weaker draws than Strikes in the current Act 1 damage plan after adding Uppercut and Molten Fist.

## Floor 3 - Route After Event

- Strategy file read: `kb/strategies/pathing.md`, `history/run19_strategy.md`.
- Current HP/status: 58/80, 0 gold, no potions.
- Options: Unknown into shop, or Monster into more combats.
- Decision: take the Monster branch at (4,3).
- Reason: After spending all gold, the immediate shop has low value; the deck needs rewards and gold, and Burning Blood helps offset early hallway damage.

## Floor 4 - Nibbit

- Strategy file read: `kb/strategies/combat.md`, `history/run19_strategy.md`.
- Entity KB read: `kb/enemies/overgrowth/nibbit.md`, `kb/cards/ironclad/tear_asunder.md`, `kb/cards/ironclad/impervious.md`.
- Current HP/status: entered 58/80, 0 gold, no potions.
- Combat notes: Morphic Grove transforms were Tear Asunder and Impervious. Used Uppercut + Strike on turn 1, then pushed damage through the Slice/Block turn.
- Outcome: won at 48/80 after Burning Blood.
- Reflection: Bash at 1 HP left Nibbit alive through a buff turn; harmless here, but exact block+HP math should be checked before spending a 2-cost attack as a nonlethal finisher.

## Floor 4 - Card Reward

- Strategy file read: `kb/strategies/reward_choice.md`, `history/run19_strategy.md`.
- Entity KB read: `kb/cards/ironclad/thunderclap.md`, `kb/cards/ironclad/shrug_it_off.md`, `kb/cards/ironclad/ashen_strike.md`, `kb/potions/clarity_extract.md`.
- Current HP/status: 48/80, 0 gold before rewards.
- Options: Thunderclap, Shrug It Off, Ashen Strike.
- Decision: take Shrug It Off; claim Clarity Extract and 11 gold.
- Reason: Damage is improved by Uppercut, Molten Fist, and Tear Asunder; Shrug adds much-needed cantrip block and helps offset the HP cost of 2-cost attack turns.

## Floor 5 - Slimes

- Strategy file read: `kb/strategies/combat.md`, `history/run19_strategy.md`.
- Entity KB read: `kb/enemies/overgrowth/slimes.md`.
- Current HP/status: entered 48/80, 11 gold, Clarity Extract.
- Combat notes: Killed Twig Slime (S) immediately, then used Uppercut + Molten Fist to kill Twig Slime (M) through Weak/Vulnerable. Finished Leaf Slime (S) after status turns.
- Outcome: won at 50/80 after Burning Blood.

## Floor 5 - Card Reward

- Strategy file read: `kb/strategies/reward_choice.md`, `history/run19_strategy.md`.
- Entity KB read: `kb/cards/ironclad/inflame.md`, `kb/cards/ironclad/ashen_strike.md`, `kb/cards/ironclad/shrug_it_off.md`.
- Current HP/status: 50/80, 11 gold before rewards, Clarity Extract.
- Options: Inflame, Ashen Strike, Shrug It Off.
- Decision: take Inflame; claim 13 gold.
- Reason: The deck has enough immediate attacks and a Shrug/Impervious defensive base; Inflame adds simple boss scaling for Ceremonial Beast and improves repeated attacks/Tear Asunder turns.

## Floor 6 - Slithering Strangler + Slimes

- Strategy file read: `kb/strategies/combat.md`, `history/run19_strategy.md`.
- Entity KB read: `kb/enemies/overgrowth/slithering_strangler.md`, `kb/enemies/overgrowth/slimes.md`.
- Current HP/status: entered 50/80, 24 gold, Clarity Extract.
- Combat notes: Killed Twig Slime first, used Molten Fist on Leaf Slime, then prioritized Strangler after Constrict. Constrict stacked to 6 before lethal; Tear Asunder hit 4 times after multiple HP-loss events.
- Outcome: won at 41/80 after Burning Blood.
- Reflection: Constrict damage is unblockable end-turn HP loss and should push faster Strangler damage once side damage is controlled.

## Floor 6 - Card Reward

- Strategy file read: `kb/strategies/reward_choice.md`, `history/run19_strategy.md`.
- Entity KB read: `kb/cards/ironclad/blood_wall.md`, `kb/cards/ironclad/true_grit.md`, `kb/cards/ironclad/drum_of_battle.md`, `kb/potions/power_potion.md`.
- Current HP/status: 41/80, 24 gold before rewards, Clarity Extract.
- Options: Blood Wall, True Grit, Drum of Battle.
- Decision: take Blood Wall; claim Power Potion and 13 gold.
- Reason: Blood Wall adds a second large block card for elite/boss turns and can deliberately enable Tear Asunder. Base True Grit's random exhaust is worse before upgrade, and Drum has a documented risk with Impervious in the deck.

## Floor 7 - Leaf Slime (M) + Flyconid

- Strategy file read: `kb/strategies/combat.md`, `history/run19_strategy.md`.
- Entity KB read: `kb/enemies/overgrowth/flyconid.md`, `kb/enemies/overgrowth/slimes.md`.
- Current HP/status: entered 41/80, 37 gold, Clarity Extract and Power Potion.
- Combat notes: Opened with Shrug It Off and two Strikes into Flyconid. Used Impervious to blank the 21-damage turn through Frail, then Bash + Molten Fist to set up Flyconid lethal. Killed Flyconid before finishing Leaf Slime; took 8 on the vulnerable attack turn.
- Outcome: won at 38/80 after Burning Blood.
- Reflection: Flyconid plus Leaf Slime status pressure makes the second attack cycle dangerous; Impervious prevented the major damage spike, but delayed Flyconid lethal still cost HP.

## Floor 7 - Card Reward

- Strategy file read: `kb/strategies/reward_choice.md`, `kb/strategies/card_impressions.md`, `history/run19_strategy.md`.
- Entity KB read: `kb/cards/ironclad/expect_a_fight.md`, `kb/cards/ironclad/inflame.md`, `kb/cards/ironclad/battle_trance.md`, `kb/potions/blessing_of_the_forge.md`.
- Current HP/status: 38/80, 37 gold before rewards, Clarity Extract and Power Potion.
- Options: Expect a Fight, Inflame, Battle Trance; potion reward was Blessing of the Forge with full potion slots.
- Decision: take Battle Trance, claim 13 gold, skip Blessing of the Forge.
- Reason: Battle Trance improves consistency for finding the deck's key attacks, block, and Inflame. A second Inflame is slower duplicate scaling, Expect a Fight is more conditional, and Blessing is less reliable than the saved Clarity Extract plus Power Potion.

## Floor 8 - Ruby Raiders

- Strategy file read: `kb/strategies/combat.md`, `history/run19_strategy.md`.
- Entity KB read: `kb/enemies/overgrowth/ruby_raiders.md`, `kb/cards/ironclad/unmovable.md`, `kb/cards/ironclad/pyre.md`, `kb/cards/ironclad/cruelty.md`, `kb/potions/snecko_oil.md`.
- Current HP/status: entered 38/80, 50 gold, Clarity Extract and Power Potion.
- Combat notes: Encounter was Assassin, Tracker, Crossbow. Opened Tear Asunder + Strike into Assassin, which was a sequencing error because Tear's 2-cost left no energy for the second Strike. Used Power Potion on the 37-damage Frail turn and chose Unmovable over Pyre/Cruelty for immediate block scaling. Used Blood Wall + Shrug under Unmovable, then Impervious + Molten Fist to kill Assassin. Used Clarity Extract later to survive the Crossbow/Tracker turn, then Tear Asunder killed Tracker and Uppercut + Strike killed Crossbow.
- Outcome: won at 13/80 after Burning Blood; both potions spent; claimed Snecko Oil and 15 gold.
- Reflection: Against Ruby Raiders, kill Assassin with exact energy math before the Crossbow fire turn. If a 2-cost attack leaves the target alive, prefer two Strikes plus block or plan potion use immediately.

## Floor 8 - Card Reward

- Strategy file read: `kb/strategies/reward_choice.md`, `kb/strategies/card_impressions.md`, `history/run19_strategy.md`.
- Entity KB read: `kb/cards/ironclad/tremble.md`, `kb/cards/ironclad/unrelenting.md`, `kb/cards/ironclad/juggling.md`.
- Current HP/status: 13/80, 65 gold, Snecko Oil.
- Options: Tremble, Unrelenting, Juggling.
- Decision: take Unrelenting.
- Reason: Tremble is good Vul setup but overlaps Bash, Uppercut, and Molten Fist. Unrelenting adds frontload and can make Bash, Uppercut, or Tear Asunder free on 3-energy turns. Juggling is too slow and attack-count dependent for the current low-HP Act 1 state.

## Floor 9 - Inklets

- Strategy file read: `kb/strategies/combat.md`, `history/run19_strategy.md`.
- Entity KB read: `kb/enemies/overgrowth/inklet.md`, `kb/potions/snecko_oil.md`.
- Current HP/status: entered 13/80, 65 gold, Snecko Oil.
- Combat notes: First attempt used Blood Wall + Snecko Oil but spent the cheap Strike and Molten Fist into the middle Inklet. That left both outer Slippery stacks intact and produced a later double-11 turn that was not survivable, so I restarted the room with Save and Quit. Retry used Blood Wall + Snecko Oil, then stripped and damaged the left outer Inklet with Strike + Molten Fist. Impervious + Inflame covered turn 2, Blood Wall + Strike killed the damaged outer on turn 3, Strike + Uppercut killed the other outer on turn 4, and Shrug + Unrelenting + Strike set up Bash lethal on the last Inklet.
- Outcome: won at 8/80 after Burning Blood; Snecko Oil spent.
- Reflection: The reusable fix was not just "use Snecko" but "do not leave both outer Inklet Slippery stacks alive for the double Piercing Gaze window." Save/load was justified because the first line was mathematically losing before damage resolved.

## Floor 9 - Card Reward

- Strategy file read: `kb/strategies/reward_choice.md`, `history/run19_strategy.md`.
- Entity KB read: `kb/cards/ironclad/armaments.md`, `kb/cards/ironclad/molten_fist.md`, `kb/cards/ironclad/juggling.md`.
- Current HP/status: 8/80, 80 gold, no potions.
- Options: Armaments, Molten Fist, Juggling.
- Decision: take Armaments.
- Reason: Armaments gives immediate block and strong future value if upgraded. Another Molten Fist is damage-only, and Juggling is too slow for a run that must survive the next forced hallway at 8 HP.

## Floor 10 - Treasure

- Strategy file read: `history/run19_strategy.md`.
- Entity KB read: `kb/relics/toxic_egg.md`.
- Current HP/status: 8/80, 119 gold, no potions.
- Reward: Toxic Egg.
- Decision: claim Toxic Egg.
- Reason: It upgrades future Skill additions and improves post-rest deck development, though it does not solve the immediate forced hallway at 8 HP.

## Floor 11 - Paired Nibbits

- Strategy file read: `kb/strategies/combat.md`, `history/run19_strategy.md`.
- Entity KB read: `kb/enemies/overgrowth/nibbit.md`, `kb/cards/ironclad/armaments.md`, `kb/cards/ironclad/unrelenting.md`, `kb/cards/ironclad/tear_asunder.md`.
- Current HP/status: entered 8/80, 119 gold, no potions.
- Combat notes: Armaments upgraded Unrelenting in hand, enabling Unrelenting+ into free Bash on turn 1. Used Impervious to blank the first 16-damage scaled attack, then Defend plus two Strikes killed the front Nibbit at 1 HP. Battle Trance found Unrelenting+ for the last Nibbit; Inflame + Unrelenting+ + Tear Asunder left it at 13, and next-turn Uppercut killed before the 19-damage attack.
- Outcome: won at 7/80 after Burning Blood.
- Reflection: Tear Asunder's live "Hits N times" display is total hit count, not base-plus-N; this mattered when estimating lethal. Blood Wall was not safe at 1 HP, so low-HP lines must account for its up-front HP cost before treating it as block.

## Floor 11 - Card Reward

- Strategy file read: `kb/strategies/reward_choice.md`, `history/run19_strategy.md`.
- Entity KB read: `kb/cards/ironclad/true_grit.md`, `kb/cards/ironclad/havoc.md`, `kb/cards/ironclad/whirlwind.md`.
- Current HP/status: 7/80, 119 gold before rewards, no potions, Toxic Egg.
- Options: True Grit+, Havoc+, Whirlwind.
- Decision: take True Grit+; claim 8 gold.
- Reason: Toxic Egg turns True Grit into its controlled exhaust version immediately. The deck needs 1-energy block and starter/status cleanup more than random top-deck Havoc play or another unupgraded damage card.

## Floor 12 - Rest Site

- Strategy file read: `history/run19_strategy.md`.
- Current HP/status: 7/80, 127 gold, no potions.
- Options: Rest for 24 HP; Smith.
- Decision: Rest.
- Reason: The next path still contains unknowns/combat before the boss, and 7 HP is far below any defensible smith threshold despite strong upgrades available.
- Outcome: healed to 31/80.

## Floor 13 - Wellspring

- Strategy file read: `history/run19_strategy.md`.
- Entity KB read: `kb/events/wellspring.md`, `kb/cards/status/guilty.md`, `kb/potions/gamblers_brew.md`.
- Current HP/status: 31/80, 127 gold, no potions.
- Options: Bottle for a random potion; Bathe to remove a card and add Guilty.
- Decision: choose Bottle; claim Gambler's Brew.
- Reason: The deck needs a potion for the next hallway/boss more than it needs a removal that adds an Unplayable curse for the remaining Act 1 combats.

## Floor 13 - Route

- Strategy file read: `kb/strategies/pathing.md`, `history/run19_strategy.md`.
- Current HP/status: 31/80, 127 gold, Gambler's Brew.
- Options: Monster into forced Elite, or Unknown into Monster.
- Decision: take Unknown.
- Reason: The run is still recovering from low HP and should avoid a forced elite before Ceremonial Beast. The right path keeps the final rest and one required hallway while preserving boss survival odds.

## Floor 14 - Shop

- Strategy file read: `kb/strategies/reward_choice.md`, `history/run19_strategy.md`.
- Entity KB read: `kb/cards/ironclad/bloodletting.md`, `kb/cards/ironclad/blood_wall.md`, `kb/cards/ironclad/fight_me.md`, `kb/cards/ironclad/juggling.md`, `kb/cards/colorless/prep_time.md`, `kb/potions/heart_of_iron.md`, `kb/potions/mazaleth_s_gift.md`, `kb/potions/colorless_potion.md`, `kb/enemies/bosses/ceremonial_beast.md`.
- Current HP/status: 31/80, 127 gold, Gambler's Brew.
- Relevant options: Bloodletting+ 49g, Blood Wall+ 24g, Heart of Iron 75g, Colorless Potion 48g, removal 100g, other cards/relics unaffordable or lower priority.
- Decision: buy Bloodletting+ and Heart of Iron.
- Reason: Bloodletting+ is premium energy for Battle Trance/Unrelenting/Tear turns and is already upgraded. Heart of Iron gives repeated Plating for the final hallway or Ceremonial Beast. Blood Wall+ was efficient but adds another HP-loss block card when HP is still the limiting resource.

## Floor 15 - Cubex Construct

- Strategy file read: `kb/strategies/combat.md`, `history/run19_strategy.md`.
- Entity KB read: `kb/enemies/overgrowth/cubex_construct.md`, `kb/cards/ironclad/unrelenting.md`, `kb/cards/ironclad/armaments.md`.
- Current HP/status: entered 31/80, 3 gold, Gambler's Brew and Heart of Iron.
- Combat notes: Cubex opened with Charge Up, so I used Inflame plus two Strikes without spending Bloodletting HP. On the first attack turn, Battle Trance found Unrelenting and Uppercut; Armaments upgraded Unrelenting, then Unrelenting+ into free Uppercut cleared Artifact and left Vulnerable. Took 5 after 5 block. Next turn Bash plus Molten Fist killed before the second 12-damage ramp attack.
- Outcome: won at 32/80 after Burning Blood; both potions preserved.
- Reflection: Against Cubex, clearing Artifact with a multi-debuff attack after a large damage setup lets the second debuff stick; Unrelenting+ made Uppercut free and kept the fight short enough to avoid the Expel Blast ramp.

## Floor 15 - Card Reward

- Strategy file read: `kb/strategies/reward_choice.md`, `kb/strategies/card_impressions.md`, `history/run19_strategy.md`.
- Entity KB read: `kb/cards/ironclad/breakthrough.md`, `kb/cards/ironclad/drum_of_battle.md`, `kb/cards/ironclad/setup_strike.md`.
- Current HP/status: 32/80, 3 gold before rewards, Gambler's Brew and Heart of Iron.
- Options: Breakthrough, Drum of Battle, Setup Strike.
- Decision: skip; claim 9 gold.
- Reason: Breakthrough and Setup Strike are late filler before the boss, and Drum of Battle can exhaust Impervious or another key card from the draw pile at the start of turns.

## Floor 16 - Rest Site

- Strategy file read: `history/run19_strategy.md`, `kb/enemies/bosses/ceremonial_beast.md`.
- Current HP/status: 32/80, 12 gold, Gambler's Brew and Heart of Iron.
- Options: Rest for 24 HP; Smith.
- Decision: Rest.
- Reason: The deck already has enough boss damage tools and two potions, but 32 HP is too exposed to repeated Plow turns or a bad Ringing hand. The extra 24 HP is stronger than one upgrade for this specific boss entry.
- Outcome: healed to 56/80.

## Floor 17 - Ceremonial Beast

- Strategy file read: `kb/strategies/bosses.md`, `history/run19_strategy.md`.
- Entity KB read: `kb/enemies/bosses/ceremonial_beast.md`, `kb/potions/heart_of_iron.md`, `kb/potions/gamblers_brew.md`.
- Current HP/status: entered 56/80, 12 gold, Gambler's Brew and Heart of Iron.
- Combat notes: Used Heart of Iron on turn 1 for Plating. Uppercut+ kept Plow turns weak/vulnerable. On the key Plow turn, Tear Asunder plus Battle Trance/Bloodletting+ enabled Inflame and enough Strikes to cross the 160 HP stun threshold before the 24-damage Plow resolved. In phase 2, used Unrelenting as the single Ringing card, then carried its Free Attack into a free Uppercut+ on the following 19-damage turn and blocked with Blood Wall plus Defend. Battle Trance later found Tear Asunder at 7 hits, which killed under Vulnerable.
- Outcome: won at 29/80 after Burning Blood; Heart of Iron spent, Gambler's Brew preserved.
- Reflection: The winning boss line followed the KB plan exactly: use burst to cross the Plow threshold during a dangerous attack turn, then save the Ringing turn for one high-value card. Heart of Iron's Plating paid for early chip and made the Ringing attack line safe.

## Floor 17 - Boss Reward

- Strategy file read: `kb/strategies/card_impressions.md`, `kb/strategies/archetypes.md`, `history/run19_strategy.md`.
- Entity KB read: `kb/cards/ironclad/hellraiser.md`, `kb/cards/ironclad/crimson_mantle.md`, `kb/cards/ironclad/mangle.md`, `kb/potions/weak_potion.md`.
- Current HP/status: 29/80, 12 gold before rewards, Gambler's Brew.
- Options: Hellraiser, Crimson Mantle, Mangle; rewards were Weak Potion and 75 gold.
- Decision: take Crimson Mantle; claim Weak Potion and 75 gold.
- Reason: Crimson Mantle is repeatable block for Act 2 and fits the HP-cost deck with Burning Blood. Hellraiser is a low-signal Strike payoff without enough commitment, and Mangle is expensive single-target mitigation that does not solve repeatable block or deck consistency.

## Act 2 Start - Route Read

- Strategy file read: `kb/strategies/pathing.md`, `kb/strategies/bosses.md`, `kb/strategies/elites.md`, `history/run19_strategy.md`.
- Entity KB read: `kb/enemies/bosses/knowledge_demon.md`.
- Current HP/status: 29/80, 87 gold, Gambler's Brew and Weak Potion.
- Boss plan: Knowledge Demon adds repeated curse choices and attacks on a four-move cycle; controlled exhaust should be prioritized for curse/status cleanup, and potion/rest choices should preserve enough HP to handle Disintegration or Sloth/Waste Away tradeoffs.

## Floor 18 - Pael

- Strategy file read: `history/run19_strategy.md`, `kb/strategies/pathing.md`.
- Entity KB read: `kb/events/pael.md`, `kb/enemies/ancients/pael.md`, `kb/relics/pael_s_flesh.md`, `kb/relics/pael_s_wing.md`, `kb/relics/pael_s_legion.md`.
- Current HP/status: 69/80 after Act transition heal, 87 gold, Gambler's Brew and Weak Potion.
- Options: Pael's Flesh, Pael's Wing, Pael's Legion.
- Decision: take Pael's Legion.
- Reason: Pael's Legion immediately improves the deck's biggest survival cards: Impervious, Blood Wall, Shrug It Off, and True Grit+. Pael's Flesh is delayed energy and Bloodletting+ already covers burst energy; Pael's Wing is delayed value when the current run still needs immediate Act 2 stability.

## Floor 18 - Act 2 Route

- Strategy file read: `kb/strategies/pathing.md`, `kb/strategies/elites.md`, `history/run19_strategy.md`.
- Current HP/status: 69/80, 87 gold, Gambler's Brew and Weak Potion, Pael's Legion.
- Options: left Monster at (2,1) into Unknown/Monster and early shop branches; right Monster at (4,1) into multiple forced Monsters before shop/rest choices.
- Decision: take the left Monster at (2,1).
- Reason: Both starts are hallway fights, but the left branch gives earlier unknown/shop flexibility and can avoid an early forced elite. The right branch overcommits to repeated Act 2 hallways before the first safety point.

## Floor 19 - Exoskeletons

- Strategy file read: `kb/strategies/combat.md`, `history/run19_strategy.md`.
- Entity KB read: `kb/enemies/hive/exoskeleton.md`, `kb/mechanics/buffs.md`, `kb/relics/pael_s_legion.md`.
- Current HP/status: entered 69/80, 87 gold, Gambler's Brew and Weak Potion.
- Combat notes: Focused the Enrage-position Exoskeleton first. Battle Trance found Unrelenting and Molten Fist; both were capped by Hard to Kill but created two separate hits. Pael's Legion doubled the first Defend, later Armaments, and then Impervious. Bloodletting+ was worth spending on turn 2 because it converted into a kill, Shrug block, a Strike, and True Grit+ exhausting Ascender's Bane. Tear Asunder at 4 hits killed the low Exoskeleton through Hard to Kill.
- Outcome: won at 64/80 after Burning Blood; both potions preserved.
- Reflection: Hard to Kill makes separate hits more important than big raw damage. Pael's Legion should be saved for attack turns; spending it into no incoming would have wasted a major defensive cycle.

## Floor 19 - Card Reward

- Strategy file read: `kb/strategies/card_impressions.md`, `history/run19_strategy.md`.
- Entity KB read: `kb/cards/ironclad/breakthrough.md`, `kb/cards/ironclad/iron_wave.md`, `kb/cards/ironclad/armaments.md`, `kb/potions/swift_potion.md`.
- Current HP/status: 64/80, 87 gold before rewards, Gambler's Brew and Weak Potion.
- Options: Breakthrough, Iron Wave, Armaments+; rewards were Swift Potion and 8 gold.
- Decision: take Breakthrough; claim 8 gold; skip Swift Potion.
- Reason: Breakthrough patches the deck's AoE hole for Act 2 and possible Decimillipede. Armaments+ is strong but duplicates an existing card, Iron Wave is medium filler, and Swift Potion is less valuable than the current potion pair of Gambler's Brew plus Weak Potion.

## Floor 19 - Route

- Strategy file read: `kb/strategies/pathing.md`, `history/run19_strategy.md`.
- Current HP/status: 64/80, 95 gold, Gambler's Brew and Weak Potion.
- Options: Unknown at (1,2) into Unknown/Shop flexibility; Monster at (3,2) into Shop/Unknown.
- Decision: take the Unknown at (1,2).
- Reason: The deck just added AoE and is healthy enough, but the Unknown keeps an early shop option with 95 gold while avoiding another immediate Act 2 hallway.

## Floor 20 - The Lantern Key

- Strategy file read: `history/run19_strategy.md`, `kb/strategies/pathing.md`.
- Entity KB read: `kb/events/the_lantern_key.md`, `kb/enemies/unknown/mysterious_knight.md`.
- Current HP/status: 64/80, 95 gold, Gambler's Brew and Weak Potion.
- Options: Return the Key for 100 gold; Keep the Key and fight Mysterious Knight.
- Decision: Return the Key.
- Reason: Mysterious Knight is a 108 HP fight that opens with 17 damage, while the known reward path is only future Lantern Key access. Taking 100 gold immediately supports the next shop and is safer than adding another Act 2 fight.

## Floor 21 - Shop

- Strategy file read: `history/run19_strategy.md`, `kb/strategies/card_impressions.md`.
- Entity KB read: `kb/cards/ironclad/fight_me.md`, `kb/cards/ironclad/true_grit.md`, `kb/cards/ironclad/bloodletting.md`, `kb/cards/ironclad/stampede.md`, `kb/cards/colorless/splash.md`, `kb/cards/colorless/jackpot.md`, `kb/relics/blood_vial.md`, `kb/potions/strength_potion.md`, `kb/potions/blood_potion.md`, `kb/potions/vulnerable_potion.md`.
- Current HP/status: 64/80, 195 gold, Gambler's Brew and Weak Potion.
- Relevant options: Fight Me! 36g sale, True Grit+ 52g, Bloodletting+ 49g, Splash+ 90g, Blood Vial 179g, removal 100g, Strength/Blood/Vulnerable potions.
- Decision: buy Fight Me!, buy True Grit+, remove a Strike.
- Reason: Fight Me! adds scaling and two separate hits for capped-damage fights. A second True Grit+ improves block, status/curse cleanup, and Pael's Legion turns. Removing a Strike keeps the deck from growing too much and improves access to the new engine pieces. Blood Vial was too slow for 179g, and another Bloodletting+ would add more HP pressure than the deck currently needs.

## Floor 21 - Route After Shop

- Strategy file read: `kb/strategies/pathing.md`, `history/run19_strategy.md`.
- Current HP/status: 64/80, 7 gold, Gambler's Brew and Weak Potion.
- Options: only Monster at (1,4), then branch to Unknown or Monster.
- Decision: take the forced Monster.
- Reason: No alternative node is available. Preserve both potions unless the hallway threatens heavy HP loss, then choose the row 5 Unknown if HP is meaningfully chipped.

## Floor 22 - Thieving Hopper

- Strategy file read: `kb/strategies/combat.md`, `history/run19_strategy.md`.
- Entity KB read: `kb/enemies/hive/thieving_hopper.md`, `kb/mechanics/buffs.md`, `kb/cards/ironclad/sword_boomerang.md`, `kb/cards/ironclad/perfected_strike.md`, `kb/cards/ironclad/iron_wave.md`, `kb/potions/fortifier.md`.
- Current HP/status: entered 64/80, 7 gold, Gambler's Brew and Weak Potion.
- Combat notes: Opened Defend + Crimson Mantle + Breakthrough. Thieving Hopper stole Unrelenting after the unplayed hand discarded, correcting the earlier KB assumption that cards held in hand were safe. Used Fight Me! on the Flutter turn, True Grit+ to exhaust Ascender's Bane, then Tear Asunder's 5 hits stunned the Hat Trick attack. Bloodletting+ funded Uppercut + Strike + Battle Trance into Molten Fist lethal before Escape.
- Outcome: won at 54/80 after Burning Blood; Unrelenting recovered; Gambler's Brew preserved; Weak Potion replaced with Fortifier; claimed 13 gold.
- Card reward: took Sword Boomerang over Perfected Strike and Iron Wave.
- Reason: Sword Boomerang is a 1-energy multi-hit Strength payoff for Fight Me!/Inflame and helps future hit-count checks. Perfected Strike is late after a Strike removal, and Iron Wave is low-impact filler.
- Reflection: Against Thieving Hopper, play or accept losing key Uncommons on turn 1; unplayed hand cards are not protected because Swipe resolves after end-turn discard. Tear Asunder is excellent once self-damage has built enough hits to clear Flutter and stun the T3 attack.

## Floor 22 - Route

- Strategy file read: `kb/strategies/pathing.md`, `history/run19_strategy.md`.
- Current HP/status: 54/80, 20 gold, Gambler's Brew and Fortifier.
- Options: Unknown at (1,5) into Monster then RestSite/Elite choices; Monster at (2,5) into RestSite then forced Elite chain.
- Decision: take the Unknown.
- Reason: HP is stable but chipped, and the deck has no need to force another Act 2 hallway when the Unknown keeps rest access and avoids committing to the elite-heavy middle branch.

## Floor 23 - Spirit Grafter

- Strategy file read: `history/run19_strategy.md`, `kb/strategies/reward_choice.md`.
- Entity KB read: `kb/events/spirit_grafter.md`, `kb/cards/colorless/metamorphosis.md`, `kb/cards/ironclad/armaments.md`.
- Current HP/status: 54/80, 20 gold, Gambler's Brew and Fortifier.
- Options: Let It In for +25 HP and Metamorphosis; Rejection for -10 HP and an upgrade.
- Decision: choose Rejection and upgrade Armaments.
- Reason: The next route has a forced Monster but then a rest site, and the potion pair covers a bad hallway. Armaments+ is permanent deck-wide hand scaling in a medium deck with many unupgraded high-impact cards, while Metamorphosis adds another 2-cost setup card and random-output variance.
- Outcome: 44/80, Armaments upgraded.

## Floor 24 - Louse Progenitor

- Strategy file read: `kb/strategies/combat.md`, `history/run19_strategy.md`.
- Entity KB read: `kb/enemies/hive/louse_progenitor.md`, `kb/cards/ironclad/headbutt.md`, `kb/cards/ironclad/true_grit.md`, `kb/cards/ironclad/blood_wall.md`, `kb/potions/swift_potion.md`.
- Current HP/status: entered 44/80, 20 gold, Gambler's Brew and Fortifier.
- Combat notes: Armaments+ upgraded the opening hand and blocked Web Cannon, then Bash+ set 3 Vulnerable. Used Unrelenting into free Molten Fist on the free Curl turn, then Uppercut + True Grit+ covered Pounce with only 2 damage leaked. Bloodletting+ funded Shrug/Defend/Sword Boomerang/Crimson Mantle on the next Web Cannon turn. Finished on the next Pounce with Unrelenting into free Uppercut, avoiding an extra Bloodletting cost.
- Outcome: won at 40/80 after Burning Blood; both potions preserved.
- Card reward: took Headbutt over True Grit+ and Blood Wall+; skipped Swift Potion and claimed 13 gold.
- Reason: Headbutt can recur Uppercut, Battle Trance, Armaments+, Impervious, or lethal attacks and gives useful 1-energy damage. A third True Grit+ is redundant with two copies already, and a second Blood Wall+ adds more HP-cost block than the deck needs. Swift Potion is weaker than Gambler's Brew plus Fortifier.

## Floor 24 - Route

- Strategy file read: `kb/strategies/pathing.md`, `kb/strategies/elites.md`, `history/run19_strategy.md`.
- Current HP/status: 40/80, 33 gold, Gambler's Brew and Fortifier.
- Options: RestSite at (1,7), or Elite at (3,7) into a second elite-heavy middle route.
- Decision: take the RestSite.
- Reason: 40/80 after a costly hallway is below the Act 2 elite comfort threshold, and the deck still lacks a complete draw/exhaust/block engine. Preserve the potion pair and recover before considering later elites.

## Floor 25 - Rest Site

- Strategy file read: `kb/strategies/pathing.md`, `kb/strategies/reward_choice.md`, `history/run19_strategy.md`.
- Entity KB read: `kb/cards/ironclad/uppercut.md`.
- Current HP/status: 40/80, 33 gold, Gambler's Brew and Fortifier.
- Options: Rest for 24 HP; Smith.
- Decision: Smith Uppercut.
- Reason: The conservative branch ahead can go Treasure into Unknown/Monster before another rest, so 40 HP plus two defensive/consistency potions is playable. Uppercut+ is a high-impact upgrade because 2 Weak and 2 Vulnerable improve hallway safety, Headbutt recursion, Molten Fist duration, and Knowledge Demon damage windows.
- Outcome: Uppercut upgraded; HP remains 40/80.

## Floor 26 - Treasure

- Strategy file read: `history/run19_strategy.md`.
- Entity KB read: `kb/relics/gremlin_horn.md`.
- Current HP/status: 40/80, 72 gold, Gambler's Brew and Fortifier.
- Reward: Gremlin Horn.
- Decision: claim Gremlin Horn.
- Reason: Free relic; it improves multi-enemy fight sequencing by turning kills into energy and draw, which helps the deck convert Breakthrough/Sword Boomerang/Uppercut turns.

## Floor 27 - Stone of All Time

- Strategy file read: `history/run19_strategy.md`, `kb/strategies/combat.md`.
- Entity KB read: `kb/events/stone_of_all_time.md`, `kb/cards/enchants/vigorous.md`, `kb/cards/ironclad/sword_boomerang.md`.
- Current HP/status: 40/80, 72 gold, Gambler's Brew and Fortifier.
- Options: Drink and Lift to lose a random potion and gain 10 max HP; Push to lose 6 HP and enchant an Attack with Vigorous 8.
- Decision: choose Push and enchant Sword Boomerang.
- Reason: Fortifier is a strong defensive potion with Pael's Legion and large block cards. Vigorous 8 on Sword Boomerang applies across its three hits, creating a much stronger 1-energy burst card than a single-hit enchant.
- Outcome: 34/80, Sword Boomerang enchanted with Vigorous 8.

## Floor 28 - The Obscura

- Strategy file read: `history/run19_strategy.md`, `kb/strategies/combat.md`, `kb/strategies/reward_choice.md`.
- Entity KB read: `kb/enemies/hive/the_obscura.md`, `kb/cards/ironclad/infernal_blade.md`, `kb/cards/ironclad/colossus.md`, `kb/cards/ironclad/bloodletting.md`.
- Current HP/status: entered 34/80, 72 gold, Gambler's Brew and Fortifier.
- Combat notes: Played Inflame into Uppercut+ on the no-damage summon opener. On the first Slam turn, Bloodletting+ funded Crimson Mantle, Tear Asunder, Headbutt, and True Grit+; Headbutt put Uppercut+ back for the next draw. Killed Parafright with Uppercut+ plus Strike to prevent a 20-damage Slam and trigger Gremlin Horn, then used the refunded energy/draw for Vigorous Sword Boomerang damage on Obscura. Later used True Grit+ to exhaust Ascender's Bane, Battle Trance to refill, and a final Bloodletting+ plus Armaments+ to upgrade Bash and Headbutt for lethal through Obscura's block.
- Outcome: won at 20/80 after Burning Blood; both potions preserved; claimed 11 gold.
- Card reward: took Colossus+ over Infernal Blade+ and Bloodletting+.
- Reason: Colossus+ directly improves the block plan and has strong overlap with the deck's Bash/Uppercut Vulnerable package. Infernal Blade+ is random tempo, and a second Bloodletting+ adds more HP pressure when the run is already low.
- Reflection: Gremlin Horn made killing Parafright profitable enough to prevent a Slam without spending Fortifier. The fight was still expensive because Bloodletting+ and Crimson Mantle carried the damage race, so the next rest site should prioritize HP recovery unless the game offers an unusually critical smith.

## Floor 29 - Rest Site

- Strategy file read: `history/run19_strategy.md`, `kb/strategies/pathing.md`, `kb/strategies/elites.md`.
- Entity KB read: `kb/enemies/elites/decimillipede.md`, `kb/enemies/elites/entomancer.md`, `kb/enemies/elites/infested_prism.md`.
- Current HP/status: 20/80, 83 gold, Gambler's Brew and Fortifier.
- Options: Rest for 24 HP; Smith.
- Decision: Rest.
- Reason: The next node is a forced Hive elite before a Monster, RestSite, and Knowledge Demon. At 20 HP, even one strong upgrade is less valuable than entering the forced elite at 44 HP with both potions available.
- Outcome: healed to 44/80.

## Floor 30 - Decimillipede Elite

- Strategy file read: `history/run19_strategy.md`, `kb/strategies/elites.md`, `kb/strategies/reward_choice.md`.
- Entity KB read: `kb/enemies/elites/decimillipede.md`, `kb/relics/gremlin_horn.md`, `kb/potions/fortifier.md`, `kb/potions/gamblers_brew.md`, `kb/potions/block_potion.md`, `kb/relics/eternal_feather.md`, `kb/cards/ironclad/setup_strike.md`, `kb/cards/ironclad/burning_pact.md`, `kb/cards/ironclad/blood_wall.md`.
- Current HP/status: entered 44/80 with Gambler's Brew and Fortifier.
- Combat notes: Opened with Pael-doubled Impervious to block the first 28 and used Vigorous Sword Boomerang to soften two segments. Fortifier on a 14-block turn became 42 block and prevented a lethal scaling turn. Killed the middle segment with Tear Asunder, but Battle Trance's No Draw prevented Gremlin Horn from drawing a card, so the fight entered a reattach race. Used Gambler's Brew to find True Grit+ and Breakthrough, then later killed the back segment with a 10-hit Tear Asunder to reduce a 42-damage turn. Finished at 2 HP by using Bloodletting+ into Breakthrough, Fight Me!+, and a Horn-refunded Strike before the final segment could attack.
- Outcome: won at 8/80 after Burning Blood; spent Fortifier and Gambler's Brew; gained 28 gold, Block Potion, Eternal Feather, and Burning Pact+.
- Card reward: took Burning Pact+ over Setup Strike and Blood Wall+.
- Reason: Burning Pact+ fills the deck's draw/exhaust hole and is already upgraded by Toxic Egg. Setup Strike is low-impact frontload this late, and a second Blood Wall+ is less valuable than consistency when the deck already has large block but struggles to find it.
- Reflection: Decimillipede confirmed as a severe Act 2 elite for this deck: staggered kills and No Draw/Horn interaction almost lost the fight. Tear Asunder can rescue a reattach race once HP-loss has built enough hits, but this path should treat the next hallway as lethal-risk until Eternal Feather and the rest site recover the run.

## Floor 31 - Hunter Killer

- Strategy file read: `history/run19_strategy.md`, `kb/strategies/combat.md`, `kb/strategies/card_impressions.md`.
- Entity KB read: `kb/enemies/hive/hunter_killer.md`, `kb/potions/block_potion.md`, `kb/cards/ironclad/juggling.md`, `kb/cards/ironclad/breakthrough.md`, `kb/cards/ironclad/sword_boomerang.md`.
- Current HP/status: entered 8/80 with Block Potion.
- Combat notes: Hunter Killer opened Tenderizing Goop. Initial Bash/Sword Boomerang and Headbutt/Burning Pact lines left no stable block for the later 19/24 attack turns, so I used save-and-continue room restarts. The winning line opened Inflame, Vigorous Sword Boomerang, and Molten Fist, then used Pael's Legion on Blood Wall instead of spending the turn on damage. Headbutt put Colossus+ back for the next draw, Colossus+ plus Block Potion covered Bite, and Crimson Mantle supplied enough start-turn block to pair Defend with Uppercut+ on the next Puncture. Tear Asunder left the enemy at 4 HP, but True Grit+ let the run survive at 2 HP and Sword Boomerang killed next turn.
- Outcome: won at 7/80 after Burning Blood; spent Block Potion; gained 9 gold and Power Potion.
- Card reward: skipped Breakthrough, Sword Boomerang, and Juggling+.
- Reason: Breakthrough and Sword Boomerang were duplicate filler, and Juggling+ is an Innate setup card that competes with boss survival energy/draw. The deck needs recovery and reliable defense more than another damage engine piece before Knowledge Demon.
- Reflection: Save/load lesson: the successful retry changed the turn-2 priority from damage to a large Pael-doubled Blood Wall. Against Hunter Killer at single-digit HP, one large block card before Tender penalties is more valuable than drawing or playing several medium cards.

## Floor 32 - Rest Site

- Strategy file read: `history/run19_strategy.md`, `kb/strategies/pathing.md`, `kb/strategies/bosses.md`.
- Entity KB read: `kb/enemies/bosses/knowledge_demon.md`, `kb/relics/eternal_feather.md`.
- Current HP/status: entered at 7/80, then Eternal Feather healed 15 to 22/80; 120 gold; Power Potion.
- Options: Rest for 24 HP; Smith.
- Decision: Rest.
- Reason: Knowledge Demon deals 18, then 9x3, then 13 plus healing/Strength while also forcing curse choices. At 22 HP, a smith cannot cover the boss's opening damage plus this deck's Bloodletting/Blood Wall/Crimson Mantle HP costs.
- Outcome: healed to 46/80 before the Act 2 boss.

## Floor 33 - Knowledge Demon Boss

- Strategy file read: `history/run19_strategy.md`, `kb/strategies/bosses.md`, `kb/strategies/combat.md`.
- Entity KB read: `kb/enemies/bosses/knowledge_demon.md`, `kb/cards/status/disintegration.md`, `kb/cards/status/mind_rot.md`, `kb/cards/status/sloth.md`, `kb/cards/status/waste_away.md`, `kb/cards/ironclad/crimson_mantle.md`, `kb/cards/ironclad/rupture.md`, `kb/cards/ironclad/vicious.md`, `kb/cards/ironclad/tear_asunder.md`.
- Current HP/status: entered at 46/80, 120 gold, Power Potion; relics Burning Blood, New Leaf, Toxic Egg, Pael's Legion, Gremlin Horn, Eternal Feather.
- Power Potion: offered Crimson Mantle, Vicious, and Rupture. Rupture looked tempting with Disintegration, but testing showed Disintegration is blockable and does not trigger Rupture if block absorbs the HP loss. The final attempt chose Crimson Mantle for recurring block.
- Retry notes: Disintegration-first lines lost to the HP clock even with Crimson Mantle. Rupture plus Disintegration was worse than expected because blocked Disintegration damage produced no Strength. The best line chose Mind Rot first and Sloth second, used Bash plus True Grit+ instead of Armaments+Bash on the first 10x3 turn, and reached the boss at 50 HP with 1 player HP before Crimson Mantle killed at the next turn start.
- Combat notes: Opened Power Potion into Crimson Mantle, Fight Me!, and Breakthrough. Chose Mind Rot over Disintegration. Used Pael-doubled True Grit+ to block Slap and Bash plus True Grit+ to partially cover 10x3 while preserving Impervious. Battle Trance into Defend plus a Vulnerable Tear Asunder dealt 84 before Ponder healed. Chose Sloth over the second Disintegration, then used Unrelenting into free Uppercut+ and Vigorous Sword Boomerang for the biggest burst turn. On the later 13x3, True Grit+ plus Breakthrough plus Strike survived at 2 HP and enabled a 14-hit Tear Asunder, but the recurring Crimson Mantle HP loss created an unavoidable final turn at 1 HP.
- Outcome: died to Knowledge Demon on floor 33. Steam run log `1778855698.run` confirms `win: false`, `was_abandoned: false`, `killed_by_encounter: ENCOUNTER.KNOWLEDGE_DEMON_BOSS`, and `killed_by_event: NONE.NONE`.
- Reflection: Resting on floor 32 was correct, but the boss still needed either more starting HP, less self-damage, or a stronger scaling potion/power. Crimson Mantle was strong block but became a lethal upkeep clock at 1 HP. Against Knowledge Demon, avoid assuming Disintegration is a Rupture engine unless the HP loss is actually unblocked; choose Sloth/Mind Rot only when the deck can still win with three high-impact cards per turn.

## Post-Run Reflection

- What worked: Vulnerable plus Molten Fist, Vigorous Sword Boomerang, and Tear Asunder produced real boss damage; Power Potion into Crimson Mantle bought several attack turns that otherwise would have been impossible.
- What cost avoidable equity: The Act 2 path forced a late elite and hallway while already low, spending both defensive potions before the boss. Bloodletting/Blood Wall/Crimson Mantle self-damage left too little HP margin for Knowledge Demon's fixed multi-hit cycle.
- Next change with the same information: prioritize a safer Act 2 route or earlier recovery before forced Hive elites; enter Knowledge Demon with enough HP to pay for one curse clock plus self-damage, or pivot harder into non-HP-cost block.
- Promoted lessons: Disintegration damage is blockable and only triggers Rupture when it actually removes HP; Crimson Mantle can solve block but kill at start of turn; Sloth is sometimes better than Disintegration at low HP, but only if the deck's key turns fit under the 3-card cap.
