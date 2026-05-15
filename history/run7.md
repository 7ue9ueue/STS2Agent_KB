# Ironclad Manual Run - 2026-04-29 20:09

- Controller: Codex via direct STS2 MCP HTTP API calls; no controller bot/script.
- Strategy source: AGENTS.md, GUIDE.md, and per-choice KB lookups.
- Goal: aim to win, log decisions, and append concise reflections.

- F1 A1: Neow offered Precise Scissors, Stone Humidifier, and Cursed Pearl. Neow KB lists Precise Scissors as a positive-pool remove-1 relic; Greed KB says Cursed Pearl adds an Unplayable Eternal curse. Took Precise Scissors.
- F1 A1: Removed Strike with Precise Scissors to reduce starter-deck filler while keeping four Defends for early block.
- F1 A1: Boss is Ceremonial Beast. Chose middle path for two early combats into possible elite with downstream rest access, matching GUIDE Act 1 build-and-fight priority.
- F2 A1: Slimes fight. Slimes KB says small Twig attacks every turn and medium Twig follows opening Slimed with possible 11-damage Chomp. Killed small Twig first, used Bash/Vulnerable to burst medium Twig, ended at 72/80 after Burning Blood.
- F2 A1: Card reward was Dominate / Tremble / Breakthrough. Dominate KB is Vul-to-Strength scaling and Tremble KB is common Vul setup, but Breakthrough KB gives 1-cost 9 AoE; picked Breakthrough for immediate Act 1 damage.
- F3 A1: Nibbit fight. Nibbit KB says solo Nibbit opens with 12, then 6+Block, then Strength. Took the Bash/Strike tempo line, used Breakthrough under Vulnerable, and ended at 59/80 after Burning Blood.
- F3 A1: Card reward was Infernal Blade / Howl from Beyond / Blood Wall. Howl KB warns it does not exhaust from hand; Blood Wall KB says it is large base block for elite/boss turns. Picked Blood Wall.
- F3 A1: Took Potion of Binding and 12 gold. Chose left path toward Monster -> Unknown -> Elite; HP 59/80 plus Blood Wall and Binding potion is enough to contest the elite, while Unknown may reduce pre-elite damage.
- F4 A1: Fuzzy Wurm Crawler. KB says it cycles 4 attack -> +7 Strength -> 11 attack, so frontloaded Bash/Breakthrough, attacked through the buff turn, then blocked the scaled hit. Ended at 59/80 after Burning Blood.
- F4 A1: Card reward was Havoc / Flame Barrier / Howl from Beyond. Havoc is uncontrolled exhaust and Howl still lacks exhaust support; Flame Barrier KB calls it an Act 1 hard block answer for elites/low HP. Picked Flame Barrier.
- F5 A1: Snapping Jaxfruit + Slithering Strangler. KB says Jaxfruit gains Strength every turn and Strangler opens with Constrict, then attack/Constrict pattern. Killed Jaxfruit first but allowed Constrict to stack to 6; fight ended at 29/80 after Burning Blood. Reflection: against Strangler, prioritize killing it sooner if Constrict starts stacking, even when a scaling side enemy is present.
- F5 A1: Card reward was Armaments / Hemokinesis / Pyre. Pyre is strong but slow at 29 HP; Hemokinesis adds HP loss. Armaments KB says it is a high-upgrade hand-quality tool, so picked Armaments.
- F5 A1: Claimed Power Potion, 17 gold. Next path is forced Unknown into forced Elite at 29/80; only continue if event improves survival or does not cost HP.
- F6 A1: Unknown became combat: Snapping Jaxfruit + Flyconid. Used Potion of Binding and Power Potion; Power Potion offered Rupture / Unmovable / Barricade, chose Unmovable for doubled Blood Wall/Flame Barrier/Armaments block. Harness note: queued card plays during the Power Potion card-select overlay were discarded without dealing damage; avoid sending combat card actions while an overlay is open.

## Outcome

- Loss: died on F6 A1 to Snapping Jaxfruit + Flyconid before the forced elite.
- Final deck: 4 Strike, 4 Defend, Bash, Breakthrough, Blood Wall, Flame Barrier, Armaments.
- Final relics: Burning Blood, Precise Scissors.
- Save run log: `1777489813.run`; it records `killed_by_encounter: ENCOUNTER.SNAPPING_JAXFRUIT_NORMAL`, `win: false`, and 6 map floors.

## Reflection

- Main strategic error: the path committed to a forced elite while already down to 29/80 and then hit a hard Unknown combat. At sub-40% HP, treat Unknown-before-elite as a combat risk, not a safety valve.
- Tactical error: in the F5 Strangler fight, Constrict stacked to 6. Kill Slithering Strangler sooner when it has applied Constrict; the drain can outpace Burning Blood and make the next node unsafe.
- Harness error: after Power Potion opens a card-select overlay, do not queue normal card plays or end turn. Select the generated card, re-read state, then explicitly play the generated card if desired.
