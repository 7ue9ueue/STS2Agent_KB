# Run 24 - Ironclad A10

- Date: 2026-05-16
- Character: Ironclad
- Ascension: 10
- Outcome: Loss
- Floor reached: Act 2 Floor 33

## Pre-Run Setup
- Read: AGENTS.md; GUIDE.md; all files in kb/strategies/ (`_index.md`, `ironclad.md`, `pathing.md`, `reward_choice.md`, `deck_size.md`, `combat.md`, `elites.md`, `bosses.md`, `archetypes.md`, `card_impressions.md`, `meta_play.md`).
- Decision: Start a new standard Ironclad run with MCP transcript logging assigned to `run24`.
- Reason: Follow the mandatory pre-run strategy reads and pair the run history with tool logs before making gameplay decisions.

## Floor 1 - Neow
- Read: history/run24_strategy.md; kb/strategies/reward_choice.md; kb/strategies/ironclad.md; kb/enemies/ancients/neow.md; kb/relics/golden_pearl.md; kb/relics/lost_coffer.md; kb/relics/hefty_tablet.md; kb/cards/status/injury.md.
- Status: 64/80 HP, 99 gold, Burning Blood. Options: Golden Pearl, Lost Coffer, Hefty Tablet.
- Decision: Choose Lost Coffer.
- Reason: Lost Coffer gives an immediate card reward and random potion with no curse or HP/max-HP downside. Act 1 needs controlled frontload and potion equity before pathing; Golden Pearl delays value until a shop, and Hefty Tablet's rare-card upside is offset by Injury and high variance.

## Floor 1 - Lost Coffer Card Reward
- Read: history/run24_strategy.md; kb/strategies/reward_choice.md; kb/strategies/card_impressions.md; kb/cards/ironclad/twin_strike.md; kb/cards/ironclad/vicious.md; kb/cards/ironclad/shrug_it_off.md.
- Status: 64/80 HP, 99 gold, Energy Potion pending. Offered Twin Strike / Vicious / Shrug It Off.
- Decision: Pick Twin Strike.
- Reason: The deck still needs immediate Act 1 damage before seeing early fights or the boss. Vicious is a strong engine only with repeated Vulnerable support, and Shrug is a strong cantrip block card but does not solve the starter deck's first damage gap.

## Floor 1 - Pathing
- Read: history/run24_strategy.md; kb/strategies/pathing.md; kb/strategies/bosses.md; kb/enemies/bosses/vantom.md; kb/potions/energy_potion.md.
- Status: 64/80 HP, 99 gold, Energy Potion, Burning Blood, Lost Coffer, Twin Strike added. Act boss: Vantom.
- Decision: Choose left Monster at (2,1).
- Reason: Vantom's Slippery 9 rewards Twin Strike and future multi-hit/frontload, while Dismember makes real block/draw important before the boss. The left route has flexible branching to early shop/rest options and can still take early hallway rewards; the right route is more linear with several forced combats before meaningful branch control.

## Floor 2 - Nibbit
- Read: history/run24_strategy.md; kb/strategies/combat.md; kb/strategies/meta_play.md; kb/mechanics/save_and_load.md; kb/enemies/overgrowth/nibbit.md.
- Status: Entered at 64/80 HP, 99 gold, Energy Potion. Solo Nibbit opened with 13 damage.
- Initial line: Bash + Twin Strike, ending turn with no block. This was winning but took the full 13.
- Save/load branch: Restarted the room and replayed Bash + Defend, then used the vulnerable turn for two Strikes plus Defend, then killed after Hiss.
- Result: Won at 60/80 HP after Burning Blood, kept Energy Potion. The reload branch preserved 5 HP versus the first line and did not spend resources.
- Lesson: Against solo Nibbit, all-out damage is not automatically best if a partial-block line still kills before the next real attack. Added this to kb/enemies/overgrowth/nibbit.md and expanded branch-search guidance in kb/mechanics/save_and_load.md.

## Floor 2 - Card Reward
- Read: history/run24_strategy.md; kb/strategies/reward_choice.md; kb/strategies/card_impressions.md; kb/strategies/ironclad.md; kb/strategies/elites.md; kb/enemies/bosses/vantom.md; kb/cards/ironclad/thunderclap.md; kb/cards/ironclad/setup_strike.md; kb/cards/ironclad/bludgeon.md.
- Status: 60/80 HP, 113 gold, Energy Potion, deck has Twin Strike as first added attack. Offered Thunderclap / Setup Strike / Bludgeon.
- Decision: Pick Bludgeon.
- Reason: The reward playbook says Act 1 needs frontloaded attacks, and Bludgeon's KB calls it strong Act 1 frontload when the deck lacks a clean elite/boss damage card. Thunderclap is weak standalone without Vicious/AoE need, and Setup Strike is only temporary same-turn scaling; Bludgeon best improves hallway and elite kill speed, with Energy Potion available to cover a key 5-energy turn.

## Floor 2 - Pathing
- Read: history/run24_strategy.md; kb/strategies/pathing.md; kb/enemies/bosses/vantom.md.
- Status: 60/80 HP, 113 gold, Energy Potion, deck has Twin Strike + Bludgeon.
- Decision: Choose Monster at (3,2).
- Reason: The pathing playbook says early Act 1 hallway fights are valuable when HP is stable. With Bludgeon and Energy Potion, the deck can use more card rewards before Vantom; this branch keeps broad future options, including rest sites, shops, treasure, and optional elites, instead of locking into the narrower early shop/rest branch.

## Floor 3 - Fuzzy Wurm Crawler
- Read: history/run24_strategy.md; kb/strategies/combat.md; kb/enemies/overgrowth/fuzzy_wurm_crawler.md.
- Status: Entered at 60/80 HP, 113 gold, Energy Potion. Fuzzy Wurm Crawler opened with Acid Goop for 6, then Inhale, then buffed Acid Goop.
- Line: Played Strike + Twin Strike + Defend to take only 1, then Bash + Strike during Inhale, then Bludgeon killed through Vulnerable before the 13-damage attack.
- Result: Won at 65/80 HP after Burning Blood, kept Energy Potion.
- Lesson: Frontload during Acid Goop/Inhale so the first buffed attack never lands. Added this to kb/enemies/overgrowth/fuzzy_wurm_crawler.md.

## Floor 3 - Rewards
- Read: history/run24_strategy.md; kb/potions/energy_potion.md; kb/potions/swift_potion.md; kb/strategies/reward_choice.md; kb/strategies/card_impressions.md; kb/cards/ironclad/stone_armor.md; kb/cards/ironclad/bloodletting.md; kb/cards/ironclad/iron_wave.md.
- Status: 65/80 HP, 120 gold after claiming 7 gold, potions Energy Potion + Swift Potion. Offered Stone Armor / Bloodletting / Iron Wave.
- Decision: Pick Bloodletting.
- Reason: Bloodletting's KB identifies it as a core energy-positive card, and this deck already has Bludgeon as a premium energy sink. Swift Potion can draw into more cards for Bloodletting turns. Stone Armor is slower setup without Barricade/Juggernaut support, and Iron Wave is low-impact filler.

