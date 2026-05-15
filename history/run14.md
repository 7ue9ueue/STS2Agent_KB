# Run 14 - Ironclad A10

- Date: 2026-04-30
- Character: Ironclad
- Ascension: 10
- Outcome: Loss
- Floor reached: 5

## Decisions

- Pre-run setup: Mandatory strategy files were read immediately before this fresh start: `kb/strategies/_index.md`, `kb/strategies/ironclad.md`, `kb/strategies/pathing.md`, `kb/strategies/archetypes.md`, and `kb/strategies/card_impressions.md`. Carryovers: prioritize safe pathing/rest access, early controlled fights, potion preservation for elites/bosses, Akabeko-style first-attack sequencing if relevant, and avoid conditionally dead Neow rare cards without enabling support.
- F1 Neow: Offered Arcane Scroll, Lost Coffer, and Leafy Poultice. Read `kb/relics/arcane_scroll.md`, `kb/relics/leafy_poultice.md`, and created missing `kb/relics/lost_coffer.md` from live text. Pick Lost Coffer because it gives an immediate card reward plus potion with no HP loss, curse, or random rare variance; Arcane Scroll can hit dead rares, and Leafy Poultice loses 12 Max HP despite improving starter cards.
- F1 Lost Coffer reward: Claimed card reward before potion to avoid reward index shifting. Offered Anger, Molten Fist, Sword Boomerang. Read `kb/cards/ironclad/anger.md`, `kb/cards/ironclad/molten_fist.md`, `kb/cards/ironclad/sword_boomerang.md`, and prior `kb/strategies/card_impressions.md`. Picked Molten Fist because it is immediate 10 damage, exhausts after use, and doubles Bash Vulnerable; Anger risks copy-bloat and Sword Boomerang is only 9 random damage without Akabeko/Strength. Claimed Dexterity Potion and should save it for elite/boss or a severe hallway block turn.
- F1 pathing: Read `kb/strategies/pathing.md`, `kb/strategies/bosses.md`, `kb/enemies/bosses/soul_fysh.md`, and `kb/strategies/elites.md`. Soul Fysh adds Beckon status cards and has Fade/Intangible, so the run wants early card growth plus controlled exhaust. Chose the central Monster at col4 because it preserves early fights, a shop branch, and a Rest Site immediately after the first optional elite; the far-left path reaches an elite before any nearby rest.
- F2 Seapunk: Read `kb/enemies/underdocks/seapunk.md`; it cycles Sea Kick 13, Spinning Kick 2x4, then Block + Strength. Used Bash before Molten Fist to get 15 damage and extend Vulnerable, blocked once on the multi-hit turn, spent no potion, and ended at 59/80 after Burning Blood. Reread `AGENTS.md` after combat as requested.
- F2 rewards: Created missing `kb/potions/liquid_bronze.md` from live reward text. Card reward offered Battle Trance, Havoc, Pillage; read `kb/strategies/card_impressions.md` plus all three card KBs. Pick Battle Trance because it is premium 0-cost draw for consistency and Soul Fysh status-clog, while Havoc is random exhaust and Pillage is less reliable in a starter deck with many Skills.
- F2 pathing: Took the Monster branch over the early Shop. `kb/strategies/pathing.md` says the first three hallway combats are usually controlled reward nodes; 59/80 HP plus two saved potions is enough to seek another card reward before spending 107 gold.
- F3 Sludge Spinner: Read `kb/enemies/underdocks/sludge_spinner.md`; it always opens Oil Spray for 9 + 1 Weak, then random non-repeat moves. Frontloaded Strike + Molten Fist + Strike on turn 1 to reduce the fight before Weak, then used Battle Trance into Bash + Defend to set up a Vulnerable kill. Took 16 combat damage, healed 6, spent no potion, ended 49/80.
- F3 reward: Offered Shrug It Off, Headbutt, True Grit. Read `kb/cards/ironclad/shrug_it_off.md`, `kb/cards/ironclad/headbutt.md`, `kb/cards/ironclad/true_grit.md`, and `kb/strategies/card_impressions.md`. Pick Shrug It Off because it gives immediate block + draw before the first campfire; True Grit+ is strong Soul Fysh tech, but the base version randomly exhausts before it can be upgraded.
- F4 Corpse Slugs: Read `kb/enemies/underdocks/corpse_slug.md` and updated its notes because live A10 Ravenous is 5 Strength, not the older A0 note of 4. Focused the attacking Slug first, killed it on turn 2 to stun the survivor, and saved both potions. Difficulty: the potion-preserving line was costly; survivor Ravenous 5 created 8x2 and 14-damage turns, ending at 35/80 after Burning Blood.
- F4 reward: Offered Sword Boomerang, Body Slam, Blood Wall. Read `kb/cards/ironclad/sword_boomerang.md`, `kb/cards/ironclad/body_slam.md`, `kb/cards/ironclad/blood_wall.md`, and `kb/strategies/card_impressions.md`. Pick Blood Wall as a one-card 16 Block answer before possible elites; Body Slam is only payoff without enough block density, and Sword Boomerang lacks Akabeko/Strength support.
- F4 pathing: At 35/80 HP, chose the right Monster path toward the row5 Shop instead of the left route that can push into the row6 elite. This follows `kb/strategies/pathing.md`: avoid optional elites when HP/pathing answers are weak, and use shops around 100+ gold for recovery, removal, or answers.
- F5 Cultists: Read `kb/enemies/underdocks/cultists.md`. Focused Calcified first per KB and used Battle Trance to line up Bash + Molten Fist for the kill. Damp Cultist was left unchecked too long and reached 21/27/33 damage. Used Dexterity Potion and Liquid Bronze once the 27-damage turn became lethal, but it was too late; the final line left Damp at 3 HP and lethal damage ended the run before Thorns could rescue it. Updated `kb/potions/liquid_bronze.md` and `kb/enemies/underdocks/cultists.md`.

## Post-Run Reflection

- Steam run log: `history/1777579280.run`; `win: false`, `was_abandoned: false`, `killed_by_encounter: ENCOUNTER.CULTISTS_NORMAL`, `killed_by_event: NONE.NONE`.
- What worked: Lost Coffer into Molten Fist gave usable early damage, Battle Trance was good, and Blood Wall did stabilize one large Damp attack.
- What cost the run: potion preservation was too rigid in a hallway that had become lethal. Dexterity/Liquid Bronze should have been used earlier in Cultists, before Damp reached 24+ Strength. F4 Corpse Slugs also cost too much HP because the line accepted repeated Ravenous-scaled attacks.
- Next change: in Cultists, treat Damp's +6 Ritual as the urgent clock if Calcified cannot die immediately; use burst/potions before the 21-damage turn, not after. Do not rely on Thorns to win after a lethal hit.

## Current State

- Died on floor 5 to `ENCOUNTER.CULTISTS_NORMAL` with 124 gold, no potions, relics: Burning Blood, Lost Coffer. Deck additions: Molten Fist, Battle Trance, Shrug It Off, Blood Wall.
