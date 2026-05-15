---
title: Primal Force
sources: [https://spire-codex.com/api/cards/PRIMAL_FORCE, https://slaythespire.wiki.gg/wiki/Slay_the_Spire_2:Primal_Force]
character: Ironclad
type: Skill
rarity: Rare
cost: 0
target: Self
keywords: []
api_tags: []
wiki_stub: true
---

# Primal Force

## Sources

- https://spire-codex.com/api/cards/PRIMAL_FORCE
- https://slaythespire.wiki.gg/wiki/Slay_the_Spire_2:Primal_Force

## Card Text

- Cost: 0
- Type/Rarity: Skill / Rare
- Target: Self
- Base: Transform all Attacks in your Hand into Giant Rock.
- Upgraded: Transform all Attacks in your Hand into Giant Rock+.

## Structured Fields

| Field | Value |
|---|---|
| ID | PRIMAL_FORCE |
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
| Spawns cards | `["GIANT_ROCK"]` |
| Vars | — |
| Upgrade | `{"description_changed": 1}` |
| Can be generated in combat | — |
| Compendium order | 78 |

---
<!-- META-AGENT NOTES — do not edit above this line -->
## Strategy Notes

<!-- Reserved for the meta-agent. Append lessons, combos, and heuristics here.
     Wiki facts live above the divider. -->
- Best when converting weak attacks into Giant Rocks; play key attacks like Fiend Fire or Conflagration first if transforming them would reduce the turn.
- Harness/state quirk: after Primal Force resolves, the immediate hand state may still display some transformed attacks by their old names, but playing those indices can produce Giant Rock.
