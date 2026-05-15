# Ironclad Manual Run - 2026-04-30

- Controller: Codex via direct STS2 MCP HTTP API calls; no controller bot/script.
- Strategy source: AGENTS.md, GUIDE.md, run9 reflection, and per-choice KB lookups.
- Carry-forward lessons from run9: keep explicit Smith/Rest math, avoid forced elite branches at medium HP, treat draw/energy as the baseline, sequence Music Box/Mummified Hand-style effects carefully, evaluate enchants and potions by damage packets, and trust live hand state over stale previews.
- Outcome: Win; defeated Doormaker on floor 48 and reached The Architect post-boss event.

- F1 A1 Neow: Offered Precise Scissors, Lava Rock, and Leafy Poultice. Neow KB says Precise Scissors is a no-downside one-card removal, Lava Rock delays value until the Act 1 boss drops two relics, and Leafy Poultice transforms one Strike/Defend at the cost of 12 Max HP. Took Precise Scissors and removed a Strike because early draw quality is reliable value and avoids starting the run at 68 Max HP. Harness note: Precise Scissors opened a deck selection screen requiring `select_card` with `index`, then `confirm_selection`.
- F2 A1 path: Boss is The Kin. Chose the left row-1 Monster path because it offers early reward information, two Unknowns, a second Monster, then a Shop with a route toward a row-6 RestSite. This is safer than the right-side three-Monster opener and avoids committing to an early forced elite before the deck has damage upgrades.
- F2 A1 combat: Fuzzy Wurm Crawler. Crawler KB says it cycles Acid Goop (4), Inhale (+7 Strength), then Acid Goop again for 11, with Strength carrying into later cycles. Opened with two Strikes plus Defend to block the first 4, used the no-attack Inhale turn for three Strikes instead of Bash because raw damage was better than a one-Strike Vulnerable payoff, then accepted a 6 HP leak on the 11 attack to keep damage moving. Killed on the next 11-intent turn with three Strikes and ended at 80/80 after Burning Blood. Reflection: Perfected Strike-type frontload would have shortened this fight; Crawler punishes slow starter hands after Inhale.
- F2 reward: Offered True Grit, Perfected Strike, Setup Strike. True Grit KB has strong long-term/exhaust signal and is a major upgrade target, while Perfected Strike KB says it is best treated as an Act 1 bridge. Picked Perfected Strike because the deck removed a Strike at Neow and needs immediate damage more than another defensive card before The Kin; do not force it as the endgame plan. Claimed 11 gold, reaching 110.
- F3 path: Chose row-2 Shop over Unknown at 110 gold. This follows the shop-at-100+ rule, can find an early premium card/removal/potion, and still routes through Unknown -> Monster to the row-5 branch with another possible shop/rest line.
- F3 shop: Bought Molten Fist for 49 and True Grit for 49, ending at 12 gold. Molten Fist is 1-cost 10 damage that doubles Vulnerable and should pair with Bash/Perfected Strike for The Kin; True Grit restores the long-term block/exhaust card skipped on F2 and is a likely smith target later. Skipped Spite because there is no reliable same-turn HP-loss enabler yet, skipped Drum of Battle because the KB warns its repeated top-card exhaust can lose important cards, and skipped removal because Precise Scissors already removed one Strike.
- F4 event: Brain Leech. Event KB says Share Knowledge gives a choice of 1 of 5 random cards, while Rip costs 5 HP for a Colorless reward. Took Share Knowledge because it preserves HP and showed a broader card choice. Offered Evil Eye, Stampede, Second Wind, Pommel Strike, and Shrug It Off. Picked Pommel Strike because its KB says it is the highest-frequency final-deck card and top smith target, it adds attack draw, and its Strike tag supports the temporary Perfected Strike plan. Skipped Shrug because True Grit already covers early block, skipped Second Wind/Evil Eye until more exhaust support exists, and skipped Stampede as slower/random.
- F5 A1 combat: Shrinker Beetle. Beetle KB says it opens with Shrinker, then alternates Chomp for 7 and Stomp for 13. Opening hand had Perfected Strike, Molten Fist, Pommel Strike, and two Defends. Played Perfected Strike first for 18 and then Molten Fist after realizing it would not stay in hand for a future Bash combo; this left the Beetle at 10 before Shrink. Live state confirmed Shrink makes Attacks deal 30% less damage while the Beetle is alive. Next turn, three reduced Strikes dealt 4 each and killed before the 7 attack. Ended at 80/80 and claimed Taunt over Colossus/Tremble because the deck needs attack-turn block plus Vulnerable support for Perfected Strike, Pommel Strike, Bash, and Molten Fist. Claimed Strength Potion and 20 gold, reaching 32 gold. Reflection: preserve hand-state discipline; non-Retain cards cannot be planned around for next turn.
- F6 path: Chose row-5 Monster over Shop because 32 gold is too low for a meaningful purchase and the deck still wants combat rewards. The Monster path still preserves a row-6 RestSite option afterward, while leaving Unknown/Elite choices open if HP remains high.

### F6 - Slimes
- Entered at 80/80. Used Taunt + Molten Fist to kill Leaf Slime S and Pommel Strike to kill Twig Slime S before extra statuses built up.
- Turn 2 chose Defend -> True Grit -> Strike to fully block 11; True Grit exhausted a spare Strike.
- Turn 3 Perfected Strike left Twig Slime M at 4 HP. Mistake/finding: Slimed costs energy in this harness/game, so drawing Strike with 0 energy did not finish; accepted one extra status turn but took 0 damage.
- Finished at 80/80; rewards: 19 gold and card reward pending.
- F6 card reward: Offered Uppercut / Armaments / Howl from Beyond. KB: Uppercut has strong 161-win signal and upgrade priority; Armaments is best when upgraded but competes with True Grit+/Pommel+/Uppercut+; Howl needs exhaust support we lack. Picked Uppercut for Weak plus Vulnerable against elites/boss. Claimed 19 gold, now 51.

### F7 path
- Chose Elite over immediate RestSite/Unknown at 80/80 with Strength Potion. GUIDE elite threshold is >70% HP; follow-up path has Monster then RestSite, so the relic chance is worth the risk.

