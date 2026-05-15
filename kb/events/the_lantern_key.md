---
title: The Lantern Key
source: https://spire-codex.com/api/events
id: THE_LANTERN_KEY
type: Event
act: Act 2 - Hive
preconditions: []
stub: false
---

# The Lantern Key

## Sources

- https://spire-codex.com/api/events

## Structured Fields

| Field | Value |
|---|---|
| ID | THE_LANTERN_KEY |
| Type | Event |
| Act | Act 2 - Hive |
| Epithet | — |
| Image URL | — |

## Preconditions

_None in source record._

## Initial Options

| ID | Title | Effect |
|---|---|---|
| RETURN_THE_KEY | Return the Key | Gain 100 Gold. |
| KEEP_THE_KEY | Keep the Key | Fight to obtain the Key. |

## Page Transition Options

| Page ID | Option ID | Title | Effect |
|---|---|---|---|
| DONE | RETURN_THE_KEY | RETURN_THE_KEY | The stranger thanks you for your help, and rewards you handsomely. |
| INITIAL | RETURN_THE_KEY | Return the Key | Gain 100 Gold. |
| INITIAL | KEEP_THE_KEY | Keep the Key | Fight to obtain the Key. |
| KEEP_THE_KEY | FIGHT | Fight | — |

## Relics

_No relic list in source record._

---
<!-- META-AGENT NOTES — do not edit above this line -->
## Strategy Notes

<!-- Reserved for the meta-agent. Append lessons, combos, and heuristics here.
     Wiki facts live above the divider. -->
