# Run 22 - Ironclad A10

- Date: 2026-05-15
- Character: Ironclad
- Ascension: 10
- Outcome: In progress

## Pre-run Reads

- Read `AGENTS.md` instructions from the user prompt.
- Read `GUIDE.md`.
- Read all strategy playbooks in `kb/strategies/`: `_index.md`, `archetypes.md`, `bosses.md`, `card_impressions.md`, `combat.md`, `elites.md`, `ironclad.md`, `meta_play.md`, `pathing.md`, `reward_choice.md`.

## Floor 1 - Neow

- Current HP/status: 64/80 HP after A10 starting penalty, 99 gold, Burning Blood, no potions.
- Entity/relic KB read: `kb/enemies/ancients/neow.md`, `kb/relics/lost_coffer.md`, `kb/relics/small_capsule.md`, `kb/relics/cursed_pearl.md`, `kb/cards/status/greed.md`.
- Options: Lost Coffer; Small Capsule; Cursed Pearl for 333 gold plus eternal Greed.
- Decision: chose Lost Coffer.
- Reason: Lost Coffer gives a controlled immediate card reward plus a potion without a curse. Small Capsule is a no-downside random relic but less controllable. Cursed Pearl's 333 gold is powerful only with early shop access and Greed is an Eternal Unplayable draw penalty.

## Floor 1 - Lost Coffer Reward

- Current HP/status: 64/80 HP, 99 gold, Colorless Potion.
- Strategy/card KB read: `kb/strategies/reward_choice.md`, `kb/strategies/card_impressions.md`, `kb/strategies/ironclad.md`, `kb/cards/ironclad/perfected_strike.md`, `kb/cards/ironclad/ashen_strike.md`, `kb/cards/ironclad/expect_a_fight.md`.
- Decision: picked Perfected Strike over Ashen Strike and Expect a Fight.
- Reason: Perfected Strike is immediately 16 damage in the starter deck and solves the first Act 1 job. Ashen Strike needs exhaust support; Expect a Fight is energy setup before we have enough attacks/draw to exploit it.

## Floor 1 - Pathing

- Current HP/status: 64/80 HP, 99 gold, Colorless Potion, Perfected Strike.
- Strategy files read: `kb/strategies/pathing.md`, `kb/strategies/elites.md`, `kb/strategies/bosses.md`, live `history/run22_strategy.md`.
- Boss/entity KB read: `kb/enemies/bosses/waterfall_giant.md`; Act 1 elite KB read: `kb/enemies/elites/bygone_effigy.md`, `kb/enemies/elites/byrdonis.md`, `kb/enemies/elites/phrog_parasite.md`.
- Decision: chose right-side Monster [2].
- Reason: Waterfall Giant needs a deck that can damage quickly while preserving HP for the Steam Eruption explosion. The right route gives several early combats and unknowns, avoids forced early elites, and has rest/shop access before the boss.

## Floor 2 - Toadpoles
- Read: history/run22_strategy.md; kb/enemies/underdocks/toadpole.md.
- Status: Entered 64/80 with Colorless Potion; ended 52/80 after Burning Blood, gold 99.
- Decision: Killed the attacking Toadpole first, blocked the Thorns turn instead of attacking into Thorns, then used the no-Thorns window to finish.
- Reason: Toadpole KB says weak encounter has front Spiken Toadpole and Whirl attacker; avoiding Thorns preserved HP while still ending before a second dangerous Spike Spit cycle. Potion held for elite/danger hallway.

## Floor 2 - Card Reward
- Read: history/run22_strategy.md; kb/strategies/card_impressions.md; kb/cards/ironclad/twin_strike.md; kb/cards/ironclad/perfected_strike.md; kb/cards/ironclad/bludgeon.md.
- Status: 52/80, 106 gold, Colorless Potion. Offered Twin Strike / Perfected Strike / Bludgeon.
- Decision: Picked Bludgeon.
- Reason: Twin Strike and a second Perfected Strike support the Strike package, but Bludgeon is cleaner one-card Act 1 frontload for elites and Waterfall Giant. Added Bludgeon KB note about its Act 1 frontload role.

## Floor 2 - Pathing
- Read: history/run22_strategy.md; kb/strategies/pathing.md; kb/enemies/bosses/waterfall_giant.md.
- Status: 52/80, 106 gold, Colorless Potion. Only next node is Unknown at (6,2).
- Decision: Take the forced Unknown.
- Reason: No alternate branch at this step; the route still offers multiple combats for rewards and later rest/shop access before Waterfall Giant, but block/draw must be prioritized before optional elite decisions.

