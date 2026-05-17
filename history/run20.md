# Run 20

- Date: 2026-05-15
- Character: Ironclad A10
- Outcome: In progress

## Required Reads

- Read `AGENTS.md`.
- Read `GUIDE.md`.
- Read every Markdown file in `kb/strategies/`: `_index.md`, `ironclad.md`, `pathing.md`, `archetypes.md`, `card_impressions.md`, `reward_choice.md`, `combat.md`, `elites.md`, `bosses.md`, and `meta_play.md`.

## Floor 1 - Neow

- Strategy file read: `GUIDE.md`, all files in `kb/strategies/`, especially `reward_choice.md`, `pathing.md`, and `meta_play.md`.
- Entity KB read: `kb/events/neow.md`, `kb/enemies/ancients/neow.md`, `kb/relics/new_leaf.md`, `kb/relics/lava_rock.md`, `kb/relics/precarious_shears.md`, `kb/cards/ironclad/breakthrough.md`.
- Current HP/status: 64/80, 99 gold, no potions, Burning Blood.
- Options: New Leaf transform 1 card; Lava Rock gives the Act 1 boss an extra relic; Precarious Shears removes 2 cards and takes 16 damage.
- Decision: choose New Leaf; transform a Strike into Breakthrough.
- Reason: Meta-play allowed inspecting the event branch. Breakthrough is a usable Act 1 AoE/frontload upgrade while preserving the full 64/80 starting HP. Precarious Shears would thin the deck but start at 48/80 with no new damage, and Lava Rock is delayed value with no help reaching Soul Fysh.
- Outcome: deck is starter Ironclad minus one Strike plus Breakthrough; relics Burning Blood and New Leaf.

## Floor 1 - Act 1 Route

- Strategy file read: `history/run20_strategy.md`, `kb/strategies/pathing.md`, `kb/strategies/bosses.md`, `kb/strategies/elites.md`.
- Entity KB read: `kb/enemies/bosses/soul_fysh.md`, `kb/enemies/elites/phantasmal_gardener.md`, `kb/enemies/elites/skulking_colony.md`, `kb/enemies/elites/terror_eel.md`.
- Current HP/status: 64/80, 99 gold, no potions; Act 1 boss is Soul Fysh.
- Options: left Monster into Unknown and early Shop; middle Monster into two Unknowns; right Monster with more early fights and possible Rest before elite but less early shop control.
- Decision: take the left Monster at (0,1).
- Reason: Soul Fysh shuffles Beckon statuses, so the deck wants early card quality, controlled exhaust, and potion/shop support. The left route gives an early fight for a card reward, an Unknown, an early Shop at 99+ gold, and later branches that can avoid excessive elite exposure while preserving rest access.

## Floor 2 - Toadpoles

- Strategy file read: `history/run20_strategy.md`, `kb/strategies/combat.md`, `kb/strategies/reward_choice.md`.
- Entity KB read: `kb/enemies/underdocks/toadpole.md`, `kb/potions/strength_potion.md`, `kb/cards/ironclad/perfected_strike.md`, `kb/cards/ironclad/breakthrough.md`, `kb/cards/ironclad/flame_barrier.md`.
- Current HP/status: entered 64/80, no potions; rewards resolved at 56/80, 110 gold, Strength Potion.
- Combat decision: Bash + Strike the attacking Toadpole on turn 1, then use Breakthrough to finish it and block the multi-hit turn.
- Reason: Toadpole KB says the weak encounter should kill the Whirl attacker first while the front Toadpole gains Thorns. Bash into Strike set up Breakthrough lethal on the attacker; Burning Blood made the planned early hit acceptable.
- Reward options: Perfected Strike, Breakthrough, Flame Barrier.
- Decision: take Perfected Strike; claim Strength Potion and 11 gold.
- Reason: Reward guidance prioritizes Act 1 frontload. Perfected Strike is a bridge attack and currently benefits from four remaining starter Strikes plus itself; the deck already has one Breakthrough for AoE, while Flame Barrier is good but does not solve the immediate damage check.

## Floor 3 - Drowning Beacon

