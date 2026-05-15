Play Slay the Spire 2 using the MCP tools (`mcp__sts2__*`). Your goal is to play as well as possible and win the run.

## Setup
1. Read `AGENTS.md` for general strategy and MCP calling tips.
2. Read `GUIDE.md` for hero-specific strategies. If the current hero isn't covered, adapt and add notes after boss fights.
3. Call `get_game_state(format="markdown")` to see the current state and begin playing.
4. **Create `history/run<N>_strategy.md` after Neow** as your live in-run memory (archetype plan, deck holes, threat watch, potion plan, open questions). Update it after every major decision; read it before every decision. See `AGENTS.md` → "In-Run Strategy File" for the required sections. This is the working memory for THIS run — distinct from `kb/` (persistent facts) and `history/run<N>.md` (append-only decision log).

## Gameplay Loop
- **Map**: Evaluate paths. Prefer elites when healthy, rest sites before bosses.
- **Combat**: Read intents. Sequence cards optimally (setup → skills → attacks). Play from right-to-left indices when possible to avoid index shift bugs.
- **Events**: Evaluate options based on current HP, gold, and deck needs.
- **Rewards**: Skip cards that don't synergize. Claim gold and relics. Potions if slots open.
- **Rest Sites**: Heal if below 80% HP before boss. Otherwise upgrade or train (Girya).
- **Shop**: Buy if 100+ gold and something useful is available.

## Important Rules
- Always re-check `get_game_state` after playing cards — indices shift.
- Use `format: "json"` in combat for precise data, `format: "markdown"` for overview screens.
- Use potions BEFORE playing cards when they grant buffs (e.g. Flex Potion).
- Focus fire on bosses — minions flee when the leader dies.

## Learning & Updating
- **After each boss is defeated**, review what worked and what didn't. Update `GUIDE.md` with new insights — hero-specific tips, boss strategies, card evaluations, or sequencing discoveries.
- If playing a hero not yet in `GUIDE.md`, create a new section for them.
