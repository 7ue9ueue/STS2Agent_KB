# Strategy Index

This directory contains the **decision playbooks** — the files the agent reads to decide what to do. Per-entity reference data lives in `kb/cards/`, `kb/relics/`, `kb/potions/`, `kb/enemies/`, `kb/events/`, `kb/mechanics/`.

For the top-level routing table, see [`GUIDE.md`](../../GUIDE.md).

## Playbooks (read before each decision)

| Decision | File |
|---|---|
| Card rewards, shop buys, smiths | [reward_choice.md](reward_choice.md) |
| Deck size and answer density | [deck_size.md](deck_size.md) |
| Map route choice | [pathing.md](pathing.md) |
| In-combat play (sequencing, mistakes) | [combat.md](combat.md) |
| Elite path readiness | [elites.md](elites.md) |
| Boss prep checklist | [bosses.md](bosses.md) |
| Save-and-load correction loop | [meta_play.md](meta_play.md) |

## Reference

| Topic | File |
|---|---|
| Ironclad draft shape and act plan | [ironclad.md](ironclad.md) |
| Ironclad archetype templates | [archetypes.md](archetypes.md) |
| Current card win-rate table | [card_winrates.md](card_winrates.md) |
| Data-informed card impressions | [card_impressions.md](card_impressions.md) |

## Where else things live

- Single card / relic / enemy / event / potion / mechanic: that entity's `## Strategy Notes` section.
- Save-and-load mechanics: [`kb/mechanics/save_and_load.md`](../mechanics/save_and_load.md).
- Run-specific analysis: `history/run<N>.md`.