## Floor 3 - Pathing
- Read: history/run24_strategy.md; kb/strategies/pathing.md; kb/enemies/bosses/vantom.md.
- Status: 65/80 HP, 120 gold, Energy Potion + Swift Potion, deck has Bludgeon/Bloodletting/Twin Strike.
- Decision: Choose Unknown at (4,3).
- Reason: The alternate Monster branch forced a long hallway chain before recovery. The Unknown branch preserved rest-site, shop, treasure, and optional-elite flexibility while still allowing more rewards before Vantom.

## Floor 4 - Brain Leech
- Read: history/run24_strategy.md; kb/events/brain_leech.md; kb/mechanics/save_and_load.md; kb/strategies/reward_choice.md; kb/cards/ironclad/pommel_strike.md; kb/cards/ironclad/uppercut.md; kb/cards/ironclad/forgotten_ritual.md; kb/cards/colorless/the_bomb.md; kb/cards/colorless/prowess.md; kb/cards/colorless/mind_blast.md.
- Status: 65/80 HP, 120 gold, Energy Potion + Swift Potion.
- Save/load branch 1: Share Knowledge offered Thunderclap / Pommel Strike / Havoc / Uppercut / Forgotten Ritual.
- Save/load branch 2: Rip the Leech Off cost 5 HP and offered The Bomb / Prowess / Mind Blast.
- Decision: Choose Share Knowledge and pick Pommel Strike.
- Reason: Pommel Strike's KB identifies it as premier Act 1 damage plus draw and a core upgrade target; it directly supports Bloodletting/Bludgeon turns without spending HP. The Colorless branch did not justify paying 5 HP, and Uppercut was good but less aligned than Pommel with the current draw/energy plan.
- Lesson: Added Brain Leech note to inspect both branches with save/load and avoid paying HP unless the Colorless branch clearly wins.

## Floor 4 - Pathing
- Read: history/run24_strategy.md; kb/strategies/pathing.md; kb/enemies/bosses/vantom.md.
- Status: 65/80 HP, 120 gold, Energy Potion + Swift Potion, Pommel Strike added.
- Decision: Choose Monster at (4,4).
- Reason: Both next nodes were combats, but the right branch led to an Unknown and possible earlier Rest Site, while the left branch forced another monster first. This preserved recovery and event flexibility.

## Floor 5 - Slimes
- Read: history/run24_strategy.md; kb/strategies/combat.md; kb/enemies/overgrowth/slimes.md.
- Status: Entered at 65/80 HP, 120 gold, Energy Potion + Swift Potion. Encounter: Leaf Slime (S), Leaf Slime (M), Twig Slime (S).
- Line: Killed Leaf Slime (S) with Twin Strike + Strike to prevent one Slimed, blocked Twig's 5. Next turn killed Twig with Pommel Strike, double-blocked Leaf Slime (M)'s 9, then used Bludgeon to leave it at 2 and killed it next turn.
- Result: Won at 71/80 HP after Burning Blood, preserved Energy Potion and Swift Potion.
- Lesson: In mixed Slime fights, reducing status load while blocking small attacks is better than spending Bloodletting HP just to avoid temporary Slimed cards. Added this to kb/enemies/overgrowth/slimes.md.

## Floor 5 - Card Reward
- Read: history/run24_strategy.md; kb/strategies/reward_choice.md; kb/cards/ironclad/twin_strike.md; kb/cards/ironclad/blood_wall.md; kb/cards/ironclad/tremble.md; kb/enemies/bosses/vantom.md.
- Status: 71/80 HP, 133 gold, Energy Potion + Swift Potion. Offered Twin Strike / Blood Wall / Tremble.
- Decision: Pick Blood Wall.
- Reason: Vantom's KB calls T3 Dismember a 30-damage survival check, and the live strategy file listed reliable block as the main hole. Tremble is strong Vul setup and Twin Strike helps Slippery, but the deck already has Bash, Twin Strike, Pommel Strike, Bludgeon, and Bloodletting for damage. Blood Wall adds a one-card block answer for elites and Vantom.

## Floor 5 - Pathing
- Read: history/run24_strategy.md; kb/strategies/pathing.md; kb/enemies/bosses/vantom.md.
- Status: 71/80 HP, 133 gold, Energy Potion + Swift Potion.
- Decision: Choose Unknown at (5,5).
- Reason: It was the only next node and preserved an immediate Rest Site option afterward.

## Floor 6 - Self-Help Book
- Read: history/run24_strategy.md; kb/events/self_help_book.md; kb/strategies/combat.md; kb/cards/ironclad/twin_strike.md; kb/cards/ironclad/bludgeon.md; kb/cards/ironclad/blood_wall.md; kb/cards/ironclad/pommel_strike.md.
- Status: 71/80 HP, 133 gold, Energy Potion + Swift Potion. Options: Sharp 2 Attack enchant, Nimble 2 Skill enchant, Power option locked.
- Decision: Choose Sharp 2 on Twin Strike.
- Reason: Self-Help Book's KB says Sharp is highest leverage on repeat-hit attacks. Twin Strike gets the bonus on both hits, improves the Vantom Slippery plan, and adds repeatable frontload; Nimble 2 on Blood Wall was useful but did not by itself solve the 30-damage Dismember threshold.
- Lesson: Added Twin Strike note that Sharp enchantments are high leverage because the bonus applies to both hits.

## Floor 6 - Pathing
- Read: history/run24_strategy.md; kb/strategies/pathing.md; kb/enemies/bosses/vantom.md.
- Status: 71/80 HP, 133 gold, Energy Potion + Swift Potion.
- Decision: Choose Unknown over immediate Rest Site.
- Reason: The Unknown still allowed an immediate Rest Site afterward, while taking the Rest Site now would skip a value node at high HP with two potions.

## Floor 7 - Shop
- Read: history/run24_strategy.md; kb/strategies/reward_choice.md; kb/cards/ironclad/armaments.md; kb/cards/colorless/flash_of_steel.md; kb/cards/ironclad/setup_strike.md; kb/cards/ironclad/sword_boomerang.md; kb/potions/clarity_extract.md; kb/potions/block_potion.md; kb/potions/swift_potion.md; kb/potions/energy_potion.md; kb/potions/explosive_ampoule.md.
- Status: 71/80 HP, 133 gold, Energy Potion + Swift Potion. Shop had Flash of Steel 85g, Armaments 49g, removal 100g, Block Potion 48g, Clarity Extract 73g, other unaffordable relics/cards.
- Decision: Buy Flash of Steel, discard Swift Potion, buy Block Potion.
- Reason: Flash of Steel is a 0-cost attack cantrip that supports Bloodletting turns and adds another cheap Vantom Slippery hit. With Flash/Pommel improving draw, Block Potion is a better second potion than Swift Potion because it gives guaranteed burst defense for elites or Vantom's Dismember.
- Lesson: Added missing Explosive Ampoule potion KB and added a Flash of Steel shop-buy note.

## Floor 7 - Pathing
- Read: history/run24_strategy.md; kb/strategies/pathing.md; kb/enemies/bosses/vantom.md.
- Status: 71/80 HP, 0 gold, Energy Potion + Block Potion.
- Decision: Choose Unknown over Rest Site.
- Reason: The Rest Site branch immediately committed into a very elite-heavy line, while the Unknown branch still reached a Rest Site next floor and kept later routing flexible.

