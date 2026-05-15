---
title: Crystal Sphere
source: https://spire-codex.com/api/events
id: CRYSTAL_SPHERE
type: Shared
act: null
preconditions: [Requires 100+ gold, Act 2+]
stub: false
---

# Crystal Sphere

## Sources

- https://spire-codex.com/api/events

## Structured Fields

| Field | Value |
|---|---|
| ID | CRYSTAL_SPHERE |
| Type | Shared |
| Act | — |
| Epithet | — |
| Image URL | — |

## Preconditions

- Requires 100+ gold
- Act 2+

## Initial Options

| ID | Title | Effect |
|---|---|---|
| UNCOVER_FUTURE | Uncover Future | Pay 51-99 Gold. Divine 3 times. |
| PAYMENT_PLAN | Payment Plan | Gain a Debt. Divine 6 times. |

## Page Transition Options

| Page ID | Option ID | Title | Effect |
|---|---|---|---|
| INITIAL | UNCOVER_FUTURE | Uncover Future | Pay 51-99 Gold. Divine 3 times. |
| INITIAL | PAYMENT_PLAN | Payment Plan | Gain a Debt. Divine 6 times. |

## Relics

_No relic list in source record._

---
<!-- META-AGENT NOTES — do not edit above this line -->
## Strategy Notes

<!-- Reserved for the meta-agent. Append lessons, combos, and heuristics here.
     Wiki facts live above the divider. -->
- Payment Plan is risky in draw-heavy decks because Debt is a permanent unplayable curse that can repeatedly drain 10 gold when drawn.
- Harness warning: the MCP proceed flow can get stuck after divinations, even with 0 divinations remaining; save/load returns to the event start, but manual UI intervention may be needed to leave the minigame.
- If retrying known layouts, small divination can target single-cell rewards without revealing adjacent curse cells; big divination can accidentally reveal nearby 2x2 curses or partial large rewards.
