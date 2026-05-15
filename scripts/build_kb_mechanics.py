#!/usr/bin/env python3
"""Rebuild kb/mechanics from structured STS2 data sources."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

import requests


REPO_ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = REPO_ROOT / "kb" / "mechanics"
BASE = "https://spire-codex.com/api"
HEADERS = {"User-Agent": "STS2MCP mechanics KB builder"}


COMMON_BUFFS = {
    "STRENGTH",
    "DEXTERITY",
    "ARTIFACT",
    "PLATING",
    "INTANGIBLE",
    "BLOCK_NEXT_TURN",
    "DRAW_CARDS_NEXT_TURN",
    "ENERGY_NEXT_TURN",
    "BARRICADE",
    "BUFFER",
    "FOCUS",
    "THORNS",
    "VIGOR",
}

COMMON_DEBUFFS = {
    "VULNERABLE",
    "WEAK",
    "FRAIL",
    "POISON",
    "DOOM",
    "CONFUSED",
    "SLOW",
    "SURROUNDED",
    "TANGLED",
    "WASTE_AWAY",
    "STRANGLE",
}


def fetch_json(endpoint: str) -> Any:
    response = requests.get(f"{BASE}/{endpoint}", headers=HEADERS, timeout=30)
    response.raise_for_status()
    return response.json()


def clean_markup(text: str | None) -> str:
    if not text:
        return ""
    text = re.sub(r"\[(gold|blue|red|green)\](.*?)\[/\1\]", r"\2", text)
    text = re.sub(r"\[energy:(\d+)\]", r"\1 Energy", text)
    text = re.sub(r"\[star:(\d+)\]", r"\1 Star", text)
    text = re.sub(r"\[Amount\]", "X", text)
    text = text.replace("0 1 Energy", "0 Energy")
    text = text.replace("1 1 Energy", "1 Energy")
    text = text.replace("by .", "by X.")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def name_from_id(value: str) -> str:
    value = re.sub(r"_(BOSS|NORMAL|WEAK|ELITE)$", "", value)
    return value.replace("_", " ").title()


def encounter_name(value: str) -> str:
    match = re.search(r"_(BOSS|NORMAL|WEAK|ELITE)$", value)
    base = name_from_id(value)
    if not match or match.group(1) == "BOSS":
        return base
    return f"{base} ({match.group(1).title()})"


def unique_names(values: list[str], encounter: bool = False) -> list[str]:
    seen: set[str] = set()
    names: list[str] = []
    for value in values:
        name = encounter_name(value) if encounter else name_from_id(value)
        if name not in seen:
            seen.add(name)
            names.append(name)
    return names


def frontmatter(title: str, source: str, generated_from: list[str] | None = None) -> str:
    lines = [
        "---",
        f"title: {title}",
        f"source: {source}",
        "generated: true",
    ]
    if generated_from:
        lines.append("generated_from:")
        lines.extend(f"  - {item}" for item in generated_from)
    lines.extend(["---", ""])
    return "\n".join(lines)


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def power_row(power: dict[str, Any]) -> str:
    desc = clean_markup(power.get("description")).replace("|", "\\|")
    negative = "yes" if power.get("allow_negative") is True else ""
    return f"| {power['name']} | `{power['id']}` | {power.get('stack_type') or ''} | {negative} | {desc} |"


def powers_doc(title: str, power_type: str, powers: list[dict[str, Any]], common_ids: set[str]) -> str:
    selected = sorted([p for p in powers if p.get("type") == power_type], key=lambda p: (p["name"], p["id"]))
    common = [p for p in selected if p["id"] in common_ids]
    lines = [
        frontmatter(title, f"{BASE}/powers"),
        f"# {title}",
        "",
        f"Structured list of `{power_type}` powers from Spire Codex. Descriptions are game text with UI color tags removed.",
        "",
        "## Stack Types",
        "",
        "- `Counter`: stack count usually tracks charges, amount, or remaining turns depending on the effect text.",
        "- `Single`: present or absent; duplicate applications generally do not create a separate visible stack.",
        "- `None`: no stack value is shown by the source data.",
        "",
        "## Common Agent Checks",
        "",
    ]
    if common:
        lines.extend(["| Name | ID | Stack | Negative? | Description |", "|---|---|---|---|---|"])
        lines.extend(power_row(power) for power in common)
    else:
        lines.append("_No common checks configured._")

    lines.extend(["", "## Full List", "", "| Name | ID | Stack | Negative? | Description |", "|---|---|---|---|---|"])
    lines.extend(power_row(power) for power in selected)
    return "\n".join(lines)


def keywords_doc(keywords: list[dict[str, Any]]) -> str:
    keywords = [kw for kw in keywords if clean_markup(kw.get("description"))]
    lines = [
        frontmatter("Keywords", f"{BASE}/keywords"),
        "# Keywords",
        "",
        "Card keywords from Spire Codex. This file is deliberately limited to keyword text exposed by the structured source.",
        "",
        "| Keyword | ID | Meaning |",
        "|---|---|---|",
    ]
    for kw in sorted(keywords, key=lambda item: item["name"]):
        lines.append(f"| {kw['name']} | `{kw['id']}` | {clean_markup(kw.get('description')).replace('|', '\\|')} |")
    return "\n".join(lines)


def ascension_doc(ascensions: list[dict[str, Any]]) -> str:
    lines = [
        frontmatter("Ascension", f"{BASE}/ascensions"),
        "# Ascension",
        "",
        "Ascension modifiers are cumulative: A10 includes the effects from A1 through A10.",
        "",
        "| Level | Name | Effect |",
        "|---:|---|---|",
    ]
    for asc in sorted(ascensions, key=lambda item: item["level"]):
        lines.append(f"| A{asc['level']} | {asc['name']} | {clean_markup(asc.get('description')).replace('|', '\\|')} |")
    lines.extend(
        [
            "",
            "## A10 Reminder",
            "",
            "At A10, the run uses every listed modifier through `Double Boss`: more elites, weaker ancient healing, less gold, one fewer potion slot, Ascender's Bane, more expensive removals, lower rare/upgraded card frequency, tougher enemies, deadlier attacks, and two Act 3 bosses.",
        ]
    )
    return "\n".join(lines)


def acts_doc(acts: list[dict[str, Any]]) -> str:
    acts = [act for act in acts if act["id"] != "DEPRECATED_ACT"]
    lines = [
        frontmatter("Acts", f"{BASE}/acts"),
        "# Acts",
        "",
        "Act data from Spire Codex. Lists use source IDs converted to names for readability.",
        "",
        "| Act | Rooms | Ancients | Bosses | Events | Encounters |",
        "|---|---:|---|---|---:|---:|",
    ]
    for act in sorted(acts, key=lambda item: item["name"]):
        lines.append(
            "| {name} | {rooms} | {ancients} | {bosses} | {event_count} | {encounter_count} |".format(
                name=act["name"],
                rooms=act["num_rooms"],
                ancients=", ".join(unique_names(act.get("ancients", []))),
                bosses=", ".join(unique_names(act.get("bosses", []))),
                event_count=len(act.get("events", [])),
                encounter_count=len(act.get("encounters", [])),
            )
        )
    for act in sorted(acts, key=lambda item: item["name"]):
        lines.extend(
            [
                "",
                f"## {act['name']}",
                "",
                f"- Source ID: `{act['id']}`",
                f"- Rooms: {act['num_rooms']}",
                f"- Ancients: {', '.join(unique_names(act.get('ancients', []))) or 'none'}",
                f"- Bosses: {', '.join(unique_names(act.get('bosses', []))) or 'none'}",
                f"- Events: {', '.join(unique_names(act.get('events', []))) or 'none'}",
                f"- Encounters: {', '.join(unique_names(act.get('encounters', []), encounter=True)) or 'none'}",
            ]
        )
    return "\n".join(lines)


def core_doc() -> str:
    return "\n".join(
        [
            frontmatter(
                "Core Mechanics",
                "https://slaythespire.wiki.gg/wiki/Slay_the_Spire_2:Mechanics",
                [f"{BASE}/keywords", f"{BASE}/powers", f"{BASE}/ascensions", f"{BASE}/acts"],
            ),
            "# Core Mechanics",
            "",
            "This file is a compact orientation page. Use the linked mechanics files for structured source-backed lists.",
            "",
            "## Resources",
            "",
            "- HP: reaching 0 HP ends the run. Max HP changes also adjust current HP by the same amount.",
            "- Energy: spent to play most cards during combat.",
            "- Gold: spent at shops and some events; earned mostly from combats, chests, events, relics, and cards.",
            "- Potions: single-use combat consumables that persist between combats until used or discarded.",
            "",
            "## Cards",
            "",
            "- Cards can be added, removed, upgraded, or transformed outside combat.",
            "- Upgrading changes card values or behavior when the card has an upgrade form.",
            "- Transform changes a card into a random card of the same color unless the effect says otherwise.",
            "- Exhaust removes a card from the current combat, not from the permanent deck.",
            "",
            "## Useful Files",
            "",
            "- `keywords.md`: card keywords from structured source data.",
            "- `buffs.md`: beneficial or neutral powers/statuses.",
            "- `debuffs.md`: harmful powers/statuses.",
            "- `ascension.md`: cumulative A0-A10 modifiers.",
            "- `acts.md`: act, boss, ancient, event, and encounter source IDs.",
            "- `map_locations.md`: map node types and reward expectations.",
        ]
    )


def map_locations_doc() -> str:
    return "\n".join(
        [
            frontmatter("Map Locations", "https://slaythespire.wiki.gg/wiki/Slay_the_Spire_2:Map_Locations"),
            "# Map Locations",
            "",
            "Map locations are the node types available while pathing through an act.",
            "",
            "| Node | What It Means | Typical Reward / Result |",
            "|---|---|---|",
            "| Monster | Normal combat encounter. Early encounters in each act come from easier pools. | Gold, card reward, possible potion. |",
            "| Elite | Hard combat encounter. The same elite cannot appear twice in a row. | Relic, gold, card reward, possible potion. |",
            "| Rest Site | Non-combat choice node. | Usually Rest or Smith; relics can add options. |",
            "| Unknown | Event-style node that can resolve into several node types. | Event, monster, merchant, or treasure depending on roll. |",
            "| Treasure | Chest node. | Relic and gold unless modified by relics/effects. |",
            "| Merchant | Shop. | Buy cards/relics/potions or remove one card. |",
            "| Boss | End-of-act boss combat. | Act 1/2 bosses give gold, rare card choice, possible potion; Act 3 victory ends the run. |",
            "| Ancient | Start-of-act ancient. | Healing and ancient relic/boon choices. Neow starts Act 1. |",
            "",
            "## Rest Sites",
            "",
            "- Rest heals 30% of max HP, rounded down.",
            "- Smith upgrades one card.",
            "- There is always a rest site before a boss encounter.",
            "",
            "## A10 Pathing Relevance",
            "",
            "- A1 increases elite frequency.",
            "- A2 reduces ancient healing to 80% of missing HP.",
            "- A3 reduces enemy and treasure gold by 25%.",
            "- A4 starts runs with one fewer potion slot.",
            "- A10 adds a second Act 3 boss.",
        ]
    )


def index_doc(counts: dict[str, int]) -> str:
    return "\n".join(
        [
            frontmatter("Mechanics Index", "mixed structured sources"),
            "# Mechanics Index",
            "",
            "Generated by `scripts/build_kb_mechanics.py` from structured sources.",
            "",
            "| File | Contents |",
            "|---|---|",
            "| `core_mechanics.md` | Compact overview and links. |",
            f"| `keywords.md` | {counts['keywords']} card keywords from Spire Codex. |",
            f"| `buffs.md` | {counts['buffs']} buff/neutral powers from Spire Codex. |",
            f"| `debuffs.md` | {counts['debuffs']} debuff powers from Spire Codex. |",
            f"| `ascension.md` | {counts['ascensions']} ascension levels from Spire Codex. |",
            f"| `acts.md` | {counts['acts']} active acts from Spire Codex. |",
            "| `map_locations.md` | Cleaned node-type reference. |",
            "| `powers.json` | Raw normalized powers data used for `buffs.md` and `debuffs.md`. |",
            "",
            "No draft priority or inferred policy is included here; these are factual references for agent use.",
        ]
    )


def main() -> int:
    powers = fetch_json("powers")
    keywords = fetch_json("keywords")
    ascensions = fetch_json("ascensions")
    acts = fetch_json("acts")

    normalized_powers = [
        {
            "id": power["id"],
            "name": power["name"],
            "type": power["type"],
            "stack_type": power.get("stack_type"),
            "allow_negative": power.get("allow_negative"),
            "description": clean_markup(power.get("description")),
            "description_raw": clean_markup(power.get("description_raw")),
            "image_url": power.get("image_url"),
        }
        for power in sorted(powers, key=lambda item: (item["type"], item["name"], item["id"]))
    ]

    write(OUT_DIR / "_index.md", index_doc({
        "keywords": len([kw for kw in keywords if clean_markup(kw.get("description"))]),
        "buffs": len([p for p in powers if p.get("type") == "Buff"]),
        "debuffs": len([p for p in powers if p.get("type") == "Debuff"]),
        "ascensions": len(ascensions),
        "acts": len([act for act in acts if act["id"] != "DEPRECATED_ACT"]),
    }))
    write(OUT_DIR / "core_mechanics.md", core_doc())
    write(OUT_DIR / "keywords.md", keywords_doc(keywords))
    write(OUT_DIR / "buffs.md", powers_doc("Buffs", "Buff", powers, COMMON_BUFFS))
    write(OUT_DIR / "debuffs.md", powers_doc("Debuffs", "Debuff", powers, COMMON_DEBUFFS))
    write(OUT_DIR / "ascension.md", ascension_doc(ascensions))
    write(OUT_DIR / "acts.md", acts_doc(acts))
    write(OUT_DIR / "map_locations.md", map_locations_doc())
    write(OUT_DIR / "powers.json", json.dumps(normalized_powers, indent=2, ensure_ascii=False))

    print(f"wrote mechanics KB to {OUT_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
