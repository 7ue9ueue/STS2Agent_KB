# STS2 MCP — AI Gameplay Guide

## MCP Tool Calling Tips

### State Polling
- After `combat_end_turn`, the state may show `is_play_phase: false` or `turn: enemy`. Call `get_game_state` again to advance to the next player turn.
- Sometimes you need to call `get_game_state` twice — once to see enemy turn results, once to see your new hand.
- Use `format: "json"` during combat for structured data; `format: "markdown"` for map/event overview.
- During combat, play **one card or action at a time**, wait about 1-1.5 seconds, then re-read state before the next move. Do not chain card plays, potion use, selections, and end-turn in one shell command; the harness can race overlays, delayed damage, and index shifts.
- Treat the live hand after each draw/shuffle as authoritative. Draw-pile previews can become stale after Battle Trance, Scrawl, reshuffles, generated cards, or selection overlays.
- After a final boss dies, the game can show a post-boss event such as `The Architect` with no options. Confirm the run result from the newest Steam `history/*.run` log before writing the final outcome.

### Menu Navigation (no MCP tool — use HTTP API directly)
The `menu_select` action is NOT exposed as a deferred MCP tool in this harness. To navigate the main menu, character select, or return from game-over, POST directly to the HTTP API at `localhost:15526`:

```bash
curl -s -X POST http://localhost:15526/api/v1/singleplayer \
  -H "Content-Type: application/json" \
  -d '{"action":"menu_select","option":"<OPTION>"}'
```

Standard run-start sequence from main menu:
1. `option:"singleplayer"` → singleplayer submenu
2. `option:"standard"` → character select
3. `option:"IRONCLAD"` (or `SILENT`, `REGENT`, `NECROBINDER`, `DEFECT`) → highlight character
4. `option:"embark"` → start the run

Game-over screen: `option:"main_menu"` to return to the main menu.

### Save and Quit
Use `save_and_quit()` or POST `{"action":"save_and_quit"}` to save the current singleplayer run through the game's pause-menu Save and Quit flow and return to the main menu. If the response says the pause menu was opened, wait about 1 second and call it again.

### Save and Load Strategy
- Use `save_and_quit` + main-menu `continue` as a current-room restart tool, not just in combat. It can reset combat turns, reward choices, events, shops, rest sites, and other room decisions back to the saved room start; mid-room changes are not persisted.
- RNG is deterministic: the same action sequence gives the same draws, generated cards, targets, and results. Retry only materially different lines that change the sequence before the random event.
- After `continue`, poll until state stabilizes; a brief `state_type: unknown` can appear during reload.
- Limit retries to a few distinct lines, usually 3-5. If none meet the survival/lethal/resource target, stop retrying, record that it is not achievable, and play the best available line or accept the loss.
- After combat, record Save and Load lessons: reusable, action-oriented fixes go in the relevant entity KB Strategy Notes; exact retry lines and run context go in `history/run<N>.md`.

### Abandoning a Run
There is no `abandon` action for singleplayer. To end a run early, **die in combat**: call `combat_end_turn` repeatedly without blocking until HP hits 0, then `state_type` becomes `game_over` and you can `menu_select` with `main_menu`.

### Card Index Shifting
- **CRITICAL**: Playing a card removes it from hand and shifts all indices. Play cards from RIGHT to LEFT (highest index first) to keep lower indices stable, or re-check state between plays.
- When targeting, always provide `target` for single-target cards. Entity IDs are UPPER_SNAKE_CASE with a `_0` suffix (e.g. `KIN_PRIEST_0`).
- Even when playing right-to-left, re-check state after each move if the card can transform cards, draw cards, exhaust cards, open a selection overlay, or apply delayed effects.

### Event, Rest, Reward, and Selection Flow
- Events: use direct HTTP action `choose_event_option` with `index`. After choosing, there is often a "Proceed" option at index 0.
- Rest sites: use `choose_rest_option`; if a smith/removal/upgrade screen opens, use `select_card` with `index`, then `confirm_selection`.
- Rewards: use `claim_reward` with `index`, claimed from right-to-left (highest index first) to avoid index shifting.
- Card rewards open a sub-screen; use `select_card_reward` with `card_index`, or `skip_card_reward`.
- Treasure chests use `claim_treasure_relic`, not `claim_reward`.
- Selection screens are not interchangeable with reward screens. Re-read state before choosing whether the action expects `index`, `card_index`, or a potion `slot`.

### Crystal Sphere Event
- Stop playing when this event occurs — MCP cannot exit it.

