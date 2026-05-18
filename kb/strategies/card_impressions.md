# Data-Informed Card Impressions

Source: current full win-rate table in [card_winrates.md](card_winrates.md), plus local KB and `analysis/` notes. These stats are reference only. Pick rate and win-rate impact are confounded by act, deck state, player desperation, and rarity; choose by function and synergy first. When numeric values here conflict with [card_winrates.md](card_winrates.md), use [card_winrates.md](card_winrates.md) as the current numeric source, but keep it subordinate to the deck's actual needs.

## How To Use Stats

- High pick rate means players often find a card useful, not that it is always correct.
- Low pick rate does not mean unplayable; some cards are narrow build-arounds.
- Negative win-rate impact does not automatically mean bad. Strong commons like Pommel Strike, Shrug It Off, and Bloodletting are often taken early or by weaker decks, which can depress their with-card win rate.
- Large positive/negative impact is still useful, but only as a supporting signal. High-impact cards deserve a serious look; low-impact cards need a concrete deck/job reason.
- Act pick-rate trends matter: a card picked mostly in Act 1 may be survival frontload, while a card picked in Act 2/3 may be engine completion or boss tech.
- Once the deck beats standard enemies comfortably, card rewards should be judged against the value of drawing existing premium cards sooner. In Act 3, skip is the default unless the card improves boss scaling, draw/energy consistency, one-card defense, or a specific matchup.

## Reward Pacing

- Act 1 builds survival through attacks first: prioritize frontloaded Attack cards, especially attacks with draw, Vulnerable, AoE, or strong single-target damage. Draw, energy, powers, and block support that plan but do not replace early damage; still skip filler. Focus more on simple numbers like apporximated damage and attack per energy. 
- Act 1 exception: against [Waterfall Giant](../enemies/bosses/waterfall_giant.md), value real defense and block upgrades earlier because Steam Eruption and Death Blow require exact block planning.
- Act 1 transition reminders: prioritize cards with great damage per energy or cards that make starter attacks hit harder. Pommel Strike is the premium attack/draw common; Anger is a good 0-cost Act 1 attack bridge and later Doormaker/Dark Embrace counterplay; Tremble is efficient Vulnerable setup; Taunt is block plus Vulnerable; Shrug It Off keeps the deck cycling while covering attack turns.
- Act 1 starter removals are balanced and synergy-aware: Perfected Strike/Hellraiser can reward Strike density, and Tighten-style effects can reward Defend density. In Acts 2/3, default to erasing Strikes first unless a live Strike payoff still needs them.
- Act 2 completes the engine: take cards that add scaling, reliable block, exhaust, energy, or a boss answer. Start skipping cards that only duplicate a solved job. Focus more on cards with great functionality and less on just the numbers. 
- Act 3 refines: if standard enemies are easy, most rewards are deck dilution. Take only cards that scale the potential of existing cards, improve access to the engine, or answer an Act 3 boss script.
- Late upgraded cards are not automatic takes. An upgraded medium attack/block is often worse than drawing Pommel Strike+, Shrug It Off, Bloodletting, Uppercut+, Vicious+, Dark Embrace, Unmovable, or the deck's real payoff sooner.

## High Impact Signal

Base Ironclad cards with at least 400 picks, sorted by win-rate-with-card minus win-rate-when-skipped:

| Card | Rarity | Pick rate | With-card WR | Skipped WR | Impact |
|---|---|---:|---:|---:|---:|
| Offering | Rare | 69.5% | 60.2% | 48.5% | +11.7pp |
| Impervious | Rare | 46.0% | 55.3% | 50.6% | +4.7pp |
| Feel No Pain | Uncommon | 25.9% | 44.9% | 40.9% | +4.0pp |
| Unmovable | Rare | 44.4% | 57.6% | 53.7% | +3.9pp |
| Battle Trance | Uncommon | 54.5% | 45.5% | 42.2% | +3.3pp |
| Crimson Mantle | Rare | 49.4% | 58.5% | 55.2% | +3.3pp |
| Dark Embrace | Rare | 27.0% | 54.7% | 52.3% | +2.4pp |
| Aggression | Rare | 32.6% | 54.2% | 53.5% | +0.7pp |
| Barricade | Rare | 30.0% | 53.2% | 53.0% | +0.2pp |
| Cascade | Rare | 30.8% | 54.5% | 54.4% | +0.1pp |

General impression: the positive-impact list heavily favors premium draw/energy, one-card defense, exhaust payoffs, and durable powers. These are not automatic picks, but they are the cards to re-check before skipping.

## Low Impact Signal

Base Ironclad cards with at least 400 picks, sorted by lowest impact:

| Card | Rarity | Pick rate | With-card WR | Skipped WR | Impact |
|---|---|---:|---:|---:|---:|
| Rampage | Uncommon | 18.7% | 26.7% | 45.3% | -18.6pp |
| Primal Force | Rare | 14.4% | 38.9% | 55.0% | -16.1pp |
| Cinder | Common | 6.0% | 26.9% | 41.4% | -14.5pp |
| Hemokinesis | Uncommon | 15.3% | 30.1% | 43.8% | -13.7pp |
| Thunderclap | Common | 15.8% | 29.7% | 42.7% | -13.0pp |
| Conflagration | Rare | 28.1% | 43.3% | 55.8% | -12.5pp |
| Breakthrough | Common | 20.0% | 31.1% | 42.7% | -11.6pp |
| Infernal Blade | Uncommon | 18.7% | 32.0% | 43.6% | -11.6pp |
| Iron Wave | Common | 11.8% | 31.5% | 42.4% | -10.9pp |
| Unrelenting | Uncommon | 20.9% | 32.8% | 43.6% | -10.8pp |
| Havoc | Common | 4.8% | 30.3% | 41.1% | -10.8pp |
| Anger | Common | 13.4% | 32.0% | 42.8% | -10.8pp |
| Grapple | Uncommon | 11.8% | 32.2% | 42.9% | -10.7pp |
| Hellraiser | Rare | 40.1% | 45.4% | 55.9% | -10.5pp |
| One-Two Punch | Rare | 33.0% | 44.4% | 54.8% | -10.4pp |

