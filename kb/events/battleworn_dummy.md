---
title: Battleworn Dummy
source: https://spire-codex.com/api/events
id: BATTLEWORN_DUMMY
type: Event
act: Act 3 - Glory
preconditions: []
stub: false
---

# Battleworn Dummy

## Sources

- https://spire-codex.com/api/events

## Structured Fields

| Field | Value |
|---|---|
| ID | BATTLEWORN_DUMMY |
| Type | Event |
| Act | Act 3 - Glory |
| Epithet | — |
| Image URL | — |

## Preconditions

_None in source record._

## Initial Options

| ID | Title | Effect |
|---|---|---|
| SETTING_1 | Setting 1 | Fight a 75 HP dummy. Procure 1 random Potion. |
| SETTING_2 | Setting 2 | Fight a 150 HP dummy. Upgrade 2 random cards. |
| SETTING_3 | Setting 3 | Fight a 300 HP dummy. Obtain a random Relic. |

## Page Transition Options

| Page ID | Option ID | Title | Effect |
|---|---|---|---|
| INITIAL | SETTING_1 | Setting 1 | Fight a 75 HP dummy. Procure 1 random Potion. |
| INITIAL | SETTING_2 | Setting 2 | Fight a 150 HP dummy. Upgrade 2 random cards. |
| INITIAL | SETTING_3 | Setting 3 | Fight a 300 HP dummy. Obtain a random Relic. |

## Relics

_No relic list in source record._

---
<!-- META-AGENT NOTES — do not edit above this line -->
## Strategy Notes

<!-- Reserved for the meta-agent. Append lessons, combos, and heuristics here.
     Wiki facts live above the divider. -->
- **300 HP / 3 turns** requires ~100 dmg/turn average. Pre-burst setup on T1 (Vicious+, Stone Armor, Rupture) may deliver ~88 T1; T2 ~67 via Vicious+×2 chain; but T3 needs a full damage hand (Bash+/Squash + Bully, not Howl alone). If T3 draw is Howl from Beyond+ only, expect ~52 dmg — dummy survives ~90 HP.
- **Do NOT pick 300 HP unless** T3 draw is reliably stocked with Vul-enablers (Bash+/Squash) AND a Bully/Dismantle finisher. A Howl+ hand with no Vul setup fails the challenge even at Str 6.
- **Choose 75 HP** if deck lacks burst consistency — the reward is still a relic, and a guaranteed pass beats a 300 HP failed attempt.
- **Dummy has no Block, no Artifact, no resistances** — pure DPS check. Every card should deal damage or set up a damage multiplier (Vul).
