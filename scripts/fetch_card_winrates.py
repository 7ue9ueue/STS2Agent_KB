#!/usr/bin/env python3
"""Fetch Ironclad card win-rate stats from sts2.fun/cards.

The cards page exposes a hidden HTML table where each row stores card stats in
data-* attributes. This script extracts those rows into a CSV and a KB-facing
Markdown table used during card reward decisions.
"""

from __future__ import annotations

import csv
import html
import json
import re
import urllib.request
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_URL = "https://sts2.fun/cards"
CSV_OUT = ROOT / "kb" / "strategies" / "card_winrates.csv"
MD_OUT = ROOT / "kb" / "strategies" / "card_winrates.md"


ATTR_RE = re.compile(r"\s(data-[\w-]+)=(['\"])(.*?)\2", re.DOTALL)
ROW_RE = re.compile(r"<tr\s+data-card=.*?</tr>", re.DOTALL)


FIELDS = [
    "card_id",
    "name",
    "upgraded",
    "card_class",
    "rarity",
    "type",
    "cost",
    "offered",
    "picked",
    "shop_picked",
    "pick_rate_pct",
    "picked_wins",
    "picked_winrate_pct",
    "skipped_wins",
    "skipped_count",
    "skipped_winrate_pct",
    "impact_pp",
    "act1_pick_rate_pct",
    "act2_pick_rate_pct",
    "act3_pick_rate_pct",
]


