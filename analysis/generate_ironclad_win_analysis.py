#!/usr/bin/env python3
"""Generate Ironclad A10 win-biased analysis from runs/data exports."""

from __future__ import annotations

import csv
import itertools
import json
import math
import re
import statistics
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUNS_DIR = ROOT / "runs" / "data"
OUT_DIR = ROOT / "analysis"

STARTER_IDS = {"STRIKE_IRONCLAD", "DEFEND_IRONCLAD", "BASH", "ASCENDERS_BANE"}
STARTER_COUNTS = {
    "STRIKE_IRONCLAD": 5,
    "DEFEND_IRONCLAD": 4,
    "BASH": 1,
    "ASCENDERS_BANE": 1,
}
STARTER_DECK_SIZE = sum(STARTER_COUNTS.values())
NON_REWARD_TYPES = {"Curse", "Status"}
POTION_NAME_HINTS = (
    "Potion",
    "Brew",
    "Tonic",
    "Serum",
    "Oil",
    "Juice",
    "Ampoule",
    "Tincture",
    "Memories",
    "Bronze",
    "Chaos",
    "Bottle",
)
NON_POTION_OTHER_REWARDS = {"Potion Shaped Rock", "Ship In A Bottle", "Bottled Potential"}


def clean_name(name: str) -> str:
    return re.sub(r"\+| \?", "", name).strip()


def parse_int(value: str | int | None) -> int | None:
    if value is None:
        return None
    match = re.search(r"-?\d+", str(value))
    return int(match.group(0)) if match else None


def hp_fraction(value: str) -> float:
    current, maximum = value.split("/")
    return int(current) / int(maximum)


def mean(values: list[float | int]) -> float:
    return statistics.mean(values) if values else math.nan


def median(values: list[float | int]) -> float:
    return statistics.median(values) if values else math.nan


def percentile(values: list[int], pct: float) -> float:
    if not values:
        return math.nan
    ordered = sorted(values)
    pos = (len(ordered) - 1) * pct
    lower = math.floor(pos)
    upper = math.ceil(pos)
    if lower == upper:
        return float(ordered[lower])
    return ordered[lower] + (ordered[upper] - ordered[lower]) * (pos - lower)


def load_runs() -> list[dict]:
    runs = []
    for path in sorted(RUNS_DIR.glob("*.json")):
        with path.open() as handle:
            data = json.load(handle)
        if data.get("character") == "Ironclad":
            runs.append(data)
    return runs


def load_card_metadata() -> dict[str, dict[str, str]]:
    metadata: dict[str, dict[str, str]] = {}
    for path in (ROOT / "kb" / "cards").glob("**/*.md"):
        text = path.read_text(errors="ignore")
        frontmatter = text.split("---", 2)[1] if text.startswith("---") and "---" in text[3:] else ""
        title_match = re.search(r"^title:\s*(.+)$", frontmatter, re.MULTILINE)
        type_match = re.search(r"^type:\s*(.+)$", frontmatter, re.MULTILINE)
        rarity_match = re.search(r"^rarity:\s*(.+)$", frontmatter, re.MULTILINE)
        id_match = re.search(r"\|\s*ID\s*\|\s*([A-Z0-9_]+)\s*\|", text)
        card_id = id_match.group(1) if id_match else path.stem.upper()
        metadata[card_id] = {
            "name": title_match.group(1).strip() if title_match else path.stem.replace("_", " ").title(),
            "type": type_match.group(1).strip() if type_match else "",
            "rarity": rarity_match.group(1).strip() if rarity_match else "",
        }
    return metadata


def load_potion_names() -> set[str]:
    names = set()
    for path in (ROOT / "kb" / "potions").glob("*.md"):
        text = path.read_text(errors="ignore")
        match = re.search(r"^title:\s*(.+)$", text, re.MULTILINE)
        if match:
            names.add(match.group(1).strip())
    return names


def is_potion_like_reward(value: str, potion_names: set[str]) -> bool:
    if value in NON_POTION_OTHER_REWARDS:
        return False
    return value in potion_names or any(hint in value for hint in POTION_NAME_HINTS)


