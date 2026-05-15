# Run 18 - Ironclad A10

Date: 2026-05-01
Character: Ironclad
Ascension: 10
Outcome: In progress

## Pre-run Reads

- Read `AGENTS.md`, `GUIDE.md`, `kb/strategies/_index.md`, `kb/strategies/ironclad.md`, `kb/strategies/pathing.md`, `kb/strategies/archetypes.md`, and `kb/strategies/card_impressions.md`.
- Main setup reminders: Act 1 needs real Attack/frontload first; trace the full visible route tree and prioritize rest sites; prefer question marks over regular enemies when not desperate for rewards; preserve potions for elites/bosses, but spend them before hallway damage creates an unrecoverable next-room state.

## Floor 1 - Neow

- Strategy files read: `GUIDE.md`, `kb/strategies/_index.md`, `kb/strategies/ironclad.md`, `kb/strategies/pathing.md`, `kb/strategies/archetypes.md`, `kb/strategies/card_impressions.md`.
- Entity KB read: `kb/relics/winged_boots.md`, `kb/relics/lost_coffer.md`, `kb/relics/large_capsule.md`.
- Current HP/status: 64/80, 99 gold, Burning Blood, no potion.
- Options: Winged Boots, Lost Coffer, Large Capsule.
- Decision: take Lost Coffer.
- Reason: Lost Coffer gives an immediate card reward and random potion without adding starter-card bloat. That best supports the current guide lessons: Act 1 needs efficient frontload/card quality, and potion equity can prevent a later hallway from becoming unrecoverable. Winged Boots is strong path control, but the last run showed path control alone does not fix low-resource forced combats; Large Capsule's two random relics are tempting but adding both Strike and Defend dilutes early draw quality unless the relics are excellent.

## Floor 1 - Lost Coffer Reward

- Strategy files read: `history/run18_strategy.md`, `kb/strategies/card_impressions.md`, `kb/strategies/archetypes.md`, `kb/strategies/ironclad.md`.
- Entity KB read: `kb/potions/strength_potion.md`, `kb/cards/ironclad/shrug_it_off.md`, `kb/cards/ironclad/drum_of_battle.md`, `kb/cards/ironclad/ashen_strike.md`.
- Current HP/status: 64/80, 99 gold, Lost Coffer, no potion before reward.
- Options: Shrug It Off, Drum of Battle, Ashen Strike; Strength Potion.
- Decision: take Shrug It Off and claim Strength Potion.
- Reason: Shrug It Off is a high-quality cantrip block card that protects draw quality while the deck searches for real damage. Drum of Battle has a documented run-ending risk from exhausting the top draw-pile card each turn. Ashen Strike is an Attack, but without exhaust support it is only Strike-rate damage and does not satisfy the Act 1 frontload need well enough.

## Floor 1 - Act 1 Map Choice

- Strategy files read: `history/run18_strategy.md`, `kb/strategies/pathing.md`, `kb/strategies/bosses.md`.
- Entity KB read: `kb/enemies/bosses/waterfall_giant.md`.
- Current HP/status: 64/80, 99 gold, Strength Potion, Lost Coffer, Shrug It Off.
- Decision: choose node [1], Monster at (6,1).
- Reason: Waterfall Giant KB says it is a high-damage Act 1 boss that punishes slow decks with Steam Eruption and Pressure Gun, so the route needs both card rewards for damage and enough rest access for upgrades/healing. The right branch has far more rest-site flexibility, shops, question marks, and optional elite avoidance. The left branch is linear and elite-heavy, with only late recovery before multiple forced elites.

## Floor 2 - Sludge Spinner

- Strategy files read: `history/run18_strategy.md`.
- Entity KB read: `kb/enemies/underdocks/sludge_spinner.md`, `kb/potions/droplet_of_precognition.md`, `kb/cards/ironclad/infernal_blade.md`, `kb/cards/ironclad/iron_wave.md`, `kb/cards/ironclad/dismantle.md`.
- Current HP/status: entered 64/80, Strength Potion.
- Decision: opened Bash + Strike, accepting Oil Spray's 9 and Weak to set Vulnerable. On the 12-damage turn, used Shrug It Off, then took the damage line with two Weak Strikes rather than spending energy on extra Defend; killed next turn with Strikes.
- Reason: Sludge Spinner always opens with Oil Spray, and Burning Blood makes controlled chip acceptable. The deck still needed to convert Bash/Vulnerable into damage instead of prolonging a Strength-scaling fight.
- Result: won at 57/80 after Burning Blood, preserved Strength Potion, gained 13 gold, picked up Droplet of Precognition, and took Dismantle over Infernal Blade / Iron Wave.
- Reward reason: Dismantle is the strongest Act 1 frontload and Waterfall Giant card in the reward. Bash turns it into a 1-cost double-hit attack, and Strength Potion scales both hits. Infernal Blade is random, and Iron Wave is low-impact medium block/damage.

## Floor 2 - Map Choice

- Strategy files read: `history/run18_strategy.md`, `kb/strategies/pathing.md`.
- Entity KB read: `kb/enemies/bosses/waterfall_giant.md` earlier this act.
- Current HP/status: 57/80, 112 gold, Strength Potion, Droplet of Precognition.
- Decision: choose only available node [0], Unknown at (6,2).
- Reason: The Unknown keeps the high-flexibility right branch intact and avoids a second immediate hallway after the deck already gained Dismantle plus two potions. Question marks are preferred when the deck is not desperate for a random card reward and rest access remains good.

## Floor 3 - Abyssal Baths

- Strategy files read: `history/run18_strategy.md`.
- Entity KB read: `kb/events/abyssal_baths.md`.
- Current HP/status: entered 57/80, 112 gold, Strength Potion, Droplet of Precognition.
- Decision: Immerse once, then Linger once, then Exit Baths.
- Reason: The first two max-HP gains were efficient while current HP remained acceptable for the right-side route and two-potion safety. Stopped at 54/84 rather than chaining further because Waterfall Giant is a high-damage Act 1 boss and current HP buffer still matters.
- Result: gained +4 max HP and ended at 54/84.

## Floor 3 - Map Choice

