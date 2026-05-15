---
title: Dominate
sources: [https://spire-codex.com/api/cards/DOMINATE, https://slaythespire.wiki.gg/wiki/Slay_the_Spire_2:Dominate]
character: Ironclad
type: Skill
rarity: Uncommon
cost: 1
target: AnyEnemy
keywords: [Exhaust]
api_tags: []
wiki_stub: true
---

# Dominate

## Sources

- https://spire-codex.com/api/cards/DOMINATE
- https://slaythespire.wiki.gg/wiki/Slay_the_Spire_2:Dominate

## Card Text

- Cost: 1
- Type/Rarity: Skill / Uncommon
- Target: AnyEnemy
- Base: Apply 1 Vulnerable. Gain 1 Strength for each Vulnerable on the enemy.
- Upgraded: Apply 2 Vulnerable. Gain 1 Strength for each Vulnerable on the enemy.

## Structured Fields

| Field | Value |
|---|---|
| ID | DOMINATE |
| Color | ironclad |
| Type key | Skill |
| Rarity key | Uncommon |
| Target | AnyEnemy |
| Keywords | `["Exhaust"]` |
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
| Powers applied | `[{"amount": 1, "power": "Vulnerable", "power_key": "Vulnerable"}]` |

## Upgrade And Generation Data

| Field | Value |
|---|---|
| Spawns cards | — |
| Vars | `{"StrengthPerVulnerable": 1, "Vulnerable": 1, "VulnerablePower": 1}` |
| Upgrade | `{"vulnerablepower": "+1"}` |
| Can be generated in combat | — |
| Compendium order | 31 |

---
<!-- META-AGENT NOTES — do not edit above this line -->
## Strategy Notes

<!-- Reserved for the meta-agent. Append lessons, combos, and heuristics here.
     Wiki facts live above the divider. -->
- 161-win signal: appears in 41.6% of final decks with moderate upgrade rate (42.0% upgraded copies).
- Fits the common defensive shell as a repeatable skill; pairs well with Bloodletting tempo and draw-heavy decks.
- Break+ into Dominate is a major burst setup: 7 Vulnerable first means base Dominate gains 8 Strength after applying its own Vulnerable.
