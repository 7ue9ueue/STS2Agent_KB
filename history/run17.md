# Run 17 - Ironclad A10

Date: 2026-05-01
Character: Ironclad
Ascension: 10
Outcome: Loss, Floor 24, killed by Bowlbugs

## Pre-run Reads

- Read `AGENTS.md`.
- Read `kb/strategies/_index.md`, `kb/strategies/ironclad.md`, `kb/strategies/pathing.md`, `kb/strategies/archetypes.md`, and `kb/strategies/card_impressions.md`.
- Main setup reminders: Act 1 needs real Attack/frontload first; trace the whole visible path and prioritize rest sites; question marks are preferred over hallway fights once deck quality is stable; preserve potions for elites/bosses when possible.

## Floor 1 - Neow

- Strategy files read: `kb/strategies/ironclad.md`, `kb/strategies/pathing.md`, `kb/strategies/archetypes.md`, `kb/strategies/card_impressions.md`, `kb/strategies/bosses.md`.
- Entity KB read: `kb/relics/lost_coffer.md`, `kb/relics/winged_boots.md`, `kb/relics/hefty_tablet.md`, `kb/relics/burning_blood.md`.
- Current HP/status: 64/80, 99 gold, Burning Blood.
- Options: Lost Coffer, Winged Boots, Hefty Tablet.
- Decision: take Winged Boots.
- Reason: Winged Boots directly supports the updated pathing priority: inspect the whole act, maximize rest-site access, avoid forced bad branches, and choose question marks or safer nodes over dangerous hallway/elite pressure. Lost Coffer offers immediate card/potion value, but Boots has higher strategic control for the full run.

## Floor 1 - Act 1 Map Choice

- Strategy files read: `kb/strategies/pathing.md`, `kb/strategies/bosses.md`.
- Entity KB read: `kb/enemies/bosses/the_kin.md`.
- Current HP/status: 64/80, Winged Boots [3], no potions.
- Decision: choose node [2], Monster at (4,1).
- Reason: The Kin rewards early follower-killing damage, so the deck needs early combats for Attack rewards. This route has early fights while preserving access to the larger right/middle route tree with several rest sites and question marks; Winged Boots can later correct into safer rest-heavy branches if the natural route becomes bad.

## Floor 2 - Nibbit

- Strategy files read: `kb/strategies/ironclad.md`, `kb/strategies/card_impressions.md`.
- Entity KB read: `kb/enemies/overgrowth/nibbit.md`.
- Current HP/status: entered 64/80, no potions.
- Decision: play three Strikes on turn 1, then Bash + Strike on turn 2, then kill during the Strength buff turn.
- Reason: Nibbit opens with 13, then 7 plus Block, then Strength. Early Ironclad needs frontload; taking the first hit keeps the fight short and avoids scaling. Ended at 50/80 after Burning Blood.

## Floor 2 - Card Reward

- Strategy files read: `kb/strategies/card_impressions.md`, `kb/strategies/archetypes.md`, `kb/strategies/ironclad.md`.
- Entity KB read: `kb/cards/ironclad/setup_strike.md`, `kb/cards/ironclad/tremble.md`, `kb/cards/ironclad/second_wind.md`.
- Current HP/status: 50/80, 110 gold, no potions.
- Options: Setup Strike, Tremble, Second Wind.
- Decision: take Tremble.
- Reason: Tremble is a recorded strong Act 1 transition card because Vulnerable improves starter Strike/Bash damage per energy and remains useful for The Kin follower kills. Setup Strike is an actual Attack but is flagged as a low-confidence survival pick without synergy; Second Wind is powerful later but too likely to exhaust too much defense before the deck has enough replacement block.

## Floor 2 - Map Choice

- Strategy files read: `kb/strategies/pathing.md`.
- Entity KB read: `kb/enemies/bosses/the_kin.md`.
- Current HP/status: 50/80, 110 gold, Winged Boots [3], no potions.
- Decision: choose node [2], Monster at (4,2).
- Reason: Act 1 still needs more frontload before elites or The Kin. The shop options are early for 110 gold and a near-starter deck; the (4,2) monster keeps the route connected to the right/middle rest-heavy branch.

## Floor 3 - Shrinker Beetle

- Strategy files read: `kb/strategies/ironclad.md`, `kb/strategies/card_impressions.md`.
- Entity KB read: `kb/enemies/overgrowth/shrinker_beetle.md`.
- Current HP/status: entered 50/80, no potions.
- Decision: Tremble + two Strikes on the debuff opener, then Bash + Strike, then kill with Strikes before Stomp landed.
- Reason: Shrinker Beetle opens with Shrink, then alternates 8 and 14 damage attacks. Tremble before Shrink let starter Strikes deal enough damage to race; accepted the 8-damage Chomp and ended at 48/80 after Burning Blood.

## Floor 3 - Card Reward

- Strategy files read: `kb/strategies/card_impressions.md`, `kb/strategies/ironclad.md`.
- Entity KB read: `kb/cards/ironclad/havoc.md`, `kb/cards/ironclad/sword_boomerang.md`, `kb/cards/ironclad/blood_wall.md`.
- Current HP/status: 48/80, 119 gold, no potions.
- Options: Havoc, Sword Boomerang, Blood Wall.
- Decision: take Sword Boomerang.
- Reason: Act 1 still needs actual Attack cards with good damage per energy. Sword Boomerang is 9 damage for 1 energy and improves with Strength/Vulnerable; Blood Wall is good block but does not solve current frontload, and Havoc has low confidence because random play/exhaust can damage consistency.

## Floor 3 - Map Choice

