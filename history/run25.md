# Run 25 - Ironclad A10

- Date: 2026-05-17
- Character: Ironclad
- Ascension: 10
- Outcome: Loss
- Floor reached: Act 2 Floor 27

## Pre-Run Setup
- Read: AGENTS.md; GUIDE.md; all files in kb/strategies/ (`_index.md`, `ironclad.md`, `pathing.md`, `reward_choice.md`, `deck_size.md`, `combat.md`, `elites.md`, `bosses.md`, `archetypes.md`, `card_impressions.md`, `meta_play.md`).
- Decision: Start a new standard Ironclad run with full MCP transcript logging assigned to `run25`.
- Reason: Follow mandatory pre-run reads, keep the live strategy file paired to the same run number, and apply the run24 lesson: preserve boss-entry HP and potion equity earlier instead of relying on exact late boss branches.

## Floor 1 - Neow
- Read: `history/run25_strategy.md`; `kb/enemies/ancients/neow.md`; `kb/relics/neow_s_torment.md`; `kb/relics/golden_pearl.md`; `kb/relics/silver_crucible.md`; `kb/cards/colorless/neow_s_fury.md`; `kb/mechanics/save_and_load.md`.
- Status: 64/80 HP, 99 gold, Burning Blood. Options were Neow's Torment, Golden Pearl, and Silver Crucible.
- Decision: Pick Neow's Torment, adding Neow's Fury.
- Reason: Neow's Fury gives immediate Act 1 damage and discard recursion without needing a visible early shop or sacrificing the first chest. Golden Pearl is strong but shop/path dependent before seeing the map; Silver Crucible improves early card rewards but has a real relic downside.

## Floor 1 - Act 1 Path
- Read: `history/run25_strategy.md`; `kb/strategies/pathing.md`; `kb/strategies/bosses.md`; `kb/enemies/bosses/soul_fysh.md`; `kb/relics/neow_s_torment.md`.
- Status: 64/80 HP, 99 gold, no potions. Act boss is Soul Fysh.
- Decision: Start on the left monster node `(2,1)`.
- Reason: Soul Fysh's KB says Beckon/Gaze add statuses, Fade gains Intangible, and Scream applies Vulnerable, so this run wants early frontload plus controlled exhaust. The left start keeps more route branches open toward question marks, rest sites, optional elites, and shops, while still taking an early low-pool combat for card rewards.

## Floor 2 - Toadpoles
- Read: `history/run25_strategy.md`; `kb/strategies/combat.md`; `kb/enemies/underdocks/toadpole.md`; `kb/strategies/reward_choice.md`; `kb/strategies/archetypes.md`; `kb/strategies/card_impressions.md`; `kb/strategies/ironclad.md`; `kb/cards/ironclad/tremble.md`; `kb/cards/ironclad/perfected_strike.md`; `kb/cards/ironclad/uppercut.md`.
- Status: Entered 64/80 HP, 99 gold, no potions. Exited 57/80 HP after Burning Blood, then claimed 13 gold and Strength Potion.
- Decision: Focus the Whirl/attacking Toadpole first; pick Uppercut over Tremble and Perfected Strike.
- Reason: Toadpole KB says the weak two-Toadpole encounter should kill the Whirl attacker first before thorns punish delayed attacks. Uppercut gives immediate 13-damage frontload, Weak, and Vulnerable, has strong win-corpus presence, and is a high-priority upgrade. Tremble is good setup but no damage; Perfected Strike is only an Act 1 bridge and would bias removals around Strike density.
- Reflection: Accepted a modest HP loss instead of reloading because the fight ended in safe range and the reward was premium. A lower-damage branch may have used Strike/Strike/Defend on turn 1, but the difference was not worth spending a retry on Floor 2.

## Floor 2 - Path
- Read: `history/run25_strategy.md`; `kb/strategies/pathing.md`.
- Status: 57/80 HP, 112 gold, Strength Potion, deck has Uppercut and Neow's Fury.
- Decision: Take the next Monster `(3,2)` over Unknown `(1,2)`.
- Reason: Pathing says the first three hallway fights are usually controlled and valuable for card rewards. Uppercut plus Strength Potion makes another early hallway acceptable, and the deck still needs more Act 1 damage/draw before optional elite decisions.

## Floor 3 - Sludge Spinner
- Read: `history/run25_strategy.md`; `kb/strategies/combat.md`; `kb/enemies/underdocks/sludge_spinner.md`; `kb/strategies/reward_choice.md`; `kb/cards/ironclad/pommel_strike.md`; `kb/cards/ironclad/inferno.md`; `kb/cards/ironclad/pillage.md`.
- Status: Entered 57/80 HP, 112 gold, Strength Potion. Exited 52/80 HP after Burning Blood, then claimed 7 gold and Explosive Ampoule.
- Decision: Preserve Strength Potion; take Pommel Strike over Inferno and Pillage.
- Reason: Sludge Spinner always opens with Oil Spray for 9 and Weak, then random non-repeat attacks/debuffs; blocking the opener and using Bash plus Uppercut finished before the 12-damage follow-up landed. Pommel Strike is the premier Act 1 attack/draw card and a top upgrade target. Inferno is a self-damage build-around without support; Pillage is useful but weaker than guaranteed damage plus draw in this mixed starter deck.

