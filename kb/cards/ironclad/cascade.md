---
title: Cascade
sources: [https://spire-codex.com/api/cards/CASCADE]
character: Ironclad
type: Skill
rarity: Rare
cost: X
target: Self
keywords: []
api_tags: []
wiki_stub: false
---

# Cascade

## Sources

- https://spire-codex.com/api/cards/CASCADE

## Card Text

- Cost: X
- Type/Rarity: Skill / Rare
- Target: Self
- Base: Play the top X cards of your Draw Pile.
- Upgraded: Play the top X+1 cards of your Draw Pile.

## Structured Fields

| Field | Value |
|---|---|
| ID | CASCADE |
| Color | ironclad |
| Type key | Skill |
| Rarity key | Rare |
| Target | Self |
| Keywords | `[]` |
| API tags | `[]` |

## Numeric Fields

| Field | Value |
|---|---|
| Damage | — |
| Block | — |
| Hit count | — |
| Cards drawn | — |
| Energy gain | — |
| HP loss | — |
| Powers applied | — |

## Upgrade And Generation Data

| Field | Value |
|---|---|
| Spawns cards | — |
| Vars | — |
| Upgrade | `{"description_changed": 1}` |
| Can be generated in combat | — |
| Compendium order | 62 |

---
<!-- META-AGENT NOTES — do not edit above this line -->
## Strategy Notes

<!-- Reserved for the meta-agent. Append lessons, combos, and heuristics here.
     Source facts live above the divider. -->
- Re-read state after Cascade before planning from draw-pile preview; it can trigger selection prompts and the live play order may differ from the visible preview.
- Do not rely on Cascade-played attacks to trigger Ornamental Fan for exact lethal block math unless the current state confirms the block was gained.
- If Cascade plays a draw card, that draw can change the next cards Cascade resolves; do not assume the initial draw-pile preview remains the full Cascade sequence.
- 0-energy Cascade is not automatically safe at lethal HP; it can still trigger draw/exhaust chains and selection prompts, so only play it when every likely follow-up selection is acceptable.
- In multi-enemy fights, avoid exact target-dependent Cascade lines; attack targeting and visible draw-pile order can differ from the plan.
- Draw-pile previews can still be stale in status-clog fights; a small Cascade may hit a Dazed/status even when the visible preview suggests a useful card, so prefer known live draws when exact output matters.