## Floor 8 - Aroma of Chaos
- Read: history/run24_strategy.md; kb/events/aroma_of_chaos.md; kb/mechanics/save_and_load.md; kb/cards/ironclad/pommel_strike.md; kb/cards/ironclad/blood_wall.md; kb/cards/ironclad/bloodletting.md.
- Status: 71/80 HP, 0 gold, Energy Potion + Block Potion.
- Save/load branch: Tried transforming a basic Strike, but the replacement was not visible through the live event state after confirmation, so the branch was not safe to commit.
- Decision: Reload, choose Maintain Control, upgrade Pommel Strike.
- Reason: Pommel Strike+ is a tier-1 upgrade and the deck's best draw/energy core piece. The next Rest Site can still smith another high-impact card before any dangerous branch.
- Lesson: Added Aroma of Chaos note: inspect transforms when visible, but prefer guaranteed premium upgrades if the replacement cannot be verified.

## Floor 9 - Rest Site
- Read: history/run24_strategy.md; kb/strategies/pathing.md; kb/strategies/reward_choice.md; kb/cards/ironclad/blood_wall.md; kb/cards/ironclad/bloodletting.md; kb/cards/ironclad/bludgeon.md; kb/cards/ironclad/bash.md.
- Status: 71/80 HP, 0 gold, Energy Potion + Block Potion.
- Decision: Smith Bloodletting.
- Reason: HP was high enough that Rest was unnecessary. Bloodletting+ gives +3 energy for the same 3 HP cost, directly supporting Pommel+/Flash draw turns, Bludgeon, and Blood Wall. Blood Wall+ remains a later pre-boss candidate, but Block Potion already covers the immediate burst-defense gap.

## Floor 10 - Treasure
- Read: history/run24_strategy.md; kb/relics/mercury_hourglass.md.
- Status: 71/80 HP, 32 gold, Energy Potion + Block Potion.
- Decision: Claim Mercury Hourglass.
- Reason: The relic is free from the chest. Its KB notes strong hallway and multi-enemy value; passive start-of-turn AoE also helps strip small enemies and supports the deck's frontload plan without spending energy.

## Floor 11 - Nibbits
- Read: history/run24_strategy.md; kb/strategies/combat.md; kb/enemies/overgrowth/nibbit.md.
- Status: Entered at 71/80 HP, 32 gold, Energy Potion + Block Potion. Encounter: paired Nibbits, front attacking/blocking and back buffing.
- Line: Bludgeoned the front Nibbit on turn 1 and accepted 7 damage rather than spend Energy Potion. Turn 2 used Sharp Twin Strike to kill the front Nibbit through block, then Blood Wall fully blocked the back Nibbit's 16. Turn 3 used Pommel Strike+ and Flash of Steel, then Bloodletting+ to convert a 5-damage leak into 3 self-damage while playing Bash, Strike, and two Defends. Killed on turn 4 with Twin Strike.
- Result: Won at 65/80 HP after Burning Blood, preserved Energy Potion and Block Potion.
- Branch note: No reload was needed; the live branch found a lower-HP-loss line by using Bloodletting+ only after Flash drew Bash and the extra energy could both accelerate lethal and cover the attack.

## Floor 11 - Card Reward
- Read: history/run24_strategy.md; kb/strategies/reward_choice.md; kb/enemies/bosses/vantom.md; kb/cards/ironclad/thunderclap.md; kb/cards/ironclad/anger.md; kb/cards/ironclad/blood_wall.md.
- Status: 65/80 HP, 39 gold after claiming gold, Energy Potion + Block Potion. Offered Thunderclap / Anger / Blood Wall.
- Decision: Pick Anger.
- Reason: Vantom's KB says Slippery 9 requires multiple damage instances before real damage starts. One Anger gives a 0-cost hit that works with Pommel/Flash/Bloodletting turns and helps strip Slippery. Thunderclap was weak without Vicious and the deck already has Bash; a second Blood Wall would improve Dismember odds but adds another 2-cost HP-loss block card when we already have Blood Wall plus Block Potion.
- Lesson: Added Anger note that one Act 1 copy can be justified for Vantom Slippery but more copies require draw/exhaust control.

## Floor 11 - Pathing
- Read: history/run24_strategy.md; kb/strategies/pathing.md; kb/strategies/elites.md; kb/enemies/elites/bygone_effigy.md; kb/enemies/elites/byrdonis.md; kb/enemies/elites/phrog_parasite.md; kb/enemies/bosses/vantom.md.
- Status: 65/80 HP, 39 gold, Energy Potion + Block Potion.
- Decision: Choose Unknown at (5,11), accepting a forced elite next.
- Reason: Pathing KB says Act 1 elites are acceptable with strong frontload, HP, potions, and recovery afterward. This deck has Bludgeon, Bash, Bloodletting+, Pommel/Flash draw, Sharp Twin Strike, Blood Wall, and two premium potions. Effigy is a frontload race that Bludgeon/Bloodletting can support; Byrdonis and Phrog are covered by Blood Wall/Block Potion and Mercury Hourglass. The Unknown offers possible event value before the elite and the path still reaches a Rest Site before Vantom.

## Floor 12 - Snapping Jaxfruit + Flyconid
- Read: history/run24_strategy.md; kb/enemies/overgrowth/snapping_jaxfruit.md; kb/enemies/overgrowth/flyconid.md.
- Status: Entered at 65/80 HP, 39 gold, Energy Potion + Block Potion. Unknown rolled into a hallway fight.
- Line: Opened with Blood Wall and Sharp Twin Strike into Jaxfruit, fully blocking 13 incoming for 2 HP. Turn 2 used Flash on Jaxfruit, then Bloodletting+ after Flash drew Bludgeon; Bash + Strike killed Jaxfruit and Bludgeon dropped Flyconid to 14 before it could attack again. Turn 3 Pommel Strike+ drew Anger/Strike, and Anger killed through the 18 incoming attack.
- Result: Won at 66/80 HP after Burning Blood, preserved Energy Potion and Block Potion.
- Branch note: Defensive opener into Bloodletting burst was the best resource line seen; it traded 5 player-turn HP for preventing Jaxfruit scaling and Flyconid's Vulnerable attack.

## Floor 12 - Card Reward
- Read: history/run24_strategy.md; kb/strategies/reward_choice.md; kb/cards/ironclad/armaments.md; kb/cards/ironclad/inferno.md; kb/cards/ironclad/body_slam.md.
- Status: 66/80 HP, 54 gold after claiming gold, Energy Potion + Block Potion. Offered Armaments / Inferno / Body Slam.
- Decision: Pick Armaments.
- Reason: Armaments' KB says it is strong when it can be upgraded, and this deck has many high-impact unupgraded cards in hand targets: Bludgeon, Blood Wall, Bash, Anger, and starter cards. Inferno has self-damage synergy but risks ongoing HP drain before Vantom; Body Slam is premature with only one large block source and no Barricade/Unmovable.

## Floor 13 - Elite: Phrog Parasite
- Read: history/run24_strategy.md; kb/enemies/elites/phrog_parasite.md; kb/enemies/overgrowth/wriggler.md; kb/cards/status/infection.md.
- Status: Entered at 66/80 HP, 54 gold, Energy Potion + Block Potion.
- Line: Turn 1 used Flash, Anger, and three Strikes while Phrog infected. Turn 2 used Bloodletting+ to play Bash, Sharp Twin Strike, and two Defends, preserving Block Potion while taking 10 from Lash. Killed Phrog with Pommel Strike+ to preserve energy for the Wriggler phase. Focused Wrigglers one at a time, using Armaments to upgrade a Strike in hand and Bloodletting later to kill one Wriggler while blocking the other. Preserved both potions.
- Result: Won at 47/80 HP after Burning Blood. Took Juggernaut, Book of Five Rings, and 26 gold; skipped Fire Potion to keep Energy Potion + Block Potion.
- Branch note: The no-potion branch cost substantial HP but preserved both boss potions and remained above the Act 1 boss median threshold with a Rest Site still available.