- Strategy files read: `history/run18_strategy.md`, `kb/strategies/pathing.md`.
- Entity KB read: `kb/enemies/bosses/waterfall_giant.md` earlier this act.
- Current HP/status: 54/84, 112 gold, Strength Potion, Droplet of Precognition.
- Decision: choose node [0], Monster at (5,3).
- Reason: The monster gives a needed Act 1 card reward chance after taking only one damage card so far, and it preserves more branching into the central rest/shop cluster. The Unknown at (6,3) is safer short-term but narrows the route into the right side with less flexibility.

## Floor 4 - Toadpoles

- Strategy files read: `history/run18_strategy.md`.
- Entity KB read: `kb/enemies/underdocks/toadpole.md`, `kb/cards/ironclad/pommel_strike.md`, `kb/cards/ironclad/iron_wave.md`, `kb/cards/ironclad/evil_eye.md`.
- Current HP/status: entered 54/84, Strength Potion, Droplet of Precognition.
- Decision: followed the Toadpole KB and focused the Whirl attacker first with three Strikes, accepting 8 damage. Next turn killed the low Whirl Toadpole, played Defend, and used Dismantle on the Thorns Toadpole. Finished with Shrug It Off plus Strikes while preserving both potions.
- Reason: The weak encounter's front Toadpole starts with Spiken, so delayed attacks into it cost Thorns damage. Killing the Whirl attacker first reduces future multi-enemy pressure even though the fight still costs HP.
- Result: won at 43/84 after Burning Blood, preserved both potions, gained 14 gold, and took Pommel Strike over Iron Wave / Evil Eye.
- Reward reason: Pommel Strike is a premier Act 1 transition card: 9 damage plus draw improves frontload without reducing draw quality, and Pommel Strike+ is a major upgrade target. Evil Eye is strong later with reliable exhaust but not active yet; Iron Wave is medium damage/block.

## Floor 4 - Map Choice

- Strategy files read: `history/run18_strategy.md`, `kb/strategies/pathing.md`.
- Entity KB read: `kb/enemies/bosses/waterfall_giant.md` earlier this act.
- Current HP/status: 43/84, 126 gold, Strength Potion, Droplet of Precognition.
- Decision: choose node [0], Unknown at (4,4).
- Reason: Current HP is medium-low after Toadpoles, and the Unknown branch reaches a forced Monster followed by an immediate RestSite/Shop choice. The Monster branch chains additional fights and can route toward an elite before comparable recovery, which is not justified at 43 HP despite two good potions.

## Floor 5 - Shop

- Strategy files read: `history/run18_strategy.md`, `kb/strategies/card_impressions.md`, `kb/strategies/ironclad.md`.
- Entity KB read: `kb/cards/ironclad/anger.md`, `kb/cards/ironclad/fight_me.md`, `kb/cards/ironclad/true_grit.md`, `kb/potions/blood_potion.md`, `kb/potions/attack_potion.md`, `kb/potions/mazaleth_s_gift.md`.
- Current HP/status: 43/84, 126 gold, Strength Potion, Droplet of Precognition.
- Decision: buy Anger for 49g, discard Droplet of Precognition, buy Blood Potion for 52g, and use Blood Potion immediately.
- Reason: Anger is a strong Act 1 damage-per-energy bridge and a known good early pick; it improves frontload without competing for energy with Bash/Dismantle. Blood Potion converted a weaker potion slot into 16 current HP before the next forced Monster, directly applying the post-run lesson not to carry low HP into forced hallways. Fight Me was cheap but gives enemies Strength and competes with Bash; True Grit is good but does not solve immediate damage and wants an upgrade.
- Result: left shop with 25 gold, 59/84 HP, and Strength Potion.

## Floor 5 - Map Choice

- Strategy files read: `history/run18_strategy.md`, `kb/strategies/pathing.md`.
- Entity KB read: `kb/enemies/bosses/waterfall_giant.md` earlier this act.
- Current HP/status: 59/84, 25 gold, Strength Potion.
- Decision: choose only available node [0], Monster at (3,5).
- Reason: Forced path. The prior Blood Potion use makes the forced hallway acceptable, and the next node offers RestSite or Shop recovery/setup.

## Floor 6 - Corpse Slugs

- Strategy files read: `history/run18_strategy.md`.
- Entity KB read: `kb/enemies/underdocks/corpse_slug.md`, `kb/mechanics/buffs.md`, `kb/strategies/card_impressions.md`, `kb/cards/ironclad/inferno.md`, `kb/cards/ironclad/pommel_strike.md`, `kb/cards/ironclad/havoc.md`.
- Current HP/status: entered 59/84, Strength Potion.
- Decision: damaged the attacking slug first with Dismantle + Strike + Defend, then killed it with Anger + Bash to trigger Ravenous stun on the survivor. Preserved Strength Potion even after leaving the survivor at 1 HP, because Shrug It Off reduced the incoming hit enough and the next turn had guaranteed lethal.
- Reason: Corpse Slug KB says the survivor becomes Stunned after eating another Slug, but live A10 Ravenous +5 Strength makes the follow-up attacks 8x2 and 14, so the line needed either quick lethal or block. Strength Potion was not worth spending to save 10 net HP in a hallway immediately before a rest/shop branch.
- Result: won at 51/84 after Burning Blood, preserved Strength Potion, gained 14 gold, and took a second Pommel Strike over Inferno / Havoc.
- Reward reason: Pommel Strike is a premium Act 1 attack/draw card and a core upgrade target. Inferno offers AoE/scaling, but the deck does not yet have the HP cushion or self-damage package to justify it before Waterfall Giant. Havoc is uncontrolled exhaust and low-confidence without top-deck control.

## Floor 6 - Map Choice

- Strategy files read: `history/run18_strategy.md`, `kb/strategies/pathing.md`.
- Entity KB read: `kb/enemies/bosses/waterfall_giant.md` earlier this act.
- Current HP/status: 51/84, 39 gold, Strength Potion.
- Decision: choose node [0], RestSite at (3,6), over Shop at (4,6).
- Reason: The branches converge, and 39 gold is not enough to make the shop valuable. The rest site can either heal if the next path is dangerous or, preferably, upgrade a key card for Waterfall Giant.