## Floor 3 - Event: Sunken Treasury
- Read: history/run22_strategy.md; kb/events/sunken_treasury.md; kb/cards/status/greed.md.
- Status: 52/80, 106 gold, Colorless Potion. Options were 66 gold or 360 gold + Greed.
- Decision: Took First Chest for 66 gold; new gold 172.
- Reason: Greed is Eternal and Unplayable, and the current Bludgeon/Perfected Strike deck needs consistent draws before Waterfall Giant more than shop money.

## Floor 3 - Pathing
- Read: history/run22_strategy.md; kb/strategies/pathing.md.
- Status: 52/80, 172 gold, Colorless Potion. Only next node is Monster at (6,3).
- Decision: Take forced combat.
- Reason: First-three Act 1 hallway fights are still reward-positive with Burning Blood; deck has improved damage but still needs block/draw before Waterfall Giant.

## Floor 4 - Sludge Spinner
- Read: history/run22_strategy.md; kb/enemies/underdocks/sludge_spinner.md.
- Status: Entered 52/80 with Colorless Potion; ended 49/80 after Burning Blood.
- Decision: Played Bludgeon on turn 1, then Bash + Strike through Weak for lethal on turn 2.
- Reason: Sludge Spinner always opens with 9 + Weak, and Bludgeon leaves 9 HP, allowing a clean two-turn kill before random follow-up attacks matter.

## Floor 4 - Rewards
- Read: kb/potions/colorless_potion.md; kb/potions/speed_potion.md; kb/cards/ironclad/havoc.md; kb/cards/ironclad/molten_fist.md; kb/cards/ironclad/twin_strike.md; kb/strategies/archetypes.md.
- Status: 49/80, 172 gold; rewards were 9 gold, Speed Potion, Havoc / Molten Fist / Twin Strike.
- Decision: Replaced Colorless Potion with Speed Potion; picked Molten Fist; claimed 9 gold (181 total).
- Reason: Speed Potion is a concrete Waterfall Giant/elite defense button. Molten Fist supports Bash into extended Vulnerable for Bludgeon/Perfected Strike and exhausts after frontload; Havoc is random and Twin Strike is lower-ceiling Strike support. Added Molten Fist KB note.

## Floor 4 - Pathing
- Read: history/run22_strategy.md; kb/strategies/pathing.md.
- Status: 49/80, 181 gold, Speed Potion. Only next node is Monster at (6,4).
- Decision: Take forced combat.
- Reason: Route remains locked; Burning Blood and Speed Potion cover some risk, but future rewards should prioritize block/draw before the first rest and Waterfall Giant.

## Floor 5 - Seapunk
- Read: history/run22_strategy.md; kb/enemies/underdocks/seapunk.md.
- Status: Entered 49/80 with Speed Potion; ended 42/80 after Burning Blood.
- Decision: Used Bludgeon turn 1 and Perfected Strike turn 2 for lethal.
- Reason: Seapunk cycles 13 -> 2x4 -> Block/Strength; Bludgeon + Perfected Strike kills before Bubble Burp can extend the fight. Speed Potion preserved for elite/boss defense.

## Floor 5 - Card Reward
- Read: kb/strategies/card_impressions.md; kb/cards/ironclad/pommel_strike.md; kb/cards/ironclad/uppercut.md; kb/cards/ironclad/rupture.md.
- Status: 42/80, 181 gold, Speed Potion. Offered Pommel Strike / Uppercut / Rupture.
- Decision: Picked Pommel Strike; claimed 9 gold (190 total).
- Reason: Pommel Strike directly fills the draw hole, adds efficient damage, keeps Perfected Strike live through its Strike tag, and is a premium smith target. Uppercut overlaps with Bash/Molten Fist and adds another 2-cost card; Rupture lacks HP-loss support.

## Floor 5 - Pathing
- Read: history/run22_strategy.md; kb/strategies/pathing.md.
- Status: 42/80, 190 gold, Speed Potion. Only next node is Monster at (6,5), then an Unknown and first rest branch.
- Decision: Take forced combat.
- Reason: No alternate route yet; preserve Speed Potion if possible, but spend it if the hallway threatens severe HP before the first rest.