## Floor 3 - Path
- Read: `history/run25_strategy.md`; `kb/strategies/pathing.md`.
- Status: 52/80 HP, 119 gold, Strength Potion, Explosive Ampoule.
- Decision: Take forced Monster `(3,3)`.
- Reason: No alternate node is available. The early combat remains acceptable because Burning Blood plus two potions cover risk, and the deck still wants one more reward before the first rest/elite fork.

## Floor 4 - Corpse Slugs
- Read: `history/run25_strategy.md`; `kb/strategies/combat.md`; `kb/enemies/underdocks/corpse_slug.md`; `kb/strategies/reward_choice.md`; `kb/strategies/deck_size.md`; `kb/cards/ironclad/perfected_strike.md`; `kb/cards/ironclad/dominate.md`; `kb/cards/ironclad/battle_trance.md`.
- Status: Entered 52/80 HP, 119 gold, Strength Potion, Explosive Ampoule. Exited 58/80 HP after Burning Blood, then claimed 12 gold.
- Decision: Use Explosive Ampoule, kill the attacking Slug turn 1, then pick Battle Trance over Dominate and Perfected Strike.
- Reason: Corpse Slug KB says Ravenous stuns and strengthens the survivor when another Slug dies; the AoE potion plus Uppercut/Strike triggered the stun immediately and prevented both damage and Frail. Battle Trance gives 0-cost draw and improves answer density for Uppercut/Pommel/Bash. Dominate fits Vulnerable decks but is slower than draw right now; Perfected Strike would overcommit to Strike density.
- KB update: Added a Corpse Slug note that AoE potion damage can enable a turn-1 Ravenous stun to skip the partner action.

## Floor 4 - Path
- Read: `history/run25_strategy.md`; `kb/strategies/pathing.md`.
- Status: 58/80 HP, 131 gold, Strength Potion.
- Decision: Take Unknown `(2,4)` over Monster `(3,4)`.
- Reason: The first three hallway rewards are complete and the deck has frontload plus draw. Pathing now favors preserving HP and flexibility; Unknown can still branch to another Unknown or Monster before the floor-6 rest/elite fork, while Monster would force another harder-pool combat immediately.

## Floor 5 - Waterlogged Scriptorium
- Read: `history/run25_strategy.md`; `kb/events/waterlogged_scriptorium.md`; `kb/mechanics/keywords.md`.
- Status: 58/80 HP, 131 gold, Strength Potion.
- Decision: Choose Prickly Sponge to pay 99 gold and enchant 2 cards with Steady.
- Reason: Retain on Battle Trance plus a key frontload/debuff card improves timing for elites and Soul Fysh more than 6 max HP. Spending to 32 gold is acceptable because later fights/chests can rebuild enough for a mid/late Act 1 shop.
- Follow-up: Selected Battle Trance and Uppercut as Steady targets.
- KB update: Added a Waterlogged Scriptorium note that Prickly Sponge allows exact deck-selection targets and that Battle Trance/Uppercut are premium targets.

## Floor 5 - Path
- Read: `history/run25_strategy.md`; `kb/strategies/pathing.md`.
- Status: 58/80 HP, 32 gold, Strength Potion, Steady Uppercut, Steady Battle Trance.
- Decision: Take Unknown `(1,5)` over Monster `(3,5)`.
- Reason: After three hallway rewards plus the Steady event, the deck has enough early power to stop forcing fights. Unknown preserves HP and can still branch to either Elite or RestSite on floor 6.

## Floor 6 - Cultists
- Read: `history/run25_strategy.md`; `kb/strategies/combat.md`; `kb/enemies/underdocks/cultists.md`; `kb/strategies/reward_choice.md`; `kb/cards/ironclad/body_slam.md`; `kb/cards/ironclad/pommel_strike.md`; `kb/cards/ironclad/sword_boomerang.md`.
- Status: Entered 58/80 HP, 32 gold, Strength Potion. Exited 37/80 HP after Burning Blood, then claimed 15 gold.
- Decision: Use Strength Potion, kill Damp Cultist first, then pick a second Pommel Strike over Body Slam and Sword Boomerang.
- Reason: Cultists KB warns Damp Cultist's A10 Ritual scales by 6 and can reach lethal damage quickly. The Strength Potion converted the retained Uppercut/Neow's Fury turn into a near-kill on Damp, but the fight still cost heavy HP because Calcified stayed alive too long. Second Pommel Strike adds attack density plus draw; Body Slam lacks large block support and Sword Boomerang lacks Strength/Vigor support after the potion is gone.
- Reflection: This was the first major avoidable resource hit. The Unknown branch preserving flexibility was reasonable, but once it rolled Cultists the combat needed either a more aggressive turn-1 plan on Calcified or a save/load retry before accepting the 21 net HP loss and potion spend. Route to the rest site now unless a very safe alternative appears.

## Floor 6 - Path
- Read: `history/run25_strategy.md`; `kb/strategies/pathing.md`; `kb/strategies/elites.md`.
- Status: 37/80 HP, 47 gold, no potions.
- Decision: Take RestSite `(1,6)` over Elite `(0,6)`.
- Reason: Pathing and elite strategy require a strong HP/potion gate before optional elites. This deck has good damage but no potion and no strong block/exhaust yet, so entering an Act 1 elite at 46% HP is not justified.

