# Ironclad Run 3 - Floor 1

- Outcome: in progress, Act 1 floor 1.
- Neow: chose Neow's Torment over Phial Holster and Scroll Boxes.
- Reasoning: Neow's Fury adds immediate 1-cost damage and discard recursion without losing gold or forcing a random three-card pack. Phial Holster is solid but potion value is uncertain; Scroll Boxes costs all starting gold and can bloat the deck.
- Current deck: starter Ironclad deck plus Neow's Fury.
- Current relics: Burning Blood, Neow's Torment.
- Current resources: 80/80 HP, 99 gold, no potions.

## Floor 2 - Monster

- Encounter: Seapunk. KB says it cycles Sea Kick 11, Spinning Kick 2x4, then Bubble Burp for block + Strength.
- Result: won at 72/80 after Burning Blood.
- Combat notes: used two Strikes plus one Defend on turn 1, accepting 6 net damage because Burning Blood would cover it. On turn 2, played Bash into Neow's Fury for 23 damage through Vulnerable, leaving Seapunk at 9 and killing it before Bubble Burp with a Vulnerable Strike.
- Rewards: took Inflame over Headbutt and Tremble; claimed Explosive Ampoule and 10 gold.
- Reasoning: Inflame gives persistent Strength for the attack-heavy starter deck plus Neow's Fury. Tremble is strong but overlaps with Bash early; Headbutt is good damage but less important than scaling.
- Current resources: 72/80 HP, 109 gold, Explosive Ampoule.

## Floor 3 - Monster

- Encounter: two Corpse Slugs. KB says they are staggered and Ravenous gives the survivor Strength plus Stun when one dies.
- Result: won at 78/80 after Burning Blood.
- Combat notes: used Explosive Ampoule for 10 AoE, then killed the 26-HP slug with Bash plus Strike, triggering Ravenous on the survivor and canceling incoming damage with Stun. Killed the 17-HP survivor next turn with three Strikes before its 12-damage attack.
- Rewards: took Breakthrough over Cinder and Taunt; claimed Speed Potion and 16 gold.
- Reasoning: Breakthrough gives 1-cost AoE that scales with Inflame and Burning Blood offsets its 1 HP cost. Cinder has higher single-target damage but random exhaust; Taunt is useful block/Vulnerable but the deck still wants efficient damage.
- Current resources: 78/80 HP, 125 gold, Speed Potion.

## Floor 4 - Event: The Legends Were True

- Choice: took Nab the Map for Spoils Map.
- Reasoning: event KB says Spoils Map marks 600 extra gold in the next Act, while the alternate option costs 8 HP for a random potion. At 78/80 HP with Speed Potion already held, the large Act 2 economy payoff was worth one unplayable card.
- Current resources: 78/80 HP, 125 gold, Speed Potion.

## Floor 5 - Monster

- Encounter: weak two-Toadpole fight. KB says the front Toadpole starts with Spiken while the back uses Whirl, so the Whirl attacker should die first.
- Result: won at 70/80 after Burning Blood.
- Combat notes: opened with Breakthrough and two Strikes into the attacking Toadpole, leaving it at 1 HP because Breakthrough plus two Strikes is 21 damage. Took 7, then killed the Thorns Toadpole with Bash plus Strike to prevent its 3x3 attack, paying 4 Thorns damage. Finished the 1-HP survivor with Neow's Fury and paid 2 Thorns.
- Rewards: took Spite over a second Breakthrough and Forgotten Ritual; claimed 20 gold.
- Reasoning: Spite is 0-cost damage that pairs with Breakthrough's player-turn HP loss and scales well with Inflame. A second Breakthrough was redundant; Forgotten Ritual has only Neow's Fury as a reliable enabler right now.
- Current resources: 70/80 HP, 145 gold, Speed Potion.

## Floor 6 - Monster