## Floor 6 - Sewer Clam
- Read: history/run22_strategy.md; kb/enemies/underdocks/sewer_clam.md; kb/potions/speed_potion.md.
- Status: Entered 42/80 with Speed Potion; ended 32/80 after Burning Blood, no potion.
- Decision: Used Bludgeon into Plating, Perfected Strike + Strike on the buff turn, then spent Speed Potion with Defend + Bash to reduce the strengthened Jet from 15 to 5 and killed with Bludgeon on the next buff turn.
- Reason: Sewer Clam Plating makes small attacks inefficient and Pressurize makes the second Jet expensive; Speed Potion saved 10 HP and preserves smith/rest flexibility at the nearby rest branch.

## Floor 6 - Card Reward
- Read: kb/cards/ironclad/sword_boomerang.md; kb/cards/ironclad/perfected_strike.md; kb/cards/ironclad/ashen_strike.md; history/run22_strategy.md.
- Status: 32/80, 190 gold, no potion. Offered Sword Boomerang / Perfected Strike / Ashen Strike.
- Decision: Picked Ashen Strike; claimed 11 gold (201 total).
- Reason: Ashen Strike is a 1-cost Strike-tag card that keeps Perfected Strike live and has natural upside from Ascender's Bane and Molten Fist exhausts. A second Perfected Strike adds more 2-cost clunk; Sword Boomerang lacks Strength support.

## Floor 6 - Pathing
- Read: history/run22_strategy.md; kb/strategies/pathing.md.
- Status: 32/80, 201 gold, no potion. Only next node is Unknown at (6,6), then Monster or Rest Site.
- Decision: Take forced Unknown.
- Reason: No alternate at this step; next branch should favor Rest if the event costs HP or gives no recovery, otherwise consider smith equity at the rest site.

## Floor 7 - Haunted Ship
- Read: history/run22_strategy.md; kb/enemies/underdocks/haunted_ship.md.
- Status: Entered 32/80 with no potion; ended 32/80 after Burning Blood.
- Decision: Used Bludgeon on the free Haunt turn, then Perfected Strike + Defend on Ramming Speed, then Molten Fist + Pommel Strike for lethal through Weak.
- Reason: Haunted Ship gives a no-damage setup turn before Dazed dilution; frontloading with Bludgeon kept the fight short and avoided the 14-damage Swipe.

## Floor 7 - Rewards
- Read: kb/potions/liquid_bronze.md; kb/cards/ironclad/anger.md; kb/cards/ironclad/barricade.md; kb/cards/ironclad/colossus.md; kb/strategies/card_impressions.md.
- Status: 32/80, 201 gold, no potion. Offered Anger / Barricade / Colossus plus Liquid Bronze and 10 gold.
- Decision: Picked Colossus; claimed Liquid Bronze and 10 gold (211 total).
- Reason: Colossus fills the block hole and works with Bash/Molten Fist Vulnerable turns. Barricade lacks a block engine; Anger risks draw pollution in a deck already dealing with status fights.

## Floor 7 - Pathing
- Read: history/run22_strategy.md; kb/strategies/pathing.md; kb/enemies/bosses/waterfall_giant.md.
- Status: 32/80, 211 gold, Liquid Bronze. Options: Monster or Rest Site, both rejoin the same future path.
- Decision: Choose Rest Site.
- Reason: At 40% HP after a hard-pool hallway and no strong defensive potion, another Monster risks losing the run or forcing a worse rest later. Rest path keeps the same future route and preserves decision flexibility.

## Floor 8 - Rest Site
- Read: history/run22_strategy.md; kb/strategies/pathing.md; kb/enemies/bosses/waterfall_giant.md.
- Status: 32/80, 211 gold, Liquid Bronze. Options: Rest to 56/80 or Smith.
- Decision: Rest.
- Reason: Pommel Strike+ is the preferred smith, but 32 HP is too low before another Unknown and Waterfall Giant. Resting protects the run and may still allow smithing at later rest sites.

## Floor 8 - Pathing
- Read: history/run22_strategy.md; kb/strategies/pathing.md.
- Status: 56/80, 211 gold, Liquid Bronze. Only next node is Unknown, then Treasure.
- Decision: Take forced Unknown.
- Reason: No alternative; HP is now stable enough to handle a moderate event/combat, and the route immediately reaches a relic chest afterward.