### Potions
- `use_potion(slot=N)` — slot is the potion slot index, not a card index.
- `discard_potion(slot=N)` — discard a potion to free up the slot when full.
- Potions don't cost energy or count as card plays. Use buff potions BEFORE playing cards.
- Compare potions by the fight plan, not by generic strength. Gigantification-style triple damage can beat Flex Potion when the deck has a large single Attack, Music Box copy, Vulnerable, or a phase-skip target.

---

## Knowledge Base (`kb/`)

The `kb/` directory contains one Markdown file per game entity, scraped from the STS2 wiki. It is scoped to **Ironclad runs only**: Ironclad + Colorless cards, all relics except other-class exclusives, and all enemies/events/potions/mechanics.

### Directory layout

```
kb/
├── cards/
│   ├── ironclad/      # one .md per Ironclad card (e.g. anger.md, bash.md)
│   ├── colorless/     # Colorless cards (apotheosis.md, alchemize.md …)
│   └── status/        # Curse and Status cards (wound.md, burn.md …)
├── relics/            # one .md per qualifying relic
├── potions/           # one .md per potion
├── enemies/
│   ├── overgrowth/    # Act 1 regular enemies
│   ├── underdocks/    # Act 1 regular enemies
│   ├── hive/          # Act 2 regular enemies
│   ├── glory/         # Act 3 regular enemies
│   ├── elites/        # Elite enemies (all acts)
│   ├── bosses/        # Act bosses
│   └── ancients/      # Ancient encounter NPCs (Neow, Orobas …)
├── events/            # one .md per event
├── potions/           # one .md per potion
├── strategies/        # fast lookup summaries that link to canonical notes
└── mechanics/         # keywords.md, buffs.md, debuffs.md, acts.md …
```

### File format

Every file has YAML frontmatter (title, source URL, stub flag, category-specific fields) followed by Markdown sections. The **source** field links to the wiki page so numbers can be verified by hand.

**Stub flag**: pages the wiki marks incomplete have `stub: true` in frontmatter. Find all stubs with:
```bash
rg 'stub: true' kb/
```

**Reserved strategy section**: every file ends with a `## Strategy Notes` section below a `<!-- META-AGENT NOTES -->` divider. The wiki facts live above the divider; the meta-agent appends lessons and heuristics below it. Never write wiki data below the divider.

### Typical lookup patterns

```bash
# Card stats
view kb/cards/ironclad/anger.md

# All Ironclad uncommon cards
rg 'rarity: Uncommon' kb/cards/ironclad/

# Enemy HP for Act 2
rg 'HP' kb/enemies/underdocks/

# Boss attacks
view kb/enemies/bosses/kaiser_crab.md

# Event choices
view kb/events/abyssal_baths.md

# A specific relic
view kb/relics/burning_blood.md

# All stubs (incomplete wiki pages) but still contains detailed information
rg 'stub: true' kb/

# Keywords / mechanics reference
view kb/mechanics/keywords.md
view kb/mechanics/buffs.md
```

### Reading KB Files Before Decisions

Do not make card, shop, pathing, elite, boss, rest-site, event, or relic decisions from memory. If a relevant `kb/strategies/` file exists, read it first and cite it in the run history before acting.

### Mandatory Strategy Reads

Before every run:
- Read `GUIDE.md`
- Read every Markdown file in `kb/strategies/` before starting, including `_index.md` and all strategy playbooks.

Before choosing a map route:
- Read `kb/strategies/pathing.md`
- Check rest-site/campfire access, first-three-combat safety, question-mark alternatives, elite risk, and next recovery point.

Before pathing into an elite:
- Read `kb/strategies/elites.md`
- Read the relevant elite KB files for the act.

At the start of each act:
- Read `kb/strategies/bosses.md`
- Read the visible boss KB file.

Before editing deck:
- Read `GUIDE.md`
- Read `kb/strategies/archetypes.md`
- Read `kb/strategies/card_impressions.md`
- Read `kb/strategies/ironclad.md`
- Read specific KB files for unfamiliar cards, close choices, or cards that match/contradict the current deck template.

For every major decision, explicitly write in `history/run<N>.md`:
- Strategy file read
- Entity KB file read
- Current HP and status
- Decision
- Reason

Before each significant encounter or choice, look up the relevant file:
- **Enemy encounters**: Read `kb/enemies/<act>/<enemy>.md` before elite and boss fights and during fights. Check Attacks, Pattern, and Strategy Notes.
- **Card rewards**: Check `kb/cards/<class>/<card>.md` for unfamiliar cards before taking or skipping.
- **Relic picks**: Check `kb/relics/<relic>.md` to understand what you're choosing between.
- **Events**: Check `kb/events/<event>.md` to evaluate options before committing.
- **Mechanics / keywords**: Unfamiliar keyword or buff/debuff → check `kb/mechanics/`.
- **Boss-generated status cards**: If a boss adds special cards (for example Frantic Escape), read the status-card KB as well as the boss KB; card cost changes and per-copy behavior can be more important than incoming damage.