General impression: the low-impact list is full of cards that can be tempting because they solve one visible problem, but they often dilute the deck or require too much support. Take them only when the current act, boss, or template gives a clear reason.

## Strong General Impressions

| Card | Site signal | General impression |
|---|---:|---|
| Offering | 69.5% pick, +11.7pp impact | Premium burst draw/energy. Usually take when HP can support it and the deck converts the turn. |
| Battle Trance | 54.5% pick, +3.3pp impact | Premium draw. Play other draw first because No Draw blocks later draw. |
| Feel No Pain | 25.9% pick, +4.0pp impact | Strong when exhaust is already present or status-clog fights are expected. |
| Unmovable | 44.4% pick, +3.9pp impact | Premium defensive scaling. Upgrade matters because 1-cost setup is much easier. |
| Impervious | 46.0% pick, +4.7pp impact | One-card answer to large attacks; excellent when the deck needs a hard defense button. |
| Dark Embrace | 27.0% pick, +2.4pp impact | Strong exhaust engine and a Doormaker counterplay. Needs enough exhaust to justify the setup. |

## High-Pick Core Cards

| Card | Site signal | General impression |
|---|---:|---|
| Pommel Strike | 45.1% pick | Core attack/draw and one of the best Act 1 transition picks because it gives efficient damage without costing draw quality. Upgrade is a major engine breakpoint. |
| Shrug It Off | 42.0% pick | Core block cantrip and good early pick because it protects draw quality while buying time for high damage-per-energy attacks. Usually good base value, lower smith priority than Pommel/True Grit. |
| Bloodletting | 32.5% pick | Core energy card. Spend HP only when the energy produces real output. |
| Burning Pact | 40.2% pick | Draw plus controlled exhaust; improves late consistency and status-clog matchups. |
| Pyre | 56.0% pick | Powerful energy scaling, but setup timing matters on heavy incoming turns. |
| Colossus | 48.6% pick | Strong defensive rare; better when the deck needs a single-card block solution. |
| Taunt | 34.8% final-deck signal | Good Act 1 transition pick: block plus Vulnerable improves damage per energy from existing attacks and later supports Vicious/Vulnerable plans. |
| Tremble | 42.9% final-deck signal | Good Act 1 transition pick when damage exists or is likely; Vulnerable improves damage per energy for starter attacks, bosses, and elite races. |

## Conditional Build-Arounds

| Card | Site signal | General impression |
|---|---:|---|
| Body Slam | 9.3% pick | Narrow but powerful. Take after large block, Unmovable, Barricade, or repeatable block exists. |
| Vicious | 24.9% pick | Vulnerable engine centerpiece. Upgrade when repeated Vulnerable is available. |
| Thunderclap | 15.8% pick, low standalone win signal | Weak generic card, but useful as Act 1 AoE/frontload and later Vicious enabler. Prefer upgraded or supported copies. |
| Barricade | 30.0% pick | Wins with surplus block and Body Slam; too slow without large block generation. |
| Whirlwind | 29.0% pick | Important AoE and burst, especially with energy/Vulnerable; avoid as unsupported late filler. |
| Fiend Fire | 29.1% pick | Burst finisher and exhaust payoff. Use to end/simplify fights, not before needed block. |

## Caution Cards

These are not bans. They need a reason.

| Card | Site signal | General impression |
|---|---:|---|
| Havoc | 4.8% pick | Very low confidence unless the deck can tolerate random play/exhaust. |
| Cinder | 6.0% pick | Low signal; random exhaust can damage consistency. |
| Rampage | 18.7% pick, very poor impact | Needs repeated cycling and time; often worse than cleaner damage or draw. |
| Thunderclap | 15.8% pick | Do not take as a generic attack unless AoE/Vulnerable needs justify it. |
| Hemokinesis | 15.3% pick | HP-cost damage needs a clear Act 1 survival reason. |
| Iron Wave | 11.8% pick | Often mediocre because it is neither strong damage nor strong block. |
| Anger / Twin Strike / Setup Strike | Low-to-mid pick, poor impact | Can be Act 1 survival picks, but become dilution quickly without synergy. |

## Current Template Biases

- Infinity/fast-cycle decks value Pommel Strike+, Shrug It Off, Battle Trance, Bloodletting, Burning Pact, Offering, and True Grit+ above raw medium attacks.
- Body Slam decks value Unmovable, Impervious, Blood Wall, Shrug It Off, True Grit+, Barricade, and Body Slam+ together; no single piece is enough.
- Vulnerable decks value Vicious+, Bash+/Break, Thunderclap, Tremble, Uppercut, Bully, Dismantle, and draw/energy to exploit the extra damage.
- Act 3 card picks should usually be engine pieces, payoff pieces, premium draw/energy, or boss-specific defense. Skip standalone cards that do not raise the ceiling of the current deck.
