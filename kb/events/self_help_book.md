---
title: Self-Help Book
source: https://spire-codex.com/api/events
id: SELF_HELP_BOOK
type: Shared
act: null
preconditions: []
stub: false
---

# Self-Help Book

## Sources

- https://spire-codex.com/api/events

## Structured Fields

| Field | Value |
|---|---|
| ID | SELF_HELP_BOOK |
| Type | Shared |
| Act | — |
| Epithet | — |
| Image URL | — |

## Preconditions

_None in source record._

## Initial Options

| ID | Title | Effect |
|---|---|---|
| READ_THE_BACK | Read the Back | Choose an Attack to Enchant with Sharp 2. |
| READ_THE_BACK_LOCKED | Locked | You don't have any Attacks that can be Enchanted. |
| READ_PASSAGE | Read a Random Passage | Choose a Skill to Enchant with Nimble 2. |
| READ_PASSAGE_LOCKED | Locked | You don't have any Skills that can be Enchanted. |
| READ_ENTIRE_BOOK | Read the Entire Book | Choose a Power to Enchant with Swift 2. |
| READ_ENTIRE_BOOK_LOCKED | Locked | You don't have any Powers that can be Enchanted. |
| NO_OPTIONS | Move On | You don't have any cards that can be Enchanted. |

## Page Transition Options

| Page ID | Option ID | Title | Effect |
|---|---|---|---|
| INITIAL | READ_THE_BACK | Read the Back | Choose an Attack to Enchant with Sharp 2. |
| INITIAL | READ_THE_BACK_LOCKED | Locked | You don't have any Attacks that can be Enchanted. |
| INITIAL | READ_PASSAGE | Read a Random Passage | Choose a Skill to Enchant with Nimble 2. |
| INITIAL | READ_PASSAGE_LOCKED | Locked | You don't have any Skills that can be Enchanted. |
| INITIAL | READ_ENTIRE_BOOK | Read the Entire Book | Choose a Power to Enchant with Swift 2. |
| INITIAL | READ_ENTIRE_BOOK_LOCKED | Locked | You don't have any Powers that can be Enchanted. |
| INITIAL | NO_OPTIONS | Move On | You don't have any cards that can be Enchanted. |

## Relics

_No relic list in source record._

---
<!-- META-AGENT NOTES — do not edit above this line -->
## Strategy Notes

<!-- Reserved for the meta-agent. Append lessons, combos, and heuristics here.
     Wiki facts live above the divider. -->
- Sharp 2 is highest leverage on X-cost or repeat-hit Attacks such as Whirlwind because the damage bonus can apply multiple times.
- Swift 2 is high leverage on 1-cost setup powers that need to be played before engine turns; Vicious and Dark Embrace convert the enchant into immediate tempo and consistency.
- If only one eligible card exists for the chosen option, the event can apply the enchant immediately without opening a selection screen.