## Floor 13 - Elite Rewards
- Read: history/run24_strategy.md; kb/strategies/reward_choice.md; kb/cards/ironclad/juggernaut.md; kb/cards/ironclad/cinder.md; kb/cards/ironclad/twin_strike.md; kb/relics/book_of_five_rings.md; kb/potions/fire_potion.md; kb/potions/energy_potion.md; kb/potions/block_potion.md.
- Status: 47/80 HP, 80 gold after claiming gold, Energy Potion + Block Potion. Offered Juggernaut / Cinder / Twin Strike; relic was Book of Five Rings; potion was Fire Potion.
- Decision: Pick Juggernaut, claim Book of Five Rings, skip Fire Potion.
- Reason: Juggernaut gives a Vantom plan where block turns also strip Slippery and deal damage while defending Dismember. Cinder is efficient frontload but random exhaust is not needed; another unenchanted Twin Strike is less important after Sharp Twin Strike, Anger, Flash, and Mercury Hourglass. Book of Five Rings now makes future card additions worth 20 HP every fifth card, but Fire Potion is lower value than Energy Potion and Block Potion for the boss.
- Lesson: Added Book of Five Rings note to count its counter before close card picks without adding weak cards solely for healing.

## Floor 13 - Pathing
- Read: history/run24_strategy.md; kb/strategies/pathing.md; kb/enemies/bosses/vantom.md.
- Status: 47/80 HP, 80 gold, Energy Potion + Block Potion.
- Decision: Choose Unknown at (6,13) over Monster into forced Elite.
- Reason: Pathing KB says avoid optional elites unless HP/potions are very healthy. After Phrog, HP is 59% and the left branch would force a second elite before the final Rest Site. The Unknown branch can go Shop or Unknown next and still reaches the last Rest Site before Vantom.

## Floor 14 - Room Full of Cheese
- Read: history/run24_strategy.md; kb/events/room_full_of_cheese.md; kb/mechanics/save_and_load.md; kb/strategies/reward_choice.md; kb/cards/ironclad/shrug_it_off.md; kb/cards/ironclad/sword_boomerang.md; kb/cards/ironclad/bloodletting.md; kb/cards/ironclad/breakthrough.md; kb/cards/ironclad/armaments.md; kb/cards/ironclad/havoc.md; kb/cards/ironclad/anger.md; kb/cards/ironclad/twin_strike.md; kb/enemies/bosses/vantom.md.
- Status: 47/80 HP, 80 gold, Energy Potion + Block Potion, Book of Five Rings 0/5. Event options were Gorge for two commons or Search for Chosen Cheese at 14 HP.
- Save/load branch: Search would drop to 33/80 before the final Rest Site. Gorge revealed Havoc / Shrug It Off / Anger / Breakthrough / Sword Boomerang / Twin Strike / Bloodletting / Armaments and was locked after inspection.
- Decision: Pick Shrug It Off and Sword Boomerang from Gorge.
- Reason: Shrug It Off adds efficient block plus draw for Bloodletting/Juggernaut turns, and Sword Boomerang gives three 1-cost damage instances that help strip Vantom's Slippery. Search's relic is attractive, but paying 14 HP would likely force Rest over Smith before the boss. Gorge also advances Book of Five Rings to 2/5.
- Lesson: Added Room Full of Cheese note that branch-inspected Gorge can beat Search when the card pool contains premium commons and/or Book of Five Rings progress matters.

## Floor 14 - Pathing to Shop
- Read: history/run24_strategy.md; kb/strategies/pathing.md; kb/enemies/bosses/vantom.md.
- Status: 47/80 HP, 80 gold, Energy Potion + Block Potion, Book of Five Rings 2/5.
- Decision: Choose Shop over Unknown before the final Rest Site.
- Reason: Pathing KB says shops are preferable when they can buy a boss-specific potion, block card, or removal. With medium HP and an Act 1 boss next, the shop was lower variance than a question mark and could preserve Smith equity at the final rest site.

## Floor 15 - Shop
- Read: history/run24_strategy.md; kb/cards/ironclad/true_grit.md; kb/cards/ironclad/tremble.md; kb/cards/ironclad/rampage.md; kb/cards/ironclad/armaments.md; kb/cards/ironclad/blood_wall.md; kb/cards/ironclad/juggernaut.md; kb/potions/fysh_oil.md; kb/potions/vulnerable_potion.md; kb/enemies/bosses/vantom.md.
- Status: 47/80 HP, 80 gold, Energy Potion + Block Potion. Affordable notable options: True Grit 25g, Tremble 48g, Rampage 74g, Fysh Oil 77g, Vulnerable Potion 50g.
- Decision: Buy True Grit and Tremble, leaving 7 gold and keeping Energy Potion + Block Potion.
- Reason: True Grit gives block/exhaust for Vantom Wounds and Juggernaut triggers; Tremble adds a 1-cost Vulnerable source that exhausts and avoids depending only on Bash. Buying both was stronger than replacing either boss potion with Fysh Oil/Vulnerable Potion and moved Book of Five Rings to 4/5 for a near-term heal. Rampage was too slow for Slippery and the current draw density.

## Floor 16 - Rest Site
- Read: history/run24_strategy.md; kb/strategies/pathing.md; kb/enemies/bosses/vantom.md; kb/cards/ironclad/armaments.md; kb/cards/ironclad/true_grit.md; kb/cards/ironclad/juggernaut.md; kb/cards/ironclad/bludgeon.md; kb/cards/ironclad/shrug_it_off.md; kb/cards/ironclad/sword_boomerang.md.
- Status: 47/80 HP, 7 gold, Energy Potion + Block Potion, Book of Five Rings 4/5.
- Save/load branch: Inspected the Smith screen. Strong targets existed (Armaments+, True Grit+, Juggernaut+, Bludgeon+), and the screen was cancelable.
- Decision: Cancel Smith inspection and Rest to 71/80.
- Reason: Vantom's KB calls it a high-damage boss with a T3 30-damage Dismember and Wound shuffle. At 47 HP, Bloodletting and Blood Wall self-damage made HP the limiting resource; no single upgrade beat 24 guaranteed HP while already holding Energy Potion and Block Potion for tactical power.

## Floor 17 - Boss: Vantom
- Read: history/run24_strategy.md; kb/enemies/bosses/vantom.md; kb/cards/ironclad/juggernaut.md; kb/potions/block_potion.md; kb/potions/energy_potion.md; kb/cards/status/wound.md.
- Status: Entered at 71/80 HP, Energy Potion + Block Potion. Vantom had 183 HP and Slippery 9.
- Line: Played Juggernaut on turn 1, then Armaments to upgrade Bludgeon while stripping a Slippery stack through Juggernaut. Used Sword Boomerang and block-trigger damage to finish Slippery by the first Dismember. Spent Block Potion on the first Dismember; it also triggered Juggernaut for damage. Used Bloodletting on the buff turn to convert block cards into Juggernaut damage, then spent Energy Potion during the second cycle to play enough attacks and block. Survived the second Dismember with Blood Wall + True Grit and killed on the following buff turn with Bludgeon+.
- Result: Won at 31/80 before rewards, then picked Unmovable to trigger Book of Five Rings and heal to 51/80; claimed Flex Potion and 75 gold.
- Lesson: Added Juggernaut/Vantom notes that block potions and block cards can be damage sources as well as defense when racing Slippery and Dismember.