## Floor 9 - Event: Abyssal Baths
- Read: history/run22_strategy.md; kb/events/abyssal_baths.md; kb/enemies/bosses/waterfall_giant.md.
- Status: 56/80, 211 gold, Liquid Bronze. Options: +2 max HP and take 3 damage, or heal 10.
- Decision: Chose Abstain for +10 HP, reaching 66/80. Added Abyssal Baths KB note.
- Reason: Immediate HP buffer is more valuable than small max HP before Waterfall Giant and future hard-pool hallways.

## Floor 9 - Pathing
- Read: history/run22_strategy.md; kb/strategies/pathing.md.
- Status: 66/80, 211 gold, Liquid Bronze. Only next node is Treasure.
- Decision: Take forced Treasure.
- Reason: No alternative; relic can improve boss/elite odds before the next route split.

## Floor 10 - Treasure
- Read: kb/relics/gambling_chip.md.
- Status: 66/80, 250 gold, Liquid Bronze.
- Decision: Claimed Gambling Chip.
- Reason: Mulligan improves opening consistency for expensive attacks, Colossus/Bash timing, and Waterfall Giant damage/block setup.

## Floor 10 - Pathing
- Read: history/run22_strategy.md; kb/strategies/pathing.md; kb/strategies/elites.md.
- Status: 66/80, 250 gold, Liquid Bronze, Gambling Chip. Options: Unknown leading to Shop/Elite, or Rest Site leading to forced Elite.
- Decision: Choose Unknown.
- Reason: Unknown keeps shop access with 250 gold and avoids a forced Underdocks elite. The deck has good frontload but still lacks upgrades and broad block/draw, so forcing an elite is unnecessary.

## Floor 11 - Event: The Legends Were True
- Read: history/run22_strategy.md; kb/events/the_legends_were_true.md; kb/mechanics/map_locations.md.
- Status: 66/80, 250 gold, Liquid Bronze. Options: Spoils Map or lose 8 HP for a random potion.
- Decision: Took Spoils Map.
- Reason: High current HP and Gambling Chip make one Unplayable more tolerable, and the Act 2 gold payoff is stronger than spending 8 HP for a random potion while already holding Liquid Bronze.

## Floor 11 - Pathing
- Read: history/run22_strategy.md; kb/strategies/pathing.md; kb/strategies/elites.md.
- Status: 66/80, 250 gold, Liquid Bronze. Options: Shop or Elite.
- Decision: Choose Shop.
- Reason: Shop can buy block/draw/removal/potion support before Waterfall Giant, while the elite is optional and the deck still lacks upgrades and broad defense.

## Floor 12 - Shop
- Read: history/run22_strategy.md; kb/cards/ironclad/dismantle.md; kb/cards/ironclad/headbutt.md; kb/cards/ironclad/expect_a_fight.md; kb/cards/ironclad/infernal_blade.md; kb/cards/ironclad/vicious.md; kb/cards/colorless/stratagem.md; kb/cards/colorless/nostalgia.md; kb/relics/lantern.md; kb/relics/vajra.md; kb/relics/lava_lamp.md; kb/potions/vulnerable_potion.md; kb/potions/liquid_bronze.md; kb/potions/distilled_chaos.md.
- Status: 66/80, 250 gold, Liquid Bronze. Key options: Lantern, Vajra, Dismantle, Vicious, sale Expect a Fight, Vulnerable Potion, removal.
- Decision: Discarded Liquid Bronze; bought Vulnerable Potion, Vicious, Expect a Fight, and Dismantle, ending at 17 gold.
- Reason: This commits to a Vulnerable package for Waterfall Giant and Act 2: Vicious adds draw, Dismantle is a high-output Vulnerable payoff, Expect a Fight provides energy in attack-heavy hands, and Vulnerable Potion gives a boss burst button. Lantern was strong but less cohesive than the full package.

## Floor 12 - Pathing
- Read: history/run22_strategy.md; kb/strategies/pathing.md; kb/enemies/bosses/waterfall_giant.md.
- Status: 66/80, 17 gold, Vulnerable Potion. Options: Rest Site or Unknown; remaining route has two forced Monsters before final Rest/Boss.
- Decision: Choose Rest Site.
- Reason: The shop added Vicious/Expect/Dismantle and the deck needs an upgrade before the forced combats and Waterfall Giant. Unknown value is less important than securing a smith/rest decision now.