- Strategy file read: `history/run20_strategy.md`, `kb/strategies/reward_choice.md`, `kb/strategies/pathing.md`.
- Entity KB read: `kb/events/drowning_beacon.md`, `kb/relics/fresnel_lens.md`, `kb/cards/enchants/nimble.md`, `kb/potions/glowwater_potion.md`.
- Current HP/status: 56/80, 110 gold, Strength Potion.
- Options: Bottle for Glowwater Potion; Climb for Fresnel Lens and lose 13 max HP.
- Decision: choose Bottle; claim Glowwater Potion.
- Reason: Glowwater gives immediate draw/burst equity for elites or Soul Fysh. Fresnel Lens is powerful only if future block cards arrive, and losing 13 max HP before the deck has a block package would reduce pathing safety too much.
- KB update: added a concise Drowning Beacon note that Bottle is safer before a block package exists.

## Floor 4 - Shop

- Strategy file read: `history/run20_strategy.md`, `kb/strategies/reward_choice.md`, `kb/strategies/archetypes.md`, `kb/strategies/card_impressions.md`.
- Entity KB read: `kb/cards/ironclad/pillage.md`, `kb/cards/ironclad/howl_from_beyond.md`, `kb/cards/ironclad/evil_eye.md`, `kb/cards/ironclad/forgotten_ritual.md`, `kb/cards/ironclad/juggling.md`, `kb/cards/colorless/dark_shackles.md`, `kb/cards/colorless/secret_weapon.md`, `kb/potions/power_potion.md`, `kb/potions/droplet_of_precognition.md`, `kb/relics/pantograph.md`.
- Current HP/status: 56/80, 110 gold, Strength Potion, Glowwater Potion.
- Shop highlights: Pillage 75, Howl from Beyond 77, Evil Eye 78, Forgotten Ritual 73, Juggling 39 sale, Dark Shackles 87, removal 100; relics unaffordable.
- Decision: buy Pillage for 75 gold.
- Reason: Pillage is the best fit for the current attack-dense Perfected Strike deck: it adds Act 1 damage and helps draw through attacks into key cards. Removal would weaken Perfected Strike too early, and the exhaust/block options are conditional without a reliable exhaust engine.

## Floor 5 - Seapunk

- Strategy file read: `history/run20_strategy.md`, `kb/strategies/combat.md`, `kb/strategies/reward_choice.md`.
- Entity KB read: `kb/enemies/underdocks/seapunk.md`, `kb/cards/ironclad/bully.md`, `kb/cards/ironclad/molten_fist.md`, `kb/cards/ironclad/body_slam.md`, `kb/potions/stable_serum.md`.
- Current HP/status: entered 56/80 with Strength Potion and Glowwater Potion; rewards resolved at 51/80, 49 gold, Stable Serum and Glowwater Potion.
- Combat decision: Bash + Defend turn 1, then Pillage + Strike + Defend turn 2. On the buff turn, use Strength Potion so Perfected Strike + Strike kills instead of leaving Seapunk at 1 HP before Bubble Burp.
- Reason: Seapunk cycles 13 attack, 2x4 attack, then 8 Block + 2 Strength. The Strength Potion prevented a bad breakpoint where Seapunk would gain block and force another attack cycle.
- Reward options: Bully, Molten Fist, Body Slam.
- Decision: take Molten Fist; claim Stable Serum and 14 gold.
- Reason: Molten Fist is immediate 1-energy frontload, exhausts itself, and doubles Bash Vulnerable for elite/boss burst. Bully needs larger Vulnerable stacks before it becomes more than filler, and Body Slam lacks a block shell.
- KB update: added a Seapunk note to avoid leaving it barely alive before Bubble Burp.

## Floor 5 - Route Choice

- Strategy file read: `history/run20_strategy.md`, `kb/strategies/pathing.md`, `kb/strategies/elites.md`.
- Entity KB read: `kb/enemies/elites/phantasmal_gardener.md`, `kb/enemies/elites/skulking_colony.md`, `kb/enemies/elites/terror_eel.md`.
- Current HP/status: 51/80, 49 gold, Stable Serum and Glowwater Potion.
- Options: Monster into low-gold Shop and then Elite; or Unknown with later choice between Shop/Unknown and Elite/Monster branches.
- Decision: take the Monster.
- Reason: The deck has enough frontload and two strong potions for an Act 1 elite, but still needs card quality before committing. A hallway reward is more valuable than an unknown event when the next shop is low value at 49 gold.

## Floor 6 - Sludge Spinner