- Strategy files read: `kb/strategies/pathing.md`.
- Entity KB read: `kb/enemies/bosses/the_kin.md`.
- Current HP/status: 48/80, 119 gold, no potions, deck added Tremble and Sword Boomerang.
- Decision: choose node [2], Monster at (5,3).
- Reason: This is still within the weak early hallway window, the deck needs more Act 1 card rewards, and the branch keeps access to multiple rest sites and question-mark alternatives later.

## Floor 4 - Slimes

- Strategy files read: `kb/strategies/ironclad.md`, `kb/strategies/card_impressions.md`, `history/run17_strategy.md` created after combat per updated `AGENTS.md`.
- Entity KB read: `kb/enemies/overgrowth/slimes.md`.
- Current HP/status: entered 48/80, no potions.
- Decision: Sword Boomerang first killed the small attacking Twig Slime; Tremble + Strike focused the medium Twig Slime, then used Strike + two Defends on the 16 incoming turn, then killed medium Twig and Leaf Slime with attacks.
- Reason: Slimes add Slimed and then attack; reducing enemy count early prevented repeated multi-enemy damage. Tremble on the medium Twig Slime let starter attacks finish it before the fight dragged too long. Ended at 48/80 after Burning Blood.

## Floor 4 - AGENTS Re-read / Live Strategy

- Strategy file read: `AGENTS.md`.
- Entity KB read: none; this was a harness/process update.
- Current HP/status: 48/80, 119 gold, rewards pending: 9 gold, Swift Potion, card reward.
- Decision: created `history/run17_strategy.md`.
- Reason: Updated `AGENTS.md` requires a live per-run strategy file that is overwritten as the plan evolves and read at every decision to preserve the run plan through context compaction.

## Floor 4 - Rewards

- Strategy files read: `history/run17_strategy.md`, `kb/strategies/card_impressions.md`, `kb/strategies/ironclad.md`.
- Entity KB read: `kb/cards/ironclad/headbutt.md`, `kb/cards/ironclad/tremble.md`, `kb/cards/ironclad/thunderclap.md`.
- Current HP/status: 48/80, 128 gold after gold reward, Swift Potion in slot 0.
- Options: Headbutt, Tremble, Thunderclap.
- Decision: take Headbutt.
- Reason: Headbutt is efficient Act 1 attack damage and gives draw-control utility by recurring Tremble, Sword Boomerang, Bash, or future premium cards. A second Tremble would overstack setup without adding damage, and unupgraded Thunderclap is weak as a generic standalone attack.

## Floor 4 - Map Choice

- Strategy files read: `history/run17_strategy.md`, `kb/strategies/pathing.md`.
- Entity KB read: `kb/enemies/bosses/the_kin.md`.
- Current HP/status: 48/80, 128 gold, Swift Potion, Winged Boots [3].
- Decision: choose node [4], Unknown at (6,4).
- Reason: After three early combats and Headbutt/Sword Boomerang/Tremble added, the deck is no longer desperate for every hallway reward. The unknown branch preserves near rest access at (4,7), avoids another forced hallway chain, and still keeps right-side rest/treasure paths open.
- Note: this move consumed a Winged Boots charge, leaving Winged Boots [2]. Future map choices must account for charge cost when choosing non-connected nodes.

## Floor 5 - Self-Help Book

- Strategy files read: `history/run17_strategy.md`.
- Entity KB read: `kb/events/self_help_book.md`, `kb/cards/ironclad/sword_boomerang.md`, `kb/cards/ironclad/headbutt.md`.
- Current HP/status: 48/80, 128 gold, Swift Potion, Winged Boots [2].
- Decision: choose Read the Back to enchant an Attack with Sharp 2.
- Reason: Self-Help Book KB says Sharp 2 is highest leverage on repeat-hit Attacks; Sword Boomerang is a repeat-hit Attack and should gain more total damage than a single-hit Headbutt if selectable.
- Selection: enchanted Sword Boomerang with Sharp 2.

## Floor 5 - Map Choice

- Strategy files read: `history/run17_strategy.md`, `kb/strategies/pathing.md`.
- Entity KB read: `kb/enemies/bosses/the_kin.md`.
- Current HP/status: 48/80, 128 gold, Swift Potion, Winged Boots [2], Sharp 2 Sword Boomerang.
- Decision: choose node [4], Unknown at (6,5).
- Reason: The deck now has enough Act 1 damage to stop forcing every hallway fight. This unknown preserves the right-side rest at (4,7) after one forced monster and supports the plan to avoid the optional elite unless HP/deck improve substantially.

## Floor 6 - Whispering Hollow

- Strategy files read: `history/run17_strategy.md`.
- Entity KB read: `kb/events/whispering_hollow.md`.
- Current HP/status: 48/80, 128 gold, Swift Potion, Winged Boots [2].
- Options: lose 27 gold for 2 random potions, or lose 9 HP to transform a card.
- Decision: Hug the Tree, then transform a Defend.
- Reason: We already have Swift Potion and appear potion-slot constrained, so two random potions risk wasting or forcing a discard. Transforming a Defend improves deck quality, and the route is aiming toward a rest site soon enough to absorb the 9 HP loss.
- Result: HP dropped to 39/80. The map state did not reveal the transformed card; identify it from the next combat/deck view.

## Floor 6 - Map Choice

- Strategy files read: `history/run17_strategy.md`, `kb/strategies/pathing.md`.
- Entity KB read: `kb/enemies/bosses/the_kin.md`.
- Current HP/status: 39/80, 128 gold, Swift Potion, Winged Boots [2].
- Decision: choose node [3], Monster at (5,6).
- Reason: This is the connected route to RestSite (4,7). With 39 HP after the transform, the elite at (6,7) is not the plan unless the forced combat gives a major upgrade.

