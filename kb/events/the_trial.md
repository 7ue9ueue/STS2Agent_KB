---
title: The Trial
source: https://spire-codex.com/api/events
id: TRIAL
type: Event
act: Act 3 - Glory
preconditions: []
stub: false
---

# The Trial

## Sources

- https://spire-codex.com/api/events

## Structured Fields

| Field | Value |
|---|---|
| ID | TRIAL |
| Type | Event |
| Act | Act 3 - Glory |
| Epithet | — |
| Image URL | — |

## Preconditions

_None in source record._

## Initial Options

| ID | Title | Effect |
|---|---|---|
| ACCEPT | Accept | Serve as today's Decider. |
| REJECT | Reject | You are not allowed to Reject. |

## Page Transition Options

| Page ID | Option ID | Title | Effect |
|---|---|---|---|
| INITIAL | ACCEPT | Accept | Serve as today's Decider. |
| INITIAL | REJECT | Reject | You are not allowed to Reject. |
| MERCHANT | GUILTY | DECIDE: Guilty | Add Regret to your Deck. Obtain 2 random Relics. |
| MERCHANT | INNOCENT | DECIDE: Innocent | Add Shame to your Deck. Upgrade 2 cards. |
| NOBLE | GUILTY | DECIDE: Guilty | Heal 10 HP. |
| NOBLE | INNOCENT | DECIDE: Innocent | Add Regret to your Deck. Obtain 300 Gold. |
| NONDESCRIPT | GUILTY | DECIDE: Guilty | Add Doubt to your Deck. Gain 2 card rewards. |
| NONDESCRIPT | INNOCENT | DECIDE: Innocent | Add Doubt to your Deck. Transform 2 cards. |
| REJECT | ACCEPT | Accept | Give in. Serve as today's Decider. |
| REJECT | DOUBLE_DOWN | Double Down | Face lethal repercussions. |

## Relics

_No relic list in source record._

---
<!-- META-AGENT NOTES — do not edit above this line -->
## Strategy Notes

<!-- Reserved for the meta-agent. Append lessons, combos, and heuristics here.
     Wiki facts live above the divider. -->