## Floor 7 - Rest Site

- Strategy files read: `GUIDE.md`, `history/run18_strategy.md`, `kb/strategies/archetypes.md`.
- Entity KB read: `kb/cards/ironclad/pommel_strike.md`.
- Current HP/status: 51/84, 39 gold, Strength Potion.
- Decision: Smith Pommel Strike.
- Reason: GUIDE and the win-corpus notes make Smith the default, and 51/84 with Burning Blood is enough HP to upgrade rather than rest. Pommel Strike+ is the highest-impact upgrade because it adds a second draw while improving damage, giving the deck a real cycle card for both Act 1 fights and Waterfall Giant.

## Floor 7 - Map Choice

- Strategy files read: `history/run18_strategy.md`, `kb/strategies/pathing.md`.
- Entity KB read: `kb/enemies/bosses/waterfall_giant.md` earlier this act.
- Current HP/status: 51/84, 39 gold, Strength Potion.
- Decision: choose only available node [0], Unknown at (4,7).
- Reason: Forced path, with the next branch offering Monster or Elite and then treasure/rest access.

## Floor 8 - Room Full of Cheese

- Strategy files read: `history/run18_strategy.md`, `GUIDE.md`, `kb/strategies/card_impressions.md`, `kb/strategies/archetypes.md`.
- Entity KB read: `kb/events/room_full_of_cheese.md`, `kb/relics/the_chosen_cheese.md`, `kb/cards/ironclad/body_slam.md`, `kb/cards/ironclad/molten_fist.md`, `kb/cards/ironclad/true_grit.md`, `kb/cards/ironclad/bloodletting.md`, `kb/cards/ironclad/iron_wave.md`, `kb/cards/ironclad/blood_wall.md`, `kb/cards/ironclad/thunderclap.md`, `kb/cards/ironclad/headbutt.md`.
- Current HP/status: 51/84, 39 gold, Strength Potion.
- Decision: choose Gorge, then take Bloodletting and True Grit.
- Reason: Search would cost 14 HP, dropping to 37 before a Monster/Elite fork and without an immediate heal. Gorge adds selected commons, not random forced bloat; Bloodletting fits the Pommel Strike+/Shrug cycle shell, and True Grit gives the deck an exhaust-block card that becomes a major upgrade target. Skipped Body Slam because the block package is not ready, Thunderclap because it is weak without AoE payoff/Vicious yet, and medium cards because Bloodletting/True Grit better support the long-term engine.

## Floor 8 - Map Choice

- Strategy files read: `history/run18_strategy.md`, `kb/strategies/pathing.md`.
- Entity KB read: `kb/enemies/bosses/waterfall_giant.md` earlier this act.
- Current HP/status: 51/84, 39 gold, Strength Potion.
- Decision: choose node [0], Monster at (4,8), over Elite at (5,8).
- Reason: At 51 HP with one potion and no Bash/True Grit upgrade yet, the immediate elite is not worth the risk. The Monster path reaches the same treasure and later rest structure, so it lets the deck earn one more reward and reassess the optional elite after treasure.

## Floor 9 - Haunted Ship

- Strategy files read: `history/run18_strategy.md`, `kb/strategies/card_impressions.md`, `kb/strategies/archetypes.md`, `kb/strategies/ironclad.md`.
- Entity KB read: `kb/enemies/underdocks/haunted_ship.md`, `kb/cards/status/dazed.md`, `kb/cards/ironclad/true_grit.md`, `kb/cards/ironclad/blood_wall.md`, `kb/cards/ironclad/breakthrough.md`.
- Current HP/status: entered 51/84, Strength Potion.
- Decision: used the no-damage Haunt turn to frontload Pommel Strike+, Pommel Strike, Anger, and Strike for 31 damage before the 5 Dazed entered the discard. On the 11 + Weak turn, played Defend plus two Strikes to reduce the hit while setting up the Bash/Dismantle kill. Killed on turn 3 with Bash into Dismantle while Weak, preserving Strength Potion.
- Reason: Haunted Ship KB says it always uses Haunt first and then attacks; the right response is to attack hard before Dazed pollutes the first reshuffle. Bash still made Dismantle lethal through Weak because the enemy was Vulnerable.
- Result: won at 51/84 after Burning Blood, gained 8 gold, and took Breakthrough over True Grit / Blood Wall.
- Reward reason: Breakthrough adds efficient AoE/frontload, which the deck lacked and which matters for Act 2 pathing. A second unupgraded True Grit adds random exhaust before the first copy is upgraded, and Blood Wall is useful boss block but less urgent than the first AoE attack.

## Floor 9 - Map Choice

- Strategy files read: `history/run18_strategy.md`, `kb/strategies/pathing.md`.
- Entity KB read: `kb/enemies/bosses/waterfall_giant.md` earlier this act.
- Current HP/status: 51/84, 47 gold, Strength Potion.
- Decision: choose only available node [0], Treasure at (5,9).
- Reason: Forced path; treasure precedes a Monster/Elite choice and then a rest site.

## Floor 10 - Treasure

- Strategy files read: `history/run18_strategy.md`.
- Entity KB read: `kb/relics/parrying_shield.md`.
- Current HP/status: 51/84, 86 gold, Strength Potion.
- Decision: claim Parrying Shield.
- Reason: Free relic. Parrying Shield rewards 10+ block turns, which line up with Shrug It Off, True Grit, and defensive Waterfall Giant turns.

## Floor 10 - Map Choice

- Strategy files read: `history/run18_strategy.md`, `kb/strategies/pathing.md`, `kb/strategies/elites.md`.
- Entity KB read: `kb/enemies/elites/phantasmal_gardener.md`, `kb/enemies/elites/skulking_colony.md`, `kb/enemies/elites/terror_eel.md`, `kb/enemies/bosses/waterfall_giant.md` earlier this act.
- Current HP/status: 51/84, 86 gold, Strength Potion.
- Decision: choose node [1], Monster at (6,10), over Elite at (4,10).
- Reason: The elite path has an immediate rest afterward, but Terror Eel remains a possible Underdocks elite and its KB says to enter around 60+ HP and spend potions. At 51 HP with only Strength Potion, the safer Monster path preserves the boss potion and still reaches a rest site.

