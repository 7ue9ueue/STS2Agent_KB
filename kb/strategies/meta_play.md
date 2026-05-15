# Meta-Play Strategy

Fast lookup for agent self-correction during runs. Canonical long-form notes live in [GUIDE.md](../../GUIDE.md).

## Reload, Learn, Prevent

- If a fight, event, shop, rest-site, or path decision reveals a strategic issue, stop and name the failed assumption before taking more actions.
- If the room can be restarted with `save_and_quit` plus `continue`, reload and replay with a materially different plan that prevents the same mistake.
- Use save/load proactively when an early combat line would cause major preventable HP loss, or when an event's alternate branches could materially change HP, potions, deck quality, relics, gold, or path equity.
- Record reusable lessons immediately: named-entity lessons go in that entity's KB Strategy Notes; cross-cutting lessons go in `kb/strategies/` or `GUIDE.md`; exact retry lines and run context go in `history/run<N>.md`.
- Do not continue a survivable but strategically bad line when it teaches a clear correction. Reloading is correct when it preserves HP, potions, path equity, or fight tempo and prevents the same mistake from repeating.
- Limit retries to distinct plans. If 3-5 serious alternatives cannot meet the goal, stop retrying, record why, and play the best remaining line.
