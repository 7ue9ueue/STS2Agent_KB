---
title: Brain Leech
source: https://spire-codex.com/api/events
id: BRAIN_LEECH
type: Shared
act: null
preconditions: [Act 1–2 only]
stub: false
---

# Brain Leech

## Sources

- https://spire-codex.com/api/events

## Structured Fields

| Field | Value |
|---|---|
| ID | BRAIN_LEECH |
| Type | Shared |
| Act | — |
| Epithet | — |
| Image URL | — |

## Preconditions

- Act 1–2 only

## Initial Options

| ID | Title | Effect |
|---|---|---|
| SHARE_KNOWLEDGE | Share Knowledge | Choose 1 of 5 random cards to add to your Deck. |
| RIP | Rip the Leech Off | Lose 5 HP. Gain a Colorless card reward. |

## Page Transition Options

| Page ID | Option ID | Title | Effect |
|---|---|---|---|
| INITIAL | SHARE_KNOWLEDGE | Share Knowledge | Choose 1 of 5 random cards to add to your Deck. |
| INITIAL | RIP | Rip the Leech Off | Lose 5 HP. Gain a Colorless card reward. |

## Relics

_No relic list in source record._

---
<!-- META-AGENT NOTES — do not edit above this line -->
## Strategy Notes

<!-- Reserved for the meta-agent. Append lessons, combos, and heuristics here.
     Wiki facts live above the divider. -->
- Use save/load to inspect both card-reward branches when possible; do not pay 5 HP for the Colorless branch unless it clearly beats the free 5-card class offer.