## Floor 13 - Rest Site
- Read: history/run22_strategy.md; kb/cards/ironclad/vicious.md; kb/cards/ironclad/pommel_strike.md; kb/cards/ironclad/bludgeon.md; kb/enemies/bosses/waterfall_giant.md.
- Status: 66/80, 17 gold, Vulnerable Potion.
- Decision: Smith Vicious.
- Reason: Vicious+ turns Bash/Molten/Vulnerable Potion into stronger draw, supporting the new Vulnerable package and Waterfall Giant damage clock. HP is high enough to skip Rest.

## Floor 13 - Pathing
- Read: history/run22_strategy.md; kb/strategies/pathing.md; kb/enemies/bosses/waterfall_giant.md.
- Status: 66/80, 17 gold, Vulnerable Potion, Vicious+.
- Decision: Take forced Monster.
- Reason: Route is fixed through two Monsters, final Rest Site, then Waterfall Giant; preserve Vulnerable Potion for the boss unless survival requires it.

## Floor 14 - Gremlin Merc
- Read: history/run22_strategy.md; kb/enemies/underdocks/gremlin_merc.md.
- Status: Entered 66/80 with Vulnerable Potion; ended 42/80 after Burning Blood, potion preserved.
- Decision: Used Gambling Chip to replace three basic Strikes; used Bash + Molten Fist to set Vulnerable, blocked the second attack turn, killed Merc, then killed Fat Gremlin before Flee to recover 17 stolen gold and finished Sneaky Gremlin.
- Reason: KB says Fat Gremlin carries stolen gold and must die before Flee. Preserved Vulnerable Potion for Waterfall Giant; accepted HP loss because final rest is next after one more forced combat.

## Floor 14 - Rewards
- Read: history/run22_strategy.md; kb/cards/ironclad/stomp.md; kb/cards/ironclad/thunderclap.md; kb/cards/ironclad/unrelenting.md.
- Status: 42/80, 0 gold, Vulnerable Potion. Offered Stomp / Thunderclap / Unrelenting.
- Decision: Picked Thunderclap; claimed 28 total gold.
- Reason: Thunderclap is weak as a generic attack but strong in this deck because Vicious+ turns Vulnerable application into draw and Dismantle rewards Vulnerable enemies. Stomp and Unrelenting add more expensive attack pressure.

## Floor 14 - Pathing
- Read: history/run22_strategy.md; kb/strategies/pathing.md; kb/enemies/bosses/waterfall_giant.md.
- Status: 42/80, 28 gold, Vulnerable Potion.
- Decision: Take forced Monster.
- Reason: Route is fixed; play to preserve HP for the final campfire and save Vulnerable Potion for Waterfall Giant if possible.

## Floor 15 - Calcified Cultist + Seapunk
- Read: history/run22_strategy.md; kb/enemies/underdocks/cultists.md; kb/enemies/underdocks/seapunk.md.
- Status: Entered 42/80 with Vulnerable Potion; ended 22/80 after Burning Blood, potion preserved.
- Decision: Used Gambling Chip to replace two basic Strikes. Focused Calcified Cultist first with Perfected Strike + Molten Fist, then Thunderclap + Strike killed it before Ritual attacks grew. Used Dismantle on Vulnerable Seapunk, then blocked rather than spending Vulnerable Potion, and finished with Ashen Strike + Strike.
- Reason: Cultist KB warns Ritual scaling becomes dangerous after Incantation, while Seapunk's second turn was manageable. Preserving Vulnerable Potion for Waterfall Giant was worth taking a controlled HP loss before the final rest site.

## Floor 15 - Rewards
- Read: history/run22_strategy.md; kb/cards/ironclad/havoc.md; kb/cards/ironclad/armaments.md; kb/cards/ironclad/rage.md.
- Status: 22/80, 37 gold, Vulnerable Potion. Offered Havoc / Armaments / Rage plus Speed Potion.
- Decision: Picked Armaments; skipped Speed Potion by keeping Vulnerable Potion.
- Reason: Armaments adds immediate block and can improve high-impact unupgraded hands for Waterfall Giant and Act 2. Havoc risks exhausting key top-deck cards in an expensive deck, and Rage is less reliable without higher attack density or an upgrade. Vulnerable Potion is more important for boss burst/draw than temporary Dexterity.

