#!/usr/bin/env python3
"""Fetch successful Ironclad A10 run summaries from sts2.fun.

The site renders the useful run data as static HTML. This script discovers
candidate run URLs from the homepage/player histories, then parses each run
page into JSON plus a readable Markdown summary.
"""

from __future__ import annotations

import argparse
import json
import re
import time
from collections import OrderedDict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


BASE_URL = "https://sts2.fun"
HEADERS = {
    "User-Agent": "STS2MCP knowledge-base scraper (+local research; contact repo owner)",
}


def clean_text(node: Any) -> str:
    if node is None:
        return ""
    return re.sub(r"\s+", " ", node.get_text(" ", strip=True)).strip()


def to_int(value: str) -> int | None:
    match = re.search(r"-?\d+", value or "")
    return int(match.group(0)) if match else None


def run_id_from_url(url: str) -> str:
    return url.rstrip("/").split("/")[-1]


def fetch(session: requests.Session, url: str, delay: float) -> str:
    response = session.get(url, headers=HEADERS, timeout=30)
    response.raise_for_status()
    if delay:
        time.sleep(delay)
    return response.text


def ordered_unique(items: list[str]) -> list[str]:
    return list(OrderedDict((item, None) for item in items).keys())


def discover_players(home_html: str, seed_players: list[str]) -> list[str]:
    soup = BeautifulSoup(home_html, "html.parser")
    players = list(seed_players)
    for link in soup.select('a[href^="/player/"]'):
        href = link.get("href", "")
        player = href.removeprefix("/player/").strip("/")
        if player:
            players.append(player)
    return ordered_unique(players)


def parse_run_history(player: str, html: str) -> list[dict[str, Any]]:
    soup = BeautifulSoup(html, "html.parser")
    table = soup.select_one("#run-history")
    if table is None:
        return []

    runs: list[dict[str, Any]] = []
    for row in table.select("tbody tr"):
        cells = row.find_all("td", recursive=False)
        if len(cells) < 8:
            continue
        link = cells[1].select_one('a[href^="/run/"]')
        if link is None:
            continue
        runs.append(
            {
                "source_player": player,
                "date": clean_text(cells[0]),
                "character": clean_text(link),
                "ascension": to_int(clean_text(cells[2])),
                "result": clean_text(cells[3]).upper(),
                "floors": to_int(clean_text(cells[4])),
                "listed_deck_size": to_int(clean_text(cells[5])),
                "duration": clean_text(cells[6]),
                "killed_by": clean_text(cells[7]).replace("—", ""),
                "url": urljoin(BASE_URL, link.get("href", "")),
            }
        )
    return runs


def direct_homepage_runs(home_html: str) -> list[dict[str, Any]]:
    soup = BeautifulSoup(home_html, "html.parser")
    runs: list[dict[str, Any]] = []
    for table in soup.select("table"):
        headers = [clean_text(th) for th in table.select("thead th")]
        if not {"Date", "Character", "A", "Result"}.issubset(set(headers)):
            continue
        header_index = {name: idx for idx, name in enumerate(headers)}
        for row in table.select("tbody tr"):
            cells = row.find_all("td", recursive=False)
            if len(cells) < 5:
                continue
            link = row.select_one('a[href^="/run/"]')
            if link is None:
                continue
            player_link = row.select_one('a[href^="/player/"]')
            def cell_text(name: str) -> str:
                idx = header_index.get(name)
                return clean_text(cells[idx]) if idx is not None and idx < len(cells) else ""

            runs.append(
                {
                    "source_player": cell_text("Player") or (clean_text(player_link) if player_link else ""),
                    "date": cell_text("Date"),
                    "character": clean_text(link),
                    "ascension": to_int(cell_text("A")),
                    "result": cell_text("Result").upper(),
                    "floors": to_int(cell_text("Floors")),
                    "listed_deck_size": to_int(cell_text("Deck")),
                    "duration": cell_text("Time"),
                    "killed_by": cell_text("Killed By").replace("—", ""),
                    "url": urljoin(BASE_URL, link.get("href", "")),
                }
            )
    return runs


def is_target_run(run: dict[str, Any]) -> bool:
    return (
        run.get("character") == "Ironclad"
        and run.get("ascension") == 10
        and run.get("result") == "WIN"
    )


