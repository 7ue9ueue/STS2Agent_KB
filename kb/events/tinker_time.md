---
title: Tinker Time
source: https://spire-codex.com/api/events
id: TINKER_TIME
type: Event
act: Act 3 - Glory
preconditions: []
stub: false
---

# Tinker Time

## Sources

- https://spire-codex.com/api/events

## Structured Fields

| Field | Value |
|---|---|
| ID | TINKER_TIME |
| Type | Event |
| Act | Act 3 - Glory |
| Epithet | — |
| Image URL | — |

## Preconditions

_None in source record._

## Initial Options

| ID | Title | Effect |
|---|---|---|
| CHOOSE_CARD_TYPE | Accept | Create a custom card to add to your Deck. |

## Page Transition Options

| Page ID | Option ID | Title | Effect |
|---|---|---|---|
| CHOOSE_CARD_TYPE | ATTACK | Weapon | Make an Attack. |
| CHOOSE_CARD_TYPE | SKILL | Protector | Make a Skill. |
| CHOOSE_CARD_TYPE | POWER | Gadget | Make a Power. |
| CHOOSE_RIDER | SAPPING | Sapping | Apply 2 Weak. Apply 2 Vulnerable. |
| CHOOSE_RIDER | VIOLENCE | Violence | Hits 2 additional times. |
| CHOOSE_RIDER | CHOKING | Choking | Whenever you play a card this turn, the enemy loses 6 HP. |
| CHOOSE_RIDER | ENERGIZED | Energized | Gain 2 Energy. |
| CHOOSE_RIDER | WISDOM | Wisdom | Draw 3 cards. |
| CHOOSE_RIDER | CHAOS | Chaos | Add a random card into your Hand. It's free to play this turn. |
| CHOOSE_RIDER | EXPERTISE | Expertise | Gain 2 Strength. Gain 2 Dexterity. |
| CHOOSE_RIDER | CURIOUS | Curious | Powers cost 1 1 Energy less. |
| CHOOSE_RIDER | IMPROVEMENT | Improvement | At the end of combat, Upgrade a random card. |
| INITIAL | CHOOSE_CARD_TYPE | Accept | Create a custom card to add to your Deck. |

## Relics

_No relic list in source record._

---
<!-- META-AGENT NOTES — do not edit above this line -->
## Strategy Notes

<!-- Reserved for the meta-agent. Append lessons, combos, and heuristics here.
     Wiki facts live above the divider. -->
- Protector + Wisdom creates a block-and-draw custom Skill, which is a strong low-risk late pick when the deck needs boss consistency more than more attacks.