## Floor 7 - Rest Site
- Read: `history/run25_strategy.md`; `kb/strategies/pathing.md`; `kb/strategies/reward_choice.md`; `kb/cards/ironclad/pommel_strike.md`; `kb/cards/ironclad/uppercut.md`; `kb/cards/ironclad/battle_trance.md`.
- Status: 37/80 HP, 47 gold, no potions. Next path has a forced Monster.
- Decision: Rest instead of Smith.
- Reason: Pommel Strike, Uppercut, and Battle Trance are all meaningful upgrades, but 37 HP with no potion before a forced hallway is below the safety bar. Resting to 61 protects the run and may reopen a later elite option.

## Floor 7 - Path
- Read: `history/run25_strategy.md`; `kb/strategies/pathing.md`.
- Status: 61/80 HP, 47 gold, no potions.
- Decision: Take forced Monster `(1,7)`.
- Reason: No alternate node is available. Preserve HP and look for a potion before deciding on the next elite/monster fork.

## Floor 8 - Corpse Slugs
- Read: `history/run25_strategy.md`; `kb/strategies/combat.md`; `kb/enemies/underdocks/corpse_slug.md`; `kb/strategies/reward_choice.md`; `kb/cards/ironclad/unmovable.md`; `kb/cards/ironclad/battle_trance.md`; `kb/cards/ironclad/perfected_strike.md`.
- Status: Entered 61/80 HP, 47 gold, no potions. Exited 42/80 HP after Burning Blood, then claimed 13 gold.
- Decision: Use Uppercut plus Neow's Fury to kill the first Slug and stun both survivors; pick Unmovable over Battle Trance and Perfected Strike.
- Reason: The Corpse Slug KB note from earlier applied cleanly without a potion: Uppercut's Vulnerable made Neow's Fury lethal and skipped two enemy actions. The final survivor still hit hard after double Ravenous, but Unmovable directly solves the current block hole and gives a strong upgrade target. A second Battle Trance adds draw but worsens No Draw sequencing; Perfected Strike remains a Strike-density trap.

## Floor 8 - Path
- Read: `history/run25_strategy.md`; `kb/strategies/pathing.md`; `kb/strategies/elites.md`.
- Status: 42/80 HP, 60 gold, no potions, Unmovable unupgraded.
- Decision: Take Monster `(2,8)` over Elite `(0,8)`.
- Reason: The elite line gives a relic but risks entering at only 52.5% HP with no potion and no upgraded defensive setup. The Monster line still reaches treasure, then Unknown/rest options, and is safer for preserving Soul Fysh resources.

## Floor 9 - Gremlin Merc
- Read: `history/run25_strategy.md`; `kb/strategies/combat.md`; `kb/enemies/underdocks/gremlin_merc.md`; `kb/strategies/reward_choice.md`; `kb/strategies/archetypes.md`; `kb/strategies/card_impressions.md`; `kb/strategies/ironclad.md`; `kb/strategies/reward_choice.md`; `kb/cards/ironclad/true_grit.md`; `kb/cards/ironclad/shrug_it_off.md`; `kb/cards/ironclad/setup_strike.md`.
- Status: Entered 42/80 HP, 60 gold, no potions. After branch search, exited 17/80 HP after Burning Blood, recovered 40 stolen gold as a reward, claimed 8 normal gold, and took Strength Potion.
- Decision: Save/load tested three lines. Rejected Unmovable-open and straight race lines because they either left Merc too healthy or could not damage Fat Gremlin before escape. Kept the race line with Battle Trance before the Merc-kill turn, then picked Shrug It Off over True Grit and Setup Strike.
- Reason: Gremlin Merc KB says Merc steals on attacks, spawns Sneaky/Fat on death, and Fat flees with stolen gold after its spawn turn. Battle Trance before Pommel Strike + Neow's Fury changed the returned cards enough to use Pommel Strike on Fat during the spawn turn, setting up Uppercut lethal before Flee. Shrug It Off solves immediate block/draw and pairs with Unmovable; True Grit+ would be excellent for Soul Fysh but unupgraded random exhaust is risky when the next rest site may need to heal; Setup Strike is low-impact filler for this deck.
- KB update: Added a Gremlin Merc note that damaging Fat on the spawn turn can be necessary and that stolen gold is paid as a post-combat reward.

## Floor 10 - Treasure
- Read: `history/run25_strategy.md`; `kb/relics/bronze_scales.md`.
- Status: Entered 17/80 HP, 68 gold, Strength Potion. Chest added 31 gold.
- Decision: Claim Bronze Scales.
- Reason: Forced chest relic. Bronze Scales adds passive hallway damage, especially into multi-hit attackers, without spending energy or HP.