## Floor 17 - Boss Card Reward
- Read: history/run24_strategy.md; kb/strategies/reward_choice.md; kb/cards/ironclad/not_yet.md; kb/cards/ironclad/demon_form.md; kb/cards/ironclad/unmovable.md.
- Status: 31/80 HP before the card pick, 7 gold, Book of Five Rings 4/5. Offered Not Yet / Demon Form / Unmovable.
- Decision: Pick Unmovable.
- Reason: The deck already has Juggernaut, Blood Wall, Shrug It Off, True Grit, and Defends, so Unmovable directly improves the defensive engine. Demon Form is slower 3-cost scaling, and Not Yet is sustain without solving future Act 2 fights. Any card pickup also triggered Book of Five Rings; Unmovable healed 20 immediately and reset the relic counter to 0.

## Act 2 Start - Pathing
- Read: history/run24_strategy.md; kb/strategies/bosses.md; kb/enemies/bosses/the_insatiable.md; kb/strategies/pathing.md.
- Status: 51/80 HP, 82 gold, Flex Potion, Book of Five Rings 0/5. Act boss: The Insatiable.
- Decision: Start on the middle Monster at (3,1).
- Reason: The Insatiable KB says Sandpit distance and early Frantic Escape management are the main boss constraints, so upgrades to Unmovable/True Grit/Armaments and stable HP matter. The middle start reaches an Unknown after one hallway and can branch toward an early shop/rest path; the left and right starts both risk three forced hallway fights before meaningful recovery or shopping.

## Floor 18 - Ancient: Darv
- Read: history/run24_strategy.md; kb/enemies/ancients/darv.md; kb/relics/pandoras_box.md; kb/relics/calling_bell.md; kb/relics/astrolabe.md; kb/mechanics/save_and_load.md; kb/cards/ironclad/fight_me.md; kb/cards/ironclad/juggling.md; kb/cards/ironclad/demon_form.md.
- Status: 74/80 HP after Act 2 transition heal, 82 gold, Flex Potion. Offered Pandora's Box / Calling Bell / Astrolabe.
- Harness note: Ancients cannot be save/load branch-inspected. Added this to kb/mechanics/save_and_load.md and kb/enemies/ancients/darv.md.
- Decision: Pick Astrolabe, transforming three basic Strikes.
- Result: The three Strikes became Fight Me!+, Juggling+, and Demon Form+. Book of Five Rings advanced to 3/5.
- Reason: Astrolabe was the controlled quality option. Pandora's Box could erase every Defend and destabilize the Unmovable/Juggernaut block engine; Calling Bell's three relics were strong but added an Eternal curse. Transforming Strikes preserved block density while upgrading all replacements.

## Floor 19 - Combat: Tunneler
- Read: history/run24_strategy.md; kb/enemies/hive/tunneler.md.
- Status: Entered at 74/80 HP, 82 gold, Flex Potion. Tunneler opened Bite for 15, then Burrow into a 26-damage Attack from Below unless its Block was broken.
- Line: Played Demon Form+ on turn 1 and accepted the 15 Bite. On the Burrow setup turn, used Flash of Steel, Bludgeon, Bloodletting+, Shrug It Off, Pommel Strike+, and Strike to lower Tunneler to 21 HP while cycling into enough attacks. On the Burrow attack turn, spent Flex Potion so Anger plus Strike exactly stripped the 34 remaining Burrow Block, stunning Tunneler and preventing the 26 hit. Played Unmovable during the stun window and killed with Fight Me!+.
- Result: Won at 62/80 after Burning Blood, with no potion remaining. Took Pommel Strike over Twin Strike / Inflame and claimed 11 gold, ending at 93 gold. Book of Five Rings advanced to 4/5.
- Reason: Tunneler KB says breaking all Burrow Block prevents Attack from Below. Spending Bloodletting HP and Flex Potion was better than taking 26 damage; the follow-up reward choice favored Pommel Strike because reward_choice/card_impressions identify Pommel as premier attack/draw, while Inflame duplicated existing Demon Form+/Fight Me!+ scaling and Twin Strike was another medium attack.

## Floor 19 - Pathing
- Read: history/run24_strategy.md; kb/strategies/pathing.md; kb/enemies/bosses/the_insatiable.md.
- Status: 62/80 HP, 93 gold, no potion, Book of Five Rings 4/5.
- Decision: Take the only available Unknown at (3,2), planning to bias future branches toward shop/rest access and potion replacement.
- Reason: Pathing KB says Act 2 should prioritize safe unknowns, shops, and rest sites over optional elites unless the deck and potions are already strong. The deck has a working block/scaling shell but no potion, and The Insatiable wants upgrades plus stable HP more than immediate elite risk.

## Floor 20 - Combat: Bowlbug (Rock) + Bowlbug (Egg)
- Read: history/run24_strategy.md; kb/strategies/combat.md; kb/enemies/hive/bowlbugs.md.
- Status: Entered at 62/80 HP, 93 gold, no potion. Rock attacked for 16 every turn and stuns if fully blocked; Egg attacked for 8 and gained 8 Block.
- Line: Used Pommel Strike+ and Pommel Strike on Egg, then the drawn Anger killed it before it could block. True Grit blocked part of Rock's first Headbutt but randomly exhausted Juggernaut. On the next turn, Tremble plus Blood Wall fully blocked Rock's 16 attack, triggering the Rock stun. Used the stun window for Fight Me!+ and Flash of Steel, then killed with Twin Strike.
- Result: Won at 57/80 after Burning Blood. Took Flame Barrier over Anger / Headbutt, triggering Book of Five Rings for +20 HP to 77/80; claimed 10 gold to reach 103.
- Reason: Bowlbugs KB says fully preventing Rock's Headbutt creates a stun, and in Rock/Egg fights full Rock block can be worth HP/self-damage because it opens time to focus Egg. Flame Barrier was the reward pick because it gives a no-HP-cost block card for Unmovable/Juggernaut turns and solves the current no-potion defensive gap; Anger would pollute the deck, and Headbutt was less urgent than real block density.

## Floor 20 - Pathing
- Read: history/run24_strategy.md; kb/strategies/pathing.md; kb/enemies/bosses/the_insatiable.md.
- Status: 77/80 HP, 103 gold, no potion, Book of Five Rings 0/5.
- Decision: Choose Shop over Monster.
- Reason: The shop route reaches a Rest Site through Unknowns and avoids extra immediate hallway damage. Pathing KB says Act 2 should favor shops/rest sites when potion support, removal, or boss-specific answers are needed; this run had no potion and enough gold for a meaningful buy.