def section_by_heading(soup: BeautifulSoup, heading_prefix: str) -> Any:
    for card in soup.select("div.card"):
        heading = card.find(["h2", "h3"])
        if heading and clean_text(heading).startswith(heading_prefix):
            return card
    return None


def parse_hp(text: str) -> dict[str, int | None]:
    match = re.search(r"(\d+)\s*/\s*(\d+)", text)
    delta_match = re.search(r"([+-]\d+)\s*$", text)
    return {
        "current": int(match.group(1)) if match else None,
        "max": int(match.group(2)) if match else None,
        "delta": int(delta_match.group(1)) if delta_match else None,
    }


def parse_gold(text: str) -> dict[str, int | None]:
    numbers = re.findall(r"[+-]?\d+", text)
    return {
        "current": int(numbers[0]) if numbers else None,
        "delta": int(numbers[-1]) if len(numbers) > 1 else None,
    }


def parse_reward_cell(cell: Any) -> dict[str, Any]:
    cards = []
    for span in cell.select("[data-card-id]"):
        cards.append(
            {
                "id": span.get("data-card-id"),
                "name": clean_card_name(span),
                "upgraded": span.get("data-upgraded") == "1",
            }
        )

    relics = []
    for span in cell.select("[data-relic-id]"):
        relics.append(
            {
                "id": span.get("data-relic-id"),
                "name": clean_relic_name(span),
            }
        )

    other = []
    for span in cell.find_all("span"):
        if span.has_attr("data-card-id") or span.has_attr("data-relic-id"):
            continue
        if span.find_parent(attrs={"data-card-id": True}) or span.find_parent(attrs={"data-relic-id": True}):
            continue
        value = clean_text(span)
        if value and not re.fullmatch(r"[+-]?\d+", value):
            other.append(value)

    return {
        "text": clean_text(cell),
        "cards": cards,
        "relics": relics,
        "other": ordered_unique(other),
    }


def clean_card_name(span: Any) -> str:
    parts = [s.strip() for s in span.stripped_strings if s.strip()]
    if parts and re.fullmatch(r"\d+", parts[-1]):
        parts = parts[:-1]
    name = " ".join(parts).replace(" +", "+")
    return name


def clean_relic_name(span: Any) -> str:
    img = span.find("img")
    if img and img.get("title"):
        return img["title"].strip()
    parts = [s.strip() for s in span.stripped_strings if s.strip()]
    if parts and re.fullmatch(r"F\d+", parts[-1]):
        parts = parts[:-1]
    return " ".join(parts)


def parse_floor_rows(soup: BeautifulSoup) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for row in soup.select("table.run-floors tbody tr"):
        cells = row.find_all("td", recursive=False)
        if len(cells) < 9:
            continue
        rows.append(
            {
                "floor": to_int(clean_text(cells[0])),
                "act": to_int(clean_text(cells[1])),
                "node_type": clean_text(cells[2]),
                "encounter": clean_text(cells[3]),
                "turns": to_int(clean_text(cells[4])),
                "damage_taken": to_int(clean_text(cells[5])),
                "hp": parse_hp(clean_text(cells[6])),
                "gold": parse_gold(clean_text(cells[7])),
                "rewards": parse_reward_cell(cells[8]),
            }
        )
    return rows


def parse_relics(soup: BeautifulSoup) -> list[dict[str, Any]]:
    section = section_by_heading(soup, "Relics")
    if section is None:
        return []
    relics = []
    for span in section.select("[data-relic-id]"):
        floor_match = re.search(r"\bF(\d+)\b", clean_text(span))
        relics.append(
            {
                "id": span.get("data-relic-id"),
                "name": clean_relic_name(span),
                "floor": int(floor_match.group(1)) if floor_match else None,
            }
        )
    return relics


def parse_final_deck(soup: BeautifulSoup) -> list[dict[str, Any]]:
    section = section_by_heading(soup, "Final Deck")
    if section is None:
        return []
    cards = []
    current_type = ""
    for element in section.find_all(["span"]):
        if not element.has_attr("data-card-id"):
            text = clean_text(element)
            if text in {"Attack", "Skill", "Power", "Curse", "Status"}:
                current_type = text
            continue
        parts = [s.strip() for s in element.stripped_strings if s.strip()]
        cost = parts[-1] if parts and re.fullmatch(r"\d+|X", parts[-1]) else None
        cards.append(
            {
                "id": element.get("data-card-id"),
                "name": clean_card_name(element),
                "upgraded": element.get("data-upgraded") == "1",
                "cost": cost,
                "type": current_type,
            }
        )
    return cards