## Floor 11 - Calcified Cultist + Seapunk

- Strategy files read: `history/run18_strategy.md`, `kb/strategies/card_impressions.md`, `kb/strategies/archetypes.md`.
- Entity KB read: `kb/enemies/underdocks/cultists.md`, `kb/enemies/underdocks/seapunk.md`, `kb/cards/ironclad/havoc.md`, `kb/cards/ironclad/blood_wall.md`, `kb/cards/ironclad/tremble.md`.
- Current HP/status: entered 51/84, Strength Potion.
- Decision: focused Calcified Cultist first while partially blocking Seapunk, then used Breakthrough + Pommel Strike to kill the Cultist before Ritual scaled. Used a no-attack enemy turn to play Anger + Strike plus 10 block, triggering Parrying Shield. Finished Seapunk with Pommel Strike+ into Anger + Strikes.
- Reason: Cultists KB says Calcified Cultist should die quickly after Incantation because Ritual makes its 11-damage Dark Strike scale every turn. Seapunk's Bubble Burp turn is a good Parrying Shield setup turn if 10 block is available.
- Result: won at 40/84 after Burning Blood, preserved Strength Potion, gained 10 gold, and took Blood Wall over Havoc / Tremble.
- Reward reason: Blood Wall gives base-value one-card block for Waterfall Giant and helps trigger Parrying Shield. Tremble is a strong Vulnerable card, but the current boss gap is surviving repeated heavy attacks; Havoc remains uncontrolled exhaust.

## Floor 11 - Map Choice

- Strategy files read: `history/run18_strategy.md`, `kb/strategies/pathing.md`.
- Entity KB read: `kb/enemies/bosses/waterfall_giant.md` earlier this act.
- Current HP/status: 40/84, 96 gold, Strength Potion.
- Decision: choose node [0], RestSite at (5,11), over Unknown at (6,11).
- Reason: 40/84 is too low to gamble on an unknown before Waterfall Giant. The rest-site branch still leaves question-mark and pre-boss rest options.

## Floor 12 - Rest Site

- Strategy files read: `GUIDE.md`, `history/run18_strategy.md`.
- Entity KB read: `kb/enemies/bosses/waterfall_giant.md` earlier this act.
- Current HP/status: 40/84, 96 gold, Strength Potion.
- Decision: Rest to 65/84.
- Reason: Smith is the default, but this HP was below the safe band after a costly hallway, and Waterfall Giant is a high-damage Act 1 boss. Resting keeps the run stable while preserving the Strength Potion and likely a later pre-boss campfire for smith/rest based on final HP.

## Floor 12 - Map Choice

- Strategy files read: `history/run18_strategy.md`, `kb/strategies/pathing.md`.
- Entity KB read: `kb/enemies/bosses/waterfall_giant.md` earlier this act.
- Current HP/status: 65/84, 96 gold, Strength Potion.
- Decision: choose only available node [0], Unknown at (4,12).
- Reason: Forced path.

## Floor 13 - Shop

- Strategy files read: `history/run18_strategy.md`, `kb/strategies/card_impressions.md`, `kb/strategies/archetypes.md`, `GUIDE.md`.
- Entity KB read: `kb/cards/ironclad/twin_strike.md`, `kb/cards/ironclad/perfected_strike.md`, `kb/cards/ironclad/havoc.md`, `kb/cards/ironclad/second_wind.md`, `kb/cards/ironclad/inflame.md`, `kb/cards/ironclad/production.md`, `kb/potions/speed_potion.md`, `kb/potions/fire_potion.md`, `kb/potions/strength_potion.md`.
- Current HP/status: 65/84, 96 gold, Strength Potion.
- Decision: buy Inflame for 78g; leave at 18g.
- Reason: Waterfall Giant is an attrition boss, and Inflame gives permanent Strength that stacks with the saved Strength Potion and improves Anger, Breakthrough, Pommel Strike, and Dismantle turns. Second Wind is strong but risky unupgraded and can exhaust too many defensive cards if misused; Production is tempo without draw guarantee; Perfected Strike is cheap but a temporary Strike-density bridge rather than boss scaling.

## Floor 13 - Map Choice

- Strategy files read: `history/run18_strategy.md`, `kb/strategies/pathing.md`.
- Entity KB read: `kb/enemies/bosses/waterfall_giant.md` earlier this act.
- Current HP/status: 65/84, 18 gold, Strength Potion.
- Decision: choose node [0], Unknown at (3,13), over Monster at (5,13).
- Reason: The deck has enough Act 1 material and a boss scaling card now. The Unknown path avoids a potentially costly hallway and guarantees Shop -> RestSite -> Waterfall Giant; the shop is low-value at 18g, but the path protects HP/potion for the boss.

## Floor 14 - Cultists

- Strategy files read: `history/run18_strategy.md`, `kb/strategies/card_impressions.md`, `kb/strategies/archetypes.md`.
- Entity KB read: `kb/enemies/underdocks/cultists.md`, `kb/cards/ironclad/cinder.md`, `kb/cards/ironclad/breakthrough.md`, `kb/cards/ironclad/perfected_strike.md`.
- Current HP/status: entered 65/84, Strength Potion.
- Decision: focused Calcified Cultist first; used Shrug It Off and Defend on turn 1 to trigger Parrying Shield, then killed Calcified with Breakthrough + Dismantle before its Ritual scaled. Played Inflame during the Damp Cultist phase, then killed Damp with Strength-boosted Strikes before taking another 15.
- Reason: The unknown path still produced a hallway, so the priority was to prevent Ritual from compounding into a boss-entry disaster while preserving Strength Potion. Damp Cultist's A10 Ritual reaches 15 quickly, so after Calcified died the fight became a damage race.
- Result: won at 58/84 after Burning Blood, preserved Strength Potion, gained 11 gold, and took Perfected Strike over Cinder / Breakthrough.
- Reward reason: Perfected Strike is a narrow Act 1 boss bridge with this deck's high Strike-tag count, including starter Strikes and two Pommel Strikes. Cinder's random exhaust can damage consistency, and a second Breakthrough is more hallway/AoE than Waterfall Giant damage.

