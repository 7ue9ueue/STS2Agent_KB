---
title: Debuffs
source: https://spire-codex.com/api/powers
generated: true
---

# Debuffs

Structured list of `Debuff` powers from Spire Codex. Descriptions are game text with UI color tags removed.

## Stack Types

- `Counter`: stack count usually tracks charges, amount, or remaining turns depending on the effect text.
- `Single`: present or absent; duplicate applications generally do not create a separate visible stack.
- `None`: no stack value is shown by the source data.

## Common Agent Checks

| Name | ID | Stack | Negative? | Description |
|---|---|---|---|---|
| Confused | `CONFUSED` | Single |  | The costs of your cards are randomized on draw, from 0 to 3. |
| Doom | `DOOM` | Counter |  | At the end of the enemy turn, if this creature has X or less HP, it dies. |
| Frail | `FRAIL` | Counter |  | While Frail, gain 25% less Block from cards. |
| Poison | `POISON` | Counter |  | Poisoned creatures lose HP at the start of their turn. Each turn, Poison is reduced by 1. |
| Slow | `SLOW` | Counter |  | Whenever you play a card, this enemy receives 10% more damage from Attacks this turn. |
| Strangle | `STRANGLE` | Counter |  | Whenever you play a card this turn, this enemy loses 2 HP. |
| Surrounded | `SURROUNDED` | Single |  | Receive 50% more damage if attacked from behind. Use targeting cards or potions to change your orientation. |
| Tangled | `TANGLED` | Counter |  | Attacks cost an additional 1 Energy for 2 turns. |
| Vulnerable | `VULNERABLE` | Counter |  | Receive 50% more damage from Attacks for X turns. |
| Waste Away | `WASTE_AWAY` | Counter |  | Gain 1 less Energy per turn. |
| Weak | `WEAK` | Counter |  | Weakened creatures deal 25% less damage with Attacks. |

## Full List