def parse_summary_stats(soup: BeautifulSoup) -> dict[str, str]:
    stats: dict[str, str] = {}
    for box in soup.select(".stat-box"):
        label = clean_text(box.select_one(".label"))
        value = clean_text(box.select_one(".value"))
        if label:
            stats[label] = value
    return stats


def parse_run_page(html: str, discovered: dict[str, Any]) -> dict[str, Any]:
    soup = BeautifulSoup(html, "html.parser")
    title = clean_text(soup.find("h1"))
    player_link = soup.select_one('a[href^="/player/"]')
    stats = parse_summary_stats(soup)
    final_deck = parse_final_deck(soup)
    floors = parse_floor_rows(soup)

    return {
        "id": run_id_from_url(discovered["url"]),
        "url": discovered["url"],
        "source": "sts2.fun",
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "discovered": discovered,
        "title": title,
        "player": clean_text(player_link) or discovered.get("source_player", ""),
        "character": discovered.get("character"),
        "ascension": discovered.get("ascension"),
        "result": discovered.get("result"),
        "date": discovered.get("date"),
        "summary_stats": stats,
        "floors": floors,
        "relics": parse_relics(soup),
        "final_deck": final_deck,
        "derived": {
            "floor_count": len(floors),
            "final_deck_entries": len(final_deck),
            "final_deck_cards_counted": len(final_deck),
            "relic_count": len(parse_relics(soup)),
            "bosses": [f["encounter"] for f in floors if f.get("node_type") == "boss" and f.get("encounter")],
            "elites": [f["encounter"] for f in floors if f.get("node_type") == "elite" and f.get("encounter")],
        },
    }