## Floor 14 - Map Choice

- Strategy files read: `history/run18_strategy.md`, `kb/strategies/pathing.md`.
- Entity KB read: `kb/enemies/bosses/waterfall_giant.md` earlier this act.
- Current HP/status: 58/84, 29 gold, Strength Potion.
- Decision: choose only available node [0], Shop at (3,14).
- Reason: Forced path to final RestSite before the boss.

## Floor 15 - Shop

- Strategy files read: `history/run18_strategy.md`, `kb/strategies/card_impressions.md`.
- Entity KB read: `kb/cards/ironclad/iron_wave.md`, plus visible but unaffordable shop entries.
- Current HP/status: 58/84, 29 gold, Strength Potion.
- Decision: skip discounted Iron Wave and proceed.
- Reason: Iron Wave is low-impact immediately before Waterfall Giant and would make it harder to draw Pommel Strike+, Blood Wall, Inflame, Bash, Perfected Strike, and True Grit+.

## Floor 16 - Rest Site

- Strategy files read: `GUIDE.md`, `history/run18_strategy.md`, `kb/strategies/archetypes.md`.
- Entity KB read: `kb/enemies/bosses/waterfall_giant.md`, `kb/cards/ironclad/true_grit.md`.
- Current HP/status: 58/84, 29 gold, Strength Potion.
- Decision: Smith True Grit.
- Reason: 58/84 is acceptable for a smith with Blood Wall, Shrug It Off, Parrying Shield, and Strength Potion. True Grit+ is the best repeated boss-turn upgrade: it improves block to 9 and changes random exhaust into controlled live-deck thinning, which matters more over a long Waterfall Giant fight than +1 Strength or another medium damage upgrade.

## Floor 17 - Boss: Waterfall Giant

- Strategy files read: `history/run18_strategy.md`, `kb/strategies/bosses.md`, `kb/strategies/card_impressions.md`, `kb/strategies/archetypes.md`.
- Entity KB read: `kb/enemies/bosses/waterfall_giant.md`, `kb/potions/strength_potion.md`, `kb/cards/ironclad/dark_embrace.md`, `kb/cards/ironclad/hellraiser.md`, `kb/cards/ironclad/fiend_fire.md`.
- Current HP/status: entered 58/84 with Strength Potion, Burning Blood, Lost Coffer, Parrying Shield.
- Decision: used Strength Potion at the start of the successful retry, set up Inflame and True Grit+ early, and prioritized blocking Pressure Gun / Stomp turns over greedy damage. Delayed final lethal through a Siphon turn so the Death Blow hand could draw Pommel Strike+ into Blood Wall and survive the 44 Steam Eruption.
- Reason: Waterfall Giant KB says the boss becomes invulnerable on lethal and then deals stored Steam Eruption at the end of the next turn. The first retry killed from the wrong hand and produced a Death Blow turn with only one Defend; that line was reloaded because it could not survive the explosion.
- Result: won at 9/84 after Death Blow, claimed 75 gold and Vulnerable Potion, and took Dark Embrace over Hellraiser / Fiend Fire.
- Reward reason: `card_impressions.md` marks Dark Embrace as a positive rare engine and a Doormaker counterplay with Anger/exhaust. Hellraiser had direct Strike synergy with Perfected Strike and the starter Strikes, but the strategy file flags it as a low-impact build-around; Fiend Fire was strong burst but risked exhausting needed block in a deck already struggling with boss survival timing.

### Live Reflection

- What worked: Strength Potion plus Inflame gave enough damage to prevent Steam Eruption from becoming completely unmanageable, and True Grit+ controlled exhaust without deleting random defense.
- Mistake prevented by reload: killing Waterfall Giant is not sufficient; lethal must be timed so the following Death Blow turn has enough block/HP. A hand with only Defend at 30 HP lost to 44 Steam Eruption.
- Next-run change: before final boss lethal, inspect the next draw pile and calculate explosion survivability. If the kill hand strands the Death Blow turn, delay lethal even through Siphon if the delayed draw is better.

## Act 2 Start - Map Choice

- Strategy files read: `kb/strategies/pathing.md`, `kb/strategies/bosses.md`, `GUIDE.md`.
- Entity KB read: `kb/enemies/bosses/kaiser_crab.md`.
- Current HP/status: 9/84, 104 gold, Vulnerable Potion.
- Decision: choose the only available Ancient node.
- Reason: The visible Act 2 boss is Kaiser Crab. Its KB says Rocket's turn-4 Laser and Crusher's turn-3 Bug Sting/Frail setup are the main danger, so this act needs recovery, one-card block, Weak/Vulnerable control, and cautious pathing. At 9 HP, the route must prioritize immediate healing/safety and avoid early elite exposure unless an event changes HP dramatically.

## Floor 18 - Ancient: Pael

- Strategy files read: `kb/strategies/card_impressions.md`, `history/run18_strategy.md`.
- Entity KB read: `kb/enemies/ancients/pael.md`, `kb/relics/pael_s_blood.md`, `kb/relics/pael_s_growth.md`, `kb/relics/pael_s_tears.md`.
- Current HP/status: Pael healed the run to 69/84 before the choice; 104 gold, Vulnerable Potion.
- Decision: take Pael's Blood.
- Reason: Pael's Blood gives +1 draw at the start of every turn, which is the strongest default support for this deck's new Dark Embrace, Inflame, True Grit+, Bloodletting, and boss setup needs. Pael's Growth could clone a premium card at rest sites, but this deck is not yet stable enough to spend future campfires duplicating; Pael's Tears is weaker because this low-curve deck rarely wants to float energy.

## Floor 18 - Map Choice