## Floor 7 - Mawler

- Strategy files read: `history/run17_strategy.md`.
- Entity KB read: `kb/enemies/overgrowth/mawler.md`, `kb/cards/ironclad/spite.md`.
- Current HP/status: entered 39/80, Swift Potion, rest site next.
- Decision: Bash + Headbutt + Spite on turn 1, putting Spite back on top; Strikes + Spite + Defend on turn 2; lethal on turn 3 with Sharp Sword Boomerang and Strikes.
- Reason: Mawler can Roar into dangerous follow-up attacks. Because a rest site was next, taking the first 10 and then 11 after one Defend was acceptable to shorten the fight and preserve Swift Potion. Ended at 24/80 after Burning Blood.

## Floor 7 - Potion Reward

- Strategy files read: `history/run17_strategy.md`, `kb/potions/_index.md`.
- Entity KB read: `kb/potions/skill_potion.md`; no individual Swift Potion file exists, only `kb/potions/_index.md` mentions Swift Potion.
- Current HP/status: 24/80, 128 gold, Swift Potion.
- Decision: replace Swift Potion with Skill Potion if only one potion slot is available.
- Reason: The deck now has Sharp Sword Boomerang for damage but still lacks reliable block. Skill Potion can produce a free defensive or utility Skill for elite/boss danger turns, while Swift Potion only draws from a still-basic deck.

## Floor 7 - Card Reward

- Strategy files read: `history/run17_strategy.md`, `kb/strategies/card_impressions.md`, `kb/strategies/ironclad.md`.
- Entity KB read: `kb/cards/ironclad/thunderclap.md`, `kb/cards/ironclad/drum_of_battle.md`, `kb/cards/ironclad/shrug_it_off.md`.
- Current HP/status: 24/80, 138 gold, Skill Potion.
- Options: Thunderclap, Drum of Battle, Shrug It Off.
- Decision: take Shrug It Off.
- Reason: The deck has enough attack frontload after Sharp Sword Boomerang and needs block/draw. Shrug It Off is a strong cantrip block that preserves draw quality; Drum of Battle has a documented run-ending risk by exhausting the top draw-pile card each turn; Thunderclap is weak unupgraded without Vicious.

## Floor 7 - Map Choice

- Strategy files read: `history/run17_strategy.md`, `kb/strategies/pathing.md`.
- Entity KB read: `kb/enemies/bosses/the_kin.md`.
- Current HP/status: 24/80, 138 gold, Skill Potion, Winged Boots [2].
- Decision: choose node [3], RestSite at (4,7).
- Reason: Low HP after Mawler makes the rest site mandatory. Optional elites are not justified despite improved frontload because the deck still lacks deep block/scaling and needs to preserve Skill Potion for The Kin or an unavoidable danger turn.

## Floor 8 - Rest Site

- Strategy files read: `history/run17_strategy.md`, `kb/strategies/pathing.md`.
- Entity KB read: none.
- Current HP/status: 24/80, 138 gold, Skill Potion.
- Options: Rest for 24 HP, or Smith.
- Decision: Rest.
- Reason: The run is too low to Smith safely before the second half of Act 1 and The Kin. The deck already has Sharp Sword Boomerang for damage; survival and potion preservation are more important than an upgrade here.
- Result: HP 48/80.

## Floor 8 - Map Choice

- Strategy files read: `history/run17_strategy.md`, `kb/strategies/pathing.md`.
- Entity KB read: `kb/enemies/bosses/the_kin.md`.
- Current HP/status: 48/80, 138 gold, Skill Potion, Winged Boots [2].
- Decision: choose node [2], Unknown at (3,8).
- Reason: This is the connected safe branch after the rest site. It avoids the right-side forced elite chain, keeps treasure access, and follows the Act 1 plan to prefer question marks once the deck has enough early damage.

## Floor 9 - Twig Slime M + Flyconid

- Strategy files read: `history/run17_strategy.md`.
- Entity KB read: `kb/enemies/overgrowth/flyconid.md`, `kb/enemies/overgrowth/slimes.md`, `kb/cards/ironclad/spite.md`.
- Current HP/status: entered 48/80, Skill Potion.
- Decision: focused Flyconid first with Shrug/Strikes/Spite, then Bash + Headbutt while accepting the 12-damage turn, putting Spite on top. Used Spite and Sharp Sword Boomerang to finish Flyconid, then Tremble + two Strikes killed Twig Slime.
- Reason: Flyconid's Vulnerable/Frail/debuff cycle is more dangerous than a medium slime once the fight drags. Preserved Skill Potion because the fight was not lethal and the potion remains better saved for elite/boss danger turns.
- Lesson: Spite only doubles if HP was lost during the current player turn, not because HP was lost on the previous enemy turn; the existing Spite KB note matched this and should guide future sequencing.
- Result: ended at 38/80 after Burning Blood, Skill Potion preserved.

## Floor 9 - Card Reward

- Strategy files read: `history/run17_strategy.md`, `kb/strategies/card_impressions.md`.
- Entity KB read: `kb/cards/ironclad/stomp.md`, `kb/cards/ironclad/molten_fist.md`, `kb/cards/ironclad/dominate.md`.
- Current HP/status: 38/80, 145 gold, Skill Potion.
- Options: Stomp, Molten Fist, Dominate.
- Decision: take Dominate.
- Reason: The deck already has Tremble/Bash for Vulnerable and Sharp Sword Boomerang as a multi-hit Strength payoff. Dominate gives a boss-scaling line by converting stacked Vulnerable into Strength, while Molten Fist is narrower single-target frontload and Stomp's AoE is attractive but less important than adding scaling for The Kin and later bosses.

