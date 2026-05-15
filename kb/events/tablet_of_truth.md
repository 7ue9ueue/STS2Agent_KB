---
title: Tablet of Truth
source: https://spire-codex.com/api/events
id: TABLET_OF_TRUTH
type: Event
act: Act 1 - Overgrowth
preconditions: []
stub: false
---

# Tablet of Truth

## Sources

- https://spire-codex.com/api/events

## Structured Fields

| Field | Value |
|---|---|
| ID | TABLET_OF_TRUTH |
| Type | Event |
| Act | Act 1 - Overgrowth |
| Epithet | — |
| Image URL | — |

## Preconditions

_None in source record._

## Initial Options

| ID | Title | Effect |
|---|---|---|
| DECIPHER_1 | Decipher | Lose 3 Max HP. Upgrade a random card. |
| SMASH | Smash | Heal 20 HP. |

## Page Transition Options

| Page ID | Option ID | Title | Effect |
|---|---|---|---|
| DECIPHER | GIVE_UP | Give Up | Stop reading the text and leave. |
| DECIPHER_1 | DECIPHER | Continue Deciphering | Lose 6 Max HP. Upgrade a random card. |
| DECIPHER_2 | DECIPHER | Keep Deciphering | Lose 12 Max HP. Upgrade a random card. |
| DECIPHER_3 | DECIPHER | KEEP DECIPHERING | Lose 24 Max HP. Upgrade a random card. |
| DECIPHER_4 | DECIPHER | Lose Everything | Set Max HP to 1. Upgrade ALL cards. |
| INITIAL | DECIPHER_1 | Decipher | Lose 3 Max HP. Upgrade a random card. |
| INITIAL | SMASH | Smash | Heal 20 HP. |

## Relics

_No relic list in source record._

---
<!-- META-AGENT NOTES — do not edit above this line -->
## Strategy Notes

<!-- Reserved for the meta-agent. Append lessons, combos, and heuristics here.
     Wiki facts live above the divider. -->