- Encounter: Haunted Ship. KB says it always opens with Haunt, shuffling 5 Dazed into the discard pile, then attacks with Ramming Speed for 10 + Weak and follows with 4x3 or Swipe.
- Result: won at 65/80 after Burning Blood.
- Combat notes: pushed 22 damage on the no-damage Haunt turn with Neow's Fury plus two Strikes. Took the 10 + Weak turn after Bash plus Strike set up Vulnerable. On turn 3, Inflame into Breakthrough enabled Spite's double-hit condition and killed through Weak before the 4x3 attack.
- Rewards: took Aggression over Twin Strike and Expect a Fight; claimed 15 gold.
- Reasoning: Aggression is a rare 1-cost power that recurs and upgrades attacks each turn, matching the deck's attack-heavy shape and helping against status pollution. Twin Strike is fine damage but lower impact; Expect a Fight needs more attack density and an upgrade.
- Current resources: 65/80 HP, 160 gold, Speed Potion.

## Floor 7 - Rest Site

- Choice: Smith, upgraded Aggression.
- Reasoning: 65/80 HP was healthy enough to skip resting. Aggression's upgrade makes it Innate, giving the deck immediate attack recursion instead of waiting to draw it through Spoils Map and larger combat decks.
- Current resources: 65/80 HP, 160 gold, Speed Potion.

## Floor 8 - Shop

- Purchases: bought Blood Wall for 26 gold, Pommel Strike for 49 gold, and Dismantle for 79 gold.
- Skipped: card removal, Inferno, Havoc, Jack of All Trades, and unaffordable relics/potions.
- Reasoning: forced elite next, so immediate combat power mattered most. Dismantle is a strong Bash/Vulnerable payoff, Pommel Strike adds damage plus draw, and discounted Blood Wall gives large block while also enabling Spite through player-turn HP loss. Removal was good but lower immediate value than three efficient cards.
- Current resources: 65/80 HP, 6 gold, Speed Potion.

## Floor 9 - Elite

- Encounter: four Phantasmal Gardeners. KB says they cycle Bite, Lash, Flail, and Enlarge, each starting at a different point; live fight showed Skittish for 6 block on first hit each turn.
- Result: won at 60/80 after Burning Blood.
- Combat notes: used Speed Potion on turn 1, but API lag caused a second Defend before Breakthrough; corrected by playing Breakthrough afterward. Blood Wall plus Breakthrough+ on turn 2 blocked nearly all 17 incoming and put all enemies into kill range. Spite into Skittish did not kill as expected because Skittish added block on the target. Aggression recurred an upgraded Breakthrough on turn 3, which killed all four.
- Rewards: took Battle Trance over True Grit and Juggling; claimed Pen Nib, Attack Potion, and 42 gold.
- Reasoning: Battle Trance gives 0-cost draw for a growing deck with Spoils Map and multiple powers. True Grit was strong but needs an upgrade; Juggling added more setup.
- Current resources: 60/80 HP, 48 gold, Attack Potion, Pen Nib.

## Floor 10 - Treasure

- Result: chest screen showed Bag of Preparation, but `claim_reward` was not valid on the treasure screen and proceeding left the player state with no Bag of Preparation relic.
- Live resources after proceed: 60/80 HP, 92 gold, Attack Potion, relics Burning Blood / Neow's Torment / Pen Nib.
- Harness lesson: treasure relics may need a treasure-specific claim action; verify relics in player state after proceeding.

## Floor 11 - Event: The Sunken Statue

- Choice: Dive into the Water for 108 gold, losing 7 HP.
- Reasoning: event KB says Sword of Stone transforms only after defeating 5 elites; this path is unlikely to support that. The gold is immediate and useful with a late shop ahead.
- Current resources: 53/80 HP, 200 gold, Attack Potion.

## Floor 12 - Monster