### F7 - Elite: Phrog Parasite
- Read KB: Phrog alternates Infect/Lash and summons 4 Wrigglers; attack-kill gives one immediate stunned enemy phase, not a full free player turn after.
- Used Strength Potion immediately because it carries into Wrigglers and reduced Phrog before Lash. Sequenced Bash -> Molten Fist for 28 damage and 4 Vulnerable.
- Killed Phrog on T2 before Lash with Perfected Strike + Strike. Wrigglers spawned stunned.
- Wriggler phase lesson: attack/status targets shift after kills, and IDs renumber visually in API output; re-read after every kill. Prioritized killing attacking Wrigglers over blocking.
- Took 20 net HP after Burning Blood (80 -> 66) mostly from Wriggler attacks and Infection hands. Reward pending: 38 gold, Happy Flower, card reward.
- F7 rewards: Card reward Body Slam / Blood Wall / Bully. KB: Body Slam wants larger repeatable block and upgrade; Bully wants larger Vulnerable stacks; Blood Wall base copy is a large one-card block tool and usually enough. Picked Blood Wall for The Kin/elite survival. Took Happy Flower and 38 gold (89 total). Live relic text says Happy Flower grants energy every 3 turns, while KB file title/text appears to describe Happy Flower??? every fifth turn; needs KB correction.

### F8 path
- Forced Monster after elite. Entering at 66/80, 89 gold, no potion, Happy Flower counter 0. Need protect HP because next immediate node may still be a fight before rest.

### F8 - Shrinker Beetle + Fuzzy Wurm Crawler
- Read KB: Beetle opens Shrink then alternates 7/13 attacks; Shrink reduces attacks 30% while Beetle lives. Fuzzy Wurm cycles 4 attack -> +7 Strength -> 11 attack.
- T1 spent Bash + Strike into Beetle, accepting 4 from Wurm to shorten Shrink duration.
- T2 Molten Fist + two Strikes left Beetle at 1; this cost the Beetle 7 attack next turn. In hindsight, count exact Shrink+Vulnerable damage and consider block if the kill misses by 1.
- T3 Happy Flower gave 4 energy; killed Beetle, clearing Shrink, then Taunt + Perfected Strike hit Wurm to 30 while taking 4.
- T4 Uppercut + Pommel Strike left Wurm at 4 and Weak reduced incoming to 8. Finished T5. Ended at 49/80 after Burning Blood.
- Reward pending: 14 gold and card reward.
- F8 card reward: Offered Feel No Pain / Bloodletting / Fight Me!. KB: Feel No Pain wants more exhaust density; Fight Me is scaling but gives enemy Strength; Bloodletting appears in 74.5% of winning final decks and supports Pommel/2-cost turns. Picked Bloodletting. Claimed 14 gold (103 total).

### F9 path
- Forced Monster at 49/80, no potion, Happy Flower counter 2. Treasure follows, then likely more pathing before rest; need preserve HP and use Blood Wall/Uppercut more defensively.

### F9 - Nibbits
- Read KB: paired Nibbits open Slice+Block and Hiss, then cycle Butt/Slice/Hiss.
- T1 Happy Flower gave 4 energy; used Perfected Strike + Strike + Defend into front Nibbit, taking 1.
- T2 used Taunt before Uppercut on the attacking back Nibbit: Uppercut benefited from Vulnerable, applied Weak, and reduced 14 incoming to 3 leaked damage.
- T3 killed front Nibbit with Bash + Molten Fist to remove 14 of 22 incoming, taking only 8 from back.
- T4 avoided Bloodletting/Blood Wall HP costs on a no-attack turn; used Pommel, Taunt, Strike. Finished T5. Ended at 43/80 after Burning Blood. Rewards pending: 20 gold, Radiant Tincture, card.
- F9 card reward: Offered Shrug It Off / Colossus / Twin Strike. KB: Shrug appears in 67.7% of final decks as base cantrip block; Colossus is conditional on enemy Vulnerable; Twin Strike is more Strike damage but no defense/draw. Picked Shrug It Off. Took Radiant Tincture and 20 gold (123 total).

### F10 path
- Taking forced Treasure at 43/80. Need claim with treasure-specific action if a relic chest opens.
- F10 treasure: Chest gave 48 gold and Vambrace. KB/text: first Block from a card each combat is doubled; sequence Blood Wall/Shrug/True Grit/Taunt before smaller block when possible. Claimed with `claim_treasure_relic`.

### F11 path
- Forced Monster before RestSite at 43/80 with Radiant Tincture, Happy Flower counter 1, Vambrace. Goal: preserve enough HP to smith at the rest site instead of being forced to heal.

### F11 - Cubex Construct
- Read KB: starts with Artifact, opens Charge Up, then Repeater/Repeater/Expel while Strength ramps.
- T1 used Uppercut to clear Artifact on the no-attack turn, then Strike; live result: Artifact blocked Weak but Vulnerable landed, Strike hit for 9.
- T2 Happy Flower gave 4 energy; Molten Fist + Strike + Defend. Vambrace doubled the first Defend to 10 and fully blocked 9.
- T3 reminder: Vambrace is once per combat, not once per turn. Taunt gave normal 7 block because Vambrace had already been used. Added Shrug to full block and skipped Bloodletting because lethal was likely next turn without HP loss.
- T4 Perfected Strike killed before 11x2 Expel. Ended at 49/80 after Burning Blood. Reward pending: 14 gold and card.
- F11 card reward: Offered Havoc / Perfected Strike / Body Slam. KB: Perfected Strike is an Act 1 bridge; Havoc is unpredictable; Body Slam becomes good with Blood Wall, Shrug, True Grit, Taunt, and Vambrace. Picked Body Slam as block-to-damage payoff. Claimed 14 gold (185 total).

### F12 rest site
- Rest option would heal 24 to 73/80. Chose Smith by rule: 49/80 plus Burning Blood, Vambrace, Radiant Tincture, and another later rest path is enough HP.
- Upgrade choice: True Grit over Pommel/Uppercut/Body Slam. KB says True Grit is a tier-1 upgrade with 87.2% upgraded final copies; True Grit+ gives 9 block and targeted exhaust, and as first Vambrace block can make 18 block.
- Smith completed: upgraded True Grit.

### F13 path
- Forced Monster at 49/80 with True Grit+, Radiant Tincture, Vambrace. Need preserve HP through two hallway fights before the next branch/rest.

### F13 - Hard Slimes
- Read Slimes KB: medium Leaf opens with 2 Slimed, medium Twig opens with 1 Slimed; small Twig attacks every turn.
- T1 Happy Flower 4 energy: Defend first, then Body Slam + Strike killed Leaf Slime S. Chose status prevention over killing Twig S because block covered the small attack.
- T2 incoming 23: True Grit+ exhausted Bloodletting via hand-select, then Taunt + Shrug fully blocked. Harness note: in-combat exhaust uses `combat_select_card` and `combat_confirm_selection`, not deck `select_card`.
- T4 two Defends + Body Slam + Strike killed Leaf Slime M and reduced 19 incoming to 1 leaked damage. This validated Body Slam pick with block density.
- Finished at 52/80 after Burning Blood. Reward pending: 16 gold and card.
- F13 card reward: Offered Anger / Tremble / Breakthrough. KB: Anger is early bridge and copy-bloats; Breakthrough is AoE with HP loss; Tremble has 42.9% final-deck signal and provides cheap 3 Vulnerable. Picked Tremble for The Kin leader-focused burst. Claimed 16 gold (201 total).