## Floor 15 - Pathing
- Read: history/run22_strategy.md; kb/strategies/pathing.md; kb/enemies/bosses/waterfall_giant.md.
- Status: 22/80, 37 gold, Vulnerable Potion. Only next node is final Rest Site.
- Decision: Take forced Rest Site.
- Reason: The deck needs HP more than another reward before Waterfall Giant; pathing is fixed.

## Floor 16 - Rest Site
- Read: history/run22_strategy.md; kb/strategies/pathing.md; kb/enemies/bosses/waterfall_giant.md.
- Status: 22/80, 37 gold, Vulnerable Potion.
- Decision: Rested to 46/80.
- Reason: Waterfall Giant's A10 explosion and Pressure Gun punish entering low. Bludgeon/Pommel/Armaments upgrades are valuable, but 22 HP cannot safely cover boss attacks plus Steam Eruption.

## Floor 16 - Pathing
- Read: history/run22_strategy.md; kb/enemies/bosses/waterfall_giant.md.
- Status: 46/80, 37 gold, Vulnerable Potion.
- Decision: Enter Waterfall Giant.
- Reason: Boss is forced; plan is early Vulnerable burst, track Steam Eruption, and avoid triggering explosion without block/HP.

## Floor 17 - Waterfall Giant
- Read: history/run22_strategy.md; kb/enemies/bosses/waterfall_giant.md; kb/cards/ironclad/colossus.md; kb/cards/ironclad/armaments.md; kb/cards/ironclad/vicious.md; kb/cards/ironclad/dismantle.md; kb/cards/ironclad/expect_a_fight.md.
- Status: Entered 46/80, 37 gold, Vulnerable Potion.
- Decision: Used save/load retries to test multiple distinct boss lines. Best line kept the opening hand, upgraded Bludgeon with Armaments, played Vicious+, used Vulnerable Potion on turn 2, used Bash/Colossus to prevent Ram damage, held Colossus for the first Pressure Gun, and used Armaments to upgrade Ashen Strike.
- Result: Loss on floor 17 to Waterfall Giant. Newest Steam history file `1778885117.run` reports `win: false`, `was_abandoned: false`, `killed_by_encounter: ENCOUNTER.WATERFALL_GIANT_BOSS`.
- Reason: The deck could either block early attacks or push damage, but not both fast enough. The best line reached Death Blow with the boss dead, but Steam Eruption had climbed to 50 while HP was 11; Armaments + Colossus only produced 10 block because the Death Blow state has no Vulnerable status, so Colossus did not halve the explosion.

## Post-Run Reflection
- Worked well: Gambling Chip plus Vicious+ made the boss opener consistent, and saving Vulnerable Potion was correct for draw and Dismantle damage. Colossus was excellent on live Vulnerable attack turns.
- Avoidable cost: The Act 1 deck took too many speculative/offensive cards and not enough real block before Waterfall Giant. The shop package improved damage but did not solve the explosion block check.
- Next change: Against Waterfall Giant, prioritize an upgraded block plan or a faster kill before the second Pressure cycle. If entering below roughly 55 HP without strong block, do not rely on late Death Blow survival.
- Harness/mechanic lesson: Save/load correctly restored the boss room, but repeated lines confirmed Death Blow is a separate next turn and strips enemy Vulnerable; Colossus only grants 5 block there.