## Floor 11 - Brain Leech
- Read: `history/run25_strategy.md`; `kb/events/brain_leech.md`; `kb/strategies/reward_choice.md`; `kb/cards/ironclad/expect_a_fight.md`; `kb/cards/ironclad/bloodletting.md`; `kb/cards/ironclad/body_slam.md`; `kb/cards/ironclad/armaments.md`; `kb/cards/ironclad/true_grit.md`.
- Status: 17/80 HP, 99 gold, Strength Potion. Free branch offered Expect a Fight, Bloodletting, Body Slam, Armaments, True Grit. Save/load inspected the 5-HP colorless branch; it offered Flash of Steel, Equilibrium, and Fasten at 12/80 HP.
- Decision: Take the free Share Knowledge branch and pick True Grit.
- Reason: Brain Leech KB recommends inspecting both branches when possible. The colorless branch was not worth 5 HP at this low HP total. True Grit is the best free boss-prep card because Soul Fysh adds statuses and the deck still lacks exhaust; Armaments and Bloodletting are strong but do not solve the status-clog problem as directly, and Body Slam is premature without upgraded Unmovable or heavier block.

## Floor 11 - Path
- Read: `history/run25_strategy.md`; `kb/strategies/pathing.md`.
- Status: 17/80 HP, 99 gold, Strength Potion.
- Decision: Take RestSite `(2,11)` over Monster `(4,11)`.
- Reason: Pathing says below 20% HP requires immediate rest. The monster/shop branch could preserve a shop line, but a forced hallway at 17 HP risks needing the Strength Potion before Soul Fysh or dying to a bad draw.

## Floor 12 - Rest Site
- Read: `history/run25_strategy.md`; `kb/strategies/pathing.md`; `kb/strategies/reward_choice.md`; `kb/cards/ironclad/true_grit.md`; `kb/cards/ironclad/unmovable.md`.
- Status: 17/80 HP, 99 gold, Strength Potion.
- Decision: Rest to 41/80 instead of smithing True Grit or Unmovable.
- Reason: True Grit+ and Unmovable+ are both high-impact upgrades, but 17/80 before more Act 1 rooms is below the survival threshold. Resting preserves the Strength Potion for Soul Fysh or a dangerous hallway.

## Floor 12 - Path
- Read: `history/run25_strategy.md`; `kb/strategies/pathing.md`; `kb/strategies/elites.md`.
- Status: 41/80 HP, 99 gold, Strength Potion.
- Decision: Take Monster `(1,12)` over Elite `(2,12)`.
- Reason: The deck has improved with True Grit but still lacks upgraded defensive setup and entered the fork at only 51% HP. The monster path keeps a final RestSite route and avoids risking the Soul Fysh potion package in an optional elite.

## Floor 13 - Sewer Clam
- Read: `history/run25_strategy.md`; `kb/strategies/combat.md`; `kb/enemies/underdocks/sewer_clam.md`; `kb/strategies/reward_choice.md`; `kb/cards/ironclad/second_wind.md`; `kb/cards/ironclad/cinder.md`; `kb/cards/ironclad/headbutt.md`; `kb/potions/cure_all.md`; `kb/potions/strength_potion.md`.
- Status: Entered 41/80 HP, 99 gold, Strength Potion. Exited 32/80 HP after Burning Blood, then claimed 14 gold and Cure All.
- Decision: Block the opening Jet with Defend/Defend/True Grit, then use Pommel Strike into Bash on the Pressurize turn and accept the 15-damage Jet to race. Pick Second Wind over Cinder and Headbutt.
- Reason: Sewer Clam KB says Plating makes small attacks inefficient and the pattern alternates Jet and Pressurize. Blocking the opener preserved HP and randomly exhausted a Strike with True Grit. The Pressurize turn was the right tempo window for Bash/Vulnerable; after that, racing prevented a 19-damage Jet from landing. Second Wind directly solves Soul Fysh's status-clog plan and provides large block with non-Attack hands; Cinder is random exhaust damage, and Headbutt is good but less urgent than status conversion.

## Floor 14 - Fossil Stalker
- Read: `history/run25_strategy.md`; `kb/strategies/combat.md`; `kb/enemies/underdocks/fossil_stalker.md`; `kb/strategies/reward_choice.md`; `kb/enemies/bosses/soul_fysh.md`; `kb/cards/status/beckon.md`; `kb/cards/ironclad/second_wind.md`; `kb/cards/ironclad/sword_boomerang.md`; `kb/cards/ironclad/cinder.md`.
- Status: Entered 32/80 HP, 113 gold, Strength Potion and Cure All. Exited 38/80 HP after Burning Blood with Strength Potion remaining, then claimed 13 gold.
- Decision: Spend Cure All on turn 1 after drawing only Strike/Defend cards, then use the extra energy and draw to play Unmovable plus two Defends and fully block Latch. Use Second Wind with Unmovable active to convert non-Attacks into enough block for Tackle, then finish with Uppercut, Neow's Fury, and Pommel Strike.
- Reason: Fossil Stalker KB warns that Suck grants 3 Strength on unblocked attack damage and Lash scales badly once Strength lands. Cure All drew Unmovable and Pommel Strike, which let the deck prevent every Suck trigger and turn the fight into a clean resource conversion. Preserving the Strength Potion matters more for Soul Fysh than preserving Cure All once the final rest site is still ahead.
- Reward: Picked a second Second Wind over Sword Boomerang and Cinder.
- Reward reason: Soul Fysh and Beckon KB say the boss adds 1-cost statuses that punish being left in hand for HP loss. A duplicate Second Wind improves access to status cleanup and block during the boss; Sword Boomerang needs Strength/Vigor support that this deck lacks, and Cinder's random exhaust is less reliable than controlled boss prep.
- KB update: Added a Fossil Stalker note that Cure All/Unmovable/Second Wind can justify a turn-1 potion spend to stop the Suck snowball.