### F14 path
- Forced Monster at 52/80, 201 gold, Radiant Tincture. Unknown then final RestSite remain before The Kin. Preserve enough HP to consider final Smith.

### F14 - Fogmog
- Read KB: focus Fogmog over Eye With Teeth because Eye revives and keeps adding Dazed; Eye is only worth killing to deny a specific Dazed turn.
- T1 used Taunt first for Vambrace, then Body Slam + Strike into Fogmog.
- T2 killed Eye with Strike to prevent 3 Dazed that turn, then Uppercut on Fogmog; accepted 6 damage.
- T3 Happy Flower gave 4 energy; Tremble -> Perfected Strike -> Molten Fist killed Fogmog before Eye added more Dazed. Tremble immediately paid off as boss-style burst setup.
- Ended at 52/80 after Burning Blood. Rewards pending: 11 gold, Blood Potion, card.
- F14 card reward: Offered True Grit / Hemokinesis / Shrug It Off. Took second Shrug It Off for cantrip block, Body Slam support, and boss consistency. Claimed Blood Potion in slot 1 and 11 gold (212 total).

### F15 path
- Taking Unknown before final RestSite at 52/80, with Radiant Tincture and Blood Potion. Avoid unnecessary HP loss; preserve final Smith option.

### F15 event - Wood Carvings
- Read KB: Bird transforms a starter into Peck; Snake enchants Slither; Torus transforms a starter into Toric Toughness.
- Chose Torus. Plan: transform a basic Defend, not a Strike, because Toric Toughness is a stronger defensive starter replacement and supports Body Slam/Vambrace without reducing damage density further.
- Transformed a basic Defend into Toric Toughness.

### F16 final rest before The Kin
- Entered at 52/80 with Blood Potion (+16 effective HP) and Radiant Tincture. Rest would heal 24 to 76/80, but Smith leaves effective 68/80 and improves boss plan. Chose Smith by rule.
- Upgrade target: Uppercut over Body Slam/Pommel/Bash. Uppercut+ gives 2 Weak and 2 Vulnerable, the highest-impact boss upgrade after True Grit+ because it improves both survival and burst.
- Smith completed: upgraded Uppercut.

### F17 boss path - The Kin
- Entering boss at 52/80, with Radiant Tincture and Blood Potion. Plan: use Blood Potion early for +16 HP; use Radiant Tincture when the hand can convert energy into burst/block. The Kin KB says damage scales over time; focus priest/leader, control followers only when necessary.

### F17 boss - The Kin
- Used Blood Potion immediately (52 -> 68) and Radiant Tincture on T1 because the hand could convert energy into Taunt -> Uppercut+ -> Molten Fist on the Priest.
- T1 dealt 34 to Priest, stacked 6 Vulnerable, and fully blocked with Taunt/Vambrace.
- T2 accepted small damage to keep pressure during Vulnerable; Perfected Strike + Strike pushed Priest to 120.
- T3 Blood Wall + Tremble + Body Slam was the key turn: Blood Wall prevented the multiattack and made Body Slam hit hard through Vulnerable, dropping Priest to 93.
- T4 Toric Toughness + Bloodletting funded Bash + Strike; True Grit+ with empty hand fully blocked the remaining follower hit.
- T5 double Shrug found Body Slam; chose Body Slam over full block, dropping Priest to 41 while taking manageable damage.
- T6 full offense with Uppercut+ and two Strikes left Priest at 4; took damage but set guaranteed leader kill.
- T7 killed Priest with Strike; minion followers fled. Act 1 boss defeated at 38/80. Rewards pending: 100 gold, Blessing of the Forge, boss card reward.
- Boss card reward: Offered Barricade / Stoke / Conflagration. Picked Barricade because the deck now has Blood Wall, two Shrugs, True Grit+, Toric Toughness, Vambrace, and Body Slam; block retention can become the Act 2 engine. Took Blessing of the Forge and 100 gold (312 total).

## Act 2 start
- Harness advanced directly to Act 2 map after boss rewards and initially displayed 38/80, but opening the Act 2 Ancient node showed 80/80. Treat the 38/80 map display as transient/pre-node state; the run effectively began Act 2 at full HP, 312 gold, and Blessing of the Forge.

### F18 Ancient - Darv
- Read Darv KB: Black Star gives delayed elite relic value, Calling Bell gives 3 immediate relics plus an Eternal unremovable Curse, and Pandora's Box transforms all Strikes and Defends.
- Picked Pandora's Box. Reasoning: Perfected Strike was only an Act 1 bridge, while the deck already has block/draw/Vulnerable pieces and benefits more from turning seven remaining basics into real cards than from preserving Strike count. Calling Bell's permanent dead draw is worse for a Barricade/Body Slam deck, and Black Star needs successful Act 2 elite routing before paying off.
- Save/deck check after transform: basics became Tremble, Stomp x2, Juggernaut, Pyre, Fiend Fire, and Unmovable. This is a major quality spike for the Barricade/Body Slam plan and makes Perfected Strike less important.

### F19 path
- Chose right-side Monster route. It reaches an early Shop/Rest branch after several nodes, which matters with 312 gold and a newly transformed deck, while still leaving optional elite value if HP remains high.

### F19 - Thieving Hopper
- Read KB: fixed sequence is Thievery -> Flutter -> Hat Trick -> Nab -> Escape; stolen cards return if Hopper dies before Escape. T1 stolen card was Stomp, confirming the threat is real but recoverable.
- T1 used Bloodletting -> Toric Toughness -> Pommel Strike -> Stomp. Took 7 combat damage plus Bloodletting HP loss; Toric gave recurring block and early damage mattered more than slow Pyre setup.
- T2 used the no-attack Flutter turn for Uppercut+ -> Molten Fist, stacking Vulnerable and dropping Hopper to 30.
- T3 used Blood Wall -> Body Slam to block the 15 attack and push Hopper to 11. Finding: Body Slam damage is still reduced by Flutter after Vulnerable math, but the block line preserved HP.
- T4 Taunt -> Fiend Fire left Hopper at 1 through Flutter, but the combat ended immediately afterward and rewards appeared with Stomp recoverable. Ended at 74/80 after Burning Blood.
- Rewards: reclaimed stolen Stomp, took Skill Potion, 11 gold, and picked a second Bloodletting over Twin Strike/Havoc. KB supports Bloodletting as a strong draw/energy shell card, and this post-Pandora deck has several expensive powers/payoffs.

### F20 path
- Chose Unknown over Monster because both routes converge at the same row-3 Unknown, the deck already grew from Pandora, and preserving HP before the shop/rest branch is worth more than one extra hallway reward.

