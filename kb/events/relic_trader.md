---
title: Relic Trader
source: https://spire-codex.com/api/events
id: RELIC_TRADER
type: Shared
act: null
preconditions: [Act 2+, Requires 5+ tradeable relics]
stub: false
---

# Relic Trader

## Sources

- https://spire-codex.com/api/events

## Structured Fields

| Field | Value |
|---|---|
| ID | RELIC_TRADER |
| Type | Shared |
| Act | — |
| Epithet | — |
| Image URL | — |

## Preconditions

- Act 2+
- Requires 5+ tradeable relics

## Initial Options

| ID | Title | Effect |
|---|---|---|
| TOP | Take the Top One | Trade one of your Relics for a random Relic. |
| MIDDLE | Take the Middle One | Trade one of your Relics for a random Relic. |
| BOTTOM | Take the Bottom One | Trade one of your Relics for a random Relic. |

## Page Transition Options

| Page ID | Option ID | Title | Effect |
|---|---|---|---|
| INITIAL | TOP | Take the Top One | Trade one of your Relics for a random Relic. |
| INITIAL | MIDDLE | Take the Middle One | Trade one of your Relics for a random Relic. |
| INITIAL | BOTTOM | Take the Bottom One | Trade one of your Relics for a random Relic. |

## Relics

_No relic list in source record._

---
<!-- META-AGENT NOTES — do not edit above this line -->
## Strategy Notes

<!-- Reserved for the meta-agent. Append lessons, combos, and heuristics here.
     Source facts live above the divider. -->
- Prefer trading away conditional or spent-value relics over core combat engines; inspect all three exact relic swaps before choosing because the event has no skip option.