- Strategy file read: `history/run20_strategy.md`, `kb/strategies/combat.md`, `kb/strategies/reward_choice.md`.
- Entity KB read: `kb/enemies/underdocks/sludge_spinner.md`, `kb/cards/ironclad/true_grit.md`, `kb/cards/ironclad/rage.md`, `kb/cards/ironclad/sword_boomerang.md`.
- Current HP/status: entered 51/80 with Stable Serum and Glowwater Potion; rewards resolved at 47/80, 64 gold, same potions.
- Combat decision: Bash into Molten Fist on turn 1, accepting the unblocked Oil Spray. Use the long Vulnerable window plus Pillage/Breakthrough/Strikes to kill on turn 2 before another cycle.
- Reason: Sludge Spinner always opens with Oil Spray and applies Weak. Bash plus Molten Fist put it to 18 HP with 4 Vulnerable, making the Weak turn still lethal after Pillage drew through the attack cluster.
- Reward options: True Grit, Rage, Sword Boomerang.
- Decision: take True Grit; claim 15 gold.
- Reason: True Grit fills the deck's block/exhaust hole, is a high-priority upgrade, and helps against Soul Fysh status pollution. Rage needs repeated attack turns or block payoff, and Sword Boomerang needs Strength/Vigor support.

## Floor 7 - Shop

- Strategy file read: `history/run20_strategy.md`, `kb/strategies/reward_choice.md`, `kb/strategies/archetypes.md`, `kb/strategies/card_impressions.md`.
- Entity KB read: `kb/cards/ironclad/battle_trance.md`, `kb/cards/ironclad/armaments.md`, `kb/cards/ironclad/twin_strike.md`, `kb/cards/ironclad/body_slam.md`, `kb/potions/attack_potion.md`, `kb/potions/block_potion.md`.
- Current HP/status: 47/80, 64 gold, Stable Serum and Glowwater Potion.
- Shop highlights: Battle Trance on sale for 38, Armaments 49, Twin Strike 48, Body Slam 50, Attack Potion 48, Block Potion 51; relics unaffordable.
- Decision: buy Battle Trance for 38 gold.
- Reason: The deck needs draw before the elite, and Battle Trance is a core draw enabler. Sequence Pillage or other draw before Battle Trance when the extra draw matters.

## Floor 8 - Phantasmal Gardeners

- Strategy file read: `history/run20_strategy.md`, `kb/strategies/combat.md`, `kb/strategies/elites.md`, `kb/strategies/meta_play.md`.
- Entity KB read: `kb/enemies/elites/phantasmal_gardener.md`, `kb/relics/red_mask.md`.
- Current HP/status: entered 47/80, 26 gold, Stable Serum and Glowwater Potion.
- Initial line: tried a more defensive opener with Breakthrough, Defend, and True Grit, then a Stable Serum turn to hold block. This failed to remove a Gardener quickly enough and left the fight at 23 HP facing 30 incoming.
- Retry line rejected: Breakthrough + Perfected Strike, then Bash + Molten Fist killed the Strength-buffer first, but the late turns spent both Glowwater Potion and Stable Serum and still exited near death.
- Final decision: retry for a resource-preserving kill. Open with Breakthrough + Perfected Strike on the buffing Gardener; turn 2 Bash + Molten Fist killed it. Use Glowwater Potion only when a three-Strike hand would otherwise take heavy damage, then block with Defend + True Grit and finish with Perfected Strike/Breakthrough.
- Outcome: won at 15/80 after Burning Blood, preserved Stable Serum, gained Red Mask and 28 gold.
- Reason: `meta_play.md` now treats "won, but barely" as a retry signal when a line spends too many potions or exits at dangerous HP. The accepted line was materially better because it saved Stable Serum for Soul Fysh or a bad hallway while avoiding a 5 HP exit.
- KB updates: added Phantasmal Gardener and meta-play notes about retrying lines that technically win but consume future pathing equity.

## Floor 8 - Elite Card Reward

- Strategy file read: `history/run20_strategy.md`, `kb/strategies/reward_choice.md`, `kb/strategies/card_impressions.md`, `kb/strategies/archetypes.md`.
- Entity KB read: `kb/cards/ironclad/iron_wave.md`, `kb/cards/ironclad/vicious.md`, `kb/cards/ironclad/evil_eye.md`.
- Current HP/status: 15/80, 54 gold, Stable Serum; relics Burning Blood, New Leaf, Red Mask.
- Options: Iron Wave, Vicious, Evil Eye.
- Decision: take Evil Eye.
- Reason: the deck's immediate problem is block density at low HP. Evil Eye is 8 block at baseline and can become 16 block after True Grit or Molten Fist exhausts a card. Vicious has future Vulnerable/draw upside, but current support is too thin and does not solve the next-fight survival check.