### F20 - Bowlbugs
- Unknown rolled a Bowlbug (Rock) + Bowlbug (Egg) fight. Bowlbugs KB says Rock is stunned if Headbutt is fully blocked; the live intent was 15 from Rock plus 7 from Egg.
- T1 Happy Flower gave 4 energy. Played Juggernaut first, then Taunt and Shrug to reach exactly 22 block, fully preventing damage and stunning Rock. Bloodletting funded extra plays; Body Slam used the 22 block to kill Egg before it could add block.
- T2 Rock was stunned; Pommel Strike -> Uppercut+ left it at 8 with Weak/Vulnerable. T3 Perfected Strike killed. Ended at 77/80 after Burning Blood.
- Rewards: picked Stone Armor+ over Stomp+/Shrug. Rationale: cheap upgraded Plating supports Barricade, Body Slam, Juggernaut, and future full-block checks; another Stomp would make the deck heavier and a third Shrug is lower marginal value.

### F21 event - Slippery Bridge
- Read event KB: Overcome removes the shown random card; Hold On rerolls the card with escalating HP loss.
- Initial removal target was Fiend Fire, which is too important as burst/exhaust payoff. Paid 3 HP to reroll.
- Reroll target became Stomp. Accepted removal because the deck had two Stomps, the card is expensive, and preserving HP plus avoiding a bad reroll was better than fishing for a perfect remove. Ended event at 74/80.

### F22 path
- Chose right Monster branch toward the row-6 Shop over the left Monster branch toward RestSite. With 74/80 HP, Burning Blood, two potions, and 334 gold, shop access is worth more than an early rest.

### F22 - Chompers
- Read Chomper KB: the pair alternates Clamp (8x2) and Screech (3 Dazed), and each starts with Artifact, so focus the currently attacking Chomper.
- Used Skill Potion because the opener had Barricade/Unmovable but no native block into 16 damage. Potion offered Taunt / Expect a Fight / Forgotten Ritual; chose Taunt for immediate block and Artifact stripping.
- T1 Bloodletting funded Barricade + Unmovable. Free potion Taunt then stacked with both Vambrace and Unmovable for 28 block, confirming the doubling interaction; Pommel added chip damage.
- T2 set Juggernaut and Pyre while using Taunt to stay fully covered. T3+ Barricade retained the block buffer, and Juggernaut plus Shrug/Toric/Stone Armor made the fight safe despite Dazed shuffles.
- Body Slam at 18 block nearly killed the first Chomper through Vulnerable; Molten Fist finished it. Stone Armor+ Plating and Toric Toughness kept block high for the second Chomper, and Uppercut+ -> Pommel Strike ended the fight.
- Ended at 74/80 after Burning Blood. Rewards: picked Breakthrough+ over Taunt/Bloodletting because upgraded 1-cost AoE replaces some lost Stomp value, helps multi-enemy Act 2 fights, and the 1 HP cost is manageable.

### F23 - Ovicopter
- Read Ovicopter KB: it opens by summoning 3 Tough Eggs, then Smash, then Tenderizer + Vulnerable; hatchlings are Minions and leave when the Ovicopter dies.
- T1 attacked Ovicopter with Pyre, Breakthrough+, and Pommel Strike before eggs existed, dropping it to 102. T2 used Blessing of the Forge because the hand contained Barricade/Blood Wall and the eggs were about to hatch; Barricade+ -> Blood Wall+ created 40 retained block.
- T3-T4 set Juggernaut and Stone Armor+ while keeping Vulnerable on Ovicopter. Breakthrough+/Stomp/Juggernaut chip managed hatchlings without shifting focus away from the leader.
- T5 Bloodletting + Blood Wall+ + Toric Toughness + Shrug It Off held enough block into Ovicopter's 21 plus hatchling damage. Shrug drew Body Slam; 34 block into Ovicopter's Vulnerable dealt lethal, and the remaining hatchling fled. Ended at 72/80 after Burning Blood.
- Rewards: took Swift Potion and 11 gold; skipped Havoc / Perfected Strike / Thunderclap. Perfected Strike lost value after Pandora removed basics, Havoc is uncontrolled in a deck with key powers, and Thunderclap duplicated existing Vulnerable from Bash/Uppercut+/two Trembles.

### F24 shop
- Entered with 72/80 HP, 363 gold, and Swift Potion before a forced elite.
- Bought Burning Pact for 38 on sale. KB/run analysis supports it as a common winning draw/exhaust card, and this deck needs faster access to Barricade/Body Slam/Power setup.
- Bought Feed for 144. The deck has enough Vulnerable/block control to set up Fatal kills, and extra max HP should matter across the remaining Act 2 and Act 3 fights.
- Bought card removal for 75 and removed Perfected Strike. Pandora removed the starter Strikes, so Perfected Strike no longer justifies a 2-energy draw.
- Bought Energy Potion and Block Potion, filling slots with Swift / Energy / Block before the forced elite. Skipped Bread because first-turn energy loss fights the deck's setup turns; skipped Festive Popper and Bronze Scales because the gold was better spent on Feed + removal + elite potions.

### F25 elite - Infested Prism
- Read KB: fixed cycle is Jab -> Radiate -> Whirlwind -> Pulsate; Vital Spark only refunds energy when Attack damage reaches HP, not when blocked.
- T1 used Swift Potion because the opener had Unmovable/Pyre/Tremble/Bloodletting/Bash but no block. Swift found Taunt, Uppercut+, and Feed. Bloodletting plus Taunt covered most of Jab; Uppercut+ dealt HP damage, triggered Vital Spark, and applied Weak; Energy Potion enabled Pyre + Unmovable + Tremble in the same turn. Saved Feed because it was not Fatal.
- T2 used the second Bloodletting to install Barricade, Juggernaut, Stone Armor+, and another Tremble. Block Potion became 12 retained block and also triggered Juggernaut for 5 damage, confirming potion block can trigger Juggernaut.
- T3 Whirlwind turn: Shrug doubled to 16 via Unmovable, Juggernaut cleared part of Prism's block, Pommel broke through for Vital Spark, then Shrug + Body Slam + Stomp pushed Prism to 101 while full-blocking.
- T4 Pulsate turn: Toric Toughness built retained block, then Molten Fist doubled the Vulnerable stack and Breakthrough+ pushed Prism to 57. Did not spend Feed at 57 because it could not be Fatal.
- T5 Burning Pact exhausted Fiend Fire to draw Bash and Uppercut+. Uppercut+ + Bash + Stomp left Prism at 13; Feed still did not line up. T6 Body Slam killed at 3 HP. Ended at 66/80 after Burning Blood.
- Rewards: took Red Mask, Attack Potion, 43 gold, and Rage over Rampage/Brand. Rage is 0-cost retained-block support with Barricade, Body Slam, and Juggernaut; Brand is strong but adds another HP-loss/selection card and only gives 1 Strength unupgraded.
- Harness note: direct HTTP action is `end_turn`, not `combat_end_turn`; Burning Pact's in-combat hand selection used `combat_select_card` followed by `combat_confirm_selection`.