## Action-by-Action Review
- Pre-run/Neow: Reads were complete. Lost Coffer into Perfected Strike was a defensible low-risk opening: it avoided Greed and immediately gave 16-damage frontload for early hallways. The downside was committing early attention to Strike-count damage rather than block before seeing Waterfall Giant.
- Floor 1 path: Right path was reasonable because it avoided forced early elites and preserved shop/rest access. The hidden cost was many forced hallways; once the first branch appeared, future choices needed to bias heavily toward HP and block.
- Floor 2 Toadpoles: Targeting the attacking Toadpole first was correct, but Steam history reports 18 raw damage and 52 HP after Burning Blood. This was the first signal that the opener had damage but not enough block density.
- Floor 2 reward: Bludgeon over Twin Strike/second Perfected Strike was correct for Act 1 frontload. The later boss loss was not because Bludgeon was bad; it was because the deck did not pair its expensive damage with enough energy/block.
- Floor 3 Sunken Treasury: Taking 66 gold over Greed was correct. Greed would have worsened an already draw-sensitive boss deck.
- Floor 4 Sludge Spinner: Bludgeon into Bash/Strike killed in 2 turns with only 9 raw damage. Clean execution; this is where Bludgeon paid for itself.
- Floor 4 reward: Speed Potion over Colorless Potion and Molten Fist over Havoc/Twin Strike were reasonable. Molten Fist later supported Vicious/Dismantle, and the Speed Potion saved real HP in Sewer Clam.
- Floor 5 Seapunk: Two-turn kill with Bludgeon + Perfected Strike was correct; 13 raw damage was acceptable but reinforced the need for defense.
- Floor 5 reward: Pommel Strike was the best pick. It added draw, damage, and a Strike tag, and should have remained a high smith candidate if Vicious had not appeared.
- Floor 6 Sewer Clam: Speed Potion use was correct; saving 10 HP before the first rest was worth more than speculative later value. Ashen Strike was acceptable as a Strike-tag 1-cost attack, but it was another damage card in a deck that already needed block.
- Floor 7 Haunted Ship: Good sequencing: using the free Haunt turn for Bludgeon and ending before Swipe avoided the fight's worst damage. Colossus pick was correct because it finally answered the block hole.
- Floor 8 Rest: Resting at 32/80 was correct. A smith would have risked losing to the next event/combat branch before boss prep.
- Floor 9 Abyssal Baths: Taking the 10 HP heal was correct with Waterfall Giant ahead. The max-HP option would have reduced current boss margin.
- Floor 10 Gambling Chip: Excellent relic for this deck. It fixed opening consistency, but it could not solve missing block once the fight went long.
- Floor 11 The Legends Were True: Spoils Map was greedy in hindsight. At 66 HP it looked affordable, but against Waterfall Giant the dead draw appeared in multiple boss hands; the random potion line may have been better because the deck already had shop money and still lacked reliable block.
- Floor 12 shop: Buying Vulnerable Potion, Vicious, Expect a Fight, and Dismantle built a coherent damage/draw package. The issue was opportunity cost: no removal, Lantern/Vajra skipped, and no hard block solution. The package improved the kill clock but did not improve the Steam Eruption survival check.
- Floor 13 smith: Vicious+ was coherent with the package and likely the best offensive upgrade. However, after the shop committed to a boss race, the run needed either faster lethal before the second Pressure cycle or an upgraded block card; Vicious+ alone made hands larger, not safer.
- Floor 14 Gremlin Merc: Killing Fat Gremlin before Flee was correct, but the fight cost 30 raw damage and left 42 HP after Burning Blood. This was the largest avoidable pathing/combat equity loss; preserving the Vulnerable Potion was useful, but the boss margin was already shrinking.
- Floor 14 reward: Thunderclap was coherent with Vicious/Dismantle. It added another Vulnerable trigger, but also another low-damage attack that did not fix Waterfall Giant's block math.
- Floor 15 Cultist + Seapunk: Targeting Cultist first was right, and preserving Vulnerable Potion was defensible. The fight still cost 26 raw damage, leaving only 22 HP before the final rest; at this point the run was locked into resting and entering the boss at 46.
- Floor 15 reward: Armaments over Havoc/Rage was correct for immediate block and hand upgrades. Skipping Speed Potion for Vulnerable Potion is close; given the final boss result, Speed Potion might have covered one late attack better, but Vulnerable Potion was needed for the best damage/draw line.
- Floor 16 rest: Mandatory at 22 HP. The earlier decisions had already spent smith equity.
- Boss retry review: Save/load use was appropriate and tested materially different lines. The best line upgraded Bludgeon, played Vicious+, used Vulnerable Potion on turn 2, blocked Ram with Bash/Colossus, used Colossus on Pressure Gun, and reached lethal. The fight still took 13 turns, giving Waterfall Giant a 50-damage Death Blow while the player had 11 HP.
- Final tactical lesson: The deck could block selected Vulnerable attack turns or push damage, but not both across a long Waterfall Giant cycle. For this boss, a late kill is not enough; the run must either kill before Steam Eruption reaches lethal size or enter the Death Blow turn with exact block and HP already secured.

## KB Updates From Review
- Added Colossus note: delayed/death-blow protection only works if the enemy is still Vulnerable at the hit.
- Added The Legends Were True note: Spoils Map can be worse than the potion line before Waterfall Giant when the deck still needs block and clean draws.
- Existing Waterfall Giant note already captures the Death Blow/Colossus interaction and remains the main boss-specific lesson.