- Encounter: three Two-Tailed Rats. KB says the group opens with Scratch, Disease Bite, and Screech, then can summon after at least two turns.
- Result: won at 48/80 after Burning Blood.
- Combat notes: opened with Aggression+ and Blood Wall to full-block the first attack wave, then used Battle Trance to find Breakthrough and Spite for multi-target pressure. Neow's Fury left the last rat at 2 HP, causing one extra 8-damage hit, but a Strike+ killed it before Call for Backup resolved.
- Rewards: took Anger over Cinder and Havoc; claimed 10 gold.
- Reasoning: Anger is a 0-cost attack that benefits from Inflame and helps advance Pen Nib without spending energy. Cinder's random exhaust and Havoc's uncontrolled top-card exhaust were less reliable with key powers, Battle Trance, and Spoils Map in the deck.
- Current resources: 48/80 HP, 210 gold, Attack Potion, Pen Nib counter 8.

## Floor 13 - Rest Site

- Choice: Rest, healing from 48/80 to 72/80.
- Reasoning: Soul Fysh's KB shows a fixed damage cycle with 16 damage on turn 2 and 11 plus 3 Vulnerable on turn 5. The deck has enough damage upgrades for Act 1, while low HP would make a bad Beckon/status draw cycle dangerous.
- Current resources: 72/80 HP, 210 gold, Attack Potion, Pen Nib counter 8.

## Floor 14 - Event: Room Full of Cheese

- Choice: Search, losing 14 HP to obtain The Chosen Cheese.
- Reasoning: event KB says Gorge adds 2 of 8 random common cards, while Search gives the relic for 14 HP. The Chosen Cheese KB says it grants 1 Max HP at the end of each combat. Because the current path offers a shop and then a rest site before Soul Fysh, the HP loss can be repaired while avoiding random deck bloat.
- Current resources: 58/80 HP, 210 gold, Attack Potion, relics Burning Blood / Neow's Torment / Pen Nib / The Chosen Cheese.

## Floor 15 - Shop

- Purchases: bought Membership Card and Speed Potion.
- Skipped: Conflagration, Unrelenting, Havoc, Blood Wall, Inferno, Prowess, Hidden Gem, Red Skull, Strike Dummy, Fairy in a Bottle, Attack Potion, and card removal.
- Reasoning: Membership Card's permanent 50% discount has high upside with Spoils Map's expected 600-gold Act 2 payout. Speed Potion used the remaining discounted gold without adding deck bloat and gives a tactical block tool for Soul Fysh's damage turns. The other buys were either too expensive after Membership Card or lower impact than the future shop economy.
- Current resources: 58/80 HP, 3 gold, Attack Potion, Speed Potion, relics Burning Blood / Neow's Torment / Pen Nib / The Chosen Cheese / Membership Card.

## Floor 16 - Rest Site

- Choice: Rest, healing from 58/80 to 80/80.
- Reasoning: final rest before Soul Fysh. Full HP plus Attack Potion and Speed Potion is safer than one more upgrade against the boss's fixed damage/status cycle.
- Current resources: 80/80 HP, 3 gold, Attack Potion, Speed Potion, Pen Nib counter 8.

## Floor 17 - Boss: Soul Fysh

- Encounter: Soul Fysh. KB says its cycle is Beckon, De-Gas, Gaze, Fade, Scream.
- Result: won at 77/81 after Burning Blood and The Chosen Cheese.
- Combat notes: opened with Aggression+ and attacks, then used Speed Potion on the 16-damage De-Gas turn to turn Defends into 10 Block each. Bash into Dismantle+ was the main damage engine, with Anger/Spite/Neow's Fury closing through Vulnerable. Attack Potion's selection appeared after a delayed state transition; picking Spite produced extra 0-cost damage but the potion timing was awkward.
- Tactical lesson: poll after each meaningful play in boss turns because the API can delay card selection screens and state updates. The floor 13 rest was too conservative after re-reading GUIDE.md; campfire default is smith except the last pre-boss rest, which GUIDE says is a universal rest.
- Rewards: took Cruelty over One-Two Punch and Juggernaut; claimed 100 gold.
- Reasoning: Cruelty directly supports the Bash/Dismantle Vul-chain plan and gives persistent scaling against Vulnerable enemies. One-Two Punch is strong with Pen Nib but more timing-dependent; Juggernaut does not match the deck's attack/Vulnerable focus.
- Current resources: 77/81 HP, 103 gold, no potions, Pen Nib counter 5.