### F26 path
- Chose the left Treasure -> Unknown -> RestSite branch. It preserves an optional post-rest elite, while the right branch gives a late shop with only 48 current gold.

### F26 treasure
- Chest gave 42 gold and Pendulum. Pendulum draws 1 card every 3 turns, which improves long fights where Barricade/Pyre/Juggernaut need cycling.

### F27 - Bowlbug Rock / Bowlbug Silk / Slumbering Beetle
- Unknown became a hallway fight. Read Bowlbug and Slumbering Beetle KB: full-block Rock to stun it, kill or heavily damage supports before waking Beetle because Roll Out gains +2 Strength every turn.
- T1 Taunt on Rock gave Vambrace block and full-blocked Headbutt, then Uppercut+ put Rock at 26 with Weak/Vulnerable. Rock stunned as expected.
- T2 Rage + Stone Armor+ + Breakthrough+ + Pommel damaged Rock/Silk while only hitting Beetle's block, keeping Beetle asleep. Pommel left Rock at 2 but missed Feed.
- T3 Bloodletting funded Unmovable + Shrug; Body Slam killed Rock, then Tremble set up Silk. Avoided unnecessary True Grit/Bloodletting lines when block was already sufficient.
- Beetle woke before Silk died, so used Burning Pact to exhaust Barricade and find Blood Wall, covering a 24-damage turn. This confirmed the risk in the KB note: delaying support cleanup lets Beetle scaling overlap with Silk pressure.
- Fed on Silk at 5 HP, raising max HP from 80 to 83. Then used Shrug/Toric/Body Slam/Pommel/Breakthrough to finish Beetle at 58/83 after Burning Blood.
- Rewards: took Howl from Beyond+ over Pommel Strike/Perfected Strike. KB says Howl must be put into Exhaust by another effect, but this deck has Burning Pact, True Grit+, and Fiend Fire; upgraded 21 AoE each turn from Exhaust is a strong late-game payoff. Took Snecko Oil and 16 gold.

### F28 rest site
- Entered at 58/83 with Attack Potion and Snecko Oil. Rest would heal 24 to 82/83, but HP plus potions were enough for the optional elite branch.
- Smith over Rest by rule. Upgraded Barricade because the cost drops from 3 to 2, directly improving the deck's core setup turns and reducing reliance on Bloodletting/potions to establish retained block.

### F29 path
- Chose optional Elite over Unknown because both branches converge to the same Monster afterward, and 58/83 with two potions plus Barricade+ is enough to chase the relic.

### F29 elite - Entomancer
- Read KB: fixed cycle is Beeeees! -> Spear -> Pheromone Spit; Personal Hive adds Dazed per Attack hit and the Pheromone turn increases Hive plus Strength.
- T1 played Unmovable then Taunt. Red Mask weakened the 2x7 opener, and Vambrace + Unmovable made Taunt enough to full-block without adding Dazed.
- T2 True Grit+ fully blocked Spear and exhausted Feed. This gave up Feed max HP but preserved Fiend Fire/Burning Pact/Tremble options in a fight where racing mattered more than a difficult Fatal setup.
- T3 used Bloodletting, Shrug, Pyre, Rage, Stone Armor+, and Breakthrough+ on the buff turn. Pyre plus Plating were the important long-fight setup; Breakthrough added Dazed but pushed damage during the safe turn.
- T4 Snecko Oil was necessary because the hand had Barricade/Howl/damage but no block into 4x7. It found Toric Toughness and True Grit+; Toric + True Grit+ plus Uppercut Weak covered the attack. Body Slam and Howl dropped Entomancer to 35.
- Important finding: playing Howl from Beyond+ from hand still put it in discard, not Exhaust, despite the card showing the Exhaust keyword in combat. It must be exhausted by another effect to start the automatic replay.
- T5 used Attack Potion because Bash + Breakthrough was just short. Picked Ashen Strike over Stomp/Hemokinesis; with 6 exhausted cards and Vulnerable, it dealt lethal. Ended at 57/83 after Burning Blood.
- Rewards: picked Infernal Blade+ over Armaments/Bloodletting. Armaments wants an upgrade and Bloodletting #3 adds HP pressure; Infernal Blade+ is already 0-cost, exhausts itself, and gives burst without permanent energy burden. Took Strawberry, raising HP to 64/90, and 40 gold.

### F30 path
- Only available node is a Monster. Entering with 64/90 HP, 146 gold, Strawberry, and no potions.

### F30 - Exoskeletons
- Read KB: Hard to Kill caps each damage instance at 9, so separate hits/AoE matter more than single large attacks; the Enrage-position Exoskeleton should be pressured before Strength stacks.
- T1 played Rage -> Stomp. Stomp dealt capped AoE to all four, and Rage reduced the incoming chip; took 9 damage because the opener had no efficient block after committing to AoE.
- T2 Infernal Blade+ generated Spite. Bloodletting enabled Spite's two-hit clause; Breakthrough+ dropped all enemies near the cap, Spite killed the Strength Exoskeleton, Bash killed another attacker, and Pyre was installed on the double-buff turn.
- T3 Feed killed the 9 HP Exoskeleton through Hard to Kill and still raised max HP from 90 to 93. Shrug then blocked the remaining attacker, and Howl chipped it to 1.
- T4 Molten Fist killed. Ended at 60/93 after Burning Blood.
- Rewards: picked Twin Strike+ over Thunderclap/Drum of Battle+. Twin Strike+ gives cheap two-hit damage for capped-damage enemies; Thunderclap was redundant, and Drum of Battle+ is risky in a slow deck with key powers/payoffs. Took 17 gold, now 163.

### F31 path
- Chose Monster over Unknown before the forced RestSite. With 60/93 HP, Burning Blood, and no potions, a hallway fight is acceptable and can refill potion/card/gold value before the Act 2 boss.