## Floor 14 - Path
- Read: `history/run25_strategy.md`; `kb/strategies/pathing.md`; `kb/strategies/elites.md`.
- Status: 38/80 HP, 126 gold, Strength Potion. Next routes are Elite -> RestSite -> Soul Fysh or Monster -> RestSite -> Soul Fysh.
- Decision: Take Monster `(2,14)` over Elite `(0,14)`.
- Reason: Pathing and elite strategy require good HP/potion backup for optional elites. This deck has boss-specific exhaust tools but only 47.5% HP and one Strength Potion; the extra relic is not worth risking Soul Fysh entry HP or spending the boss potion.

## Floor 15 - Two-Tailed Rats
- Read: `history/run25_strategy.md`; `kb/strategies/combat.md`; `kb/enemies/underdocks/two_tailed_rat.md`; `kb/strategies/reward_choice.md`; `kb/cards/ironclad/sword_boomerang.md`; `kb/cards/ironclad/feed.md`; `kb/cards/ironclad/unrelenting.md`; `kb/mechanics/save_and_load.md`.
- Status: Entered 38/80 HP, 126 gold, Strength Potion. Exited 24/80 HP after Burning Blood with Strength Potion preserved, then claimed 12 gold.
- Decision: Use Second Wind on turn 1 to exhaust True Grit/Defend for 10 block and Strike the 9-damage rat twice. Turn 2 used Strike, Neow's Fury, and returned Strike to kill one rat and set up the second at 1 HP. Turn 3 killed the summoning rat and used Uppercut on the final rat, then finished on turn 4.
- Reason: Two-Tailed Rat KB warns that Call for Backup after turn 2 stretches the fight. The line prioritized killing the first two rats before they could summon while keeping Strength Potion for Soul Fysh. This still cost heavy HP because Frail reduced block and the deck lacked AoE.
- Save/load note: Tried to reload from the reward screen after seeing the 24 HP exit, but the harness resumed rewards rather than the fight start. Added a `kb/mechanics/save_and_load.md` note that combat branch searches must happen before lethal if the goal is to improve HP/potion outcomes.
- Reward: Picked Unrelenting over Sword Boomerang and Feed.
- Reward reason: Unrelenting KB says it is strongest with high-impact 2-cost attacks such as Bash and Uppercut. This deck has Bash, steady Uppercut, two Pommel Strikes, and a Strength Potion, so Unrelenting improves immediate Soul Fysh burst and effective energy. Feed is good long-term max HP but does not help current HP or the Act 1 boss kill, and Sword Boomerang lacks Strength/Vigor support.

## Floor 16 - Rest Site
- Read: `history/run25_strategy.md`; `kb/strategies/pathing.md`; `kb/enemies/bosses/soul_fysh.md`; `kb/cards/ironclad/true_grit.md`; `kb/cards/ironclad/unmovable.md`; `kb/cards/ironclad/second_wind.md`.
- Status: 24/80 HP, 138 gold, Strength Potion. Boss next.
- Decision: Rest to 48/80 instead of Smithing True Grit, Unmovable, or Second Wind.
- Reason: The upgrade targets are high impact, especially True Grit+ and 1-cost Unmovable, but Soul Fysh's De-Gas, Scream, and Beckon HP loss make 24 HP too low. Resting gives room to survive one bad draw cycle while preserving the Strength Potion for a burst/lethal window.

## Floor 17 - Boss: Soul Fysh
- Read: `history/run25_strategy.md`; `kb/strategies/bosses.md`; `kb/enemies/bosses/soul_fysh.md`; `kb/cards/status/beckon.md`; `kb/cards/ironclad/unmovable.md`; `kb/cards/ironclad/second_wind.md`; `kb/cards/ironclad/true_grit.md`; `kb/cards/ironclad/unrelenting.md`; `kb/mechanics/save_and_load.md`.
- Status: Entered 48/80 HP, 138 gold, Strength Potion. Exited 20/80 HP after Burning Blood, no potion, 213 gold, Explosive Ampoule.
- Decision: Used Strength Potion on turn 1. Save/load tested a pure damage line and an Unmovable line; kept the line that installed Unmovable on round 3, accepted one Beckon HP loss, then used Second Wind with Unmovable to clear Beckon clusters and block De-Gas/Scream turns.
- Reason: Soul Fysh KB says the pattern is Beckon, De-Gas, Gaze, Fade, Scream and that Intangible makes Fade/Scream damage inefficient. The pure damage branch reached low boss HP but died because Battle Trance drew extra Beckons after energy was spent. The winning branch gave up early burst to install Unmovable; that made Shrug/Defend/Second Wind large enough to survive the second cycle while preserving enough damage for a round-11 kill.
- Tactical lessons: Do not draw on low-energy De-Gas/Scream turns unless a Beckon answer remains. Second Wind is premium against Beckon, and Unmovable turns it into a hard block button. Unrelenting's Free Attack buff persisted across turns when no follow-up attack was played, enabling a lethal setup after an Intangible turn.
- Reward: Picked Dark Embrace over Stoke and Thrash; claimed Explosive Ampoule and 75 gold.
- Reward reason: `kb/strategies/archetypes.md` and `kb/cards/ironclad/dark_embrace.md` identify Dark Embrace as the exhaust draw engine. This deck already has two Second Winds, True Grit, Unmovable, and status-clog matchups; Stoke is random generated output and Thrash randomly exhausts attacks.
- KB update: Added Soul Fysh, Beckon, and Unrelenting notes for Unmovable/Second Wind sequencing, draw-risk with Beckons, and Free Attack persistence.