- Strategy files read: `kb/strategies/pathing.md`, `GUIDE.md`, `history/run18_strategy.md`.
- Entity KB read: `kb/enemies/bosses/kaiser_crab.md`.
- Current HP/status: 69/84, 104 gold, Vulnerable Potion, Pael's Blood.
- Decision: choose node [2], Monster at (4,1), over Monster nodes at (0,1), (2,1), and (6,1).
- Reason: All branches start with a hallway, but the (4,1) branch reaches Unknown -> Shop immediately afterward and then has multiple Unknown/rest branches. The left branches force more early combats before shop/rest access, while Act 2 pathing should favor safety, question marks, and recovery before optional elites.

## Floor 19 - Exoskeletons

- Strategy files read: `history/run18_strategy.md`, `kb/strategies/card_impressions.md`.
- Entity KB read: `kb/enemies/hive/exoskeleton.md`, `kb/mechanics/buffs.md`, `kb/potions/liquid_bronze.md`, `kb/potions/vulnerable_potion.md`, `kb/cards/ironclad/true_grit.md`, `kb/cards/ironclad/breakthrough.md`, `kb/cards/ironclad/headbutt.md`.
- Current HP/status: entered 69/84 with Vulnerable Potion; ended 60/84 after Burning Blood with Vulnerable Potion and Liquid Bronze.
- Decision: opened with Breakthrough to exploit Hard to Kill across all three enemies, used True Grit+ for block and a controlled Defend exhaust, then used Inflame, Anger, Pommel Strike, and Bloodletting to remove attacking Exoskeletons before their Strength scaling could compound.
- Reason: Exoskeleton KB says each damage instance is capped at 9, so separate hits and AoE are more valuable than one large attack. Spending 3 HP on Bloodletting was correct because it converted into extra capped hits and likely prevented a 20-damage attack cycle.
- Reward decision: claimed Liquid Bronze because a second potion slot was available, claimed 15 gold, and took True Grit over Breakthrough / Headbutt.
- Reward reason: Act 2 card guidance says to add engine, reliable block, exhaust, energy, or boss answers rather than duplicate solved jobs. A second Breakthrough is redundant AoE and HP loss; Headbutt can recur Pommel Strike or Perfected Strike, but the deck's bigger Kaiser Crab risk is defensive density. True Grit is imperfect unupgraded, but it adds block, exhaust support for Dark Embrace, and a future upgrade target; sequence it last when random exhaust would be dangerous.

## Floor 20 - Event: Crystal Sphere

- Strategy files read: `history/run18_strategy.md`, `kb/strategies/pathing.md`.
- Entity KB read: `kb/events/crystal_sphere.md`, `kb/cards/status/debt.md`.
- Current HP/status: entered 60/84 with 119 gold, Vulnerable Potion, Liquid Bronze.
- Decision: chose Uncover Future over Payment Plan.
- Reason: Payment Plan adds Debt, a permanent unplayable curse that drains 10 gold when drawn. Pael's Blood increases hand volume, so Debt would trigger more often and dilute the new Dark Embrace/True Grit engine. Paying gold was strategically cleaner despite weakening the next shop.
- Reload lesson: the first big center click revealed a nearby 2x2 Curse, so the room was reloaded and the known curse area was avoided. A second line revealed partial large rewards and got stuck. A third line used small divinations only on known single-cell gold, but after reward/proceed attempts the harness still returned to the Crystal Sphere screen.
- Harness blocker: `crystal_sphere_proceed()` and `proceed_to_map()` reported success or availability but did not leave the minigame after rewards/divinations. Save/load consistently returns to the event start. Manual UI intervention may be needed to exit this room.
- Manual resolution: user advanced the event manually; final known outcome was Petrified Toad relic, Not Yet and Second Wind added, and arrival at the next shop with 129 gold.

## Floor 21 - Shop

- Strategy files read: `kb/strategies/card_impressions.md`, `kb/strategies/pathing.md`, `history/run18_strategy.md`.
- Entity KB read: `kb/cards/ironclad/rupture.md`, `kb/cards/colorless/purity.md`, `kb/cards/ironclad/rage.md`, `kb/cards/ironclad/expect_a_fight.md`, `kb/cards/ironclad/sword_boomerang.md`, `kb/cards/ironclad/twin_strike.md`, `kb/potions/fortifier.md`, `kb/relics/petrified_toad.md`.
- Current HP/status: 60/84, 129 gold, Vulnerable Potion, Liquid Bronze; Petrified Toad now procures a Potion-Shaped Rock at combat start.
- Decision: bought Rupture for 72 gold and skipped the rest, leaving 57 gold.
- Reason: Rupture is the best shop scaling buy because Bloodletting, Blood Wall, Breakthrough, and other player-turn HP loss can convert into Strength for long fights. Purity overlaps with Second Wind/True Grit and does not add block by itself; common attacks add damage but dilute the new Dark Embrace/Second Wind/Rupture setup; removal was unaffordable after buying the stronger scaling piece.

## Floor 22 - Event: Amalgamator

- Strategy files read: `kb/strategies/pathing.md`, `kb/strategies/card_impressions.md`, `history/run18_strategy.md`.
- Entity KB read: `kb/events/amalgamator.md`, `kb/cards/colorless/ultimate_strike.md`, `kb/cards/colorless/ultimate_defend.md`, `kb/cards/ironclad/second_wind.md`.
- Current HP/status: 60/84, 57 gold, Vulnerable Potion, Liquid Bronze.
- Initial mistake: chose Combine Defends for Ultimate Defend, overvaluing compact block for Kaiser Crab.
- Correction: user pointed out that Second Wind+ makes extra Defends acceptable exhaust-to-block fuel, while basic Strikes remain weak cards. Reloaded the event with save/load, chose Combine Strikes, removed two Strikes, and added Ultimate Strike.
- Reason: the deck already has Second Wind, True Grit+, Blood Wall, Shrug It Off, Not Yet, and potions for defense; cleaning two Strikes improves draw quality and Ultimate Strike gives a single efficient attack without weakening Second Wind fuel.

## Floor 23 - Event: Field of Man-Sized Holes