When making decisions, explicitly cite what you read: "The Terror Eel kb says Screech fires at 70 HP and applies 99 Vulnerable — I need to kill it within 2 turns after the stun."

### Writing Agent Notes to KB Files

KB maintenance is mandatory during play, not optional cleanup. When a run encounters a new card, relic, potion, enemy, event, boss, mechanic, or other named entity that does not have a KB file yet, create a new KB entry in the appropriate `kb/` subdirectory before relying on memory for future decisions. Use the existing file format when possible: YAML frontmatter, factual notes/source if known, `<!-- META-AGENT NOTES -->`, and a `## Strategy Notes` section.

If a strategy, warning, mechanic quirk, target order, card interaction, pickup rule, or pathing implication is discovered about a named entity, add a concise note to that entity's `## Strategy Notes` section immediately after the combat/choice where it was learned. Do not leave it only in `history/`.

### In-Game Reflection Checkpoints

During a run, pause briefly after each combat, event, shop, rest site, elite, boss, and major card/relic choice to reflect before continuing:
- Did anything behave differently than expected from the KB?
- Did a card, relic, potion, enemy, event, or mechanic reveal a useful strategy or warning?
- Did the decision expose a reusable pathing, deck-building, target-order, or combat-sequencing lesson?
- Is there a missing KB file for a named entity encountered this floor?

If yes, update the relevant KB file immediately with a concise `## Strategy Notes` bullet, then record the run-specific details in `history/run<N>.md`. Do not wait until the end of the run if the lesson could affect later decisions in the same run.

After encounters, append **concise** learnings to the `## Strategy Notes` section (below the `<!-- META-AGENT NOTES -->` divider). Never edit wiki content above the divider. Keep it to 1–3 bullets of key facts — no narrative, no run context. Should be brief and bullet points. 

Good note: `- Kill within 2 turns after Screech; Vigor + player Vulnerable makes turns 3+ unsurvivable at low HP.`
Bad note: `- In my run I entered at 17 HP and died because the Eel had 5 HP left and I couldn't finish it.`

Detailed run analysis (what happened, what failed, lessons) goes in `history/` — not in kb files.
If the kb is incorrect / missing for a fact that you encounter, add / correct it. Note both what worked well and what didn't work.

### Where Each Kind of Note Belongs

| Topic | Goes in |
|---|---|
| Card-specific behavior, warnings, mechanic quirks (e.g. "Drum of Battle exhausts top draw card") | `kb/cards/<class>/<card>.md` Strategy Notes |
| Card pick rates, upgrade rates, per-card synergy partners | `kb/cards/<class>/<card>.md` Strategy Notes |
| Per-relic warnings or stat anomalies | `kb/relics/<relic>.md` Strategy Notes |
| Per-enemy patterns, tactical responses | `kb/enemies/<act>/<enemy>.md` Strategy Notes |
| Per-event option ratings | `kb/events/<event>.md` Strategy Notes |
| Cross-entity quick lookup summaries | `kb/strategies/` |
| Hero-level archetypes, deck-building shape, HP curves, pathing rules | `GUIDE.md` |
| Run-by-run play-throughs, post-mortems, data analyses | `history/` |

**Rule**: if a note is about a single named entity (one card, one relic, one enemy), it belongs in that entity's KB file. `GUIDE.md` should reference the KB by name and stay strategic-shape only. `kb/strategies/` is a fast lookup/index layer and should link back to canonical files rather than becoming the only home for detailed lessons.

### In-Run Strategy File (`history/run<N>_strategy.md`)

Each run also has a **live strategy file** at `history/run<N>_strategy.md` (same `<N>` as the decision log). Unlike `history/run<N>.md` (append-only post-decision log) and `kb/` (persistent facts across runs), this file is the agent's **working memory for the current run only** — sections are overwritten as the plan evolves.

**Create it on Floor 1** (after Neow), and **update it after every major decision**: card pick/skip, relic, elite/boss kill, shop, event, rest site, and any time the deck plan shifts. If a section is no longer true, replace it — do not accumulate stale plans.

Required sections (keep each to a few bullets, no narrative):