## Act 2 Start
- Read: `kb/strategies/bosses.md`; `kb/enemies/bosses/kaiser_crab.md`; `kb/strategies/pathing.md`; `history/run25_strategy.md`.
- Status: 20/80 HP, 213 gold, Explosive Ampoule. Visible boss is Kaiser Crab.
- Plan: Kaiser Crab KB says Rocket's turn-4 Laser is the key check, especially after Crusher's Bug Sting applies Frail/Weak. The deck needs recovery, upgraded Dark Embrace/Unmovable/True Grit, and ideally a defensive or burst potion before the boss. Avoid optional Act 2 elites while HP is low unless the route and potion situation improve sharply.

## Floor 18 - Ancient: Tezcatara
- Read: `history/run25_strategy.md`; `kb/events/tezcatara.md`; `kb/relics/yummy_cookie.md`; `kb/relics/seal_of_gold.md`; `kb/relics/golden_compass.md`; `kb/mechanics/save_and_load.md`.
- Status: 20/80 HP, 213 gold, Explosive Ampoule. Act transition then left the run at 68/80 HP after the Ancient.
- Decision: Choose Yummy Cookie over Seal of Gold and Golden Compass.
- Reason: Ancient branches cannot be save/load inspected in this harness, so the visible best option had to be chosen directly. Yummy Cookie upgraded Dark Embrace+, Unmovable+, True Grit+, and Pommel Strike+, solving the deck's setup costs and block quality. Seal of Gold would drain shop/removal equity, and Golden Compass's forced elites are too risky with an Act 2 Kaiser route.

## Floor 18 - Path
- Read: `history/run25_strategy.md`; `kb/strategies/pathing.md`; `kb/enemies/bosses/kaiser_crab.md`.
- Status: 68/80 HP, 213 gold, Explosive Ampoule.
- Decision: Take the right branch toward Monster, Unknown, then Shop.
- Reason: The route gives one hallway for reward/relic growth, then event/shop access with 213 gold. It avoids Golden Compass-style forced elites and preserves recovery/removal options before Kaiser Crab's Rocket Laser check.

## Floor 19 - Bowlbugs
- Read: `history/run25_strategy.md`; `kb/strategies/combat.md`; `kb/enemies/hive/bowlbugs.md`; `GUIDE.md`; `kb/strategies/reward_choice.md`; `kb/strategies/archetypes.md`; `kb/strategies/card_impressions.md`; `kb/strategies/ironclad.md`; `kb/strategies/deck_size.md`; `kb/cards/ironclad/shrug_it_off.md`; `kb/cards/ironclad/taunt.md`; `kb/cards/ironclad/body_slam.md`.
- Status: Entered 68/80 HP, 213 gold, Explosive Ampoule. Exited 46/80 HP after Burning Blood, then claimed 10 gold.
- Decision: Killed Bowlbug Egg quickly, then installed Dark Embrace+ against Bowlbug Rock and used Second Wind plus Shrug It Off to full-block Headbutt and trigger the Rock stun. Picked Body Slam over Shrug It Off and Taunt.
- Reason: Bowlbugs KB says Rock is stunned only if Headbutt is fully blocked; setting up Dark Embrace and using Second Wind drew into Shrug, converting a likely repeated 16-damage attack into a no-damage stun turn. Body Slam is now justified because the deck has Unmovable+, upgraded True Grit, Shrug, two Second Winds, and Dark Embrace; it gives large block turns a damage payoff for Kaiser and later fights. Shrug was safer draw quality, and Taunt was useful block/Vulnerable, but neither added a new payoff lane.

## Floor 20 - Event: Bugslayer
- Read: `history/run25_strategy.md`; `kb/events/bugslayer.md`; `kb/cards/colorless/exterminate.md`; `kb/cards/colorless/squash.md`; `kb/cards/ironclad/exterminate.md`; `kb/cards/ironclad/squash.md`.
- Status: 46/80 HP, 223 gold, Explosive Ampoule.
- Decision: Learn Extermination Technique, adding Exterminate.
- Reason: The run plan identified AoE/multi-target damage as a hole. Exterminate gives 1-cost all-enemy damage for Hive fights and Kaiser claws. Squash is efficient Vulnerable, but the deck already has Bash and Uppercut for single-target Vulnerable.