- Strategy files read: `kb/strategies/pathing.md`, `kb/strategies/card_impressions.md`, `history/run18_strategy.md`.
- Entity KB read: `kb/events/field_of_man_sized_holes.md`, `kb/cards/status/normality.md`, `kb/cards/enchants/perfect_fit.md`.
- Current HP/status: 60/84, 57 gold, Vulnerable Potion, Liquid Bronze.
- Decision: chose Enter Your Hole and enchanted Pommel Strike+ with Perfect Fit.
- Reason: Resist would remove two cards but add Normality, which is dangerous in a Pael's Blood/Dark Embrace/Bloodletting deck that can need more than three plays on boss defense turns. Perfect Fit does not help the opening shuffle, but on later reshuffles it places Pommel Strike+ on top, improving access to draw, damage, and engine pieces.

## Floor 24 - Event: The Future of Potions?

- Strategy files read: `kb/strategies/card_impressions.md`, `history/run18_strategy.md`.
- Entity KB read: `kb/events/the_future_of_potions.md`, `kb/potions/liquid_bronze.md`, `kb/potions/vulnerable_potion.md`, `kb/cards/ironclad/whirlwind.md`, `kb/cards/ironclad/spite.md`, `kb/cards/ironclad/dismantle.md`.
- Current HP/status: 60/84, 57 gold, Vulnerable Potion, Liquid Bronze.
- Decision: traded Liquid Bronze for an upgraded uncommon Attack reward, then took Whirlwind+ over Spite+ / Dismantle+.
- Reason: the event had no skip and Vulnerable Potion is the higher-value Kaiser Crab burst potion. Trading Liquid Bronze also opens a potion slot for Petrified Toad's Potion-Shaped Rock. Whirlwind+ is strong with Bloodletting, Rupture, Inflame, Vulnerable, and Kaiser Crab's two bodies; Spite+ fits HP-loss turns but is narrower, and Dismantle+ duplicates an existing Vulnerable payoff.

## Floor 25 - Rest Site

- Strategy files read: `GUIDE.md`, `kb/strategies/card_impressions.md`, `history/run18_strategy.md`.
- Entity KB read: `kb/cards/ironclad/dark_embrace.md`, `kb/cards/ironclad/rupture.md`, `kb/cards/ironclad/bloodletting.md`, `kb/cards/ironclad/second_wind.md`.
- Current HP/status: 60/84, 57 gold, Vulnerable Potion.
- Decision: Smith Dark Embrace.
- Reason: 60/84 is enough HP to follow the Smith default with more rest access visible. Dark Embrace's upgrade from 2 to 1 energy is the biggest setup breakpoint for the Second Wind+/True Grit+/Not Yet exhaust engine; Rupture+ is strong but still playable at base cost, while unupgraded Dark Embrace can be too slow on Kaiser Crab's early pressure turns.

## Floor 26 - Treasure

- Strategy files read: `history/run18_strategy.md`.
- Entity KB read: `kb/relics/stone_cracker.md`.
- Current HP/status: 60/84, 96 gold, Vulnerable Potion.
- Decision: claimed Stone Cracker.
- Reason: free combat upgrades are high value in a deck that still has unupgraded Bloodletting, Rupture, Bash, Blood Wall, Not Yet, Ultimate Strike, and several basics.

## Floor 27 - Elite: Decimillipede

- Strategy files read: `GUIDE.md`, `history/run18_strategy.md`, `kb/strategies/elites.md`, `kb/strategies/card_impressions.md`, `kb/strategies/archetypes.md`.
- Entity KB read: `kb/enemies/elites/decimillipede.md`, `kb/potions/vulnerable_potion.md`, `kb/potions/energy_potion.md`, `kb/relics/regal_pillow.md`, `kb/cards/ironclad/dominate.md`, `kb/cards/ironclad/headbutt.md`, `kb/cards/ironclad/body_slam.md`.
- Current HP/status: entered 60/84 with 96 gold, Vulnerable Potion, and Petrified Toad's Potion-Shaped Rock; ended 25/84 with Energy Potion, Regal Pillow, and 126 gold.
- Initial mistake: the first winning line left the run at only 8 HP because Vulnerable was assigned to the wrong Decimillipede segment, allowing a killed segment to reattach before the final cleanup.
- Correction: reloaded the fight and used a coordinated stagger plan. Dark Embrace+, Breakthrough, low-X Whirlwind, and Anger equalized the segments; Inflame plus Second Wind+ created a full-block turn; Potion-Shaped Rock plus Ultimate Strike killed one segment; final turn used Vulnerable Potion on the segment that Perfected Strike could kill, then Bash plus Pommel Strike killed the last segment before reattach.
- Reason: Decimillipede KB says killed segments revive with 25 HP if any segment remains alive. The improved line converted potions into synchronized kills instead of spending them as generic damage.
- Reward decision: claimed Regal Pillow, Energy Potion, 30 gold, and took Dominate over Headbutt / Body Slam.
- Reward reason: Regal Pillow makes low-HP recovery much stronger, Energy Potion should be saved for Kaiser Crab or a lethal-prevention fight, and Dominate adds boss scaling while exhausting for Dark Embrace. Headbutt was useful but lower ceiling here; Body Slam is still premature without Barricade, Unmovable, or a stronger repeated large-block plan.

### Live Reflection

- What worked: save/load prevented a technically survived but strategically losing 8-HP exit, and the replay used the same deterministic fight with a better resource assignment.
- Mistake prevented by reload: do not treat Vulnerable Potion as generic damage in Decimillipede. It should go on the segment that turns a specific attack into a kill and preserves the reattach timer.
- Next-run change: against revive/reattach enemies, plan the final two kills before spending the first burst potion.

## Floor 27 Map Choice / Floor 28 Rest Site

- Strategy files read: `GUIDE.md`, `kb/strategies/pathing.md`, `history/run18_strategy.md`.
- Entity KB read: `kb/enemies/bosses/kaiser_crab.md`, `kb/relics/regal_pillow.md`.
- Current HP/status: 25/84, 126 gold, Energy Potion.
- Decision: chose the immediate RestSite branch and rested to 65/84.
- Reason: the alternate branch began with a forced Monster at 25 HP. Pathing notes prioritize rest access and warn that leaving an Act 2 fight around 20-25 HP can still be unrecoverable if another hallway is next. Regal Pillow made Rest heal 40 total, which is stronger than a marginal smith before a route that still includes a forced elite and Kaiser Crab.