## Floor 9 - Map Choice

- Strategy files read: `history/run17_strategy.md`, `kb/strategies/pathing.md`.
- Entity KB read: `kb/enemies/bosses/the_kin.md` earlier this act.
- Current HP/status: 38/80, 145 gold, Skill Potion, Winged Boots [2].
- Options: left Treasure into possible forced elite line, middle Treasure with immediate RestSite option, right Treasure into forced Elite.
- Decision: choose node [1], Treasure at (2,9).
- Reason: The middle branch traces to an immediate rest site and preserves later shop/rest alternatives. The right branch forces an elite at too-low HP, and the left branch has worse forced elite risk despite later rest access.

## Floor 10 - Treasure

- Strategy files read: `history/run17_strategy.md`.
- Entity KB read/created: `kb/relics/nunchaku.md` did not exist; created from in-game text before claiming.
- Current HP/status: 38/80, 176 gold, Skill Potion.
- Relic: Nunchaku.
- Decision: claim Nunchaku.
- Reason: Treasure relic is mandatory value. Nunchaku fits the attack-dense current deck and can produce extra energy on turns with Sword Boomerang, Headbutt, Bash, or future draw chains, but its counter must be tracked so the energy is not wasted.

## Floor 10 - Map Choice

- Strategy files read: `history/run17_strategy.md`, `kb/strategies/pathing.md`.
- Entity KB read: `kb/enemies/bosses/the_kin.md` earlier this act.
- Current HP/status: 38/80, 176 gold, Skill Potion, Winged Boots [2], Nunchaku.
- Options: Unknown/Monster into left elite pressure, RestSite into unknown then elite path, or immediate Elite.
- Decision: choose node [2], RestSite at (3,10).
- Reason: Immediate rest-site access is the priority at 38/80. This branch also preserves a later rest before The Kin, while the alternatives expose the run to elites without first stabilizing HP or upgrading key cards.

## Floor 11 - Rest Site

- Strategy files read: `history/run17_strategy.md`, `kb/strategies/pathing.md`.
- Entity KB read: none.
- Current HP/status: 38/80, 176 gold, Skill Potion, forced elite likely after one unknown.
- Options: Rest for 24 HP, or Smith.
- Decision: Rest.
- Reason: The next branch can force an elite before the following rest site. Smithing Dominate, Sword Boomerang, Bash, or Shrug would be valuable, but entering the unknown/elite sequence at 38 HP risks losing the run or the Skill Potion before The Kin. Resting to 62 gives enough buffer to take the forced elite path.

## Floor 11 - Map Choice

- Strategy files read: `history/run17_strategy.md`, `kb/strategies/pathing.md`.
- Entity KB read: `kb/enemies/bosses/the_kin.md` earlier this act.
- Current HP/status: 62/80, 176 gold, Skill Potion, Winged Boots [2], Nunchaku.
- Options: immediate Elite, Unknown into forced Elite, or RestSite at (6,11) into later combats/elite/rest.
- Decision: choose node [2], RestSite at (6,11).
- Reason: The rest-site route gives an immediate Smith/Rest decision and delays the elite until after more rooms, while still preserving a final rest before The Kin. This follows the full-path rest-site priority better than the unknown branch, which forces an elite next floor.

## Floor 12 - Rest Site

- Strategy files read: `history/run17_strategy.md`, `kb/strategies/pathing.md`.
- Entity KB read: `kb/cards/ironclad/sword_boomerang.md`, `kb/cards/ironclad/dominate.md`, `kb/cards/ironclad/bash.md`, `kb/cards/ironclad/shrug_it_off.md`.
- Current HP/status: 62/80, 176 gold, Skill Potion, Winged Boots [1], Nunchaku.
- Options: Rest for 24 HP, or Smith.
- Decision: Smith Sword Boomerang.
- Reason: At 62 HP with a later rest before boss, Smith is correct. Sword Boomerang's upgrade adds a fourth hit; because the card already has Sharp 2 and the deck now has Dominate Strength scaling, this is both immediate frontload and a better boss/elite payoff than the smaller Dominate or Bash upgrade.

## Floor 12 - Map Choice

- Strategy files read: `history/run17_strategy.md`, `kb/strategies/pathing.md`.
- Entity KB read: `kb/enemies/bosses/the_kin.md` earlier this act.
- Current HP/status: 62/80, 176 gold, Skill Potion, Winged Boots [1], Nunchaku.
- Options: Unknown, RestSite, immediate Elite, or hallway fights into later elite.
- Decision: choose node [1], RestSite at (1,12), spending the last Winged Boots charge if required.
- Reason: Another rest site gives a second Smith/Rest decision and opens a potential shop route with 176 gold. This has better full-path value than immediate elite pressure or hallway fights, and it still leaves final rest access before The Kin.

## Floor 13 - Rest Site

- Strategy files read: `history/run17_strategy.md`, `kb/strategies/pathing.md`.
- Entity KB read: `kb/cards/ironclad/dominate.md` and prior upgrade reads.
- Current HP/status: 62/80, 176 gold, Skill Potion, Winged Boots [0], Nunchaku.
- Options: Rest for 24 HP, or Smith.
- Decision: Smith Dominate.
- Reason: HP is stable enough to upgrade. Dominate+ increases the Vulnerable applied before calculating Strength gain, improving the Tremble/Bash into Dominate scaling line for elites, The Kin, and later bosses. With Sword Boomerang+ already upgraded, Strength conversion is now much better.