## Floor 21 - Shop
- Read: history/run24_strategy.md; kb/cards/ironclad/whirlwind.md; kb/cards/ironclad/thunderclap.md; kb/cards/ironclad/flame_barrier.md; kb/potions/energy_potion.md.
- Status: 77/80 HP, 103 gold, no potion. Notable shop options: Whirlwind 73g, Thunderclap 51g, Flame Barrier sale 38g, Energy Potion 51g, removal 100g.
- Decision: Buy Whirlwind, leaving 30 gold.
- Reason: The run strategy listed AoE as a major Act 2 hole. Whirlwind is the cleanest AoE offered and scales with Bloodletting energy, Fight Me!/Demon Form Strength, and Vulnerable. Energy Potion was valuable but did not solve multi-enemy fights; Thunderclap plus Energy Potion was lower ceiling and added a weaker standalone attack. Removal was less urgent than adding the missing AoE tool.

## Floor 21 - Pathing
- Read: history/run24_strategy.md; kb/strategies/pathing.md; kb/enemies/bosses/the_insatiable.md.
- Status: 77/80 HP, 30 gold, no potion, Book of Five Rings 1/5.
- Decision: Take the only available Unknown at (5,4).
- Reason: The shop branch continues through Unknowns to a Rest Site. With Whirlwind added and no optional elite forced yet, the route still aligns with the Act 2 safety plan.

## Floor 22 - Combat: Chompers
- Read: history/run24_strategy.md; kb/strategies/combat.md; kb/enemies/hive/chomper.md.
- Status: Entered at 77/80 HP, 30 gold, no potion. Chomper pair alternated Clamp 9x2 and Screech for 3 Dazed; each had Artifact 2.
- Line: Focused the currently Clamping Chomper as the KB recommends. Used Flash/Pommel/Pommel/Sword early for damage, then Armaments upgraded Sharp Twin Strike+ for a 9x2 turn. Flame Barrier reduced the next Clamp and returned damage. Fight Me!+ into 1-energy Whirlwind killed the active attacking Chomper and left the other low enough to finish next turn.
- Result: Won at 51/80 after Burning Blood. Took Bloodletting over Anger / Molten Fist, claimed Fire Potion, and 14 gold to reach 44.
- Reason: Bloodletting adds a second energy-positive card to fund Whirlwind, Bludgeon, Unmovable, and multi-card block turns. Anger was rejected because its KB warns against adding more in Act 2 without exhaust control. Molten Fist was narrower, depending on already-applied Vulnerable. Fire Potion replaced the missing potion slot.
- Save/load lesson: This fight should have been branch-inspected before accepting the 18-damage opening. After Pommel+ drew Blood Wall on turn 1, a lower-HP-loss branch likely existed by playing Blood Wall instead of spending the remaining energy on Pommel/Sword damage. In future expensive Act 2 hallway turns, reload before claiming rewards if the line loses 20+ net HP and a clear defensive branch was available.

## Floor 23 - Event: The Lantern Key
- Read: history/run24_strategy.md; kb/events/the_lantern_key.md; kb/events/war_historian_repy.md; kb/relics/history_course.md.
- Status: 51/80 HP, 44 gold, Fire Potion, Book of Five Rings 2/5. Options: Return the Key for 100 gold or Keep the Key and fight.
- Decision: Return the Key, gaining 100 gold.
- Reason: Keeping the Key requires an immediate fight at medium HP and only pays off if War Historian, Repy appears later. Returning it is guaranteed value and puts the run at 144 gold before a known future shop, which can become removal, potion support, or a boss-specific card.

## Floor 24 - Rest Site
- Read: history/run24_strategy.md; kb/strategies/pathing.md; kb/strategies/reward_choice.md; kb/cards/ironclad/unmovable.md; kb/cards/ironclad/whirlwind.md.
- Status: 51/80 HP, 144 gold, Fire Potion. Next branch can avoid the elite and go Monster into Treasure/Shop.
- Decision: Smith Whirlwind+ instead of Rest.
- Reason: Pathing KB says Smith is the default when HP is stable and an immediate elite can be avoided. Whirlwind+ raises AoE from 5 to 8 damage per energy and synergizes with Bloodletting, Fight Me!/Demon Form Strength, and Vulnerable. The upgrade should save more HP in Act 2 multi-enemy fights than resting now, while Fire Potion remains as an emergency stop.

## Floor 25 - Combat: Mytes
- Resume note: After context compaction, re-read AGENTS.md, GUIDE.md, history/run24.md, history/run24_strategy.md, all kb/strategies playbooks, kb/mechanics/save_and_load.md, and kb/enemies/hive/myte.md. Verified MCP transcript logging remains `full` and assigned to `run24`.
- Status: Entered at 51/80 HP, 144 gold, Fire Potion. Encounter: two Mytes; one opens Toxic Cornucopia for 2 Toxic and the other opens Suck for 6 plus Strength.
- Plan: Focus the Suck Myte first to reduce scaling, play or exhaust Toxic cards when possible, and consider save/load if the opening line creates major avoidable HP loss.
- Save/load branch 1: Played Demon Form+ on turn 1. This preserved scaling but failed the status-tempo test; Toxic taxes plus the 18-damage Bite line pushed the fight toward sub-20 HP before control was established.
- Save/load branch 2: Replayed with Armaments into double Pommel Strike+ on the Suck Myte, then Blood Wall + Strike while accepting two Toxic hits. On turn 3, Bloodletting+ funded Tremble, Sword Boomerang, Bash, Shrug, and a Fire Potion kill on the Suck Myte. Juggernaut + True Grit/Defend later let the single Myte die after one more attack cycle.
- Result: Won at 24/80 after Burning Blood, spent Fire Potion, claimed Body Slam, Explosive Ampoule, and 12 gold to reach 156. Book of Five Rings advanced to 3/5.
- Reward decision: Picked Body Slam over Bloodletting / Perfected Strike after reading reward_choice, deck_size, Body Slam, Bloodletting, Perfected Strike, and Book of Five Rings. Body Slam now has a real shell with Unmovable, Blood Wall, Flame Barrier, Shrug, True Grit, and Juggernaut; third Bloodletting adds too much HP pressure at 24 HP, and Perfected Strike is not the deck plan.
- Lesson: Added a Myte note that early frontload plus partial block beats slow power setup when Toxic cards are about to tax energy and HP.

## Floor 26 - Treasure
- Read: history/run24_strategy.md; kb/relics/parrying_shield.md.
- Status: 24/80 HP, 194 gold, Explosive Ampoule, Book of Five Rings 3/5.
- Decision: Claim Parrying Shield.
- Reason: Free relic from chest. Parrying Shield rewards turns that already reach 10+ Block, which this deck can do with Blood Wall, Flame Barrier, Shrug, True Grit, Unmovable, and future Body Slam turns.