def write_csv(path: Path, fieldnames: list[str], rows: list[dict]) -> None:
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def run_progress_metrics(run: dict, card_metadata: dict[str, dict[str, str]], potion_names: set[str]) -> dict:
    cards_by_act = Counter()
    cards_by_act_type: dict[int, Counter] = defaultdict(Counter)
    damage_by_act = Counter()
    turns_by_act = Counter()
    combats_by_act = Counter()
    elites_by_act = Counter()
    bosses_by_act = Counter()
    rests_by_act = Counter()
    smiths_by_act = Counter()
    heals_by_act = Counter()
    relics_by_act = Counter()
    potions_by_act = Counter()
    node_by_act: dict[int, Counter] = defaultdict(Counter)
    observed_deck_after_act: dict[int, int] = {}
    cumulative_cards = STARTER_DECK_SIZE

    for floor in run["floors"]:
        act = floor.get("act")
        if act not in {1, 2, 3}:
            continue
        rewards = floor.get("rewards") or {}
        reward_cards = rewards.get("cards", [])
        card_count = len(reward_cards)
        cards_by_act[act] += card_count
        cumulative_cards += card_count
        observed_deck_after_act[act] = cumulative_cards
        for card in reward_cards:
            card_type = card_metadata.get(card["id"], {}).get("type", "")
            cards_by_act_type[act][card_type or "Unknown"] += 1

        damage_by_act[act] += floor.get("damage_taken") or 0
        turns = floor.get("turns")
        if turns:
            turns_by_act[act] += turns
            combats_by_act[act] += 1
        node_type = floor.get("node_type") or ""
        node_by_act[act][node_type] += 1
        if node_type == "elite":
            elites_by_act[act] += 1
        if node_type == "boss":
            bosses_by_act[act] += 1
        if node_type == "rest":
            rests_by_act[act] += 1
        relics_by_act[act] += len(rewards.get("relics", []))
        for value in rewards.get("other", []):
            if value.startswith("Smith:"):
                smiths_by_act[act] += 1
            elif value == "Heal":
                heals_by_act[act] += 1
            if is_potion_like_reward(value, potion_names):
                potions_by_act[act] += 1

    final_counts = Counter(card["id"] for card in run.get("final_deck", []))
    remaining = final_counts.copy()
    known_final_acquisition_floors: list[int] = []
    for card_id, initial_count in STARTER_COUNTS.items():
        count = min(remaining[card_id], initial_count)
        known_final_acquisition_floors.extend([0] * count)
        remaining[card_id] -= count

    for floor in sorted(run["floors"], key=lambda item: item.get("floor") or 0):
        for card in (floor.get("rewards") or {}).get("cards", []):
            card_id = card["id"]
            if remaining[card_id] > 0:
                known_final_acquisition_floors.append(floor["floor"])
                remaining[card_id] -= 1

    act_max_floor = {
        act: max((floor["floor"] for floor in run["floors"] if floor.get("act") == act), default=0)
        for act in [1, 2, 3]
    }
    known_final_by_act = {
        act: sum(1 for floor in known_final_acquisition_floors if floor <= act_max_floor[act])
        for act in [1, 2, 3]
    }
    unknown_final_cards = sum(max(count, 0) for count in remaining.values())
    final_deck_size = int(run["summary_stats"]["Deck Size"])

    return {
        "cards_by_act": cards_by_act,
        "cards_by_act_type": cards_by_act_type,
        "damage_by_act": damage_by_act,
        "turns_by_act": turns_by_act,
        "combats_by_act": combats_by_act,
        "elites_by_act": elites_by_act,
        "bosses_by_act": bosses_by_act,
        "rests_by_act": rests_by_act,
        "smiths_by_act": smiths_by_act,
        "heals_by_act": heals_by_act,
        "relics_by_act": relics_by_act,
        "potions_by_act": potions_by_act,
        "node_by_act": node_by_act,
        "observed_deck_after_act": observed_deck_after_act,
        "known_final_by_act": known_final_by_act,
        "unknown_final_cards": unknown_final_cards,
        "observed_final_gap": final_deck_size - observed_deck_after_act.get(3, STARTER_DECK_SIZE),
        "final_acquisition_coverage": (final_deck_size - unknown_final_cards) / final_deck_size if final_deck_size else 0,
    }