## Floor 13 - Map Choice

- Strategy files read: `history/run17_strategy.md`, `kb/strategies/pathing.md`.
- Entity KB read: `kb/enemies/bosses/the_kin.md` earlier this act.
- Current HP/status: 62/80, 176 gold, Skill Potion, Winged Boots [0], Nunchaku.
- Options: Unknown, Elite, or Shop, all preserving final rest access.
- Decision: choose node [2], Shop at (2,13).
- Reason: With 176 gold, shop can buy removal, block/draw, or a boss potion. It avoids optional elite risk and still routes to Monster -> RestSite -> The Kin.

## Floor 14 - Shop

- Strategy files read: `history/run17_strategy.md`, `kb/strategies/card_impressions.md`.
- Entity KB read: `kb/cards/ironclad/offering.md`, `kb/cards/ironclad/dismantle.md`, `kb/cards/ironclad/blood_wall.md`, `kb/cards/ironclad/inflame.md`, `kb/potions/_index.md`.
- Current HP/status: 62/80, 176 gold, Skill Potion.
- Notable inventory: Offering 153g, Dismantle 71g, sale Headbutt 25g, Blood Wall 52g, Inflame 75g, potions 49-52g, remove 100g.
- Decision: buy Offering.
- Reason: Offering is premium burst draw/energy and lets this deck convert Dominate+, Sword Boomerang+, Bash, Headbutt, and Nunchaku turns. Removal and the cheaper cards were useful, but none raised the elite/boss ceiling as much as Offering. Remaining 23 gold cannot buy anything.

## Floor 14 - Map Choice

- Strategy files read: `history/run17_strategy.md`, `kb/strategies/pathing.md`.
- Entity KB read: `kb/enemies/bosses/the_kin.md` earlier this act.
- Current HP/status: 62/80, 23 gold, Skill Potion, Nunchaku.
- Decision: choose only available node [0], Monster at (1,14).
- Reason: Forced path to final RestSite then The Kin.

## Floor 15 - Double Nibbit

- Strategy files read: `history/run17_strategy.md`.
- Entity KB read: `kb/enemies/overgrowth/nibbit.md`.
- Current HP/status: entered 62/80, Skill Potion, Nunchaku [0].
- Decision: used Offering immediately, then Dominate+ on the back Nibbit that was opening with Hiss. Sword Boomerang+ plus Headbutt/Strike killed the back Nibbit before its buff turn resolved; Tremble + Sword Boomerang+ killed the front Nibbit on turn 2.
- Reason: Nibbit KB says paired Nibbits start on different cycle points, with the back one opening Hiss and the front one opening Slice. Killing the buffing back Nibbit first prevents Strength scaling from snowballing. Offering was acceptable because a rest site is next and it converted directly into a fast kill.
- Result: ended at 55/80 after Burning Blood, Skill Potion preserved, Nunchaku at 5.

## Floor 15 - Card Reward

- Strategy files read: `history/run17_strategy.md`, `kb/strategies/card_impressions.md`.
- Entity KB read: `kb/cards/ironclad/stone_armor.md`, `kb/cards/ironclad/armaments.md`, `kb/cards/ironclad/fiend_fire.md`.
- Current HP/status: 55/80, 35 gold, Skill Potion, final rest before boss.
- Options: Stone Armor, Armaments, Fiend Fire.
- Decision: take Fiend Fire.
- Reason: The deck is already strong enough to skip filler, but Fiend Fire is a real finisher with Offering, Nunchaku, and large hands. It can delete a Kin follower or finish the boss; use it only to end or simplify fights, not before needed block/setup cards.

## Floor 15 - Map Choice

- Strategy files read: `history/run17_strategy.md`, `kb/strategies/pathing.md`.
- Entity KB read: `kb/enemies/bosses/the_kin.md` earlier this act.
- Current HP/status: 55/80, 35 gold, Skill Potion, Nunchaku [5].
- Decision: choose only available node [0], RestSite at (0,15).
- Reason: Final rest before The Kin.

## Floor 16 - Rest Site

- Strategy files read: `history/run17_strategy.md`, `kb/strategies/pathing.md`, `kb/strategies/card_impressions.md`.
- Entity KB read: `kb/enemies/bosses/the_kin.md`, `kb/cards/ironclad/fiend_fire.md`.
- Current HP/status: 55/80, 35 gold, Skill Potion, Nunchaku [5].
- Options: Rest to 79 HP, or Smith.
- Decision: Smith Fiend Fire.
- Reason: The Kin KB emphasizes killing Kin Followers quickly before Frail/Weak plus Strength scaling snowball. At 55 HP with Skill Potion, the run has enough buffer; Fiend Fire+ adds 3 damage per exhausted card and can remove a follower or finish the boss, likely preventing more damage than a Rest would recover.

## Floor 16 - Boss Map Choice

- Strategy files read: `history/run17_strategy.md`.
- Entity KB read: `kb/enemies/bosses/the_kin.md`.
- Current HP/status: 55/80, 35 gold, Skill Potion, Nunchaku [5].
- Decision: choose boss node, The Kin.
- Reason: Only available node. Fight plan is follower-first, use Skill Potion early if it prevents follower delay or covers dangerous Frail/Weak turns, and reserve Fiend Fire+ for deleting a follower or finishing/simplifying the fight after setup.

## Floor 17 - The Kin

