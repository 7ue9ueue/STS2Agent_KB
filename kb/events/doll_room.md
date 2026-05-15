---
title: Doll Room
source: https://spire-codex.com/api/events
id: DOLL_ROOM
type: Shared
act: null
preconditions: [Act 2 only]
stub: false
---

# Doll Room

## Sources

- https://spire-codex.com/api/events

## Structured Fields

| Field | Value |
|---|---|
| ID | DOLL_ROOM |
| Type | Shared |
| Act | — |
| Epithet | — |
| Image URL | — |

## Preconditions

- Act 2 only

## Initial Options

| ID | Title | Effect |
|---|---|---|
| RANDOM | Pick at Random | Obtain a random Doll Relic. |
| TAKE_SOME_TIME | Take Some Time | Lose 5 HP. Choose 1 of 2 Doll Relics. |
| EXAMINE | Examine Each and Make the Best Choice | Lose 15 HP. Choose 1 of 3 Doll Relics. |

## Page Transition Options

| Page ID | Option ID | Title | Effect |
|---|---|---|---|
| INITIAL | RANDOM | Pick at Random | Obtain a random Doll Relic. |
| INITIAL | TAKE_SOME_TIME | Take Some Time | Lose 5 HP. Choose 1 of 2 Doll Relics. |
| INITIAL | EXAMINE | Examine Each and Make the Best Choice | Lose 15 HP. Choose 1 of 3 Doll Relics. |
| TAKE | TAKE | TAKE | Receive a random Relic. |

## Relics

_No relic list in source record._

---
<!-- META-AGENT NOTES — do not edit above this line -->
## Strategy Notes

<!-- Reserved for the meta-agent. Append lessons, combos, and heuristics here.
     Wiki facts live above the divider. -->