### F31 - The Obscura
- Read KB: Obscura opens by summoning Parafright; focus the leader because Parafright is a Minion and leaves when the leader dies.
- T1 used the summon turn to install Juggernaut. This gave up early damage but made every block card chip the leader/minion.
- T2 installed Unmovable, then Shrug for 32 block. Infernal Blade+ generated Thunderclap, which applied AoE Vulnerable while block covered the Parafright Slam plus Obscura hit.
- T3 True Grit+ exhausted Bloodletting and made enough block; Breakthrough+ killed the Parafright and damaged Obscura, then Body Slam hit Obscura with the block buffer.
- T4 Taunt and Pommel pushed Obscura down while reapplying Vulnerable, but the turn only had 14 block into 22 incoming, so took 8.
- T5 Bloodletting funded Stone Armor+ and Molten Fist. The Wail turn made the next attacks dangerous; Plating plus Rage only partially covered Parafright.
- T6 Fiend Fire into 5-card hand left Obscura at 2 instead of lethal, but end-of-turn Plating triggered Juggernaut for 5 and killed the leader before enemy attacks resolved. Ended at 47/93 after Burning Blood.
- Rewards: picked Dismantle over Rage/Armaments. The deck has abundant Vulnerable, so Dismantle is a cheap double-hit payoff; second Rage is lower marginal value, and Armaments remains unattractive without a spare upgrade. Took 18 gold, now 181.
- Sequencing note from user: exhaust-selection cards such as Burning Pact and True Grit do not require exhausting anything if played as the last card in hand. Use this to preserve key cards when possible.

### F32 rest site
- Entered final Act 2 rest at 47/93 with no potions before The Insatiable. Boss KB says the fight averages about 29 damage in winning runs and scales after Salivate; smithing would leave too little margin for bad draws.
- Rest over Smith despite the smith-default rule. Rest heals 27 to 74/93, which is a safer boss entry than upgrading Dismantle/Fiend Fire/Blood Wall at 47 HP.

### F33 boss - The Insatiable
- Read KB: fixed cycle opens Liquify Ground, then Thrash / Lunging Bite / Salivate / Thrash / Lunging Bite; Salivate is a free offense turn, and Sandpit must be managed before it reaches the enemy turn at 1.
- T1 used Bloodletting to fund Barricade+, Shrug, Twin Strike+, Blood Wall, and last-card Burning Pact. Burning Pact as the final card drew without forcing an exhaust selection, confirming the sequencing note for exhaust-selection cards.
- T2-T4 used Frantic Escape when Sandpit was low, stacked Vulnerable with Tremble/Uppercut+/Bash, and used the Salivate turn to install Stone Armor+ plus free Infernal Blade damage.
- F37 A3 combat: 4 Scrolls of Biting. Used Colorless Potion on a no-block opener and chose Fisticuffs for immediate block. T1 line tried to convert Fisticuffs + Apotheosis + Burning Pact into lethal, but the draw did not match the visible preview; Burning Pact exhausted Barricade+ from the choices Howl/Barricade/Stomp. This was a mistake because exhausting Howl would have preserved Barricade and enabled Howl's automatic AoE next turn. The fight leaked heavily on T2-T3, dropping max HP from 95 to 89 before stabilizing with Impervious+ into Body Slam+. Feed+ killed the final Scroll, recovering +4 max HP; ended at 83/93 after Burning Blood. Lesson: against Scrolls, preserve retained-block engines unless the current-turn kill is certain, and prefer exhausting Howl over Barricade when offered.
- F37 rewards: picked Shrug It Off+ over Molten Fist+/Iron Wave because the deck's failure mode is missing block/draw on setup turns, not lacking another damage card. Claimed 14 gold, reaching 319.
- F38 shop: Bought Candelabra for 214 and Radiant Tincture for 77, leaving 28 gold. Chose deterministic energy over Oddly Smooth Stone/removal because the deck's strongest turns require fitting Apotheosis/Barricade/Unmovable/Pyre/block into the first two turns, and no single removable card was worse than losing those setup accelerants. Skipped discounted Tremble because the deck already has enough Vulnerable and is large.
- Mid-fight decision: installed Pyre over Howl on a 10x2 turn. This cost immediate damage, but the extra energy let later turns combine Frantic Escape, block, and attacks. The fight still went long, so this was only barely justified.
- Important tactical correction: missing one Frantic Escape is acceptable at Sandpit 2 if it enables Weak/lethal setup, but the next turn must either kill or play Escape. The fight reached Sandpit 1 twice and would have died to one more slow turn.
- Endgame: Unmovable plus Blood Wall created 41 block, and Body Slam dealt 61 through Vulnerable, leaving The Insatiable at 4. Dismantle killed before Sandpit mattered. Ended at 28/93 after Burning Blood.
- Rewards: took Impervious over Conflagration/Tear Asunder. Impervious fits the low-HP Act 3 entry and the Barricade/Unmovable/Body Slam block-to-damage plan. Took Clarity Extract and 100 gold, entering Act 3 at 28/93 with 281 gold.

### F34 ancient - Nonupeipe
- Act transition healed to 93/93.
- Read Nonupeipe/Apotheosis/Glam KB. Chose Jewelry Box over Glitter/Diamond Diadem. Apotheosis is Innate and upgrades the current deck every combat, which is stronger than future-only Glam rewards this late and better aligned than Diamond Diadem's two-card-turn restriction.

### F35 path
- Chose the left opening Monster at row 1. This preserves the early Shop branch and optional later elite/treasure branch after seeing one Act 3 hallway fight.

### F35 - Scrolls of Biting
- Read Scroll of Biting KB: every unblocked attack hit can trigger Paper Cuts, so full block or kill is more important than ordinary HP-trading.
- T1 Apotheosis from Jewelry Box upgraded the whole deck, then Shrug It Off+ used Vambrace to make 22 block and fully block 16 incoming.
- T2 used Clarity Extract because the hand could not cover 24 incoming. The potion drew Taunt+, not the visible Bash+ from the draw preview, so trust live hand state over draw-pile assumptions. Bloodletting funded Rage, Taunt, Tremble, Twin Strike, and Toric Toughness; block reached 20, but 4 damage leaked and triggered 2 max HP loss.
- T3 recovered by using Bloodletting -> Unmovable+ -> Blood Wall+ for 47 block, Dismantle+ to kill the wounded Scroll, and Pyre+ for future energy.
- T4 Shrug/Uppercut/Pommel found a Feed line. Feed+ killed an 8 HP Scroll and raised max HP by 4, offsetting the Paper Cuts loss; Stomp and generated Bully pushed the last Scroll low while block covered the attack.
- T5 Bash+ into Bully killed the final Scroll. Ended at 91/95 after Burning Blood.
- Rewards: picked Pommel Strike over Body Slam+/Howl from Beyond. Jewelry Box upgrades it in combat, and a second Pommel adds broadly useful attack-draw; second Body Slam is more conditional, and unupgraded second Howl is too heavy unless exhausted.