- Strategy files read: `history/run17_strategy.md`, `kb/strategies/card_impressions.md`, `AGENTS.md` after combat.
- Entity KB read: `kb/enemies/bosses/the_kin.md`; live potion options from Skill Potion were Forgotten Ritual, Burning Pact, and Dominate.
- Current HP/status: entered 55/80, Skill Potion, Nunchaku [5].
- First attempt: chose Burning Pact from Skill Potion and used Fiend Fire+ to delete the first follower, but the line exhausted too many Defends and reached Priest at 3 HP with no block against 18 incoming. Reloaded the room with save-and-quit + continue.
- Replay decision: chose Forgotten Ritual instead, played Dominate+ first so Forgotten Ritual became free burst energy, and used the extra energy for Shrug/Bash/Strike/Defend without exhausting basic Defends. Used Offering on turn 2, then killed the first follower with Spite/Strike/Sword Boomerang; used Fiend Fire+ later only when it killed the second follower while exhausting mostly attacks rather than the remaining block package.
- Reason: The Kin KB rewards deleting followers early, but the failed line showed that follower deletion is not enough if Fiend Fire/Burning Pact remove the deck's remaining defense before the solo Priest phase. Forgotten Ritual was the better Skill Potion pick here because Dominate+ already exhausts and turns it into a large energy gain without sacrificing block.
- Result: won at 15/80 after Burning Blood, spent Skill Potion, no potions remaining, rewards pending.
- Reusable lesson: in boss/elite fights, use save/load when a line exposes a strategic error; replay with a materially different plan and preserve enough block cards unless the exhaust line immediately ends or decisively simplifies the fight.

## Floor 17 - Boss Rewards

- Strategy files read: `kb/strategies/card_impressions.md`, `kb/strategies/archetypes.md`.
- Entity KB read: `kb/cards/ironclad/aggression.md`, `kb/cards/ironclad/offering.md`, `kb/cards/ironclad/not_yet.md`.
- Current HP/status: 15/80, 110 gold after rewards, Energy Potion, Nunchaku [5].
- Rewards: 75 gold, Energy Potion, rare card choice: Aggression, Offering, Not Yet.
- Decision: claim gold and Energy Potion; take Aggression.
- Reason: The deck already has one Offering and is at low HP, so a second HP-cost burst card is riskier than a persistent engine. Not Yet would patch HP but does not solve Act 2 scaling or draw quality. Aggression can recur and upgrade attacks each turn, giving a long-fight engine with Sword Boomerang, Headbutt/Bash lines, and future attacks.

## Act 2 Start - Map Choice

- Strategy files read: `history/run17_strategy.md`, `kb/strategies/bosses.md`, `kb/strategies/pathing.md`, `kb/strategies/ironclad.md`.
- Entity KB read: `kb/enemies/bosses/the_insatiable.md`.
- Current HP/status: 15/80, 110 gold, Energy Potion, no Winged Boots charges.
- Visible boss: The Insatiable.
- Decision: choose only available node [0], Ancient at (3,0).
- Reason: The Insatiable KB says Sandpit distance and cheap Frantic Escapes matter more than raw attack damage; Act 2 drafting should prioritize block/draw/energy and controlled exhaust so the deck can play Escape cards without falling behind. Pathing has no first-node choice, but future branches should favor rest sites, question marks, shops, and avoiding optional Act 2 elites at this low HP.

## Floor 18 - Tezcatara

- Strategy files read: `history/run17_strategy.md`, `kb/strategies/ironclad.md`, `kb/strategies/pathing.md`.
- Entity KB read: `kb/events/tezcatara.md`, `kb/relics/nutritious_soup.md`, `kb/relics/storybook.md`, `kb/relics/toy_box.md`, `kb/cards/colorless/brightest_flame.md`, `kb/cards/enchants/tezcataras_ember.md`.
- Current HP/status: act transition healed to 67/80, 110 gold, Energy Potion.
- Options: Nutritious Soup, Storybook, Toy Box.
- Decision: take Storybook.
- Reason: Brightest Flame gives 0-cost energy plus draw, which supports Aggression setup, Offering/Fiend Fire conversion turns, emergency block turns, and The Insatiable's Frantic Escape pressure. The 1 max-HP loss is acceptable when it prevents real HP loss. Nutritious Soup would make Strikes 0-cost but Eternal, conflicting with Act 2/3 Strike removal defaults; Toy Box is temporary high-variance relic value when the deck needs a reliable plan.

## Floor 18 - Map Choice

- Strategy files read: `history/run17_strategy.md`, `kb/strategies/pathing.md`, `kb/strategies/ironclad.md`.
- Entity KB read: `kb/enemies/bosses/the_insatiable.md`.
- Current HP/status: 67/80, 110 gold, Energy Potion, Storybook.
- Decision: choose node [1], Monster at (3,1).
- Reason: All first nodes are monsters, but the middle route keeps the most branch flexibility after the first fight: immediate unknown/monster choice, access to the central rest-site clusters, and no commitment to the right-side linear shop path with a later first rest. Act 2 still needs safer block/draw/engine rewards before optional elites.

## Floor 19 - Thieving Hopper