## Floor 18 - Ancient: Pael

- Choice: took Pael's Blood over Pael's Tears and Pael's Claw.
- Reasoning: Pael's Blood gives +1 card draw each turn, matching GUIDE.md's draw priority and helping find Aggression+, Cruelty, Bash, and Dismantle. Pael's Tears requires floating energy, which this low-curve attack deck rarely does, and Pael's Claw invests in starter Defends rather than the deck's Vulnerable burst plan.
- Current resources: 81/81 HP, 103 gold, no potions, relics Burning Blood / Neow's Torment / Pen Nib / The Chosen Cheese / Membership Card / Pael's Blood.

## Floor 19 - Monster: Thieving Hopper

- Encounter: Thieving Hopper. KB says it follows Thievery, Flutter, Hat Trick, Nab, then Escape; stolen cards are returned only if it dies before fleeing.
- Result: won at 70/82 after Burning Blood and The Chosen Cheese; recovered stolen Dismantle.
- Combat notes: Hopper stole Dismantle from the draw/discard pile. On the Hat Trick turn, Breakthrough, two Spite hits, Neow's Fury, and Strike+ gave enough attack-damage hits to remove Flutter and stun the enemy, preventing 21 incoming damage. Anger+ killed it on the next turn before Escape.
- Rewards: reclaimed Dismantle, took 15 gold, and picked True Grit+ over Armaments+ and Tremble.
- Reasoning: True Grit+ was already upgraded, and its KB notes it is a high-priority upgraded pick. It adds efficient block plus selective exhaust for Spoils Map, basic cards, or bad status cards in longer Act 2 fights. Tremble was tempting with Cruelty, but Bash and Dismantle already provide Vulnerable payoff.
- Pathing note: after Pael, the intended early-shop route did not remain available in the API map options, so this node became a monster path. Re-check the map before committing further.
- Current resources: 70/82 HP, 118 gold, no potions, Pen Nib counter 5.

## Floor 20 - Shop

- Purchases: bought Block Potion, Swift Potion, Taunt, and Shrug It Off for 110 total gold.
- Skipped: Self-Forming Clay, Punch Dagger, Intimidating Helmet, Juggernaut, Fasten, Salvo, Twin Strike, Sword Boomerang, Attack Potion, and card removal.
- Reasoning: Self-Forming Clay had good synergy with Breakthrough and Blood Wall, but spending 117 of 118 gold would leave no potion safety. Shrug It Off's KB rates it as a strong take without needing an upgrade, and Taunt gives block plus Vulnerable support for Cruelty and Dismantle. Swift Potion and Block Potion cover bad Act 2 turns better than another speculative attack.
- Current resources: 70/82 HP, 8 gold, Block Potion, Swift Potion, Pen Nib counter 5.

## Floor 21 - Event: Colorful Philosophers

- Choice: chose Green for Silent card reward screens.
- Picks: took The Hunt over Abrasive and Accelerant; took Dash over Outbreak and Expertise; took Piercing Wail over Dodge and Roll and Blade Dance.
- Reasoning: the event KB lists each color as granting three off-class cards, and live state showed each as a skippable reward screen. Green was chosen because Silent cards were more likely to offer generic block, draw, weak/strength reduction, or cheap attacks than Defect orb-dependent cards or unknown Regent cards. The Hunt gives exhaust damage with Fatal upside, Dash adds block plus damage, and Piercing Wail is a strong one-turn answer to large attack turns.
- Current resources: 70/82 HP, 8 gold, Block Potion, Swift Potion, Pen Nib counter 5.

## Floor 22 - Monster: Tunneler