def fetch_html() -> str:
    request = urllib.request.Request(
        SOURCE_URL,
        headers={"User-Agent": "STS2MCP-card-winrate-fetcher/1.0"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8")


def parse_float(raw: str) -> float:
    if raw == "":
        return 0.0
    return float(raw)


def parse_int(raw: str) -> int:
    if raw == "":
        return 0
    return int(float(raw))


def fmt_pct(value: float) -> str:
    return f"{value:.1f}%"


def fmt_pp(value: float) -> str:
    sign = "+" if value > 0 else ""
    return f"{sign}{value:.1f}"


def display_name(row: dict[str, object]) -> str:
    suffix = "+" if int(row.get("upgraded") or 0) else ""
    return f"{row['name']}{suffix}"


def row_attrs(row_html: str) -> dict[str, str]:
    attrs: dict[str, str] = {}
    for key, _quote, value in ATTR_RE.findall(row_html):
        attrs[key[5:].replace("-", "_")] = html.unescape(value)
    return attrs


def parse_act_pick_rates(raw: str) -> tuple[float, float, float]:
    if not raw:
        return (0.0, 0.0, 0.0)
    data = json.loads(raw)
    rates = [float(item.get("pick_rate") or 0) * 100 for item in data[:3]]
    while len(rates) < 3:
        rates.append(0.0)
    return (rates[0], rates[1], rates[2])


def extract_rows(page_html: str) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for row_html in ROW_RE.findall(page_html):
        attrs = row_attrs(row_html)
        if attrs.get("cardclass") != "Ironclad":
            continue
        winrate = parse_float(attrs.get("winrate", ""))
        skipped_winrate = parse_float(attrs.get("skipped_winrate", ""))
        act1, act2, act3 = parse_act_pick_rates(attrs.get("act_data", ""))
        upgraded = parse_int(attrs.get("upgraded", ""))
        rows.append(
            {
                "card_id": attrs.get("card", ""),
                "name": attrs.get("displayname", ""),
                "upgraded": upgraded,
                "card_class": attrs.get("cardclass", ""),
                "rarity": attrs.get("rarity", ""),
                "type": attrs.get("type", ""),
                "cost": attrs.get("cost_upgraded" if upgraded else "cost", ""),
                "offered": parse_int(attrs.get("offered", "")),
                "picked": parse_int(attrs.get("picked", "")),
                "shop_picked": parse_int(attrs.get("shop_picked", "")),
                "pick_rate_pct": round(parse_float(attrs.get("pickrate", "")), 2),
                "picked_wins": parse_int(attrs.get("wins", "")),
                "picked_winrate_pct": round(winrate, 2),
                "skipped_wins": parse_int(attrs.get("skipped_wins", "")),
                "skipped_count": parse_int(attrs.get("skipped_count", "")),
                "skipped_winrate_pct": round(skipped_winrate, 2),
                "impact_pp": round(winrate - skipped_winrate, 2),
                "act1_pick_rate_pct": round(act1, 2),
                "act2_pick_rate_pct": round(act2, 2),
                "act3_pick_rate_pct": round(act3, 2),
            }
        )
    return sorted(rows, key=lambda row: (str(row["name"]).lower(), int(row["upgraded"])))


def write_csv(rows: list[dict[str, object]]) -> None:
    with CSV_OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def write_markdown(rows: list[dict[str, object]]) -> None:
    generated = date.today().isoformat()
    sorted_by_impact = sorted(rows, key=lambda row: float(row["impact_pp"]), reverse=True)
    top = sorted_by_impact[:10]
    bottom = sorted_by_impact[-10:]

    lines = [
        "# Card Win Rates",
        "",
        f"Source: `{SOURCE_URL}` hidden cards data table, fetched on {generated}.",
        "",
        "These are global Ironclad card-offer stats from the site, not causal card strength. A low picked win rate can mean the card is taken in desperate positions or too late; a high skipped win rate can mean the card is commonly offered to already-strong decks. Use this table as a scrutiny signal alongside `reward_choice.md`, `card_impressions.md`, and the specific card KB file.",
        "",
        "Definitions:",
        "- `Picked WR`: win rate when the card was picked from an offer.",
        "- `Skipped WR`: win rate when the card was offered but skipped.",
        "- `Impact`: `Picked WR - Skipped WR`, in percentage points.",
        "- `A1/A2/A3 Pick`: pick rate by act when offered.",
        "- Upgraded offer rows are labeled with `+`.",
        "",
        "## Highest Positive Impact",
        "",
        "| Card | Rarity | Type | Pick Rate | Picked WR | Skipped WR | Impact |",
        "|---|---|---|---:|---:|---:|---:|",
    ]
    for row in top:
        lines.append(
            f"| {display_name(row)} | {row['rarity']} | {row['type']} | "
            f"{fmt_pct(float(row['pick_rate_pct']))} | "
            f"{fmt_pct(float(row['picked_winrate_pct']))} | "
            f"{fmt_pct(float(row['skipped_winrate_pct']))} | "
            f"{fmt_pp(float(row['impact_pp']))} |"
        )

    lines.extend(
        [
            "",
            "## Lowest Impact",
            "",
            "| Card | Rarity | Type | Pick Rate | Picked WR | Skipped WR | Impact |",
            "|---|---|---|---:|---:|---:|---:|",
        ]
    )
    for row in bottom:
        lines.append(
            f"| {display_name(row)} | {row['rarity']} | {row['type']} | "
            f"{fmt_pct(float(row['pick_rate_pct']))} | "
            f"{fmt_pct(float(row['picked_winrate_pct']))} | "
            f"{fmt_pct(float(row['skipped_winrate_pct']))} | "
            f"{fmt_pp(float(row['impact_pp']))} |"
        )

    lines.extend(
        [
            "",
            "## All Ironclad Cards",
            "",
            "| Card | Rarity | Type | Cost | Offered | Picked | Pick Rate | Picked WR | Skipped WR | Impact | A1 Pick | A2 Pick | A3 Pick |",
            "|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in rows:
        lines.append(
            f"| {display_name(row)} | {row['rarity']} | {row['type']} | {row['cost']} | "
            f"{row['offered']} | {row['picked']} | "
            f"{fmt_pct(float(row['pick_rate_pct']))} | "
            f"{fmt_pct(float(row['picked_winrate_pct']))} | "
            f"{fmt_pct(float(row['skipped_winrate_pct']))} | "
            f"{fmt_pp(float(row['impact_pp']))} | "
            f"{fmt_pct(float(row['act1_pick_rate_pct']))} | "
            f"{fmt_pct(float(row['act2_pick_rate_pct']))} | "
            f"{fmt_pct(float(row['act3_pick_rate_pct']))} |"
        )

    lines.extend(
        [
            "",
            "## Rebuild",
            "",
            "```bash",
            "python3 scripts/fetch_card_winrates.py",
            "```",
            "",
        ]
    )
    MD_OUT.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    rows = extract_rows(fetch_html())
    if not rows:
        raise SystemExit("No Ironclad card rows found")
    write_csv(rows)
    write_markdown(rows)
    print(f"Wrote {len(rows)} rows to {CSV_OUT.relative_to(ROOT)}")
    print(f"Wrote {MD_OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