def write_markdown(run: dict[str, Any], path: Path) -> None:
    stats = run["summary_stats"]
    deck = run["final_deck"]
    relics = run["relics"]
    floors = run["floors"]
    campfires = next((value for key, value in stats.items() if key.startswith("Campfires")), "")

    lines = [
        f"# {run['player']} - Ironclad A10 WIN",
        "",
        f"- Source: {run['url']}",
        f"- Date: {run.get('date') or 'unknown'}",
        f"- Floors: {stats.get('Floors', run['discovered'].get('floors'))}",
        f"- Duration: {stats.get('Duration', run['discovered'].get('duration'))}",
        f"- Final HP: {stats.get('Final HP', '')}",
        f"- Deck Size: {stats.get('Deck Size', run['discovered'].get('listed_deck_size'))}",
        f"- Final Gold: {stats.get('Final Gold', '')}",
        f"- Elites Killed: {stats.get('Elites Killed', '')}",
        f"- Campfires: {campfires}",
        "",
        "## Relics",
        "",
    ]
    lines.extend(
        f"- F{relic['floor']}: {relic['name']} (`{relic['id']}`)"
        if relic.get("floor")
        else f"- {relic['name']} (`{relic['id']}`)"
        for relic in relics
    )
    lines.extend(["", "## Final Deck", ""])
    for card in deck:
        suffix = "+" if card.get("upgraded") and not card["name"].endswith("+") else ""
        cost = f", cost {card['cost']}" if card.get("cost") is not None else ""
        lines.append(f"- {card['name']}{suffix} (`{card['id']}`{cost})")

    lines.extend(["", "## Floor Decisions And Outcomes", ""])
    lines.append("| Floor | Type | Encounter | HP | Gold | Turns | Damage | Rewards / Actions |")
    lines.append("|---:|---|---|---|---:|---:|---:|---|")
    for floor in floors:
        hp = floor.get("hp", {})
        hp_text = ""
        if hp.get("current") is not None:
            hp_text = f"{hp['current']}/{hp['max']}"
            if hp.get("delta") is not None:
                hp_text += f" ({hp['delta']:+d})"
        gold = floor.get("gold", {})
        gold_text = str(gold.get("current") or "")
        if gold.get("delta") is not None:
            gold_text += f" ({gold['delta']:+d})"
        reward_text = floor["rewards"]["text"].replace("|", "\\|")
        lines.append(
            "| {floor} | {node_type} | {encounter} | {hp} | {gold} | {turns} | {damage} | {rewards} |".format(
                floor=floor.get("floor") or "",
                node_type=floor.get("node_type") or "",
                encounter=(floor.get("encounter") or "").replace("|", "\\|"),
                hp=hp_text,
                gold=gold_text,
                turns=floor.get("turns") or "",
                damage=floor.get("damage_taken") or "",
                rewards=reward_text,
            )
        )

    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_index(runs: list[dict[str, Any]], out_dir: Path) -> None:
    index_rows = []
    for run in runs:
        stats = run["summary_stats"]
        index_rows.append(
            {
                "id": run["id"],
                "player": run["player"],
                "date": run.get("date"),
                "url": run["url"],
                "duration": stats.get("Duration", run["discovered"].get("duration")),
                "deck_size": stats.get("Deck Size", run["discovered"].get("listed_deck_size")),
                "final_hp": stats.get("Final HP", ""),
                "relic_count": run["derived"]["relic_count"],
                "bosses": run["derived"]["bosses"],
            }
        )
    (out_dir / "index.json").write_text(json.dumps(index_rows, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lines = [
        "# Successful Ironclad A10 Runs",
        "",
        "Data scraped from sts2.fun static HTML. The site exposes selected floor outcomes/rewards, final deck, relics, and summary stats; it does not expose full turn-by-turn combat play logs in these pages.",
        "",
        "| Date | Player | Deck | Final HP | Duration | Run |",
        "|---|---|---:|---|---:|---|",
    ]
    for row in index_rows:
        lines.append(
            f"| {row['date'] or ''} | {row['player']} | {row['deck_size']} | {row['final_hp']} | {row['duration']} | [{row['id'][:8]}](data/{row['id']}.json) |"
        )
    (out_dir / "_index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="runs", help="Output directory")
    parser.add_argument("--max-players", type=int, default=80)
    parser.add_argument("--max-runs", type=int, default=40)
    parser.add_argument("--delay", type=float, default=0.05)
    parser.add_argument("--seed-player", action="append", default=["timeless-outrider"])
    parser.add_argument("--save-html", action="store_true", help="Save raw run HTML under raw_html/")
    args = parser.parse_args()

    out_dir = Path(args.out)
    data_dir = out_dir / "data"
    md_dir = out_dir / "markdown"
    raw_dir = out_dir / "raw_html"
    data_dir.mkdir(parents=True, exist_ok=True)
    md_dir.mkdir(parents=True, exist_ok=True)
    if args.save_html:
        raw_dir.mkdir(parents=True, exist_ok=True)

    session = requests.Session()
    home_html = fetch(session, BASE_URL + "/", args.delay)

    candidates_by_url: OrderedDict[str, dict[str, Any]] = OrderedDict()
    for run in direct_homepage_runs(home_html):
        if is_target_run(run):
            candidates_by_url[run["url"]] = run

    players = discover_players(home_html, args.seed_player)[: args.max_players]
    for index, player in enumerate(players, start=1):
        if len(candidates_by_url) >= args.max_runs:
            break
        try:
            html = fetch(session, f"{BASE_URL}/player/{player}", args.delay)
        except requests.RequestException as exc:
            print(f"warning: failed player {player}: {exc}")
            continue
        for run in parse_run_history(player, html):
            if is_target_run(run):
                candidates_by_url.setdefault(run["url"], run)
                if len(candidates_by_url) >= args.max_runs:
                    break
        print(f"scanned player {index}/{len(players)}: {player}; candidates={len(candidates_by_url)}")

    parsed_runs: list[dict[str, Any]] = []
    for idx, discovered in enumerate(candidates_by_url.values(), start=1):
        if idx > args.max_runs:
            break
        run_id = run_id_from_url(discovered["url"])
        try:
            html = fetch(session, discovered["url"], args.delay)
        except requests.RequestException as exc:
            print(f"warning: failed run {run_id}: {exc}")
            continue
        run = parse_run_page(html, discovered)
        parsed_runs.append(run)
        (data_dir / f"{run_id}.json").write_text(json.dumps(run, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        write_markdown(run, md_dir / f"{run_id}.md")
        if args.save_html:
            (raw_dir / f"{run_id}.html").write_text(html, encoding="utf-8")
        print(f"saved run {idx}/{min(len(candidates_by_url), args.max_runs)}: {run_id}")

    write_index(parsed_runs, out_dir)
    print(f"wrote {len(parsed_runs)} runs to {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