## Floor 27 - Shop
- Read: history/run24_strategy.md; kb/strategies/reward_choice.md; kb/strategies/deck_size.md; kb/cards/ironclad/not_yet.md; kb/cards/colorless/equilibrium.md; kb/cards/ironclad/pommel_strike.md; kb/cards/ironclad/shrug_it_off.md; kb/potions/heart_of_iron.md; kb/potions/block_potion.md; kb/potions/vulnerable_potion.md; kb/relics/meal_ticket.md; kb/relics/toolbox.md.
- Status: 24/80 HP, 194 gold, Explosive Ampoule, Book of Five Rings 3/5. Shop had Pommel Strike 49g, Shrug It Off 49g, Not Yet 78g sale, Equilibrium 82g, Heart of Iron 72g, Block Potion 49g, removal 100g, and relics that were either too expensive or lower priority.
- Decision: Buy Pommel Strike, Shrug It Off, and Heart of Iron.
- Result: Book of Five Rings triggered after the second card purchase, healing to 44/80. Ended at 24 gold with Explosive Ampoule + Heart of Iron.
- Reason: Pommel and Shrug are high-quality cantrips that improve draw/access and triggered immediate +20 HP from Book. Heart of Iron gives repeated Plating for the forced elite/boss route and is stronger future prevention than a one-shot Block Potion. Not Yet was attractive sustain, but buying it would lose either Heart of Iron or the Pommel/Shrug Book-heal package.

## Floor 27 - Pathing
- Read: history/run24_strategy.md; kb/strategies/pathing.md; kb/strategies/elites.md; kb/enemies/bosses/the_insatiable.md.
- Status: 44/80 HP, 24 gold, Explosive Ampoule + Heart of Iron. Next options: Unknown, immediate Elite, or Monster, with a forced elite later on visible lines.
- Decision: Choose Unknown.
- Reason: Pathing KB says Act 2 should avoid optional elites and prefer question marks when HP is medium/low. Unknown preserves the Rest Site branch before the forced elite; immediate Elite or hallway combat would spend resources before recovery.

## Floor 28 - Event: Stone of All Time
- Read: history/run24_strategy.md; kb/events/stone_of_all_time.md; kb/cards/enchants/vigorous.md; kb/potions/heart_of_iron.md.
- Status: 44/80 HP, 24 gold, Explosive Ampoule + Heart of Iron. Options: Drink and Lift loses Heart of Iron for +10 max HP; Push loses 6 HP to enchant an Attack with Vigorous 8.
- Decision: Choose Push and enchant Whirlwind+ with Vigorous 8.
- Result: HP 38/80, Heart of Iron preserved.
- Reason: Heart of Iron is a high-value defensive potion for the forced elite and The Insatiable, while +10 max HP gives no immediate survival. Vigorous is strongest on repeat-hit/X-cost attacks, and Whirlwind+ is the best target for AoE/energy/Vulnerable turns.
- Lesson: Added Stone of All Time note that Push can beat Drink and Lift when the potion is a key defensive resource and Whirlwind/repeat-hit attacks are available.

## Floor 28 - Pathing
- Read: history/run24_strategy.md; kb/strategies/pathing.md; kb/strategies/elites.md; kb/enemies/bosses/the_insatiable.md.
- Status: 38/80 HP, Explosive Ampoule + Heart of Iron. Options: Monster before forced Elite, or Rest Site before forced Elite.
- Decision: Choose Rest Site.
- Reason: The Monster branch gives no recovery before an elite. The Rest Site branch enters the forced elite with higher HP and still reaches another rest before The Insatiable.

## Floor 29 - Rest Site
- Read: history/run24_strategy.md; kb/strategies/pathing.md; kb/strategies/elites.md; kb/strategies/reward_choice.md.
- Status: 38/80 HP, Explosive Ampoule + Heart of Iron, forced Hive elite next.
- Decision: Rest to 62/80 instead of Smith.
- Reason: Pathing KB says Rest if below 60% before an elite. Body Slam+, Unmovable+, and True Grit+ are strong upgrades, but 38/80 into a forced Hive elite would risk losing the run before the final campfire.

## Floor 30 - Elite: Entomancer
- Read: history/run24_strategy.md; kb/enemies/elites/entomancer.md; kb/cards/status/dazed.md; kb/strategies/combat.md; kb/potions/heart_of_iron.md; kb/potions/explosive_ampoule.md.
- Status: Entered at 62/80 HP with Explosive Ampoule + Heart of Iron. Entomancer opened Beeeees! for 3x8 and Personal Hive 1.
- Line: Used Heart of Iron immediately, played Armaments to upgrade Body Slam, then took the frontload line with Body Slam+, Pommel Strike, and Twin Strike instead of slow Juggling setup. On the Spear turn, Bloodletting funded Unmovable, Bash, and Defend, taking a controlled 7 net HP for Vulnerable plus the block engine. On the Pheromone turn, Tremble extended Vulnerable, Flash/Strike dealt damage, and Shrug cycled while triggering Parrying Shield. On the second Beeeees! turn, spent Explosive Ampoule as Dazed-free damage, then Pommel/Pommel+/Shrug kept the race alive. Vigorous Whirlwind+ killed at 26 HP remaining on the following turn.
- Result: Won at 37/80 after Burning Blood, spent both potions, claimed Red Mask and 29 gold to reach 53.
- Reward decision: Read kb/strategies/reward_choice.md, kb/strategies/deck_size.md, kb/cards/ironclad/sword_boomerang.md, kb/cards/ironclad/perfected_strike.md, and kb/cards/ironclad/havoc.md. Plan is to skip Sword Boomerang+ / Perfected Strike+ / Havoc: Sword Boomerang+ is another Personal Hive/status-taxed multi-hit and duplicates an existing role, Perfected Strike+ is off-plan Act 1 bridge damage, and unupgraded Havoc can exhaust key boss answers.
- Lesson: Added Entomancer and potion notes. Heart of Iron is good pre-attack Plating into multi-hit patterns; Explosive Ampoule is high-value here because it does not add Dazed. User correction confirmed again: Ancients cannot be save/load branch-inspected; promoted that exception into GUIDE.md.

## Floor 30 - Pathing
- Read: history/run24_strategy.md; kb/strategies/pathing.md; kb/enemies/bosses/the_insatiable.md.
- Status: 37/80 HP, 53 gold, no potions. Only visible route is Monster -> Rest Site -> The Insatiable.
- Decision: Take the forced Monster node.
- Reason: No alternate route exists. Pathing priority is now minimizing hallway damage to preserve the final rest-site decision; without a potion and below 50% HP, Rest before The Insatiable is likely unless the hallway is nearly flawless.

## Floor 31 - Combat: Bowlbugs + Slumbering Beetle
- Read: history/run24_strategy.md; kb/strategies/combat.md; kb/enemies/hive/bowlbugs.md; kb/enemies/hive/slumbering_beetle.md; kb/mechanics/debuffs.md; kb/mechanics/buffs.md.
- Status: Entered at 37/80 HP, no potions. Encounter: Bowlbug Rock attacking for 12 due Red Mask Weak, Bowlbug Silk debuffing, Slumbering Beetle asleep with Slumber 3.
- Line: Opened Bloodletting+ into Shrug, then installed Juggling+ and Demon Form+ while Body Slam hit Rock; accepted 4 chip when full Rock stun was not available. On turn 2, Bloodletting plus Unmovable and Blood Wall fully blocked Rock + Silk, stunned Rock, and used Anger to reduce Rock. Killed Rock with Twin Strike while it was stunned, then Bash set up Silk. Pommel Strike+ killed Silk as Beetle woke, and Flash/Strike/True Grit raced Beetle while taking only 4 from the first Roll Out. Whirlwind+ was lethal the next turn at 72 HP.
- Result: Won at 27/80 after Burning Blood, claimed 10 gold to reach 63.
- Reward decision: Read kb/strategies/reward_choice.md, kb/strategies/deck_size.md, kb/cards/ironclad/anger.md, kb/cards/ironclad/pommel_strike.md, and kb/cards/ironclad/barricade.md. Picked Barricade over Anger / Pommel Strike. Anger is a late draw-pollution risk, and another base Pommel is only incremental; Barricade is a real boss-engine card with Unmovable, Blood Wall, Flame Barrier, Shrug, Body Slam, and The Insatiable's non-attack opener.
- Lesson: Added Barricade note that The Insatiable opener can install it before the attack cycle if the deck already has large block and Unmovable.