- Strategy files read: `history/run17_strategy.md`, `kb/strategies/card_impressions.md`, `GUIDE.md`.
- Entity KB read: `kb/enemies/hive/thieving_hopper.md`, `kb/cards/ironclad/hemokinesis.md`, `kb/cards/ironclad/second_wind.md`, `kb/cards/ironclad/whirlwind.md`.
- Current HP/status: entered 67/79 after Storybook max-HP loss, Energy Potion.
- Decision: used Brightest Flame on turn 1 for burst energy/draw, played five Strikes and Defend, then Bash + Sword Boomerang+ on Flutter setup. Hopper stole Spite, so turn 3 prioritized lethal and recovery: Dominate+ for Strength, Headbutt to place Brightest Flame on top, Shrug It Off to draw it, then Brightest Flame drew Offering/Fiend Fire+ and Fiend Fire+ killed the Hopper.
- Reason: Hopper KB says stolen cards are recovered only if the enemy dies, and Flutter halves Attack damage. The Headbutt plus Brightest Flame line converted a low-energy turn into Fiend Fire+ lethal without spending Energy Potion, recovering Spite before Escape. This cost 1 max HP from Brightest Flame but avoided the 23-damage attack and preserved the potion.
- Result: won at 59/78 after Burning Blood, recovered Spite, preserved Energy Potion, gained 10 gold, skipped duplicate Energy Potion, and took Whirlwind over Hemokinesis+ / Second Wind.
- Reward reason: Whirlwind fills an Act 2 AoE hole and scales with Brightest Flame, Offering, Nunchaku, Vulnerable, and future Strength. Hemokinesis+ adds more HP pressure to a deck already using Offering/Brightest Flame, and Second Wind is risky here because the run has already shown that exhausting too many Defends can lose elite/boss phases.
- Campfire reminder from `GUIDE.md`: Smith is the default; Rest requires explicit HP/path/boss math, not merely missing HP.

## Floor 19 - Map Choice

- Strategy files read: `history/run17_strategy.md`, `kb/strategies/pathing.md`.
- Entity KB read: `kb/enemies/bosses/the_insatiable.md` earlier this act.
- Current HP/status: 59/78, 120 gold, Energy Potion, Venerable Tea Set??? not yet acquired.
- Decision: choose node [0], Unknown at (2,2).
- Reason: Both branches keep broad rest-site access, but the Unknown avoids another immediate Act 2 hallway fight when the deck is no longer desperate for card rewards. This follows the updated pathing rule to prefer question marks over monsters once standard fights are manageable.

## Floor 20 - The Merchant???

- Strategy files read: `history/run17_strategy.md`, `kb/strategies/pathing.md`.
- Entity KB read: `kb/events/the_merchant.md`, `kb/relics/venerable_tea_set.md`, `kb/relics/anchor.md`, `kb/relics/snecko_eye.md`, `kb/relics/happy_flower.md`, `kb/relics/mango.md`, `kb/relics/lee_s_waffle.md`.
- Current HP/status: 59/78, 120 gold, Energy Potion.
- Options: Snecko Eye??? 46g, Venerable Tea Set??? 45g, Happy Flower??? 44g, Mango??? 46g, Lee's Waffle??? 51g, Anchor??? 46g.
- Decision: buy Venerable Tea Set??? and Anchor???; skip the rest.
- Reason: Venerable Tea Set??? triggers on entering rest sites even when Smithing, supporting the Smith > Rest default while giving extra opening energy for Aggression, Whirlwind, Fiend Fire, or boss setup turns. Anchor??? gives repeated start-of-combat block, buying time to play powers/draw without spending the Energy Potion. Snecko Eye??? risks randomizing the deck's many 0-1 cost cards; Mango??? and Lee's Waffle??? are modest one-time sustain; Happy Flower??? is slower and less reliable than immediate opening block.

## Floor 21 - Tunneler

- Strategy files read: `history/run17_strategy.md`.
- Entity KB read: `kb/enemies/hive/tunneler.md`, `kb/cards/ironclad/vicious.md`, `kb/cards/ironclad/molten_fist.md`, `kb/cards/ironclad/havoc.md`.
- Current HP/status: entered 59/78, Energy Potion, Anchor??? start block.
- Decision: turn 1 used Tremble + Strike + Defend, taking 6. Turn 2 used Brightest Flame and Offering on the no-attack Burrow setup turn, then Dominate+, Spite, Bash, Strikes, and Headbutt killed before Burrow resolved.
- Reason: Tunneler KB says breaking or avoiding the 37 Block Burrow cycle prevents the 26-damage Attack from Below. Spending Brightest Flame max HP and Offering HP on the no-attack setup turn converted Vulnerable into lethal and preserved Energy Potion.
- Result: won at 53/77 after Burning Blood, claimed 13 gold, took Vicious.
- Reward reason: Vicious is a real engine card for the current Vulnerable package: Tremble, Bash, Dominate+, and future Vulnerable cards become draw, improving boss scaling and consistency. Molten Fist is narrower damage/Vulnerable doubling, and Havoc is too random with Offering/Fiend Fire in the deck.

## Floor 21 - Map Choice

- Strategy files read: `history/run17_strategy.md`, `kb/strategies/pathing.md`.
- Entity KB read: `kb/enemies/bosses/the_insatiable.md` earlier this act.
- Current HP/status: 53/77, 42 gold, Energy Potion.
- Decision: choose node [1], Unknown at (2,4).
- Reason: The Unknown branch keeps comparable rest-site access while avoiding another visible Act 2 hallway fight. The deck already has enough card quality after Vicious/Whirlwind/Armaments-style needs are identified, so question marks are preferred when rest access is not worse.

## Floor 22 - Chompers