```markdown
# Run <N> Strategy — <Character> A<Ascension>

## Snapshot
- Floor: <act>-<floor> | HP: <cur>/<max> | Gold: <g> | Potions: <list>
- Act boss: <name> (key threats)

## Archetype Plan
- Primary: <e.g. Strength scaling, Exhaust, Block-pivot>
- Backup pivot: <e.g. switch to Exhaust if no Strength by F8>

## Deck Shape
- Core synergy cards: <list>
- Holes / needs: <e.g. block, AoE, draw, removal>
- Cards to remove next: <if any>

## Threat Watch
- <Boss/elite/hallway threat>: 
- <Future-act threat>: 

## Potion / Relic Plan
- Save: <potion> for <when>
- Use freely: <potion>
- Key relic interactions: 

## Open Questions
- <Decision pending next reward/shop>
```

**Read this file at the start of every decision** alongside the relevant `kb/` files. It is the answer to "what am I trying to do in this run?" — if it disagrees with a card pick, either change the pick or change the plan and write down why.

After the run ends, the strategy file's final state is a useful artifact for the post-run reflection in `history/run<N>.md`; do not delete it.

### Run History (`history/`)

During each run (win or loss) after making each decision, write or update a summary in `history/` as `history/run<N>.md`, where `<N>` is the next unused global run number. Do not reset numbering by date or character, and do not put the current floor in the filename; record date, character, and floor reached inside the file. Include:
- Run outcome, character, floor reached
- Key decisions such as card picks at each floor
- What killed the run or enabled the win
- Tactical lessons to carry forward

This is where detailed combat breakdowns belong — not in kb files or GUIDE.md. Don't modify GUIDE.md unless an important strategy is discovered. GUIDE.md should include bullet points that is important about the game mechanism. 

### Run Analysis (`analysis/`)

The `analysis/` directory contains aggregate Ironclad A10 run analysis generated from `runs/data/*.json`.

Key files:
- `analysis/ironclad_a10_win_analysis.md` — human-readable summary of the current win corpus.
- `analysis/run_summary.csv` — one row per run, including exact final deck size and visible deck-growth estimates.
- `analysis/act_summary.csv` — visible card additions, estimated deck size after each act, act damage, turns, elites, rests, smiths, heals.
- `analysis/card_pick_timing.csv` — visible card picks by act/floor/source.
- `analysis/final_deck_card_frequency.csv` — exact final deck card frequencies and upgrade rates.
- `analysis/smith_targets.csv` — cards most often upgraded at campfires.
- `analysis/encounter_summary.csv` — encounter damage/turns across the run set.

Current interpretation rules:
- The corpus is win-biased until failing runs are fetched. Treat it as "what winning decks looked like", not causal win-rate proof.
- Exact final deck size is reliable. Deck size after each act is a visible-growth estimate: starter deck size plus cards shown in floor rewards. The static site does not fully expose shop/event buys, transforms, or removals.
- Use act pacing as a draft guide: winning A10 runs add about 7.8 visible cards in Act 1, 5.6 in Act 2, and 3.6 in Act 3. Build early, refine late.
- Campfire default is Smith. In the 161-win corpus, smith share is 75.0% in Act 1, 67.1% in Act 2, and 66.8% in Act 3; heal when HP/pathing risk demands it.
- Rebuild analysis after adding new runs with:
```bash
.venv/bin/python analysis/generate_ironclad_win_analysis.py
```

### Rebuilding the KB

Run `scripts/build_kb_wiki.py` from the repo root to refresh all files. Re-runs are idempotent — only changed content is re-written.

```bash
# Full rebuild (requires: pip install beautifulsoup4 requests)
python3 scripts/build_kb_wiki.py

# Single category only
python3 scripts/build_kb_wiki.py --only cards

# Dry-run (no writes)
python3 scripts/build_kb_wiki.py --dry-run
```

### Detailed Run History Reflection

Path: /Users/tonywu/Library/Application Support/Steam/userdata/1407082853/2868840/remote/modded/profile1/saves
After each combat, read the markdown notes in the history folder, and find the corresponding run log in the path above. Analyse choicing and append the analysis to the end of the markdown note, GUIDE.md, and kb. Consider what improvements could be made and what are some mistakes that could be prevented. Also note what went well. Also record the harnessing and gameplay that is worth noting. 

After a run ends, inspect the newest `.run` file under the Steam save `history/` directory and record whether it has `win: true`, `was_abandoned`, and any `killed_by_*` fields. Add a short post-run reflection to the local `history/run<N>.md` that answers:
- What worked well enough to repeat?
- What cost avoidable HP, potions, or pathing equity?
- What would change in the next run with the same information?
- Which mechanic or harness fact was unknown at the start and should be promoted into `GUIDE.md`, `AGENTS.md`, or entity-specific KB notes?

Keep the split clean: detailed run narrative belongs in `history/`; general Ironclad rules and pathing heuristics belong in `GUIDE.md`; named card/relic/enemy/event facts belong in that entity's KB file.