## Floor 21 - Shop
- Read: `history/run25_strategy.md`; `kb/strategies/reward_choice.md`; `kb/strategies/pathing.md`; `kb/enemies/bosses/kaiser_crab.md`; `kb/cards/ironclad/burning_pact.md`; `kb/relics/meal_ticket.md`; `kb/relics/ringing_triangle.md`; `kb/potions/duplicator.md`; `kb/potions/blood_potion.md`; `kb/potions/colorless_potion.md`; `kb/cards/colorless/the_bomb.md`.
- Status: 46/80 HP, 223 gold, Explosive Ampoule.
- Decision: Buy Burning Pact, remove a Strike, and leave with 51 gold.
- Reason: Burning Pact is premium in the current Dark Embrace exhaust engine: it chooses exhaust fuel, draws, and shrinks the live deck toward Unmovable/Second Wind/Body Slam turns. Strike removal improves answer density for Kaiser. Ringing Triangle and Meal Ticket were strong but too expensive after the engine purchase; a second Body Slam or Stampede would dilute the deck. Kept Explosive Ampoule instead of buying Blood/Colorless Potion because Act 2 multi-enemy burst and Kaiser claw math are still relevant.
- KB update: Created `kb/relics/ringing_triangle.md` from the observed shop text.

## Floor 21 - Path
- Read: `history/run25_strategy.md`; `kb/strategies/pathing.md`; `kb/strategies/elites.md`.
- Status: 46/80 HP, 51 gold, Explosive Ampoule.
- Decision: Take Monster `(4,4)` over Monster `(6,4)`.
- Reason: The right branch offered an earlier shop/rest but forced two Act 2 elites. The left branch forces three hallways before a rest and one later elite, which is still risky but has lower forced-elite exposure. Pathing and elite strategy warn that Hive elites need a higher bar because Decimillipede can punish weak AoE/block.

## Floor 22 - Thieving Hopper
- Read: `history/run25_strategy.md`; `kb/strategies/combat.md`; `kb/enemies/hive/thieving_hopper.md`; `kb/strategies/reward_choice.md`; `kb/cards/ironclad/thunderclap.md`; `kb/cards/ironclad/tremble.md`; `kb/cards/ironclad/expect_a_fight.md`.
- Status: Entered 46/80 HP, 51 gold, Explosive Ampoule. Hopper stole Second Wind. Exited 38/80 HP after Burning Blood, then recovered the stolen Second Wind and claimed 15 gold.
- Decision: Played Unrelenting plus free Strike on turn 1 while blocking 5, then installed Dark Embrace+ and applied Bash on the free Flutter turn. On the Hat Trick turn, used Exterminate plus Pommel Strike+ to remove all five Flutter stacks and stun the 23-damage attack, then killed with Uppercut into Neow's Fury before Escape.
- Reason: Thieving Hopper KB says it steals a card, then uses Flutter, Hat Trick, Nab, and Escape; stolen cards return if Hopper dies before Escape. The line accepted 14 early damage to keep pace, then used Exterminate's four packets plus Pommel's fifth hit to stun the dangerous turn. Picked Tremble over Thunderclap and Expect a Fight because it Exhausts for Dark Embrace and provides long Vulnerable for Body Slam/burst turns; Thunderclap is weak generic AoE now that Exterminate exists, and unupgraded Expect a Fight is too clunky.
- KB update: Added Hopper and Exterminate notes for using Exterminate plus one extra Attack hit to stun Flutter.

## Floor 23 - Chompers
- Read: `history/run25_strategy.md`; `kb/strategies/combat.md`; `kb/enemies/hive/chomper.md`; `kb/strategies/reward_choice.md`; `kb/cards/ironclad/taunt.md`; `kb/cards/ironclad/armaments.md`; `kb/cards/ironclad/howl_from_beyond.md`.
- Status: Entered 38/80 HP, 66 gold, Explosive Ampoule. Exited 26/80 HP after Burning Blood, no Explosive Ampoule, then claimed Weak Potion and 12 gold.
- Decision: Spend Explosive Ampoule immediately, then use Exterminate and Pommel Strike to focus the opening Clamping Chomper. Played Second Wind to block part of the first 18, installed Unmovable on turn 2, and used Shrug/Neow's Fury to cover the second Clamp. Finished the first Chomper with Unrelenting plus Pommel/Strike, then blocked and killed the second with Uppercut/Unrelenting.
- Reason: Chomper KB says the pair alternates Clamp and Screech, and recommends focusing the currently Clamping Chomper. At 38 HP with another forced hallway before rest, the potion spend was justified to shorten the fight and keep the status pile from snowballing further. Picked Taunt over Armaments and Howl from Beyond because Taunt is immediate block plus Vulnerable for the next low-HP hallway; Armaments needs an upgrade plan that the route may not allow, and Howl is too clunky without a guaranteed exhaust setup.