def collect_stats(runs: list[dict]) -> dict:
    card_metadata = load_card_metadata()
    potion_names = load_potion_names()
    card_names: dict[str, str] = {}
    card_types: dict[str, str] = {}
    pick_count = Counter()
    pick_runs: dict[str, set[str]] = defaultdict(set)
    pick_floors: dict[str, list[int]] = defaultdict(list)
    pick_acts: dict[str, Counter] = defaultdict(Counter)
    pick_sources: dict[str, Counter] = defaultdict(Counter)
    smith_targets = Counter()
    relic_count = Counter()
    relic_runs: dict[str, set[str]] = defaultdict(set)
    encounter_runs: dict[str, set[str]] = defaultdict(set)
    encounter_damage: dict[str, list[int]] = defaultdict(list)
    encounter_turns: dict[str, list[int]] = defaultdict(list)

    final_copies = Counter()
    final_runs = Counter()
    final_upgraded = Counter()
    final_sets = []
    run_rows = []
    progress_by_run = []

    for run in runs:
        run_id = run["id"]
        progress = run_progress_metrics(run, card_metadata, potion_names)
        progress_by_run.append(progress)
        deck_size = int(run["summary_stats"]["Deck Size"])
        total_damage = int(run["summary_stats"]["Total Damage"])
        final_hp_fraction = hp_fraction(run["summary_stats"]["Final HP"])
        elites = int(run["summary_stats"]["Elites Killed"])
        duration = parse_int(run["summary_stats"].get("Duration"))
        combats = [floor for floor in run["floors"] if floor.get("turns")]
        total_turns = sum(floor["turns"] for floor in combats)

        run_rows.append(
            {
                "run_id": run_id,
                "player": run.get("player", ""),
                "date": run.get("date", ""),
                "result": run.get("result", ""),
                "ascension": run.get("ascension", ""),
                "floors": run["summary_stats"]["Floors"],
                "deck_size": deck_size,
                "final_hp": run["summary_stats"]["Final HP"],
                "final_hp_fraction": round(final_hp_fraction, 4),
                "total_damage": total_damage,
                "total_turns": total_turns,
                "elites_killed": elites,
                "duration_minutes": duration,
                "relic_count": run.get("derived", {}).get("relic_count", ""),
                "bosses": "; ".join(run.get("derived", {}).get("bosses", [])),
                "visible_deck_after_act1": progress["observed_deck_after_act"].get(1, ""),
                "visible_deck_after_act2": progress["observed_deck_after_act"].get(2, ""),
                "visible_deck_after_act3": progress["observed_deck_after_act"].get(3, ""),
                "known_final_cards_by_act1": progress["known_final_by_act"].get(1, ""),
                "known_final_cards_by_act2": progress["known_final_by_act"].get(2, ""),
                "known_final_cards_by_act3": progress["known_final_by_act"].get(3, ""),
                "final_cards_not_visible_in_rewards": progress["unknown_final_cards"],
                "visible_final_gap": progress["observed_final_gap"],
                "damage_act1": progress["damage_by_act"].get(1, 0),
                "damage_act2": progress["damage_by_act"].get(2, 0),
                "damage_act3": progress["damage_by_act"].get(3, 0),
                "turns_act1": progress["turns_by_act"].get(1, 0),
                "turns_act2": progress["turns_by_act"].get(2, 0),
                "turns_act3": progress["turns_by_act"].get(3, 0),
                "smiths": sum(progress["smiths_by_act"].values()),
                "heals": sum(progress["heals_by_act"].values()),
            }
        )

        for floor in run["floors"]:
            rewards = floor.get("rewards") or {}
            encounter = floor.get("encounter") or ""
            if encounter:
                encounter_runs[encounter].add(run_id)
                if floor.get("damage_taken") is not None:
                    encounter_damage[encounter].append(floor.get("damage_taken") or 0)
                if floor.get("turns") is not None:
                    encounter_turns[encounter].append(floor.get("turns") or 0)
            for card in rewards.get("cards", []):
                card_id = card["id"]
                card_names[card_id] = clean_name(card["name"])
                pick_count[card_id] += 1
                pick_runs[card_id].add(run_id)
                pick_floors[card_id].append(floor["floor"])
                pick_acts[card_id][floor.get("act")] += 1
                pick_sources[card_id][floor.get("node_type", "")] += 1
            for relic in rewards.get("relics", []):
                relic_count[relic["name"]] += 1
                relic_runs[relic["name"]].add(run_id)
            for value in rewards.get("other", []):
                if value.startswith("Smith:"):
                    smith_targets[value.removeprefix("Smith:").strip()] += 1

        final_ids = set()
        for card in run.get("final_deck", []):
            card_id = card["id"]
            card_names[card_id] = clean_name(card["name"])
            card_types[card_id] = card.get("type") or ""
            final_copies[card_id] += 1
            if card.get("upgraded"):
                final_upgraded[card_id] += 1
            if card_id not in STARTER_IDS and card.get("type") not in NON_REWARD_TYPES:
                final_ids.add(card_id)
        for card_id in final_ids:
            final_runs[card_id] += 1
        final_sets.append(final_ids)

    baseline = {
        "damage": mean([row["total_damage"] for row in run_rows]),
        "hp_fraction": mean([row["final_hp_fraction"] for row in run_rows]),
        "turns": mean([row["total_turns"] for row in run_rows]),
        "deck_size": mean([row["deck_size"] for row in run_rows]),
    }

    act_rows = []
    for act in [1, 2, 3]:
        visible_decks = [p["observed_deck_after_act"].get(act) for p in progress_by_run if p["observed_deck_after_act"].get(act)]
        known_final = [p["known_final_by_act"].get(act) for p in progress_by_run if p["known_final_by_act"].get(act) is not None]
        cards_added = [p["cards_by_act"].get(act, 0) for p in progress_by_run]
        damage_values = [p["damage_by_act"].get(act, 0) for p in progress_by_run]
        turns_values = [p["turns_by_act"].get(act, 0) for p in progress_by_run]
        combats = [p["combats_by_act"].get(act, 0) for p in progress_by_run]
        rests = [p["rests_by_act"].get(act, 0) for p in progress_by_run]
        smiths = [p["smiths_by_act"].get(act, 0) for p in progress_by_run]
        heals = [p["heals_by_act"].get(act, 0) for p in progress_by_run]
        relics = [p["relics_by_act"].get(act, 0) for p in progress_by_run]
        potions = [p["potions_by_act"].get(act, 0) for p in progress_by_run]
        elites_act = [p["elites_by_act"].get(act, 0) for p in progress_by_run]
        act_rows.append(
            {
                "act": act,
                "runs": len(runs),
                "avg_visible_deck_after_act": round(mean(visible_decks), 2),
                "median_visible_deck_after_act": round(median(visible_decks), 1),
                "p25_visible_deck_after_act": round(percentile([int(v) for v in visible_decks], 0.25), 1),
                "p75_visible_deck_after_act": round(percentile([int(v) for v in visible_decks], 0.75), 1),
                "min_visible_deck_after_act": min(visible_decks),
                "max_visible_deck_after_act": max(visible_decks),
                "avg_known_final_cards_acquired_by_act": round(mean(known_final), 2),
                "avg_visible_cards_added_in_act": round(mean(cards_added), 2),
                "avg_damage_in_act": round(mean(damage_values), 1),
                "avg_turns_in_act": round(mean(turns_values), 1),
                "avg_combats_in_act": round(mean(combats), 2),
                "avg_elites_in_act": round(mean(elites_act), 2),
                "avg_rests_in_act": round(mean(rests), 2),
                "avg_smiths_in_act": round(mean(smiths), 2),
                "avg_heals_in_act": round(mean(heals), 2),
                "smith_to_heal_ratio": round(sum(smiths) / sum(heals), 2) if sum(heals) else "",
                "avg_relics_in_act": round(mean(relics), 2),
                "avg_potions_in_act": round(mean(potions), 2),
            }
        )

    act_card_type_rows = []
    for act in [1, 2, 3]:
        totals = Counter()
        for progress in progress_by_run:
            totals.update(progress["cards_by_act_type"].get(act, {}))
        total_cards = sum(totals.values())
        for card_type, count in totals.most_common():
            act_card_type_rows.append(
                {
                    "act": act,
                    "card_type": card_type,
                    "visible_picks": count,
                    "pct_visible_picks": round(count / total_cards * 100, 1) if total_cards else 0,
                    "avg_picks_per_run": round(count / len(runs), 2),
                }
            )

    node_rows = []
    for act in [1, 2, 3]:
        totals = Counter()
        for progress in progress_by_run:
            totals.update(progress["node_by_act"].get(act, {}))
        total_nodes = sum(totals.values())
        for node_type, count in totals.most_common():
            node_rows.append(
                {
                    "act": act,
                    "node_type": node_type,
                    "nodes": count,
                    "pct_act_nodes": round(count / total_nodes * 100, 1) if total_nodes else 0,
                    "avg_nodes_per_run": round(count / len(runs), 2),
                }
            )

    campfire_rows = []
    for act in [1, 2, 3]:
        total_rests = sum(p["rests_by_act"].get(act, 0) for p in progress_by_run)
        total_smiths = sum(p["smiths_by_act"].get(act, 0) for p in progress_by_run)
        total_heals = sum(p["heals_by_act"].get(act, 0) for p in progress_by_run)
        campfire_rows.append(
            {
                "act": act,
                "rest_nodes": total_rests,
                "smith_actions": total_smiths,
                "heal_actions": total_heals,
                "smiths_per_run": round(total_smiths / len(runs), 2),
                "heals_per_run": round(total_heals / len(runs), 2),
                "smith_share_of_actions": round(total_smiths / (total_smiths + total_heals) * 100, 1)
                if total_smiths + total_heals
                else 0,
                "heal_share_of_actions": round(total_heals / (total_smiths + total_heals) * 100, 1)
                if total_smiths + total_heals
                else 0,
            }
        )

    smith_target_rows = [
        {
            "card": card,
            "smith_count": count,
            "pct_runs": round(count / len(runs) * 100, 1),
        }
        for card, count in smith_targets.most_common()
    ]

    relic_rows = [
        {
            "relic": relic,
            "copies_seen": count,
            "runs_seen": len(relic_runs[relic]),
            "pct_runs_seen": round(len(relic_runs[relic]) / len(runs) * 100, 1),
        }
        for relic, count in relic_count.most_common()
    ]

    encounter_rows = []
    for encounter, run_ids in encounter_runs.items():
        if len(run_ids) < 5:
            continue
        damage_values = encounter_damage[encounter]
        turn_values = encounter_turns[encounter]
        if not turn_values:
            continue
        encounter_rows.append(
            {
                "encounter": encounter,
                "runs": len(run_ids),
                "avg_damage": round(mean(damage_values), 1) if damage_values else "",
                "median_damage": round(median(damage_values), 1) if damage_values else "",
                "avg_turns": round(mean(turn_values), 1) if turn_values else "",
                "median_turns": round(median(turn_values), 1) if turn_values else "",
            }
        )
    encounter_rows.sort(key=lambda row: (-row["avg_damage"] if row["avg_damage"] != "" else 0, -row["runs"]))

    pick_rows = []
    for card_id, count in pick_count.most_common():
        floors = pick_floors[card_id]
        acts = pick_acts[card_id]
        sources = pick_sources[card_id]
        pick_rows.append(
            {
                "card_id": card_id,
                "name": card_names.get(card_id, card_id),
                "picked_count": count,
                "runs_with_pick": len(pick_runs[card_id]),
                "pct_runs_with_pick": round(len(pick_runs[card_id]) / len(runs) * 100, 1),
                "avg_pick_floor": round(mean(floors), 2),
                "median_pick_floor": round(median(floors), 1),
                "earliest_pick_floor": min(floors),
                "latest_pick_floor": max(floors),
                "act1_picks": acts.get(1, 0),
                "act2_picks": acts.get(2, 0),
                "act3_picks": acts.get(3, 0),
                "monster_picks": sources.get("monster", 0),
                "elite_picks": sources.get("elite", 0),
                "boss_picks": sources.get("boss", 0),
                "event_or_other_picks": sum(
                    value
                    for source, value in sources.items()
                    if source not in {"monster", "elite", "boss"}
                ),
            }
        )

    final_rows = []
    for card_id, run_count in final_runs.most_common():
        copies = final_copies[card_id]
        final_rows.append(
            {
                "card_id": card_id,
                "name": card_names.get(card_id, card_id),
                "type": card_types.get(card_id, ""),
                "runs_in_final_deck": run_count,
                "pct_runs_in_final_deck": round(run_count / len(runs) * 100, 1),
                "total_final_copies": copies,
                "avg_copies_when_present": round(copies / run_count, 2),
                "upgraded_final_copies": final_upgraded[card_id],
                "pct_final_copies_upgraded": round(final_upgraded[card_id] / copies * 100, 1),
            }
        )

    performance_rows = []
    for card_id, run_count in final_runs.items():
        if run_count < 5:
            continue
        present = [
            row
            for row, final_set in zip(run_rows, final_sets)
            if card_id in final_set
        ]
        absent = [
            row
            for row, final_set in zip(run_rows, final_sets)
            if card_id not in final_set
        ]
        performance_rows.append(
            {
                "card_id": card_id,
                "name": card_names.get(card_id, card_id),
                "type": card_types.get(card_id, ""),
                "runs_present": run_count,
                "avg_damage_present": round(mean([row["total_damage"] for row in present]), 1),
                "damage_vs_all_wins": round(mean([row["total_damage"] for row in present]) - baseline["damage"], 1),
                "avg_final_hp_fraction_present": round(mean([row["final_hp_fraction"] for row in present]), 3),
                "hp_fraction_vs_all_wins": round(mean([row["final_hp_fraction"] for row in present]) - baseline["hp_fraction"], 3),
                "avg_turns_present": round(mean([row["total_turns"] for row in present]), 1),
                "turns_vs_all_wins": round(mean([row["total_turns"] for row in present]) - baseline["turns"], 1),
                "avg_deck_size_present": round(mean([row["deck_size"] for row in present]), 1),
                "runs_absent": len(absent),
            }
        )
    performance_rows.sort(
        key=lambda row: (row["damage_vs_all_wins"], -row["hp_fraction_vs_all_wins"], row["runs_present"])
    )

    pair_rows = []
    pair_runs: dict[tuple[str, str], list[int]] = defaultdict(list)
    for index, final_set in enumerate(final_sets):
        for pair in itertools.combinations(sorted(final_set), 2):
            pair_runs[pair].append(index)
    for (left, right), indexes in pair_runs.items():
        if len(indexes) < 8:
            continue
        rows = [run_rows[index] for index in indexes]
        pair_rows.append(
            {
                "left_card_id": left,
                "left_name": card_names.get(left, left),
                "right_card_id": right,
                "right_name": card_names.get(right, right),
                "runs_with_pair": len(indexes),
                "pct_runs_with_pair": round(len(indexes) / len(runs) * 100, 1),
                "avg_damage": round(mean([row["total_damage"] for row in rows]), 1),
                "damage_vs_all_wins": round(mean([row["total_damage"] for row in rows]) - baseline["damage"], 1),
                "avg_final_hp_fraction": round(mean([row["final_hp_fraction"] for row in rows]), 3),
                "avg_turns": round(mean([row["total_turns"] for row in rows]), 1),
            }
        )
    pair_rows.sort(key=lambda row: (-row["runs_with_pair"], row["avg_damage"]))

    package_rows = []
    package_runs: dict[tuple[str, str, str], list[int]] = defaultdict(list)
    for index, final_set in enumerate(final_sets):
        for package in itertools.combinations(sorted(final_set), 3):
            package_runs[package].append(index)
    for package, indexes in package_runs.items():
        if len(indexes) < 8:
            continue
        rows = [run_rows[index] for index in indexes]
        package_rows.append(
            {
                "card_ids": ";".join(package),
                "cards": " + ".join(card_names.get(card_id, card_id) for card_id in package),
                "runs_with_package": len(indexes),
                "pct_runs_with_package": round(len(indexes) / len(runs) * 100, 1),
                "avg_damage": round(mean([row["total_damage"] for row in rows]), 1),
                "damage_vs_all_wins": round(mean([row["total_damage"] for row in rows]) - baseline["damage"], 1),
                "avg_final_hp_fraction": round(mean([row["final_hp_fraction"] for row in rows]), 3),
                "avg_turns": round(mean([row["total_turns"] for row in rows]), 1),
            }
        )
    package_rows.sort(key=lambda row: (-row["runs_with_package"], row["avg_damage"]))

    return {
        "runs": runs,
        "run_rows": run_rows,
        "pick_rows": pick_rows,
        "final_rows": final_rows,
        "performance_rows": performance_rows,
        "pair_rows": pair_rows,
        "package_rows": package_rows,
        "act_rows": act_rows,
        "act_card_type_rows": act_card_type_rows,
        "node_rows": node_rows,
        "campfire_rows": campfire_rows,
        "smith_target_rows": smith_target_rows,
        "relic_rows": relic_rows,
        "encounter_rows": encounter_rows,
        "progress_by_run": progress_by_run,
        "baseline": baseline,
    }