### F36 - Living Shield / Turret Operator
- Read Turret Operator KB: kill Living Shield first because Rampart gives Turret Operator 25 Block each player turn; killing Operator first makes Shield switch to heavier Smash attacks.
- T1 Apotheosis upgraded the deck, then True Grit+ fully blocked and exhausted Stomp+ as the least important remaining card for the Shield-first plan.
- T2 Bloodletting funded Impervious+ and Molten Fist+ into Living Shield. Shrug drew Barricade+ instead of the visible Bloodletting preview, so played Barricade+ over Fiend Fire; this kept 51 block retained after the enemy turn.
- T3 used Uppercut+ and two attack-draw cards to kill Living Shield before Rampart could keep snowballing the Operator.
- T4 Shrug It Off+ drew Body Slam+; 41 retained block killed Turret Operator exactly. Ended at 94/95 after Burning Blood.
- Rewards: took Molten Fist+ over Anger+/Drum of Battle. Drum remains too risky for a slow deck with key powers and survival cards, and Anger is late bloat; Molten is upgraded, cheap, exhausts, and supports Vulnerable burst. Took Colorless Potion and 11 gold, now 305.

### F39 - Frog Knight
- Read Frog Knight KB: opens Tongue Lash, then Strike Down Evil / For the Queen / conditional Beetle Charge; below half can trigger a 35-damage charge, so retained block matters before pushing under 95 HP.
- T1 played Apotheosis and Shrug It Off+ to fully block the weakened opener. T2 used Candelabra energy to play Barricade+, Unmovable+, and Impervious+, retaining 39 block after the 21 hit.
- T3 stacked Vulnerable with Tremble+ and Bash+, then used Bloodletting and two Pommel Strikes to install Pyre+ instead of overcommitting to Fiend Fire. Infernal Blade produced Fiend Fire, but playing Pyre preserved long-fight energy and avoided exhausting Feed/other useful cards.
- T4 played Juggernaut+ and Toric Toughness+, then Burning Pact+ exhausted Fiend Fire+ rather than Bloodletting/Stomp. Bloodletting funded Rage+ into Stomp+, preserving enough retained block for the next attack.
- T5 lethal line: Molten Fist+ doubled Vulnerable to 10, Blood Wall+ raised retained block to 84, and Body Slam+ killed through Vulnerable before the 26 attack. Ended at 81/93 after Burning Blood.
- Rewards: picked Battle Trance+ over Cinder/Mangle because free upgraded draw improves setup consistency; noted its No Draw warning from KB. Took 20 gold and skipped Fortifier to keep Radiant Tincture for boss/elite setup energy.

### F40 path
- Forced into the row-6 Monster, then won a Treasure route. Afterward the only next node is Treasure, then a branch to RestSite or Unknown.

### F40 - Owl Magistrate
- Read Owl Magistrate KB: fixed cycle is Magistrate Scrutiny, Peck Assault, Judicial Flight, Verdict, repeat; Verdict is the 33-damage Vulnerable hit after Soar.
- T1 hand included Apotheosis, Body Slam, Molten Fist, Burning Pact, and Howl from Beyond. Played Apotheosis, then Burning Pact and exhausted Howl instead of preserving it in hand; this preserved Body Slam and confirmed the user correction that exhausting Howl makes it autoplay next turn. Howl autoplayed on T2, dealt 21, then moved to discard.
- T2 used the Candelabra turn to install Barricade+ after Shrug/Battle Trance sequencing. Important sequencing: play draw cards before Battle Trance when possible because Battle Trance turns off later draw.
- T3 on Judicial Flight used Uppercut+ to apply Weak 2 before Verdict. Weak 2 carried into Verdict and reduced the 33 attack to 24; Weak 1 usually would have expired before helping.
- Barricade+ plus Unmovable+ let Blood Wall+/Impervious+ convert setup turns into retained block. This made the later 4x6 and buff turns safe even when Body Slam was not drawn on schedule.
- T7 Feed+ was not lethal at 29 HP, so Feed set Owl to 11 and Dismantle+ killed through Vulnerable. Ended at 63/93 after Burning Blood.
- Rewards: skipped Tremble+/Sword Boomerang+/True Grit+. The deck already has enough Vulnerable and late common additions mostly dilute access to Apotheosis, Barricade, Unmovable, draw, and payoff cards. Took 16 gold, reaching 64.

### F41-F42 treasure/rest
- F41 Treasure contained gold only, raising gold from 64 to 108.
- Chose RestSite over Unknown because it preserved the shop route while giving a controlled smith/heal decision.
- At 63/93, chose Smith over Rest. This follows the smith-default rule because the next node can be Shop and the following row is another RestSite, so HP risk is manageable.
- Upgraded Apotheosis. Jewelry Box makes Apotheosis innate every combat, so reducing its setup cost is stronger than upgrading a single payoff that Apotheosis can already upgrade after it is played.

### F43-F44 shop/rest
- F43 shop: bought discounted Vicious for 37 gold, leaving 71. Vicious KB marks it as a strong Vul-chain engine, and this deck applies Vulnerable repeatedly with Bash, Tremble, Taunt, Uppercut, and Molten Fist.
- Skipped Second Wind because it can exhaust unplayed powers in a setup-heavy deck. Kept Radiant Tincture over buying Attack/Power Potion because Radiant is more reliable for boss setup turns.
- F44 RestSite: rested from 63/93 to 90/93. This is an intentional exception to smith-default because Apotheosis+ already upgrades the deck in combat, making another smith low marginal value compared with entering the final fights healthy.

### F45 - Globe Head
- Read Globe Head KB: fixed cycle Shocking Slap / Thunder Strike / Galvanic Burst; Galvanic makes powers cost 6 HP via Galvanized.
- T1 played Apotheosis+ and Infernal Blade+, then Tremble+ into Pommel/Sword Boomerang. Took the 9-damage Frail opener because no efficient block was available.
- T2 skipped Vicious+/Pyre+ despite buying Vicious. Galvanic made each power cost 6 HP, and the hand already had a Tremble -> Pommel -> Stomp line; this was better for a hallway race.
- T3 Battle Trance+ found Bloodletting+ and block. Because Battle Trance applied No Draw, Burning Pact was not worth playing for draw; used one Bloodletting to afford Breakthrough+, Twin Strike+, Toric Toughness+, Shrug, and True Grit+.
- T4 Dismantle+ put Globe Head at 15, then Feed+ killed for +4 max HP. Ended at 85/97 after Burning Blood.
- Rewards: picked Feel No Pain over Body Slam+/Ashen Strike. KB supports taking it when the deck already has exhaust enablers; this deck has True Grit, Burning Pact, Fiend Fire, Tremble, Molten Fist, Feed, Impervious, and Howl exhaust lines. Took 11 gold and skipped Explosive Ampoule to keep Radiant Tincture.

