---
title: Ranwid the Elder
source: https://spire-codex.com/api/events
id: RANWID_THE_ELDER
type: Shared
act: null
preconditions: [Act 2+, Requires at least one potion]
stub: false
---

# Ranwid the Elder

## Sources

- https://spire-codex.com/api/events

## Structured Fields

| Field | Value |
|---|---|
| ID | RANWID_THE_ELDER |
| Type | Shared |
| Act | — |
| Epithet | — |
| Image URL | — |

## Preconditions

- Act 2+
- Requires at least one potion

## Initial Options

| ID | Title | Effect |
|---|---|---|
| POTION | Give Potion | Obtain a random Relic. |
| POTION_LOCKED | Locked | You don't have any Potions that can be given. |
| GOLD | Give 100 Gold | Obtain a random Relic. |
| RELIC | Give Relic | Obtain 2 random Relics. |
| RELIC_LOCKED | Locked | You don't have any Relics that can be given. |

## Page Transition Options

| Page ID | Option ID | Title | Effect |
|---|---|---|---|
| INITIAL | POTION | Give Potion | Obtain a random Relic. |
| INITIAL | POTION_LOCKED | Locked | You don't have any Potions that can be given. |
| INITIAL | GOLD | Give 100 Gold | Obtain a random Relic. |
| INITIAL | RELIC | Give Relic | Obtain 2 random Relics. |
| INITIAL | RELIC_LOCKED | Locked | You don't have any Relics that can be given. |

## Relics

_No relic list in source record._

---
<!-- META-AGENT NOTES — do not edit above this line -->
## Strategy Notes

<!-- Reserved for the meta-agent. Append lessons, combos, and heuristics here.
     Wiki facts live above the divider. -->