## Floor 8 - Route Choice

- Strategy file read: `history/run20_strategy.md`, `kb/strategies/pathing.md`.
- Entity KB read: visible boss/elite notes already read this act: `kb/enemies/bosses/soul_fysh.md`, `kb/enemies/elites/phantasmal_gardener.md`, `kb/enemies/elites/skulking_colony.md`, `kb/enemies/elites/terror_eel.md`.
- Current HP/status: 15/80, 54 gold, Stable Serum.
- Options: Monster into Treasure/Elite chain, or immediate RestSite.
- Decision: take the immediate RestSite.
- Reason: pathing rules say below 20% HP after a fight means immediate rest site. The monster route risks dying before recovery and would force another elite later.

## Floor 9 - Rest Site

- Strategy file read: `history/run20_strategy.md`, `kb/strategies/pathing.md`, `kb/strategies/card_impressions.md`.
- Entity KB read: `kb/cards/ironclad/true_grit.md`, `kb/cards/ironclad/evil_eye.md`.
- Current HP/status: 15/80, 54 gold, Stable Serum.
- Options: Rest to heal 24, or Smith a key card such as True Grit.
- Decision: Rest.
- Reason: True Grit upgrade is high value, but 15 HP before multiple Act 1 rooms and Soul Fysh is an emergency state. Resting to 39/80 restores pathing safety and lets Red Mask/Burning Blood stabilize future hallways.
- Outcome: 39/80 HP.

## Floor 9 - Route Choice

- Strategy file read: `history/run20_strategy.md`, `kb/strategies/pathing.md`.
- Entity KB read: `kb/enemies/bosses/soul_fysh.md`.
- Current HP/status: 39/80, 54 gold, Stable Serum.
- Options: left Treasure into forced Elite; right Treasure into RestSite.
- Decision: take the right Treasure.
- Reason: both branches give a chest, but the left branch forces another elite while the right branch reaches a rest site immediately. At 39 HP after a costly elite, rest access is worth more than extra relic pressure.

## Floor 10 - Treasure

- Strategy file read: `history/run20_strategy.md`, `kb/strategies/pathing.md`.
- Entity KB read: `kb/relics/pendulum.md`.
- Current HP/status: 39/80, 85 gold, Stable Serum.
- Reward: Pendulum.
- Decision: claim Pendulum.
- Reason: periodic draw supports the Battle Trance/Pillage plan and helps cycle through Soul Fysh statuses in a medium deck.

## Floor 10 - Route Choice

- Strategy file read: `history/run20_strategy.md`, `kb/strategies/pathing.md`, `kb/strategies/elites.md`.
- Entity KB read: `kb/enemies/elites/phantasmal_gardener.md`, `kb/enemies/elites/skulking_colony.md`, `kb/enemies/elites/terror_eel.md`.
- Current HP/status: 39/80, 85 gold, Stable Serum.
- Options: only RestSite, followed by a forced Elite.
- Decision: take the RestSite.
- Reason: route is forced, but this confirms the next fire must be evaluated as pre-elite prep rather than a normal upgrade opportunity.

## Floor 11 - Rest Site

- Strategy file read: `history/run20_strategy.md`, `kb/strategies/pathing.md`, `kb/strategies/elites.md`, `kb/strategies/card_impressions.md`.
- Entity KB read: `kb/cards/ironclad/true_grit.md`, `kb/enemies/elites/phantasmal_gardener.md`, `kb/enemies/elites/skulking_colony.md`, `kb/enemies/elites/terror_eel.md`.
- Current HP/status: 39/80, 85 gold, Stable Serum; forced elite next.
- Options: Rest to 63/80, or Smith True Grit for controlled exhaust.
- Decision: Rest.
- Reason: the next node is a forced elite and pathing rules rest below about 60% HP before elites. True Grit+ is valuable, but entering a forced elite at 39/80 after the previous elite nearly killed the run would be too fragile.
- Outcome: 63/80 HP.
