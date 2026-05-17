---
title: Stone of All Time
source: https://spire-codex.com/api/events
id: STONE_OF_ALL_TIME
type: Shared
act: null
preconditions: [Act 2 only, Requires at least one potion]
stub: false
---

# Stone of All Time

## Sources

- https://spire-codex.com/api/events

## Structured Fields

| Field | Value |
|---|---|
| ID | STONE_OF_ALL_TIME |
| Type | Shared |
| Act | — |
| Epithet | — |
| Image URL | — |

## Preconditions

- Act 2 only
- Requires at least one potion

## Initial Options

| ID | Title | Effect |
|---|---|---|
| LIFT | Drink and Lift | Lose a random Potion. Gain 10 Max HP. |
| LIFT_LOCKED | Locked | Requires a Potion. |
| PUSH_LOCKED | Locked | Requires an Attack. |
| PUSH | Push | Lose 6 HP. Enchant an Attack with Vigorous 8. |

## Page Transition Options

| Page ID | Option ID | Title | Effect |
|---|---|---|---|
| INITIAL | LIFT | Drink and Lift | Lose a random Potion. Gain 10 Max HP. |
| INITIAL | LIFT_LOCKED | Locked | Requires a Potion. |
| INITIAL | PUSH_LOCKED | Locked | Requires an Attack. |
| INITIAL | PUSH | Push | Lose 6 HP. Enchant an Attack with Vigorous 8. |

## Relics

_No relic list in source record._

---
<!-- META-AGENT NOTES — do not edit above this line -->
## Strategy Notes

<!-- Reserved for the meta-agent. Append lessons, combos, and heuristics here.
     Source facts live above the divider. -->
- When the only potion is Fairy in a Bottle and HP is low, prefer Push if the 6 HP cost is survivable; +10 Max HP does not replace the death buffer.
- A card that already has an enchant may be unavailable for the Push attack enchant; choose the next best finisher such as Break+.
- Vigorous 8 is strongest on attacks with multiple damage packets; if Whirlwind is unavailable, prefer Fiend Fire over single-hit attacks when the deck can feed it.
- If holding a high-value defensive potion for a forced elite/boss, Push can beat Drink and Lift even at medium HP; put Vigorous on Whirlwind or another repeat-hit attack.