- Encounter: Tunneler. KB says it opens with Bite, then Burrow for 32 Block; while Burrowed, fully breaking its Block stuns it and prevents Attack from Below.
- Result: won at 67/83 after Burning Blood and The Chosen Cheese.
- Combat notes: opened with Taunt, Neow's Fury, and Aggression+, taking 6 damage. On Burrow, spent the turn on Breakthrough, Pommel Strike, and Strike+ to set Pen Nib to 9. The next turn used Inflame, Pen Nib The Hunt, Anger, Spite, and Strike+ to break all Burrow block, stun Tunneler, and avoid the 23-damage attack. Finished after one small Bite turn.
- Rewards: took 10 gold, replaced Block Potion with Dexterity Potion, and picked Shrug It Off over Body Slam and Breakthrough.
- Reasoning: a second Shrug is still strong because it blocks while replacing itself; Body Slam is not upgraded and the deck is not committed to block-damage, while another Breakthrough would add more HP-loss AoE than needed. Dexterity Potion is a better long-fight potion than Block Potion now that the deck has Shrug It Off, True Grit+, Blood Wall, Dash, Defends, and Piercing Wail support.
- Current resources: 67/83 HP, 18 gold, Dexterity Potion, Swift Potion, Pen Nib counter 6.

## Floor 23 - Monster: Bowlbugs and Slumbering Beetle

- Encounter: Bowlbug (Rock), Bowlbug (Silk), and Slumbering Beetle. Bowlbugs KB says Rock stuns only if Headbutt damage is fully prevented, and Silk alternates Weak with 4x2. Slumbering Beetle KB says it wakes after Slumber is gone and then Rolls Out every turn for 16 while gaining 2 Strength.
- Result: won at 8/84 after Burning Blood and The Chosen Cheese.
- Combat notes: used Dexterity Potion immediately for a long block-heavy fight. Battle Trance applied No Draw, so the Swift Potion attempted afterward did not draw. Rock was killed before its repeated Headbutts got out of hand, but failing to fully block one Headbutt by 1 damage missed a stun. Beetle woke while both supports were still alive and scaled to 26 damage per turn. The fight was stabilized only by killing Silk, using Bash/Vulnerable and Pen Nib damage, then finishing Beetle at 1 HP with Dash.
- Rewards: claimed 19 gold and Powdered Demise; took Body Slam+ over Breakthrough+ and Forgotten Ritual.
- Reasoning: Body Slam+ is now a strong zero-cost damage card because the deck has Blood Wall, Dash, True Grit+, Taunt, Shrug It Off, Defends, Dexterity scaling, and frequent turns where blocking is mandatory. Forgotten Ritual has Exhaust synergy but is conditional; Breakthrough+ would add more HP-loss AoE at a dangerously low HP total.
- Tactical lesson: Slumbering Beetle plus Bowlbug supports punishes slow cleanup. Kill or nearly kill supports before the Beetle wakes, and do not use Swift Potion after Battle Trance because No Draw prevents it from helping.
- Current resources: 8/84 HP, 37 gold, Powdered Demise, Pen Nib counter 5. Next node is likely a regular combat before the rest site; if HP stays low, the next campfire is a Rest despite GUIDE.md's default Smith rule.

## Floor 24 - Monster: Spiny Toad

- Encounter: Spiny Toad. KB says it cycles Protruding Spikes, Spike Explosion for 23, then Tongue Lash for 17.
- Result: died on floor 24.
- Combat notes: entered at 8/84 with a forced fight before the next rest site. Used Powdered Demise immediately because the Toad had 117 HP and the fight would otherwise be too long. Played Battle Trance on turn 1, then Aggression+ and Bash before Thorns came online. Turn 2 drew Taunt as the only block card against 23 incoming; Taunt's 7 Block was not enough, and attacking into 5 Thorns at 8 HP was not a viable escape line.
- Death cause: the prior Slumbering Beetle fight left the run at single-digit HP before a forced hallway fight. Spiny Toad's front-loaded 23 damage on turn 2 punished the low HP and a block-light draw.
- Lesson: verify how many forced fights remain before the next rest site before accepting low-HP survival lines. Below 20% HP is already an immediate-rest state in GUIDE.md, but that only helps if the chosen path actually reaches a rest before another combat.
