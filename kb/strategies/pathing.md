# Path Choosing Strategy

Pathing is rest-site planning first, defensive planning second, and reward optimization third. Before choosing a route, inspect the whole visible map graph from the current node to the boss and count how many rest sites/campfires each branch can reach. A path with more rest sites is usually stronger because it creates both upgrade opportunities and emergency healing outs. Planning the path is very important: choose a route carefully at the beginning of each act.

## Core Rules

- Prioritize the route with the most rest sites/campfires over the full visible path to the boss. They are the most important safety and power nodes because they allow Smith by default and Rest when the path or boss demands it.
- Do not choose from only the next node or one-step lookahead. For each candidate next node, trace every reachable branch to the boss and compare rest count, forced combats before first rest, shops, elite exposure, and question-mark alternatives.
- The first three hallway enemies of an act are usually weak; early combats are often good because they give card rewards, gold, and potions before the harder encounter pool appears.
- Prefer question marks over regular enemies when the deck is not desperate for immediate card rewards. The API does not reveal what a question mark contains, but unknown nodes are generally safer than hard hallway fights and can give removals, upgrades, relics, gold, healing, or other value.
- Avoid optional elites unless the run is in Act 1 with strong early damage, or the deck/HP/potions are already very healthy.
- In Act 2, be especially cautious with elites because Decimillipede can appear; without AoE, multi-target damage, or a solid block/draw engine, path away.
- Low current HP changes even hallway math: if the next node is a forced Act 2 combat, keep a defensive potion or route to recovery before spending the last survival resource.
- After a costly Act 2 hallway, check the next forced node before accepting the outcome. Exiting around 20-25 HP with no potion can still be unrecoverable if another hallway stands before the first rest site.

## How To Pick A Route

1. Check the visible act boss and read the boss strategy file.
2. For every available next node, trace the whole visible route tree to the boss before committing.
3. Count rest sites/campfires on each route. Prefer the branch with the most rest access unless it adds unacceptable forced elites or combat damage.
4. Count forced combats before the first rest site; avoid routes that can trap low current HP into repeated hallway fights.
5. Prefer question marks over regular enemies when HP is medium/low or the deck already has enough card rewards.
6. Take the first three hallway combats only when HP is stable and the route still has good rest access; they are a controlled way to improve the deck.
7. Take elites only when the deck has the act-specific answer and enough HP/potion backup.
8. Prefer shops when holding about 100+ gold or when the run needs removal, potion support, or a specific boss/elite answer.

## Act Bias

| Act | Default pathing bias |
|---|---|
| Act 1 | Take early fights for damage cards; elites are acceptable only with good damage/HP/potions and a rest-site fallback. |
| Act 2 | Be conservative with elites; prioritize rest sites, question marks, shops, and safe fights unless the deck is clearly strong. |
| Act 3 | Path around the final boss plan; skip optional elites that risk the potion or HP needed for the boss. |

## Elite Readiness Check

Before choosing an elite path, answer all of these:
- What elites can appear in this act?
- Which strategy file and enemy KB files were read?
- What exact cards, relics, potions, or HP total make this elite safe?
- Where is the next rest site if the fight goes badly?

If those answers are weak, take the safer path.

## HP Thresholds By Act

| Act | Elite floor | Unknown node floor |
|---|---|---|
| Act 1 | >70% HP (~64+ HP) | 50–70% HP |
| Act 2 | >70% HP, with caution for Hive elites | 50–70% HP |
| Act 3 | >60% HP, with potion/defense reserve | tighter — fewer safe outcomes |

- **Below 20% HP after any fight → immediate rest site.** Don't chain combats at low HP.
- Before taking a low-HP survival line, check whether the path has forced combats before the next rest; if it does, spend resources earlier or reroute.
- In Act 2, a forced hallway at ~25 current HP can be lethal even without an elite. Keep a defensive potion, route to recovery, or avoid spending the last survival resource in the previous fight.
- After any costly Act 2 hallway, immediately inspect the next node before treating the fight as "survived." Leaving at 20–25 HP with no potion can still be a losing state if the next room is a forced hallway before the rest site.

## Campfire Defaults

From the 161 A10 win corpus, smith share by act:

| Act | Smith share |
|---|---:|
| Act 1 | 75.0% |
| Act 2 | 67.1% |
| Act 3 | 66.8% |

- **Default = Smith.** Heal only at low HP or before a known hard boss.
- **Final pre-boss rest needs explicit math.** Do not rest just because HP is not full; if relics/cards already cover the next boss's expected damage, smith the highest-impact card instead.
- Before the final campfire, re-check the full route tree rather than trusting the previous branch read. If the remaining path can still force an elite or hallway before the last rest, low HP should push Rest over Smith even when the upgrade is high value.

## HP Checkpoints (Winning A10 Medians)

| Checkpoint | Median HP% | Rule |
|---|---|---|
| Before Act 1 boss | 63% | Acceptable; smith unless boss-specific math says HP is the limiting resource |
| Start of Act 2 | 87% | Boss heal expected |
| Before any elite | 73% | Rest if below 60% |
| Before Act 3 boss #1 | 98% | Near-full is common; final rest can still be a Smith with Pantograph/Fairy and a concrete boss plan |
| Before final boss | 70% | First A3 boss costs ~20pp HP on average; for Queen, require a guaranteed post-Bound Beam defense or a kill plan for Amalgam |

**Key rule**: Reach the last campfire before each boss with a plan. Default to Smith if HP is stable; heal if a hard boss or low HP would make the fight unsafe.

## Act-Specific Notes

### Act 1
- Fight every regular combat — Burning Blood heals 6, making chip damage nearly free.
- The first three hallway fights are usually weak; use early combats to earn cards, gold, and potions before the harder encounter pool.

### Act 2
- Re-check whether a branch forces an elite immediately after the next node. A full-HP monster can still be a bad choice if the following elite is forced and the parallel unknown branch avoids it.
- **Hive elites are dangerous** because Decimillipede can appear. If the deck lacks AoE, strong multi-target damage, or a solid block/draw engine, path away from optional Act 2 elites even at decent HP.
- **Decimillipede**: don't treat early segment kills as pure progress. Spread damage with AoE, then coordinate kills so reattach doesn't restore multiple 25 HP segments.
- **Battleworn Dummy**: pick the tier you can mathematically guarantee clear. 300HP is only viable if T3 draw reliably contains Vul-enablers + a Bully/Dismantle finisher. Default to 75HP for guaranteed reward.

### Act 3
- Enemy damage is higher and patterns are less forgiving — raise the elite HP floor.
- For final-boss access, add a mandatory safety gate: if the next sequence gives only one prep rest and no defensive potion/Buffer preserved, avoid optional Act 3 elites that move you below a defended Queen Beam floor.
- Entering the Act 3 two-boss gauntlet below ~70% HP with no defensive potion is an emergency state. Prefer Rest or safer routing earlier; do not plan to make up the deficit with exact self-damage scaling lines.
- When both branches reach the same rest site, prefer Shop over Monster if gold can buy a boss-specific potion, block card, or removal. Avoiding the hallway can preserve more HP than Burning Blood can refund.