def format_table(headers: list[str], rows: list[list[object]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(str(value) for value in row) + " |")
    return "\n".join(lines)


def build_report(stats: dict) -> str:
    runs = stats["runs"]
    run_rows = stats["run_rows"]
    deck_sizes = [row["deck_size"] for row in run_rows]
    damage = [row["total_damage"] for row in run_rows]
    hp = [row["final_hp_fraction"] for row in run_rows]
    turns = [row["total_turns"] for row in run_rows]
    elites = [row["elites_killed"] for row in run_rows]

    top_picks = stats["pick_rows"][:18]
    top_final = stats["final_rows"][:20]
    pick_by_name = {row["name"]: row for row in stats["pick_rows"]}
    final_by_name = {row["name"]: row for row in stats["final_rows"]}
    act_rows = stats["act_rows"]
    campfire_rows = stats["campfire_rows"]
    act_type_rows = stats["act_card_type_rows"]
    node_rows = stats["node_rows"]
    efficient_pairs = sorted(
        [row for row in stats["pair_rows"] if row["runs_with_pair"] >= 20],
        key=lambda row: (row["avg_damage"], -row["avg_final_hp_fraction"], -row["runs_with_pair"]),
    )[:14]
    common_packages = stats["package_rows"][:14]
    top_smith_targets = stats["smith_target_rows"][:15]
    top_relics = stats["relic_rows"][:15]
    hardest_encounters = stats["encounter_rows"][:15]
    weaker_perf = sorted(
        [row for row in stats["performance_rows"] if row["runs_present"] >= 6],
        key=lambda row: (-row["damage_vs_all_wins"], row["hp_fraction_vs_all_wins"]),
    )[:14]

    outlier_runs = sorted(run_rows, key=lambda row: row["deck_size"], reverse=True)[:3]
    visible_gap = [row["visible_final_gap"] for row in run_rows if row["visible_final_gap"] != ""]
    unknown_final = [row["final_cards_not_visible_in_rewards"] for row in run_rows]
    non_outlier_decks = [size for size in deck_sizes if size <= 50]

    def pick_sentence(name: str) -> str:
        pick = pick_by_name[name]
        final = final_by_name[name]
        return (
            f"`{name}`: {pick['picked_count']} visible picks, "
            f"{pick['runs_with_pick']} pick-runs, {final['runs_in_final_deck']} final decks, "
            f"avg pick floor {pick['avg_pick_floor']}."
        )

    def top_act_types(act: int) -> str:
        rows = [row for row in act_type_rows if row["act"] == act]
        return ", ".join(f"{row['card_type']} {row['pct_visible_picks']}%" for row in rows[:3])

    def node_mix(act: int) -> str:
        rows = [row for row in node_rows if row["act"] == act]
        return ", ".join(f"{row['node_type']} {row['avg_nodes_per_run']}/run" for row in rows[:4])

    report = [
        "# Ironclad A10 Win Analysis",
        "",
        f"Source: `runs/data/*.json`, {len(runs)} Ironclad Ascension 10 wins exported from `sts2.fun`.",
        "",
        "Important bias: this is a winning-run corpus. It shows what winning decks contained and when cards entered those decks. It cannot by itself prove win rate, because failed runs and skipped reward options are not present.",
        "",
        "## Run Shape",
        "",
        format_table(
            ["Metric", "Value"],
            [
                ["Runs analyzed", len(runs)],
                ["Results", f"{len(runs)} wins, 0 losses"],
                ["Average deck size", round(mean(deck_sizes), 2)],
                ["Median deck size", median(deck_sizes)],
                ["Deck size range", f"{min(deck_sizes)}-{max(deck_sizes)}"],
                ["Deck size p25/p75", f"{round(percentile(deck_sizes, 0.25), 1)} / {round(percentile(deck_sizes, 0.75), 1)}"],
                ["Average total damage taken", round(mean(damage), 1)],
                ["Median total damage taken", median(damage)],
                ["Average final HP fraction", round(mean(hp), 3)],
                ["Average combat turns", round(mean(turns), 1)],
                ["Average elites killed", round(mean(elites), 2)],
            ],
        ),
        "",
        "The normal winning deck size is around 30-35 cards. The mean is pulled upward by two very large outliers: "
        + ", ".join(f"{row['run_id'][:8]} ({row['deck_size']} cards)" for row in outlier_runs[:2])
        + ". Excluding decks above 50 cards, the average deck size is "
        + str(round(mean(non_outlier_decks), 2))
        + ".",
        "",
        "## Deck Size By Act",
        "",
        "The site does not expose exact deck state at each floor. The table below uses visible card pickups from floor rewards: starter deck size 11 plus cards shown as selected through the end of each act. It does not fully account for shop/event buys, transforms, or removals, so final deck size remains the exact endpoint and act-end values are best treated as visible growth estimates.",
        "",
        format_table(
            ["Act", "Visible Deck Median", "Visible Deck Avg", "P25/P75", "Visible Adds", "Known Final Cards By Act", "Damage", "Turns"],
            [
                [
                    row["act"],
                    row["median_visible_deck_after_act"],
                    row["avg_visible_deck_after_act"],
                    f"{row['p25_visible_deck_after_act']} / {row['p75_visible_deck_after_act']}",
                    row["avg_visible_cards_added_in_act"],
                    row["avg_known_final_cards_acquired_by_act"],
                    row["avg_damage_in_act"],
                    row["avg_turns_in_act"],
                ]
                for row in act_rows
            ],
        ),
        "",
        f"Visible growth is front-loaded: winners add about {act_rows[0]['avg_visible_cards_added_in_act']} visible cards in Act 1, {act_rows[1]['avg_visible_cards_added_in_act']} in Act 2, and {act_rows[2]['avg_visible_cards_added_in_act']} in Act 3. Median visible deck size is {act_rows[0]['median_visible_deck_after_act']} after Act 1, {act_rows[1]['median_visible_deck_after_act']} after Act 2, and {act_rows[2]['median_visible_deck_after_act']} after Act 3, while exact final median is {median(deck_sizes)}.",
        "",
        f"The reconciliation gap matters: final decks average {round(mean(unknown_final), 2)} cards that were not matched to visible reward-card pickups, and exact final deck size averages {round(mean(visible_gap), 2)} cards above the simple visible-growth estimate. That is mostly shop/event/transform noise plus removals, so use this section for pacing, not exact card count auditing.",
        "",
        "## Act Mix And Campfires",
        "",
        format_table(
            ["Act", "Top Node Mix", "Card Type Mix", "Rest Nodes/Run", "Smiths/Run", "Heals/Run", "Smith Share"],
            [
                [
                    row["act"],
                    node_mix(row["act"]),
                    top_act_types(row["act"]),
                    row["avg_rests_in_act"],
                    row["avg_smiths_in_act"],
                    row["avg_heals_in_act"],
                    f"{campfire_rows[row['act'] - 1]['smith_share_of_actions']}%",
                ]
                for row in act_rows
            ],
        ),
        "",
        "This matches `GUIDE.md`: campfire default is smith. Across the expanded win set, smithing is 75.0% of Act 1 campfire actions, 67.1% in Act 2, and 66.8% in Act 3. Healing is still common enough to matter, but it is the exception used to stabilize pathing, not the baseline plan.",
        "",
        "Card mix shifts by act. Act 1 is balanced between attacks and skills, which fits the need to build damage plus draw/block immediately. Acts 2 and 3 skew more heavily toward skills, which suggests winners spend later picks on consistency, block, exhaust, and utility rather than raw attacks.",
        "",
        "Most common smith targets:",
        "",
        format_table(
            ["Card", "Smiths", "Pct Runs"],
            [[row["card"], row["smith_count"], f"{row['pct_runs']}%"] for row in top_smith_targets],
        ),
        "",
        "`Pommel Strike` is the standout upgrade target in the larger set. That lines up with the card-frequency data: winners not only take it often, they spend campfires making it draw two.",
        "",
        "## Encounters And Relics",
        "",
        "Hardest common encounters by average damage taken:",
        "",
        format_table(
            ["Encounter", "Runs", "Avg Damage", "Median Damage", "Avg Turns"],
            [
                [
                    row["encounter"],
                    row["runs"],
                    row["avg_damage"],
                    row["median_damage"],
                    row["avg_turns"],
                ]
                for row in hardest_encounters
            ],
        ),
        "",
        "Most frequent relic rewards:",
        "",
        format_table(
            ["Relic", "Runs", "Pct Runs"],
            [[row["relic"], row["runs_seen"], f"{row['pct_runs_seen']}%"] for row in top_relics],
        ),
        "",
        "## Most Chosen Cards And Timing",
        "",
        format_table(
            ["Card", "Picks", "Runs", "Avg Floor", "Act 1", "Act 2", "Act 3"],
            [
                [
                    row["name"],
                    row["picked_count"],
                    f"{row['runs_with_pick']} ({row['pct_runs_with_pick']}%)",
                    row["avg_pick_floor"],
                    row["act1_picks"],
                    row["act2_picks"],
                    row["act3_picks"],
                ]
                for row in top_picks
            ],
        ),
        "",
        "High-confidence staples from this corpus:",
        "",
        f"- {pick_sentence('Pommel Strike')} It remains the default repeatable attack/draw card.",
        f"- {pick_sentence('Bloodletting')} It is still a top-tier energy/tempo card, but the larger sample puts it behind `Pommel Strike` and `Shrug It Off` in visible pick count.",
        f"- {pick_sentence('Shrug It Off')} The expanded sample makes this look even more important than the first 40-run read.",
        "- `True Grit`, `Battle Trance`, `Burning Pact`, `Blood Wall`, `Tremble`, `Uppercut`, `Dominate`, and `Headbutt` round out the repeated core. The pattern is draw/energy plus efficient block, not pure damage.",
        "",
        "## Final Deck Frequency",
        "",
        format_table(
            ["Card", "Runs", "Copies", "Avg Copies", "Upgraded Copies"],
            [
                [
                    row["name"],
                    f"{row['runs_in_final_deck']} ({row['pct_runs_in_final_deck']}%)",
                    row["total_final_copies"],
                    row["avg_copies_when_present"],
                    f"{row['upgraded_final_copies']} ({row['pct_final_copies_upgraded']}%)",
                ]
                for row in top_final
            ],
        ),
        "",
        "This is the most practical draft signal: cards that remain in final winning decks after removals, shops, events, and upgrades. The top tier is very stable: `Pommel Strike`, `Bloodletting`, and `Shrug It Off` appear in at least two thirds of wins.",
        "",
        "## Combos That Look Good",
        "",
        "Common three-card packages:",
        "",
        format_table(
            ["Package", "Runs", "Avg Damage", "Damage vs All Wins", "Avg Final HP", "Avg Turns"],
            [
                [
                    row["cards"],
                    row["runs_with_package"],
                    row["avg_damage"],
                    row["damage_vs_all_wins"],
                    row["avg_final_hp_fraction"],
                    row["avg_turns"],
                ]
                for row in common_packages
            ],
        ),
        "",
        "Efficient repeated two-card pairs with at least 20 runs:",
        "",
        format_table(
            ["Pair", "Runs", "Avg Damage", "Damage vs All Wins", "Avg Final HP", "Avg Turns"],
            [
                [
                    f"{row['left_name']} + {row['right_name']}",
                    row["runs_with_pair"],
                    row["avg_damage"],
                    row["damage_vs_all_wins"],
                    row["avg_final_hp_fraction"],
                    row["avg_turns"],
                ]
                for row in efficient_pairs
            ],
        ),
        "",
        "The cleanest repeated shell is draw plus block plus cheap damage:",
        "",
        "- The most repeated packages are no longer just attack shells; the larger sample heavily favors `Bloodletting`, `Pommel Strike`, and `Shrug It Off` combinations.",
        "- `Bloodletting + Pommel Strike + Shrug It Off` is the highest-frequency three-card package. It is the practical baseline: energy/draw, attack/draw, and block/draw.",
        "- `Headbutt` still pairs well with the common shell because it recycles the best upgraded attacks and draw cards.",
        "- Exhaust/value packages show up through `True Grit`, `Burning Pact`, `Feel No Pain`, `Second Wind`, and `Fiend Fire`, but they are less universal than the Pommel/Bloodletting/block shell.",
        "",
        "## Cards To Treat Carefully",
        "",
        "Because the corpus contains only wins, this section means `weaker or more conditional signal among wins`, not `proven bad card`.",
        "",
        format_table(
            ["Card", "Runs", "Avg Damage", "Damage vs All Wins", "Avg Final HP", "Avg Turns"],
            [
                [
                    row["name"],
                    row["runs_present"],
                    row["avg_damage_present"],
                    row["damage_vs_all_wins"],
                    row["avg_final_hp_fraction_present"],
                    row["avg_turns_present"],
                ]
                for row in weaker_perf
            ],
        ),
        "",
        "Cautions from the win set:",
        "",
        "- Cards in this table are not automatically bad. Many are chosen when a deck is already under pressure or needs a specific answer.",
        "- `Perfected Strike` remains the cleanest example of an Act 1 bridge: it is picked much more often than it survives as a central endgame card.",
        "- Damage-only attacks with weaker draw/block contribution should be treated as context picks unless the deck has clear relic or Vulnerable support.",
        "",
        "## Draft Rules Suggested By These Wins",
        "",
        f"1. Prioritize `Pommel Strike` early and accept duplicates. Winning decks averaged {final_by_name['Pommel Strike']['avg_copies_when_present']} copies when present.",
        f"2. Take `Bloodletting` highly. It appears in {final_by_name['Bloodletting']['pct_runs_in_final_deck']}% of final decks and supports larger decks without losing tempo.",
        "3. Build block with cantrip/scaling pieces instead of pure defense only: `Shrug It Off`, `Blood Wall`, `True Grit`, `Dominate`, `Tremble`, and `Colossus` are repeated names.",
        "4. Add draw/exhaust once the deck has enough payoff. `Battle Trance`, `Offering`, `Burning Pact`, `Feel No Pain`, `Second Wind`, and `Fiend Fire` are the package to watch.",
        "5. Treat Act 1 as the main deck-building window. The visible growth estimate adds roughly eight cards in Act 1, then slows each act. By Act 3, winners are much more selective.",
        "",
        "## Data Limitations",
        "",
        "- The run exports include chosen cards and final decks, but not the full reward screens. A card missing from the data may have been offered and skipped.",
        "- Shop purchases and event transforms are imperfectly observable from floor rewards; final deck frequency is therefore more reliable than pick source for those cards.",
        "- All runs are wins. The next useful comparison is a matched loss/failure set to identify overpicked cards, failed archetypes, and deck-size thresholds that stop working.",
        "",
        "## Generated Tables",
        "",
        "- `run_summary.csv`: one row per run.",
        "- `card_pick_timing.csv`: chosen-card counts and floor/act timing.",
        "- `final_deck_card_frequency.csv`: final-deck card frequency and upgrade rates.",
        "- `card_performance_winset.csv`: present-card averages within the win corpus.",
        "- `card_pair_cooccurrence.csv`: common final-deck card pairs.",
        "- `card_package_cooccurrence.csv`: common final-deck three-card packages.",
        "- `act_summary.csv`: act-level visible deck growth, damage, turns, elites, rests, smiths, heals, relics.",
        "- `act_card_type_mix.csv`: visible picked-card type mix by act.",
        "- `node_mix_by_act.csv`: node distribution by act.",
        "- `campfire_usage.csv`: smith/heal split by act.",
        "- `smith_targets.csv`: most common cards upgraded at campfires.",
        "- `relic_frequency.csv`: relic appearance frequency in the win set.",
        "- `encounter_summary.csv`: damage and turns by encounter.",
        "",
    ]
    return "\n".join(report)


def main() -> None:
    OUT_DIR.mkdir(exist_ok=True)
    runs = load_runs()
    stats = collect_stats(runs)

    write_csv(
        OUT_DIR / "run_summary.csv",
        [
            "run_id",
            "player",
            "date",
            "result",
            "ascension",
            "floors",
            "deck_size",
            "final_hp",
            "final_hp_fraction",
            "total_damage",
            "total_turns",
            "elites_killed",
            "duration_minutes",
            "relic_count",
            "bosses",
            "visible_deck_after_act1",
            "visible_deck_after_act2",
            "visible_deck_after_act3",
            "known_final_cards_by_act1",
            "known_final_cards_by_act2",
            "known_final_cards_by_act3",
            "final_cards_not_visible_in_rewards",
            "visible_final_gap",
            "damage_act1",
            "damage_act2",
            "damage_act3",
            "turns_act1",
            "turns_act2",
            "turns_act3",
            "smiths",
            "heals",
        ],
        stats["run_rows"],
    )
    write_csv(
        OUT_DIR / "card_pick_timing.csv",
        [
            "card_id",
            "name",
            "picked_count",
            "runs_with_pick",
            "pct_runs_with_pick",
            "avg_pick_floor",
            "median_pick_floor",
            "earliest_pick_floor",
            "latest_pick_floor",
            "act1_picks",
            "act2_picks",
            "act3_picks",
            "monster_picks",
            "elite_picks",
            "boss_picks",
            "event_or_other_picks",
        ],
        stats["pick_rows"],
    )
    write_csv(
        OUT_DIR / "final_deck_card_frequency.csv",
        [
            "card_id",
            "name",
            "type",
            "runs_in_final_deck",
            "pct_runs_in_final_deck",
            "total_final_copies",
            "avg_copies_when_present",
            "upgraded_final_copies",
            "pct_final_copies_upgraded",
        ],
        stats["final_rows"],
    )
    write_csv(
        OUT_DIR / "card_performance_winset.csv",
        [
            "card_id",
            "name",
            "type",
            "runs_present",
            "avg_damage_present",
            "damage_vs_all_wins",
            "avg_final_hp_fraction_present",
            "hp_fraction_vs_all_wins",
            "avg_turns_present",
            "turns_vs_all_wins",
            "avg_deck_size_present",
            "runs_absent",
        ],
        stats["performance_rows"],
    )
    write_csv(
        OUT_DIR / "card_pair_cooccurrence.csv",
        [
            "left_card_id",
            "left_name",
            "right_card_id",
            "right_name",
            "runs_with_pair",
            "pct_runs_with_pair",
            "avg_damage",
            "damage_vs_all_wins",
            "avg_final_hp_fraction",
            "avg_turns",
        ],
        stats["pair_rows"],
    )
    write_csv(
        OUT_DIR / "card_package_cooccurrence.csv",
        [
            "card_ids",
            "cards",
            "runs_with_package",
            "pct_runs_with_package",
            "avg_damage",
            "damage_vs_all_wins",
            "avg_final_hp_fraction",
            "avg_turns",
        ],
        stats["package_rows"],
    )
    write_csv(
        OUT_DIR / "act_summary.csv",
        [
            "act",
            "runs",
            "avg_visible_deck_after_act",
            "median_visible_deck_after_act",
            "p25_visible_deck_after_act",
            "p75_visible_deck_after_act",
            "min_visible_deck_after_act",
            "max_visible_deck_after_act",
            "avg_known_final_cards_acquired_by_act",
            "avg_visible_cards_added_in_act",
            "avg_damage_in_act",
            "avg_turns_in_act",
            "avg_combats_in_act",
            "avg_elites_in_act",
            "avg_rests_in_act",
            "avg_smiths_in_act",
            "avg_heals_in_act",
            "smith_to_heal_ratio",
            "avg_relics_in_act",
            "avg_potions_in_act",
        ],
        stats["act_rows"],
    )
    write_csv(
        OUT_DIR / "act_card_type_mix.csv",
        ["act", "card_type", "visible_picks", "pct_visible_picks", "avg_picks_per_run"],
        stats["act_card_type_rows"],
    )
    write_csv(
        OUT_DIR / "node_mix_by_act.csv",
        ["act", "node_type", "nodes", "pct_act_nodes", "avg_nodes_per_run"],
        stats["node_rows"],
    )
    write_csv(
        OUT_DIR / "campfire_usage.csv",
        [
            "act",
            "rest_nodes",
            "smith_actions",
            "heal_actions",
            "smiths_per_run",
            "heals_per_run",
            "smith_share_of_actions",
            "heal_share_of_actions",
        ],
        stats["campfire_rows"],
    )
    write_csv(
        OUT_DIR / "smith_targets.csv",
        ["card", "smith_count", "pct_runs"],
        stats["smith_target_rows"],
    )
    write_csv(
        OUT_DIR / "relic_frequency.csv",
        ["relic", "copies_seen", "runs_seen", "pct_runs_seen"],
        stats["relic_rows"],
    )
    write_csv(
        OUT_DIR / "encounter_summary.csv",
        ["encounter", "runs", "avg_damage", "median_damage", "avg_turns", "median_turns"],
        stats["encounter_rows"],
    )
    (OUT_DIR / "ironclad_a10_win_analysis.md").write_text(build_report(stats))


if __name__ == "__main__":
    main()