### F46 - Knights elite
- Took the optional elite at 85/97 because the path had a RestSite afterward and the deck had Radiant Tincture preserved.
- Read Knights KB: Magi applies Dampen, Spectral applies Hex, and Flail scales with Strength. Target plan was Magi first, Spectral second, Flail last.
- T1 Apotheosis+ upgraded the deck, then Tremble+ and Pommel Strike+ hit Magi. Pommel missed Bloodletting, so the turn ended with no block and took chip.
- T2 Spectral's Hex made all cards Ethereal, and Magi's Dampen turn was coming. Used Blood Wall+ -> Body Slam+ to put Magi to 12, then installed Pyre+ and Stone Armor+; True Grit+ as the last card gave block without forcing an exhaust.
- T3 Dampen landed, but Feed killed Magi through Vulnerable for +4 max HP. Installed Feel No Pain first so the Feed exhaust added block, then used Shrug and Tremble to stabilize and put Vulnerable on Spectral.
- Hex was the main danger: it exhausted Barricade+ at end of turn because Radiant Tincture would only provide 1 immediate energy, not enough to save the 2-cost power. This was not a chosen Barricade exhaust, but a cost of leaving Spectral alive.
- T4 Unmovable+ plus Taunt+ covered the first block card, Infernal Blade made Whirlwind, and Breakthrough -> Whirlwind heavily damaged both remaining knights. Whirlwind did not exhaust after play, so Feel No Pain did not add block from it.
- T5 Shrug set block, then Fiend Fire+ targeted Spectral with four other cards in hand. It exhausted Vicious+, Toric Toughness+, Juggernaut+, and Rage+, but only dealt one visible 15-damage packet instead of the expected multi-packet hand-size burst; Spectral still died at the start of the enemy turn, ending Hex.
- T6 Battle Trance on the Flail buff turn found Uppercut, Pommel, Burning Pact, and Howl. Bloodletting funded Uppercut+ into Dismantle+ and Howl+ lethal. Ended at 61/101 after Burning Blood.
- Rewards: took Unsettling Lamp, which doubles the first enemy debuff each combat and should be deliberately spent on Uppercut/Tremble/Bash/Taunt against the boss. Took 43 gold to reach 125. Skipped Cascade/Anger/True Grit: Cascade is uncontrolled late variance, Anger is late bloat, and an unupgraded second True Grit has no remaining smith.

### F47 rest
- Read Doormaker KB: after Dramatic Open, cycle is Hunger 30, Scrutiny 24, then Grasp 10x2 plus 3 Strength, with rotating powers that punish attacks/skills, draw, and card plays.
- Rested from 61/101 to 91/101 over Smith. Apotheosis+ already upgrades the deck in combat, and the boss's known opening damage makes the extra 30 HP more valuable than a marginal permanent upgrade.

### F48 boss - Doormaker
- Read Doormaker KB: opening Door transforms, then the boss cycles Hunger / Scrutiny / Grasp. Entered at 91/101 with Radiant Tincture and no other potions.
- T1 against Door played Apotheosis+ and Barricade+. Deliberately did not play Tremble on the infinite-HP Door, preserving Unsettling Lamp for Doormaker proper. Pyre+ was left unplayed because Barricade was the more important survival engine.
- T2 Hunger: used Radiant Tincture, Pommel draw, Toric Toughness+, Unmovable+, then Bash+. Unsettling Lamp doubled Bash's 3 Vulnerable to 6. Took 16 damage because Toric only gave 14 block here, but Unmovable and Barricade were online.
- T3 Scrutiny: ignored extra draw because Scrutiny blocks it. Blood Wall+ created a large retained block buffer, then Tremble+ into Molten Fist+ raised Vulnerable to 18.
- T4 Grasp: Bloodletting was strong despite the HP loss because it netted energy through the per-card energy tax. Shrug raised block, Body Slam+ dealt 99 through Vulnerable, then Vicious+ and Taunt+ extended the draw/Vulnerable engine.
- T5 Hunger: Bloodletting funded Stone Armor+, Impervious+, Rage+, and last-card Burning Pact+. Burning Pact drew without forcing an exhaust selection, confirming the last-card exhaust-selection rule. Battle Trance drew the remaining burst; Infernal Blade made Spite; played Spite, Molten Fist+, and Howl+. Howl exhausted, autoplayed next turn for 31, then moved to discard.
- T6-T7: installed Pyre+ on Scrutiny to help the next Grasp turn. On Grasp, Body Slam+ hit for 160, Breakthrough+ dropped Doormaker to 26, and Fiend Fire+ exhausted the remaining hand for lethal. Ended at 69/101 after Burning Blood; post-boss state was The Architect event with no options.
- Key findings: preserve Unsettling Lamp for the real boss, not Door; Barricade + Unmovable + Blood Wall/Impervious creates enough retained block to trivialize the damage cycle; use draw before Scrutiny or accept no draw; Pyre/Radiant Tincture help offset Grasp; Howl in the exhaust pile autoplays once at turn start and then goes to discard.

## Post-run reflection

- Steam history check: newest save log was `1777538652.run` at 2026-04-30 14:23. It records Ironclad, 48 floors, `win: true`, `was_abandoned: false`, `killed_by_encounter: NONE.NONE`, and `killed_by_event: NONE.NONE`.
- What worked well: the deck won by combining early draw/energy with a late retained-block engine. Apotheosis+ from Jewelry Box removed most smith pressure, Bloodletting/Pyre/Radiant Tincture solved expensive setup turns, and Barricade + Unmovable turned Blood Wall/Impervious/Shrug into both defense and Body Slam damage.
- What cost avoidable value: the worst mistake was exhausting Barricade instead of Howl against Scrolls of Biting, which delayed the retained-block engine and cost max HP. A smaller boss mistake was underestimating the T2 Doormaker block total after Toric Toughness, leaking 16 HP, though the retained block plan still recovered.
- Deck-size correction: the final Steam log shows 38 cards, which is noticeably above the ~31-card winning median in `GUIDE.md`. This run got away with it because of innate Apotheosis, multiple draw cards, Bloodletting/Pyre energy, and a high-value Pandora transform, but the larger deck still made Barricade/Unmovable/Body Slam less reliable. I should have been more aggressive about skips/removals and more skeptical of late speculative additions.
- What to change next run: treat key setup powers as protected cards unless current-turn lethal is certain; when an exhaust choice includes Howl and an engine card, usually exhaust Howl. Save once-per-combat first-debuff effects for real targets, not decoys or infinite-HP opening phases.
- Important discovered mechanics: last-card exhaust-selection cards can be played without exhausting anything; exhausted Howl autoplays at the start of the next turn then moves to discard; Doormaker Scrutiny blocks extra draw; Doormaker Grasp taxes energy per card, so net-energy cards and potions matter more than usual; the post-boss state can appear as The Architect with no options, so confirm final outcome from the Steam `.run` log.
