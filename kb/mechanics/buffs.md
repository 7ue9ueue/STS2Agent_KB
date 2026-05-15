---
title: Buffs
source: https://spire-codex.com/api/powers
generated: true
---

# Buffs

Structured list of `Buff` powers from Spire Codex. Descriptions are game text with UI color tags removed.

## Stack Types

- `Counter`: stack count usually tracks charges, amount, or remaining turns depending on the effect text.
- `Single`: present or absent; duplicate applications generally do not create a separate visible stack.
- `None`: no stack value is shown by the source data.

## Common Agent Checks

| Name | ID | Stack | Negative? | Description |
|---|---|---|---|---|
| Artifact | `ARTIFACT` | Counter |  | Negates debuffs. |
| Barricade | `BARRICADE` | Single |  | Block is not removed at the start of your turn. |
| Block Next Turn | `BLOCK_NEXT_TURN` | Counter |  | At the start of your next turn, gain 4 Block. |
| Buffer | `BUFFER` | Counter |  | Prevent the next 2 times you would lose HP. |
| Dexterity | `DEXTERITY` | Counter | yes | Increases Block gained from cards by X. |
| Draw Cards Next Turn | `DRAW_CARDS_NEXT_TURN` | Counter |  | At the start of your next turn, draw 1 additional card. |
| Energy Next Turn | `ENERGY_NEXT_TURN` | Counter |  | Gain additional Energy next turn. |
| Focus | `FOCUS` | Counter | yes | Increases the effectiveness of Orbs by X. |
| Intangible | `INTANGIBLE` | Counter |  | Reduce all damage taken and HP loss to 1 this turn. |
| Plating | `PLATING` | Counter |  | At the end of your turn, gain X Block. Plating is reduced by 1 at the start of your turn. |
| Strength | `STRENGTH` | Counter | yes | Increases attack damage by X. |
| Thorns | `THORNS` | Counter |  | When hit by an attack, deal damage back. |
| Vigor | `VIGOR` | Counter |  | This creature's next Attack deals X additional damage. |

## Full List