## Floor 29 - Tunneler

- Strategy files read: `history/run18_strategy.md`, `kb/strategies/card_impressions.md`, `kb/strategies/archetypes.md`.
- Entity KB read: `kb/enemies/hive/tunneler.md`, `kb/potions/weak_potion.md`, `kb/cards/ironclad/armaments.md`, `kb/cards/ironclad/blood_wall.md`, `kb/cards/ironclad/headbutt.md`.
- Current HP/status: entered 65/84 with Energy Potion; ended 71/84 with Energy Potion, Weak Potion, and 134 gold.
- Decision: used Perfected Strike plus Second Wind+ on turn 1 to block the Bite and exhaust Debt. On the Burrow turn, used Bash, Potion-Shaped Rock, Pommel Strike+, and Anger+ to lower Tunneler to 16 HP before the 37 Block appeared. On the Attack from Below turn, Inflame plus Dismantle plus Ultimate Strike broke the block and killed before damage.
- Reason: Tunneler KB says the A10 Burrow gives 37 Block and Attack from Below hits for 26; the safe plan is either near-kill before Burrow or break the Block immediately. The line preserved the real Energy Potion and took no damage.
- Reward decision: claimed Weak Potion and 8 gold, then took Blood Wall over Armaments / Headbutt.
- Reward reason: Weak Potion is a Kaiser Crab Laser answer. Blood Wall is immediate one-card defense for the forced elite and boss, and it also triggers Rupture. Armaments would need a smith before it becomes a broad upgrade tool, while Headbutt is useful recursion but does not solve the next room's damage risk.

## Floor 30 - Elite: Infested Prism

- Strategy files read: `history/run18_strategy.md`, `kb/strategies/elites.md`, `kb/strategies/card_impressions.md`, `kb/strategies/archetypes.md`.
- Entity KB read: `kb/enemies/elites/infested_prism.md`, `kb/enemies/elites/decimillipede.md`, `kb/enemies/elites/entomancer.md`, `kb/potions/power_potion.md`, `kb/relics/gambling_chip.md`, `kb/cards/ironclad/aggression.md`, `kb/cards/ironclad/stomp.md`, `kb/cards/ironclad/dismantle.md`.
- Current HP/status: entered 71/84 with Energy Potion and Weak Potion; ended 50/84 with Energy Potion, Power Potion, Gambling Chip, Aggression, and 151 gold.
- Decision: set Rupture+ on turn 1, used Blood Wall and block/draw cards to cover early attacks, spent Weak Potion on the 10x3 Whirlwind turn, and converted Bloodletting / Blood Wall / Breakthrough self-damage into Strength. Dominate+ plus Bash/Perfected Strike created the burst window, and Breakthrough -> Pommel Strike+ -> Whirlwind+ killed before the next attack.
- Reason: Infested Prism KB says T3 Whirlwind is the main pressure turn and Vital Spark only refunds when attacks deal HP damage. Weak Potion reduced the T3 hit from 30 to 21, buying enough HP to keep Energy Potion for Kaiser Crab while Rupture scaling closed the fight.
- Reward decision: claimed Gambling Chip, Power Potion, 27 gold, and took Aggression over Stomp / Dismantle.
- Reward reason: Gambling Chip improves boss opening consistency, and Power Potion is a free setup option for Kaiser Crab. Aggression is the only reward that improves long boss scaling by recurring upgraded attacks; Stomp and a second Dismantle add damage but do not raise the deck's boss ceiling as much.

## Floor 31 - Shop

- Strategy files read: `GUIDE.md`, `history/run18_strategy.md`, `kb/strategies/card_impressions.md`, `kb/strategies/archetypes.md`.
- Entity KB read: `kb/cards/ironclad/feel_no_pain.md`, `kb/cards/ironclad/shrug_it_off.md`, `kb/cards/ironclad/colossus.md`, `kb/potions/power_potion.md`.
- Current HP/status: 50/84, 151 gold, Energy Potion, Power Potion.
- Decision: bought Feel No Pain for 77 gold and sale Shrug It Off for 25 gold; skipped Colossus, Block Potion, and removal.
- Reason: Feel No Pain completes the Dark Embrace/Second Wind/True Grit exhaust block engine before Kaiser Crab. Sale Shrug It Off adds cantrip block without weakening draw quality. Colossus is useful if a claw is Vulnerable, but buying it would block the discounted Shrug; Block Potion would require discarding a stronger boss potion; removal was unaffordable after the engine buy.

## Floor 32 - Rest Site

- Strategy files read: `GUIDE.md`, `history/run18_strategy.md`, `kb/enemies/bosses/kaiser_crab.md`.
- Entity KB read: `kb/relics/regal_pillow.md`, `kb/relics/gambling_chip.md`.
- Current HP/status: 50/84, 49 gold, Energy Potion, Power Potion.
- Decision: rested to 84/84.
- Reason: Smith targets were real, especially Aggression innate or Feel No Pain+, but Kaiser Crab is a high-damage boss and Regal Pillow converted Rest into a full heal. Full HP plus two boss potions is a stronger plan than entering at 50/84 with one additional upgrade.

## Floor 33 - Boss: Kaiser Crab Retry Note

- Strategy files read: `history/run18_strategy.md`, `kb/strategies/bosses.md`.
- Entity KB read: `kb/enemies/bosses/kaiser_crab.md`.
- Current HP/status: replay line reached round 9 at 16/84 with no potions; Rocket at 92 HP was attacking for 61 and the hand could neither kill it nor block.
- Mistake: played the boss too evenly and defensively after setup, leaving Rocket alive too long. The deck should prioritize exhaust to shrink quickly and cycle Bloodletting / Second Wind / key attacks, then kill Rocket first because Rocket is the dangerous claw.
- Correction plan: reload the boss, use Power Potion early as before, but mulligan and sequence for Dark Embrace / Feel No Pain / exhaust density and Rocket-focused damage. Save Energy Potion for a turn that extends exhaust/draw or converts into Rocket lethal, not merely generic setup.
