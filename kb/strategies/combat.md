# In-Combat Playbook

How to play a single turn. For card-specific behavior, see the relevant `kb/cards/<color>/<card>.md` Strategy Notes. For enemy patterns, see `kb/enemies/`.

## Read Before Acting

1. Check active relics — many change card order, energy, or first-card effects.
2. Read every enemy's intent. Sleep/Buff = go all-out offense. Attack = balance block and damage. Debuff = usually no incoming damage, treat as offense turn.
3. Compute lethal. If you can kill this turn, skip blocking entirely.
4. Check enemy HP for kill thresholds (especially scaling enemies and reviving minions).

## Sequencing Within A Turn

1. Play 0-cost utility/setup cards first.
2. Play Skills before Attacks when possible — many mechanics reward this order (e.g. Slow stacks per card played).
3. Play biggest attacks last to benefit from accumulated buffs/debuffs (Vulnerable, Strength, Weak applied to enemies).
4. Be careful with draw mid-turn. Drawing is usually good, but check energy first: if key cards are still in the draw pile and the hand has low probability of gaining energy, draw can pull premium cards before you can afford to play them.
5. After each card, re-read the hand: indices shift left, generated cards appear, discounts can change the whole turn.

## Status / Reviving Enemies

- Against reviving minions or decoys, do not confuse "preventing every minion hit" with winning the fight. Kill the minion only when it prevents a major unblocked attack; otherwise spend energy on the leader before scaling makes the room worse.
- Save once-per-combat first-debuff effects for the real target. Do not spend them on decoys, minions that flee, or infinite-HP opening phases unless the fight plan explicitly requires it.
- Enemies with the "Minion" power flee when their leader dies — kill the leader.

## Power Card Timing

- Setup Powers (Pyre, Rupture, Feel No Pain) are strongest on Sleep, Debuff, Intangible, or already-covered turns. Avoid installing them during heavy incoming turns without enough block.
- Defensive scaling Powers (Barricade, Unmovable) want to be installed before the boss's debuff/tax phase begins, not during it.

## Exhaust Discipline

Exhaust is virtual deck-thinning. Removing Wounds, Burns, Dazed, statuses, curses, and spent setup cards shrinks the live deck so the next reshuffle is denser with premium cards. Especially valuable in long boss fights and status-clog fights.

## Harness And Overlay Hygiene

- Never queue combat actions while a potion or card-select overlay is open. Resolve the overlay, re-read state, then play cards.
- Don't race the harness by chaining combat actions. Play one action, wait briefly, re-read state, then play the next.
- Treat the live hand after each action as authoritative; draw-pile previews can lie after draw/shuffle effects.

## Common Mistakes

- Blocking when enemies are sleeping/buffing — wasted energy.
- Forgetting indices shift left after playing a card.
- Forgetting Save and Load can restart the fight from turn 1 (see [save_and_load](../mechanics/save_and_load.md)) — use it before accepting a likely death, wasted rare potion, or major sequencing mistake.
- Waiting too long to spend defensive potions against scaling hallway enemies. If a Cultist-style enemy is already attacking for 21+ and still scaling, the potion may need to be used before the visibly lethal turn.
- Treating Vigorous/Sharp-style damage enchants like flat single-card bonuses. They are strongest on repeat-hit or per-card damage packets such as Whirlwind and Fiend Fire.
- Spending repeated full turns killing reviving minions while the leader scales — short-term HP gain, fight-timer loss.
- Taking too long to kill bosses — most enemies scale every turn.

## Boss Fights

- Boss fights are wars of attrition. The longer they go, the more enemies scale.
- Use potions aggressively; they don't carry between acts.
- Pick and replace potions for the expected boss phase. A phase-skip potion (e.g. Gigantification) can beat a generic Flex Potion when the deck has Vulnerable, Music Box, or one large Attack.
- Against bosses with rotating powers, map the next turn before spending draw, energy, or debuff cards. Draw before no-draw turns; bank energy/block before per-card tax turns; keep the engine card over a marginal current-turn play.
- Against distance/countdown bosses, the countdown can matter more than attack damage. Play timer-reset cards while they're cheap.
- Per-boss tactical plans: read the relevant `kb/enemies/bosses/<boss>.md` Strategy Notes at the start of each act and before the final rest.