| Name | ID | Stack | Negative? | Description |
|---|---|---|---|---|
| Accelerant | `ACCELERANT` | Counter |  | Poison is triggered an additional time. |
| Accuracy | `ACCURACY` | Counter |  | Shivs deal additional damage. |
| Adaptable | `ADAPTABLE` | Single |  | When this creature would be defeated, it instead revives even stronger. |
| Afterimage | `AFTERIMAGE` | Counter |  | Whenever you play a card, gain 1 Block. |
| Aggression | `AGGRESSION` | Counter |  | At the start of your turn, put a random Attack from your Discard Pile into your Hand and Upgrade it for the rest of combat. |
| Arsenal | `ARSENAL` | Counter |  | Whenever you create a card, gain 1 Strength. |
| Artifact | `ARTIFACT` | Counter |  | Negates debuffs. |
| Asleep | `ASLEEP` | Counter |  | Awakens upon losing HP or after 2 turns. |
| Automation | `AUTOMATION` | Counter |  | Every 10 cards you draw, gain 1 Energy. |
| Back Attack | `BACK_ATTACK_LEFT` | Single |  | Deals 50% more damage when it is attacking you from behind. |
| Back Attack | `BACK_ATTACK_RIGHT` | Single |  | Deals 50% more damage when it is attacking you from behind. |
| Barricade | `BARRICADE` | Single |  | Block is not removed at the start of your turn. |
| Beacon of Hope | `BEACON_OF_HOPE` | Single |  | Whenever you gain Block on your turn, other players gain half that much Block. |
| Black Hole | `BLACK_HOLE` | Counter |  | Whenever you spend or gain 1 Star, deal 3 damage to ALL enemies. |
| Block Next Turn | `BLOCK_NEXT_TURN` | Counter |  | At the start of your next turn, gain 4 Block. |
| Blur | `BLUR` | Counter |  | Block is not removed at the start of your next 2 turns. |
| Buffer | `BUFFER` | Counter |  | Prevent the next 2 times you would lose HP. |
| Burrowed | `BURROWED` | Single |  | Block is not removed at the start of this creature's turn. Stunned if all Block is removed. |
| Burst | `BURST` | Counter |  | Your next 2 Skills are played an extra time this turn. |
| Calamity | `CALAMITY` | Counter |  | Whenever you play an Attack, add 2 random Attacks into your Hand. |
| Calcify | `CALCIFY` | Counter |  | Osty's attacks deal additional damage. |
| Call of the Void | `CALL_OF_THE_VOID` | Counter |  | At the start of your turn, add 1 random card into your Hand and apply Ethereal to it. |
| Child of the Stars | `CHILD_OF_THE_STARS` | Counter |  | Gain 1 Block for each 1 Star spent. |
| Clarity | `CLARITY` | Counter |  | At the start of your next 2 turns, draw 1 additional card. |
| Colossus | `COLOSSUS` | Counter |  | You receive 50% less damage from Vulnerable enemies for 2 turns. |
| Consuming Shadow | `CONSUMING_SHADOW` | Counter |  | At the end of your turn, Evoke your 2 leftmost Orbs. |
| Coolant | `COOLANT` | Counter |  | At the start of your turn, gain 3 Block for each unique Orb you have. |
| Corrosive Wave | `CORROSIVE_WAVE` | Counter |  | Whenever you draw a card this turn, apply 2 Poison to ALL enemies. |
| Corruption | `CORRUPTION` | Single |  | Skills cost 0. Whenever you play a Skill, Exhaust it. |
| Countdown | `COUNTDOWN` | Counter |  | At the start of your turn, apply 6 Doom to a random enemy. |
| Covered | `COVERED` | Single |  | An ally is covering you. All attacks that would be directed to you are redirected to them instead. |
| Crab Rage | `CRAB_RAGE` | Single |  | When an ally dies, this creature gains 6 Strength and 99 Block. |
| Creative AI | `CREATIVE_AI` | Counter |  | At the start of your turn, add 2 random Powers into your Hand. |
| Crimson Mantle | `CRIMSON_MANTLE` | Counter |  | At the start of your turn, lose 0 HP and gain X Block. |
| Cruelty | `CRUELTY` | Counter |  | Vulnerable enemies take additional damage. |
| Curious | `CURIOUS` | Counter |  | Powers cost 1 Energy less. |
| Curl Up | `CURL_UP` | Counter |  | When damaged, rolls up and gains block. (Once per combat) |
| Danse Macabre | `DANSE_MACABRE` | Counter |  | Whenever you play a card that costs 2 Energy or more, gain X Block. |
| Dark Embrace | `DARK_EMBRACE` | Counter |  | Whenever a card is Exhausted, draw 1 card. |
| Demesne | `DEMESNE` | Counter |  | At the start of your turn, gain 1 Energy and draw 1 additional card. |
| Demon Form | `DEMON_FORM` | Counter |  | At the start of your turn, gain 2 Strength. |
| Devour Life | `DEVOUR_LIFE` | Counter |  | Whenever you play a Soul, Summon 1. |
| Dexterity | `DEXTERITY` | Counter | yes | Increases Block gained from cards by X. |
| Diamond Diadem | `DIAMOND_DIADEM` | Single |  | Enemies deal 50% less damage this turn. |
| Die for You | `DIE_FOR_YOU` | Single |  | Osty absorbs all unblocked attack damage. |
| Double Damage | `DOUBLE_DAMAGE` | Counter |  | For the next 2 turns, Attacks deal double damage. |
| Draw Cards Next Turn | `DRAW_CARDS_NEXT_TURN` | Counter |  | At the start of your next turn, draw 1 additional card. |
| Drum of Battle | `DRUM_OF_BATTLE` | Counter |  | At the start of your turn, Exhaust the top 2 cards of your Draw Pile. |
| Duplication | `DUPLICATION` | Counter |  | Your next 2 cards are played an extra time. |
| Echo Form | `ECHO_FORM` | Counter |  | The first 2 cards you play each turn are played an extra time. |
| Energy Next Turn | `ENERGY_NEXT_TURN` | Counter |  | Gain additional Energy next turn. |
| Enrage | `ENRAGE` | Counter |  | Whenever you play a Skill, gains 2 Strength. |
| Entropy | `ENTROPY` | Counter |  | At the start of your turn, Transform 1 card in your Hand. |
| Envenom | `ENVENOM` | Counter |  | Whenever you deal unblocked attack damage, apply 1 Poison. |
| Escape Artist | `ESCAPE_ARTIST` | Counter |  | Tries to escape the combat after 2 turns. |
| Fan of Knives | `FAN_OF_KNIVES` | Single |  | Shivs hit ALL enemies. |
| Fasten | `FASTEN` | Counter |  | Gain an additional 4 Block from Defend cards. |
| Feel No Pain | `FEEL_NO_PAIN` | Counter |  | Whenever a card is Exhausted, gain 3 Block. |
| Feral | `FERAL` | Counter |  | The first 2 times you play a 01 Energy Attack each turn, return it to your Hand. |
| Flame Barrier | `FLAME_BARRIER` | Counter |  | Whenever you are attacked this turn, deal 4 damage back. |
| Flutter | `FLUTTER` | Counter |  | Receives 50% less damage from Attacks. Deal attack damage X times to Stun it. |
| Focus | `FOCUS` | Counter | yes | Increases the effectiveness of Orbs by X. |
| Forbidden Grimoire | `FORBIDDEN_GRIMOIRE` | Counter |  | At the end of combat, remove a card from your Deck. |
| Foregone Conclusion | `FOREGONE_CONCLUSION` | Counter |  | Next turn, put 3 cards from your Draw Pile into your Hand. |
| Free Attack | `FREE_ATTACK` | Counter |  | Your next 2 Attacks cost 0 Energy. |
| Free Power | `FREE_POWER` | Counter |  | The next 2 Powers you play cost 0 Energy. |
| Free Skill | `FREE_SKILL` | Counter |  | The next 2 Skills you play cost 0 Energy. |
| Friendship | `FRIENDSHIP` | Counter |  | Gain 1 Energy at the start of each turn. |
| Furnace | `FURNACE` | Counter |  | At the start of your turn, Forge 5. |
| Galvanic | `GALVANIC` | Counter |  | Powers are afflicted with Galvanized. |
| Genesis | `GENESIS` | Counter |  | At the start of your turn, gain 1 Star. |
| Gigantification | `GIGANTIFICATION` | Counter |  | The next 2 Attacks you play deal triple damage. |
| Grasp | `GRASP` | Single |  | Whenever you play a card, lose 1 Energy. |
| Gravity | `GRAVITY` | Counter |  | Whenever you play a card this turn, deal 2 damage to ALL enemies. |
| Guarded | `GUARDED` | Single |  | Take half damage from enemies. |
| Hailstorm | `HAILSTORM` | Counter |  | At the end of your turn, if you have Frost, deal 6 damage to ALL enemies. |
| Hammer Time | `HAMMER_TIME` | Single |  | Whenever you Forge, all allies Forge as well. |
| Hard to Kill | `HARD_TO_KILL` | Counter |  | Reduce all damage taken and HP lost by this creature to 9. |
| Hardened Shell | `HARDENED_SHELL` | Counter |  | This creature cannot lose more than X HP each turn. |
| Hatch | `HATCH` | Counter |  | Hatches after X turns. |
| Haunt | `HAUNT` | Counter |  | Whenever you play a Soul, a random enemy loses 3 HP. |
| Heist | `HEIST` | Counter |  | When killed, returns all the stolen Gold. |
| Hello World | `HELLO_WORLD` | Counter |  | At the start of your turn, add 1 random Common card into your Hand. |
| Hellraiser | `HELLRAISER` | Single |  | Whenever you draw a card containing "Strike", it is played against a random enemy. |
| High Voltage | `HIGH_VOLTAGE` | Counter |  | At the start of this creature's turn, it gains X Strength. |
| Hunger | `HUNGER` | Single |  | Whenever you play an Attack or Skill, it is Exhausted. |
| Illusion | `ILLUSION` | Single |  | When this dies, it revives next turn at full HP. |
| Improvement | `IMPROVEMENT` | Counter |  | At the end of combat, Upgrade a random card. |
| Inferno | `INFERNO` | Counter |  | At the start of your turn, lose 0 HP. Whenever you lose HP on your turn, deal X damage to ALL enemies. |
| Infested | `INFESTED` | Single |  | Upon dying, summons... something. |
| Infinite Blades | `INFINITE_BLADES` | Counter |  | At the start of your turn, add 2 Shivs into your Hand. |
| Intangible | `INTANGIBLE` | Counter |  | Reduce all damage taken and HP loss to 1 this turn. |
| Intercept | `INTERCEPT` | Single |  | You are covering another player. All attacks that would be directed towards them are redirected towards you. |
| Iteration | `ITERATION` | Counter |  | The first time you draw a Status each turn, draw more cards. |
| Juggernaut | `JUGGERNAUT` | Counter |  | Whenever you gain Block, deal 5 damage to a random enemy. |
| Juggling | `JUGGLING` | Counter |  | Add a copy of the third Attack you play each turn into your Hand. |
| Leadership | `LEADERSHIP` | Counter |  | All other allies deal 1 additional damage. |
| Lethality | `LETHALITY` | Counter |  | The first Attack each turn deals 50% additional damage. |
| Lightning Rod | `LIGHTNING_ROD` | Counter |  | At the start of the next 2 turns, Channel 1 Lightning. |
| Loop | `LOOP` | Counter |  | At the start of your turn, trigger the passive ability of your next Orb. |
| Machine Learning | `MACHINE_LEARNING` | Counter |  | At the start of your turn, draw 1 additional card. |
| Master Planner | `MASTER_PLANNER` | Single |  | When you play a Skill, it gains Sly. |
| Mayhem | `MAYHEM` | Counter |  | At the start of your turn, play the next 2 top cards of your Draw Pile. |
| Minion | `MINION` | Single |  | Minions abandon combat without their leader. |
| Monarch's Gaze | `MONARCHS_GAZE` | Counter |  | Whenever you attack an enemy, it loses 1 Strength this turn. |
| Monologue | `MONOLOGUE` | None |  | Whenever you play a card this turn, gain 1 Strength this turn. Currently granting 0 Strength. |
| Necro Mastery | `NECRO_MASTERY` | Counter |  | Whenever Osty loses HP, ALL enemies lose that much HP as well. |
| Nemesis | `NEMESIS` | Single |  | At the end of every other turn, gains Intangible 1. |
| Nightmare | `NIGHTMARE` | Counter |  | Add 2 [Card] cards into your Hand next turn. |
| Nostalgia | `NOSTALGIA` | Counter |  | The first 2 Attacks or Skills you play each turn are placed on top of your Draw Pile. |
| Noxious Fumes | `NOXIOUS_FUMES` | Counter |  | At the start of your turn, apply 2 Poison to ALL enemies. |
| One-Two Punch | `ONE_TWO_PUNCH` | Counter |  | Your next 2 Attacks are played an extra time this turn. |
| Orbit | `ORBIT` | Counter |  | Every 4 Energy you spend, gain 1 Energy. |
| Outbreak | `OUTBREAK` | Counter |  | Every 3 times you apply Poison, deal X damage to ALL enemies. |
| Pagestorm | `PAGESTORM` | Counter |  | Whenever you draw an Ethereal card, draw 1 card. |
| Painful Stabs | `PAINFUL_STABS` | Counter |  | Shuffle 1 Wound into your Discard Pile each time you receive unblocked attack damage. |
| Pale Blue Dot | `PALE_BLUE_DOT` | Counter |  | If you play 5 or more cards in a turn, draw X additional cards at the start of your next turn. |
| Panache | `PANACHE` | Counter |  | If you play 5 more cards this turn, deal X damage to ALL enemies. |
| Paper Cuts | `PAPER_CUTS` | Counter |  | Whenever this creature deals unblocked attack damage to you, you lose X Max HP. |
| Parry | `PARRY` | Counter |  | Whenever you play Sovereign Blade, gain 8 Block. |
| Personal Hive | `PERSONAL_HIVE` | Counter |  | Whenever this enemy is hit by an Attack, add Dazed into your Draw Pile. |
| Phantom Blades | `PHANTOM_BLADES` | Counter |  | Shivs gain Retain. The first Shiv you play each turn deals 9 additional damage. |
| Pillar of Creation | `PILLAR_OF_CREATION` | Counter |  | Whenever you create a card, gain 5 Block. |
| Plating | `PLATING` | Counter |  | At the end of your turn, gain X Block. Plating is reduced by 1 at the start of your turn. |
| Possess Speed | `POSSESS_SPEED` | Single |  | When killed, return all stolen Dexterity to the player. |
| Possess Strength | `POSSESS_STRENGTH` | Single |  | When killed, return all stolen Strength to the player. |
| Prep Time | `PREP_TIME` | Counter |  | At the start of your turn, gain 4 Vigor. |
| Pyre | `PYRE` | Counter |  | Gain 1 Energy at the start of each turn. |
| Radiance | `RADIANCE` | Counter |  | Gain additional 1 Energy for the next 2 turns. |
| Rage | `RAGE` | Counter |  | Whenever you play an Attack this turn, gain 3 Block. |
| Rampart | `RAMPART` | Counter |  | At the start of the player's turn, Turret Operator gains 25 Block. |
| Ravenous | `RAVENOUS` | Counter |  | When an enemy dies, Corpse Slug immediately eats it, becoming Stunned and gaining Strength equal to the visible Ravenous amount. |
| Reaper Form | `REAPER_FORM` | Counter |  | Whenever Attacks deal damage, they also apply 2 times that much Doom. |
| Reattach | `REATTACH` | Single |  | If other segments are still alive, revives in 2 turns with 25 HP. |
| Rebound | `REBOUND` | Counter |  | The next 2 cards you play this turn are placed on the top of your Draw Pile. |
| Reflect | `REFLECT` | Counter |  | Blocked damage is reflected to your attacker. |
| Regen | `REGEN` | Counter |  | Regen heals HP at the end of your turn. Each turn, Regen is reduced by 1. |
| Retain Hand | `RETAIN_HAND` | Counter |  | Retain your Hand for the next 2 turns. |
| Ritual | `RITUAL` | Counter |  | Gain Strength at the end of your turn. |
| Rolling Boulder | `ROLLING_BOULDER` | Counter |  | At the start of your turn, deal X damage to ALL enemies and increase this damage by 5. |
| Royalties | `ROYALTIES` | Counter |  | At the end of combat, gain 25 Gold. |
| Rupture | `RUPTURE` | Counter |  | Whenever you lose HP on your turn, gain 1 Strength. |
| Sandpit | `SANDPIT` | Counter |  | In 2 turns, you will be eaten and die. |
| Scrutiny | `SCRUTINY` | Single |  | You cannot draw additional cards during your turn. |
| Seeking Edge | `SEEKING_EDGE` | Single |  | Sovereign Blade now hits ALL enemies. |
| Self-Forming Clay | `SELF_FORMING_CLAY` | Counter |  | Gain 3 Block next turn. |
| Sentry Mode | `SENTRY_MODE` | Counter |  | At the start of your turn, add 1 Sweeping Gaze into your Hand. |
| Serpent Form | `SERPENT_FORM` | Counter |  | Whenever you play a card, deal 4 damage to a random enemy. |
| Shadow Step | `SHADOW_STEP` | Counter |  | For the next 2 turns after this one, Attacks deal double damage. |
| Shadowmeld | `SHADOWMELD` | Counter |  | Double your Block gain this turn 2 times. |
| Shroud | `SHROUD` | Counter |  | Whenever you apply Doom, gain 3 Block. |
| Signal Boost | `SIGNAL_BOOST` | Counter |  | Your next 2 Powers are played an extra time. |
| Skittish | `SKITTISH` | Counter |  | The first time this creature is hit each turn, it gains X Block. |
| Sleight of Flesh | `SLEIGHT_OF_FLESH` | Counter |  | Whenever you apply a debuff to an enemy, they take 13 damage. |
| Slippery | `SLIPPERY` | Counter |  | The next 2 times this creature loses HP, it only loses 1 HP instead. |
| Slumber | `SLUMBER` | Counter |  | Awakens upon taking turns or losing HP 3 times. |
| Smokestack | `SMOKESTACK` | Counter |  | Whenever you create a Status, deal damage to ALL enemies. |
| Sneaky | `SNEAKY` | Counter |  | Whenever another player attacks an enemy, gain Block. |
| Soar | `SOAR` | Single |  | Receives 50% less attack damage until it lands. |
| Spectrum Shift | `SPECTRUM_SHIFT` | Counter |  | At the start of your turn, add 1 random Colorless card into your Hand. |
| Speedster | `SPEEDSTER` | Counter |  | Whenever you draw a card during your turn, deal 1 damage to ALL enemies. |
| Spinner | `SPINNER` | Counter |  | At the start of your turn, Channel 1 Glass. |
| Spirit of Ash | `SPIRIT_OF_ASH` | Counter |  | Whenever you play an Ethereal card, gain 4 Block. |
| Stampede | `STAMPEDE` | Counter |  | At the end of your turn, 1 random Attack in your Hand is played against a random enemy. |
| Star Next Turn | `STAR_NEXT_TURN` | Counter |  | Gain 1 1 Star next turn. |
| Steam Eruption | `STEAM_ERUPTION` | Counter |  | When killed, deals damage at the end of your next turn. |
| Stock | `STOCK` | Counter |  | When killed, a new Axebot is summoned in its place. |
| Storm | `STORM` | Counter |  | Whenever you play a Power, Channel 1 Lightning. |
| Stratagem | `STRATAGEM` | Counter |  | Whenever you shuffle your Draw Pile, choose 1 card from it to put into your Hand. |
| Strength | `STRENGTH` | Counter | yes | Increases attack damage by X. |
| Subroutine | `SUBROUTINE` | Counter |  | Whenever you play a Power, gain 1 Energy. |
| Suck | `SUCK` | Counter |  | Whenever this creature deals unblocked attack damage, it gains X Strength. |
| Summon Next Turn | `SUMMON_NEXT_TURN` | Counter |  | At the start of your next turn, Summon 2. |
| Surprise | `SURPRISE` | Single |  | Something is off about this creature... |
| Swipe | `SWIPE` | Single |  | Upon killing this enemy, the stolen card is returned. |
| Sword Sage | `SWORD_SAGE` | Counter |  | Sovereign Blade now hits 1 additional time. |
| Tank | `TANK` | Single |  | Take double damage from enemies. Allies take half damage from enemies. |
| Temporary Dexterity | `ANTICIPATE` | Counter |  | Gain Dexterity until the end of this turn. |
| Temporary Dexterity | `HELICAL_DART` | Counter |  | Gain Dexterity until the end of this turn. |
| Temporary Dexterity | `SPEED_POTION` | Counter |  | Gain Dexterity until the end of this turn. |
| Temporary Focus | `FOCUSED_STRIKE` | Counter |  | Gain Focus until the end of this turn. |
| Temporary Focus | `HOTFIX` | Counter |  | Gain Focus until the end of this turn. |
| Temporary Focus | `SYNCHRONIZE` | Counter |  | Gain Focus until the end of this turn. |
| Temporary Strength | `COORDINATE` | Counter |  | Gain Strength until the end of this turn. |
| Temporary Strength | `FEEDING_FRENZY` | Counter |  | Gain Strength until the end of this turn. |
| Temporary Strength | `FLEX_POTION` | Counter |  | Gain Strength until the end of this turn. |
| Temporary Strength | `REPTILE_TRINKET` | Counter |  | Gain Strength until the end of this turn. |
| Temporary Strength | `SETUP_STRIKE` | Counter |  | Gain Strength until the end of this turn. |
| Territorial | `TERRITORIAL` | Counter |  | At the end of its turn, gains 1 Strength. |
| The Bomb | `THE_BOMB` | Counter |  | At the end of 3 turns, deal 40 damage to ALL enemies. |
| The Hunt | `THE_HUNT` | Counter |  | Gain 1 additional card reward at the end of combat. |
| The Sealed Throne | `THE_SEALED_THRONE` | Counter |  | Whenever you play a card, gain 1 Star. |
| Thievery | `THIEVERY` | Counter |  | Steals Gold when Attacking. |
| Thorns | `THORNS` | Counter |  | When hit by an attack, deal damage back. |
| Thunder | `THUNDER` | Counter |  | Whenever you Evoke Lightning, deal 8 damage to each enemy hit. |
| Time Limit | `BATTLEWORN_DUMMY_TIME_LIMIT` | Counter |  | You have 3 more turns to defeat the Battleworn Dummy. |
| Tools of the Trade | `TOOLS_OF_THE_TRADE` | Counter |  | At the start of your turn, draw 1 card and discard 1 card. |
| Toric Toughness | `TORIC_TOUGHNESS` | Counter |  | Gain 5 Block at the start of the next 2 turns. |
| Tracking | `TRACKING` | Counter |  | Weak enemies take 2 times more damage from Attacks. |
| Trash to Treasure | `TRASH_TO_TREASURE` | Counter |  | Whenever you create a Status, Channel 2 random Orbs. |
| Tyranny | `TYRANNY` | Counter |  | At the start of your turn, draw 2 cards and Exhaust 2 cards from your Hand. |
| Unmovable | `UNMOVABLE` | Counter |  | The first 2 times you gain Block from a card each turn, double the amount gained. |
| Veilpiercer | `VEILPIERCER` | Counter |  | The next Ethereal card you play costs 0. |
| Vicious | `VICIOUS` | Counter |  | Whenever you apply Vulnerable, draw 1 card. |
| Vigor | `VIGOR` | Counter |  | This creature's next Attack deals X additional damage. |
| Vital Spark | `VITAL_SPARK` | Counter |  | The first time this creature takes Attack damage each turn, the attacker gains 1 Energy. |
| Void Form | `VOID_FORM` | Counter |  | The first 2 cards you play each turn are free to play. |
| Well-Laid Plans | `WELL_LAID_PLANS` | Counter |  | At the end of your turn, Retain up to 1 card. |

---
<!-- META-AGENT NOTES — do not edit above this line -->
## Strategy Notes

- Artifact negates one debuff application per stack; a multi-stack Vulnerable card can remove only one Artifact stack and apply no Vulnerable.