## Floor 24 - The Obscura
- Read: `history/run25_strategy.md`; `kb/strategies/combat.md`; `kb/enemies/hive/the_obscura.md`; `kb/mechanics/save_and_load.md`; `kb/strategies/reward_choice.md`; `kb/cards/ironclad/rupture.md`; `kb/cards/ironclad/breakthrough.md`; `kb/cards/ironclad/burning_pact.md`; `kb/potions/heart_of_iron.md`.
- Status: Entered 26/80 HP, 78 gold, Weak Potion. Exited 9/80 HP after Burning Blood, no Weak Potion, then claimed Heart of Iron and 11 gold.
- Decision: Save/load restarted after a branch mistake on round 3. The kept line killed the first Parafright Slam turn with Exterminate plus Pommel Strike, installed Unmovable+, used Weak Potion on Parafright and Uppercut on Obscura for the first big double-attack turn, then raced Obscura while using Second Wind and Body Slam to survive and close.
- Reason: Obscura KB says Parafright revives next turn and Obscura scales all enemies with Wail, so repeated minion kills are losing if they do not prevent immediate lethal. The restart corrected a two-Strike line that left too little energy for Uppercut; the winning line used Weak Potion to reduce Parafright, kept pressure on Obscura, and used Body Slam after a 30-block Second Wind turn to put Obscura in Unrelenting lethal range.
- Reward: Picked Burning Pact over Rupture and Breakthrough; took Heart of Iron.
- Reward reason: Burning Pact KB says it is strong with exhaust payoffs and improves consistency by exhausting filler/statuses. This deck has Dark Embrace+, two Second Winds, True Grit+, and Unmovable+; a second Burning Pact is on-plan. Rupture and Breakthrough require HP-loss support, which is unsafe at 9 HP and not the current archetype.
- KB update: Added an Obscura note that Weak on Parafright can buy a key Wail-scaling turn while leader damage remains the priority.

## Floor 25 - Rest Site
- Read: `history/run25_strategy.md`; `kb/strategies/pathing.md`; `kb/enemies/bosses/kaiser_crab.md`.
- Status: 9/80 HP, 89 gold, Heart of Iron. Treasure next, then forced elite.
- Decision: Rest to 33/80 instead of Smithing Body Slam or Burning Pact.
- Reason: Pathing strategy says below 20% HP after a fight should go to the immediate rest site, and this branch has a forced elite after the treasure. Body Slam+ would be high value for the block engine, but entering a forced Hive elite at 9 HP is not viable.

## Floor 26 - Treasure
- Read: `history/run25_strategy.md`; `kb/relics/ornamental_fan.md`.
- Status: 33/80 HP, 120 gold, Heart of Iron.
- Decision: Claimed Ornamental Fan.
- Reason: Single relic chest. Ornamental Fan adds incidental block on three-Attack turns; Pommel Strikes, Unrelenting's Free Attack, Neow's Fury, Exterminate, and starter attacks can trigger it, but the forced elite still needs Heart of Iron and the main Unmovable/Second Wind block plan.

## Floor 27 - Elite: Decimillipede
- Read: `history/run25_strategy.md`; `kb/strategies/elites.md`; `kb/enemies/elites/decimillipede.md`; `kb/enemies/elites/entomancer.md`; `kb/enemies/elites/infested_prism.md`; `kb/potions/heart_of_iron.md`; `kb/mechanics/save_and_load.md`.
- Status: Entered 33/80 HP, 120 gold, Heart of Iron. Died on floor 27. Steam history `1778974994.run` reports `win: false`, `was_abandoned: false`, `killed_by_encounter: "ENCOUNTER.DECIMILLIPEDE_ELITE"`.
- Decision: Used Heart of Iron immediately. Save/load tested multiple materially different lines: early Battle Trance/aggression, original Heart + Pommel + double Defend, heavier Second Wind defense, and Pommel/Neow's Fury branch fishing from discard. None survived the forced elite.
- Reason: Decimillipede KB says all three segments cycle offset Bulk/Writhe/Outgas and reattach if killed while another segment lives. The deck could create large Unmovable/Second Wind turns, but entering at 33 HP meant every imperfect turn was lethal and the deck lacked enough immediate multi-target damage to kill or suppress a segment before the 34-40 incoming turns.
- Best branch: Heart of Iron, Pommel front, double Defend; turn 2 Battle Trance into Unmovable+, Defend, Exterminate; turn 3 Shrug + Defend + Second Wind preserved 6 HP. Turn 4 still failed because the hand could not combine enough block, a front-segment kill, and enough damage reduction before 36 incoming.
- Save/load notes: Reloading from combat worked, but after `continue` the first poll sometimes briefly reported "Combat ended. Waiting for rewards..." before the combat state stabilized. Polling again showed the correct room-start state.

## Post-Run Reflection
- What worked: The Act 1 exhaust/block pivot was real. Unmovable+, Dark Embrace+, Second Wind, Burning Pact, and Yummy Cookie were strong enough to beat Soul Fysh and several Act 2 hallways from poor HP positions.
- What cost the run: The Act 2 path still forced an elite after entering the rest at 9 HP and leaving at only 33 HP. Heart of Iron made Decimillipede close, but it did not replace the missing HP buffer, Body Slam upgrade, and stronger AoE/frontload.
- Next change: Treat Decimillipede as a hard route gate. At low HP, a forced Act 2 elite after treasure needs either very high burst/AoE, a stronger defensive potion stack, or enough HP to absorb two bad turns; otherwise earlier pathing/card picks need to prioritize avoiding that branch or entering the rest with far more HP.
- Harness lesson: Combat save/load is useful for line search, but branch before the reward boundary and poll twice after `continue` if the first state looks transient or contradictory.