## Floor 32 - Rest Site
- Read: history/run24_strategy.md; kb/strategies/pathing.md; kb/strategies/bosses.md; kb/enemies/bosses/the_insatiable.md; kb/cards/status/frantic_escape.md; kb/mechanics/buffs.md.
- Status: 27/80 HP, 63 gold, no potions, The Insatiable next.
- Decision: Rest to 51/80 instead of Smith.
- Reason: Barricade+ would be the best boss-specific upgrade, but 27/80 with no potion is too low for Sandpit management plus Thrash/Lunging Bite. The boss plan is to install Barricade on the Liquify Ground opener or Salivate turn when possible, play cheap Frantic Escape copies early, and use retained Unmovable/Blood Wall/Flame Barrier block for Body Slam/Parrying Shield value.

## Floor 33 - Boss: The Insatiable (resume checkpoint)
- Resume note: After context compaction, re-read AGENTS.md, GUIDE.md, history/run24.md, history/run24_strategy.md, all kb/strategies playbooks, kb/mechanics/save_and_load.md, kb/strategies/bosses.md, kb/enemies/bosses/the_insatiable.md, and kb/cards/status/frantic_escape.md. Verified MCP transcript logging remains `full` and assigned to `run24`.
- User correction carried forward: Ancients cannot be save/load branch-inspected in this harness; evaluate visible options and commit there.
- Current status: Round 2, 51/80 HP, 63 gold, no potions. The Insatiable is 303/341 HP with Sandpit 5 and attacks for 9x2. Hand after playing one Frantic Escape is Tremble, Defend, Barricade, and Body Slam with 2 energy.
- Planned line: Apply Tremble for 3 Vulnerable, play Defend for 5 Block, then end turn. Barricade is not affordable this turn, and Body Slam deals 0 before block; preserving Sandpit and reducing Thrash chip is higher value.
- Save/load branch 1 failed: Played Frantic Escape, Tremble, and Defend on round 2; Bloodletting+ funded Flame Barrier and a Juggling-copied Twin Strike burst on round 3; played Frantic Escape + Fight Me!+ on the Salivate turn; then Frantic Escape plus double Shrug survived the first post-Salivate Thrash at 6 HP. The next 13x2 turn had only Pommel Strike+, Sword Boomerang, Defend, Defend, and Strike, with Bloodletting/Pommel/Unmovable in draw, so no line could cover 26 incoming at 6 HP. Restarting the room and testing a Barricade-install line.
- Save/load branch 2 failed: Installed Barricade on round 2, used Bloodletting+ + Flame Barrier + Anger/Flash/Twin/Twin copy on round 3, then played Frantic Escape + True Grit on Salivate to bank 7 Block. Frantic Escape plus double Shrug on round 5 survived to 10 HP, but round 6 still showed Pommel Strike+, Sword Boomerang, Defend, Defend, and Strike against 12x2. Even drawing Unmovable/Bloodletting could only make 15 Block after the HP cost, so the line remained dead. Next retry keeps Barricade but skips Bloodletting+ on round 3 to preserve HP.
- Save/load branch 3 in progress after resume: Re-read AGENTS.md, GUIDE.md, history/run24.md, history/run24_strategy.md, all kb/strategies playbooks, kb/enemies/bosses/the_insatiable.md, kb/cards/status/frantic_escape.md, and kb/mechanics/save_and_load.md after compaction. Continuing the Barricade branch that skips Bloodletting+ on round 3 to preserve HP; current live state is round 4 after Frantic Escape + True Grit, 14/80 HP, 7 retained Block, Sandpit 3, and Fight Me!+ exhausted by True Grit.
- Save/load branch 3 failed: Skipping Bloodletting+ on round 3 preserved HP, but round 6 still arrived at 13 HP with 24 incoming, no Frantic Escape in hand, and only Pommel Strike+ / Sword Boomerang / Defend / Defend / Strike. Pommel+ could draw Bloodletting and Pommel, and Pommel could draw Unmovable, but even Bloodletting into Unmovable plus a Defend only made 10 Block after dropping to 10 HP. This branch cannot survive the second post-Salivate attack.
- Save/load branch 4 failed: Changed the opener to full-energy Vigorous Whirlwind+ and skipped Juggling/Pommel setup. Round 2 had the same Frantic Escape / Tremble / Defend / Barricade / Body Slam hand, but Escape left only 2 energy so Barricade was not playable. Played Escape + Tremble + Defend, then used Vulnerable attacks and Flame Barrier on Lunging Bite, Fight Me!+ on Salivate, and Escape + double Shrug on the next attack. The branch reached round 6 at 9 HP against 13x2 with boss still at 205 HP; Pommel+ into Bloodletting/Pommel/Unmovable still could not block enough or kill. Next retry keeps the Whirlwind opener but installs Barricade on round 2 by skipping that Escape.
- Save/load branch 5 failed: Kept the full-energy Vigorous Whirlwind+ opener, skipped the round-2 Frantic Escape, and installed Barricade immediately. This entered round 3 at 33 HP with Sandpit 3, then used Flash/Anger/Twin Strike/Flame Barrier. On Salivate, played Frantic Escape + True Grit to bank 7 Block, but True Grit again exhausted Fight Me!+. Round 5 Escape + double Shrug reached round 6 at 13 HP with boss still at 234 HP and no surviving line against 12x2. After five distinct retries, stopped branching per the save/load retry limit and accepted the loss.

## Final Outcome
- Steam log: `/Users/tonywu/Library/Application Support/Steam/userdata/1407082853/2868840/remote/modded/profile1/saves/history/1778966426.run`
- Confirmed fields: `win: false`, `was_abandoned: false`, `killed_by_encounter: ENCOUNTER.THE_INSATIABLE_BOSS`, `killed_by_event: NONE.NONE`.
- The run died on Act 2 Floor 33 to The Insatiable.

## Post-Run Reflection
- What worked: Act 1 routing and reward choices built a real frontload/draw shell; Book of Five Rings was used well for a mid-Act 2 heal; save/load preserved HP in several earlier rooms and identified the exact boss failure mode.
- What cost the run: Entering The Insatiable at 51/80 with no potion, unupgraded Barricade, no upgraded True Grit, and multiple HP-cost cards left too little budget for Sandpit plus the first Salivate cycle. Resting was correct at the final campfire, but the route and potion economy had already made the boss math too tight.
- What to change next time: Treat potionless low-HP Insatiable as an emergency earlier in Act 2. Prioritize a defensive potion, Barricade+ if Barricade is the boss plan, or a safer route/rest earlier rather than relying on exact Frantic Escape ordering.
- Mechanic/harness lesson: Save/load was useful for combat branch search, but deterministic retries converged after five distinct lines. The newly confirmed Ancient limitation remains promoted in GUIDE.md and kb/mechanics/save_and_load.md: do not rely on save/load to branch-inspect Ancients.