| Name | ID | Stack | Negative? | Description |
|---|---|---|---|---|
| Biased Cognition | `BIASED_COGNITION` | Counter |  | At the start of your turn, lose 1 Focus. |
| Borrowed Time | `BORROWED_TIME` | Counter |  | Cards cost an additional 1 Energy this turn. |
| Chains of Binding | `CHAINS_OF_BINDING` | Counter |  | The first 3 cards drawn each turn are Afflicted with Bound. |
| Confused | `CONFUSED` | Single |  | The costs of your cards are randomized on draw, from 0 to 3. |
| Conqueror | `CONQUEROR` | Counter |  | Sovereign Blade deals double damage to this creature for the next 2 turns. |
| Constrict | `CONSTRICT` | Counter |  | While the Slithering Strangler is alive, at the end of your turn, take 1 damage. |
| Dampen | `DAMPEN` | None |  | While Magi Knight is alive, ALL your cards are Downgraded. |
| Debilitate | `DEBILITATE` | Counter |  | Vulnerable and Weak are twice as effective for the next 2 turns. |
| Demise | `DEMISE` | Counter |  | At the end of this creature's turn, it loses X HP. |
| Disintegration | `DISINTEGRATION` | Counter |  | At the end of your turn, take 5 damage. |
| Doom | `DOOM` | Counter |  | At the end of the enemy turn, if this creature has X or less HP, it dies. |
| Flanking | `FLANKING` | Counter |  | Other allies deal 2x more attack damage to this enemy this turn. |
| Frail | `FRAIL` | Counter |  | While Frail, gain 25% less Block from cards. |
| Hang | `HANG` | Counter |  | All Hangs deal 2 times more damage to this enemy. |
| Hex | `HEX` | Single |  | While Spectral Knight is alive, ALL your cards are Ethereal. |
| Imbalanced | `IMBALANCED` | Single |  | If this creature's attacks are fully blocked, it becomes Stunned. |
| Knockdown | `KNOCKDOWN` | Counter |  | This creature takes X times the damage from other players this turn. |
| Magic Bomb | `MAGIC_BOMB` | Counter |  | Take 20 damage at the end of your turn. Is cleared if the Magi Knight dies. |
| Mind Rot | `MIND_ROT` | Counter |  | Draw 1 fewer card each turn. |
| Neurosurge | `NEUROSURGE` | Counter |  | At the start of your turn, apply 3 Doom to yourself. |
| No Block | `NO_BLOCK` | Counter |  | You cannot gain Block from cards for 2 turns. |
| No Draw | `NO_DRAW` | Single |  | You may not draw any more cards this turn. |
| No Energy Gain | `NO_ENERGY_GAIN` | Single |  | You cannot gain additional 1 Energy this turn. |
| Oblivion | `OBLIVION` | Counter |  | Whenever you play a card, this enemy gains 1 Doom. |
| Plow | `PLOW` | Counter |  | The first time this creature's HP reaches X or below, it becomes Stunned and loses all its Strength. |
| Poison | `POISON` | Counter |  | Poisoned creatures lose HP at the start of their turn. Each turn, Poison is reduced by 1. |
| Ringing | `RINGING` | Single |  | You can only play 1 card this turn. |
| Shriek | `SHRIEK` | Counter | yes | The first time this creature's HP reaches X or below, it becomes Stunned. |
| Shrink | `SHRINK` | None | yes | This creature's Attacks deal 30% less damage. |
| Sic 'Em | `SIC_EM` | Counter |  | Whenever Osty hits this enemy this turn, Summon 3. |
| Sloth | `SLOTH` | Counter |  | You cannot play more than 3 cards each turn. |
| Slow | `SLOW` | Counter |  | Whenever you play a card, this enemy receives 10% more damage from Attacks this turn. |
| Smoggy | `SMOGGY` | Single |  | You can only play 1 Skill per turn. |
| Strangle | `STRANGLE` | Counter |  | Whenever you play a card this turn, this enemy loses 2 HP. |
| Surrounded | `SURROUNDED` | Single |  | Receive 50% more damage if attacked from behind. Use targeting cards or potions to change your orientation. |
| Tag Team | `TAG_TEAM` | Counter |  | The next Attack another player plays on the enemy is played an extra time. |
| Tangled | `TANGLED` | Counter |  | Attacks cost an additional 1 Energy for 2 turns. |
| Temporary Strength Down | `CRUSH_UNDER` | Counter |  | Lose Strength until the end of this turn. |
| Temporary Strength Down | `DARK_SHACKLES` | Counter |  | Lose Strength until the end of this turn. |
| Temporary Strength Down | `DYING_STAR` | Counter |  | Lose Strength until the end of this turn. |
| Temporary Strength Down | `ENFEEBLING_TOUCH` | Counter |  | Lose Strength until the end of this turn. |
| Temporary Strength Down | `MANGLE` | Counter |  | Lose Strength until the end of this turn. |
| Temporary Strength Down | `MONARCHS_GAZE_STRENGTH_DOWN` | Counter |  | Lose Strength until the end of this turn. |
| Temporary Strength Down | `PIERCING_WAIL` | Counter |  | Lose Strength until the end of this turn. |
| Temporary Strength Down | `SHACKLING_POTION` | Counter |  | Lose Strength until the end of this turn. |
| Tender | `TENDER` | Counter |  | Whenever you play a card, lose 1 Strength and 1 Dexterity this turn. |
| The Gambit | `THE_GAMBIT` | Single |  | If you take unblocked attack damage this combat, die. |
| Vulnerable | `VULNERABLE` | Counter |  | Receive 50% more damage from Attacks for X turns. |
| Waste Away | `WASTE_AWAY` | Counter |  | Gain 1 less Energy per turn. |
| Weak | `WEAK` | Counter |  | Weakened creatures deal 25% less damage with Attacks. |
| Wraith Form | `WRAITH_FORM` | Counter |  | At the start of your turn, lose 1 Dexterity. |