- Strategy files read: `history/run17_strategy.md`.
- Entity KB read: `kb/enemies/hive/chomper.md`, `kb/cards/ironclad/headbutt.md`, `kb/cards/ironclad/uppercut.md`, `kb/cards/ironclad/armaments.md`.
- Current HP/status: entered 53/77, Energy Potion, Anchor??? start block.
- Decision: played Aggression first, then Tremble + Strike + Spite on the opening attacker while accepting 14 damage after Anchor. Used Offering on turn 2 to activate Spite+ and draw block, fully blocked the second Chomper's Clamp with Shrug + Defends while dealing damage. On turn 3, Brightest Flame drew Fiend Fire+, and Fiend Fire+ killed the active attacker before its 18 damage landed. Finished the remaining low Chomper with Sword Boomerang+ and Strike+.
- Reason: Chomper KB says the pair alternates Clamp and Screech, so focus the current attacker and prevent repeated 9x2 turns. Artifact made Vulnerable setup low-value until stripped; Aggression and upgraded attacks carried the fight better than forcing Vicious early.
- Result: won at 39/76 after Burning Blood, preserved Energy Potion, claimed 10 gold, skipped Vulnerable Potion due full slot, took Armaments+.
- Reward reason: Armaments+ adds block and upgrades whole hands without spending a campfire, supporting the Smith > Rest plan and improving Fiend Fire/Whirlwind/Strike hands. Uppercut is good Vicious support but needs an upgrade; Headbutt+ duplicates an existing job.

## Floor 22 - Map Choice

- Strategy files read: `history/run17_strategy.md`, `kb/strategies/pathing.md`.
- Entity KB read: `kb/enemies/bosses/the_insatiable.md` earlier this act.
- Current HP/status: 39/76, 52 gold, no potion after the next fight was not yet known.
- Decision: choose only available node [0], Monster at (3,5).
- Reason: Forced path. The visible route still reaches a rest-site branch soon, but current HP requires careful hallway potion/HP math.

## Floor 23 - Hunter Killer

- Strategy files read: `history/run17_strategy.md`.
- Entity KB read: `kb/enemies/hive/hunter_killer.md`, `kb/cards/ironclad/havoc.md`, `kb/cards/ironclad/feel_no_pain.md`, `kb/cards/ironclad/evil_eye.md`.
- Current HP/status: entered 39/76, Energy Potion, Nunchaku [8].
- Decision: turn 1 used Dominate+ into attacks to exploit Vulnerable and trigger Nunchaku, holding Fiend Fire because it would not kill. On the 19-damage turn, front-loaded Sword Boomerang+ and Whirlwind through Vulnerable/Tender and accepted the hit rather than spending potion. On the next 24-damage turn, used Energy Potion because the hand could not kill or block enough on 3 energy, then Armaments+ upgraded the hand and the fight ended at low HP.
- Reason: Hunter Killer KB says Tender punishes long utility turns, so attacks must happen before low-impact cards once Tender is active. The potion was spent only when the alternative line risked lethal/near-lethal before the next rest path.
- Result: won at 19/76 after Burning Blood, Energy Potion spent, claimed 8 gold, took Feel No Pain.
- Reward reason: Feel No Pain is the best defensive engine for this deck's exhaust package: Tremble, Offering, Fiend Fire, Ascender's Bane, and statuses. Evil Eye is good immediate block, but Feel No Pain has better boss and status-fight scaling; Havoc+ remains too random.

## Floor 24 - Bowlbugs

- Strategy files read: `history/run17_strategy.md`, `kb/strategies/pathing.md`.
- Entity KB read: `kb/enemies/hive/bowlbugs.md`, `kb/mechanics/debuffs.md`.
- Current HP/status: entered 19/76, no potion, Anchor??? start block, Nunchaku [6].
- Decision: first attempt used Shrug It Off, then Sword Boomerang+, Spite, and Strike to reduce incoming/future damage; turn 2 used Brightest Flame, Defend, and Fiend Fire+ to kill Rock. This survived to 1 HP but exhausted too many attacks and left only setup into Nectar/Egg lethal. Reloaded the room with `save_and_quit` + main-menu `continue`.
- Retry decision: second distinct line used Shrug It Off, Bash on Rock, and Spite on Egg to set Rock Vulnerable and keep a better Fiend Fire+ break point. Turn 2 still required Brightest Flame, Defend, Strike, and Fiend Fire+ to kill Rock. The line again reached 1 HP but could not answer Nectar's 19 plus Egg's 8.
- Reason: Bowlbug KB says Rock attacks every turn unless its 16 damage is fully prevented; the opening hand could reach only 12 block after Shrug, so Rock could not be stunned. At 19 HP with no potion, no tested line could both remove Rock and preserve enough attacks/block for Nectar after its +16 Strength buff.
- Result: died on floor 24. Steam run log `1777643422.run` reports `win: false`, `was_abandoned: false`, and `killed_by_encounter: ENCOUNTER.BOWLBUGS_NORMAL`.

## Post-Run Reflection

- What worked: Act 1 pathing and card picks built real frontload; Winged Boots helped route flexibility; Tremble, Dominate+, Vicious, Aggression, Whirlwind, Offering, and Fiend Fire+ formed a coherent Vulnerable/burst shell. The Hunter Killer potion use was justified by survival math.
- What cost the run: entering a forced Act 2 hallway at 19 HP with no potion left no margin for Bowlbugs. The previous Hunter Killer fight consumed both HP and the Energy Potion; after that, the path still had a forced Monster before the rest site, so the run was already in emergency state.
- Next change: after a costly Act 2 fight, evaluate the next forced node before spending the last potion or accepting a low-HP exit. If the next node is a forced hallway and the deck has no potion, the threshold for spending earlier resources or choosing a safer previous path must be higher.
- Harness/gameplay lesson: save/load correctly reset the room start, but deterministic retries need a materially different strategic premise. Here the repeated premise "kill Rock with Fiend Fire after surviving at 4 HP" was still losing because it exhausted the multi-enemy follow-up needed for Nectar/Egg.
