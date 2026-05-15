#!/usr/bin/env python3
"""
Build a compact STS2 knowledge base for agent play.

This script intentionally writes to kb_new/ by default. It uses the existing
wiki parser helpers from build_kb_wiki.py, but changes the output contract:

- one concise page per card
- no dialogue, update history, or generic obtaining sections
- no generated play/draft policy
- coverage reports that compare against the current kb/

The current implementation focuses on Ironclad cards first, because those are
the highest-impact gap for Ironclad agent play.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import build_kb_wiki as wiki  # noqa: E402

DEFAULT_OUTPUT = REPO_ROOT / "kb_new"
OLD_KB = REPO_ROOT / "kb"
SPIRE_CODEX_API = "https://spire-codex.com/api/cards"


def search_titles(query: str, namespace: int = wiki.NS_STS2, limit: int = 10) -> list[str]:
    """Use MediaWiki search instead of broad categorymembers, which wiki.gg may challenge."""
    titles: list[str] = []
    seen: set[str] = set()
    cont: dict[str, str] = {}

    while True:
        params: dict[str, object] = {
            "action": "query",
            "list": "search",
            "srsearch": query,
            "srnamespace": namespace,
            "srlimit": limit,
        }
        params.update(cont)
        data = wiki.api_get(params)
        for item in data.get("query", {}).get("search", []):
            title = item.get("title", "")
            if title and title not in seen:
                seen.add(title)
                titles.append(title)
        if "continue" not in data:
            break
        cont = data["continue"]
        time.sleep(0.1)

    return titles


def yaml_list(items: list[str]) -> str:
    if not items:
        return "[]"
    return "[" + ", ".join(str(x).replace("]", "\\]") for x in items) + "]"


def agent_frontmatter(**fields: object) -> str:
    lines = ["---"]
    for key, value in fields.items():
        if isinstance(value, list):
            lines.append(f"{key}: {yaml_list([str(v) for v in value])}")
        elif isinstance(value, bool):
            lines.append(f"{key}: {'true' if value else 'false'}")
        else:
            lines.append(f"{key}: {value}")
    lines.append("---")
    return "\n".join(lines)


def compact_text(text: str) -> str:
    text = text or ""
    text = re.sub(r"\[(?:gold|red|green|blue|purple|gray)\](.*?)\[/[a-z]+\]", r"\1", text)
    text = re.sub(r"\[energy:(\d+)\]", r"\1 Energy", text)
    text = re.sub(r"\[block_icon\]", "Block", text)
    text = re.sub(r"\s+", " ", text).strip()
    text = text.replace(" .", ".").replace(" ,", ",")
    return text


def card_slug_from_name(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_")


def fetch_spire_codex_ironclad_cards() -> list[dict[str, Any]]:
    response = wiki.SESSION.get(
        SPIRE_CODEX_API,
        params={"color": "ironclad"},
        timeout=30,
    )
    response.raise_for_status()
    cards = response.json()
    if not isinstance(cards, list):
        raise RuntimeError("Unexpected Spire Codex cards API response")
    return cards


def codex_cost(card: dict[str, Any]) -> str:
    if card.get("is_x_cost"):
        return "X"
    if card.get("is_x_star_cost"):
        return "X*"
    cost = card.get("cost")
    star = card.get("star_cost")
    if star is not None:
        return f"{cost} + {star}*"
    return str(cost if cost is not None else "?")


def codex_keywords(card: dict[str, Any]) -> list[str]:
    raw = card.get("keywords_key") or card.get("keywords")
    if not raw:
        return []
    if isinstance(raw, list):
        return [str(x) for x in raw]
    return [x.strip() for x in re.split(r"[,;/]", str(raw)) if x.strip()]


def codex_list(value: object) -> list[str]:
    if not value:
        return []
    if isinstance(value, list):
        return [str(x) for x in value]
    return [x.strip() for x in re.split(r"[,;/]", str(value)) if x.strip()]


def source_value(value: object) -> str:
    if value is None:
        return "—"
    if isinstance(value, (dict, list)):
        return f"`{json.dumps(value, sort_keys=True)}`"
    text = compact_text(str(value))
    return text if text else "—"


def wiki_title_candidates(name: str) -> list[str]:
    candidates = [f"Slay the Spire 2:{name}"]
    if name == "Strike":
        candidates.insert(0, "Slay the Spire 2:Strike (Ironclad)")
    if name == "Defend":
        candidates.insert(0, "Slay the Spire 2:Defend (Ironclad)")
    return candidates


def get_wiki_card_context(name: str) -> tuple[str | None, dict[str, str], str, bool]:
    for title in wiki_title_candidates(name):
        try:
            wt = wiki.get_wikitext(title)
        except Exception:
            return None, {}, "", False
        if not wt:
            continue
        if wiki.extract_card_color(wt) != "Ironclad":
            continue
        try:
            cats = wiki.page_categories(title)
        except Exception:
            cats = []
        return title, wiki.extract_sections(wt), wt, wiki.is_stub(wt, cats)
    return None, {}, "", False


def existing_kb_facts(name: str, max_items: int = 10) -> list[str]:
    path = OLD_KB / "cards" / "ironclad" / f"{card_slug_from_name(name)}.md"
    if name == "Strike":
        path = OLD_KB / "cards" / "ironclad" / "strike_ironclad.md"
    elif name == "Defend":
        path = OLD_KB / "cards" / "ironclad" / "defend_ironclad.md"
    if not path.exists():
        return []
    text = path.read_text()
    match = re.search(r"## Notes\n\n(.*?)(?:\n## Update History|\n---\n<!-- META)", text, re.DOTALL)
    if not match:
        return []
    facts: list[str] = []
    for raw_line in match.group(1).splitlines():
        line = raw_line.strip()
        line = re.sub(r"^\*+\s*", "", line)
        line = re.sub(r"^-+\s*", "", line)
        if not line or line.startswith("###") or line.startswith("====") or line == "_None._":
            continue
        if line.startswith(("Obtaining ", "Can be bought", "Can be obtained")):
            continue
        line = re.sub(r"^\*\*(.+?)\*\*$", r"\1", line)
        if len(line) > 220:
            line = line[:217].rstrip() + "..."
        if line not in facts:
            facts.append(line)
        if len(facts) >= max_items:
            break
    return facts


def upgrade_delta_text(upgrade: object) -> str:
    if not isinstance(upgrade, dict):
        return str(upgrade)
    if not upgrade:
        return ""
    return "; ".join(f"{key}: {value}" for key, value in upgrade.items())


USEFUL_SECTION_NAMES = {
    "Notes",
    "Interactions",
    "Synergies",
    "Anti-Synergies",
}


def useful_wiki_facts(sections: dict[str, str], max_items: int = 10) -> list[str]:
    facts: list[str] = []
    useful_verbs = re.compile(
        r"\b(trigger|triggers|derive|derives|increase|increases|reduce|reduces|"
        r"count|counts|cause|causes|allow|allows|activate|activates|double|"
        r"doubles|exhaust|vulnerable|replay|damage|block|strength|energy|"
        r"draw|discard|retain|fatal|play|played)\b",
        re.I,
    )
    for heading, body in sections.items():
        if heading not in USEFUL_SECTION_NAMES:
            continue
        cleaned = wiki.clean_wikitext(body)
        cleaned = re.sub(r"^=+\s*(.+?)\s*=+\s*$", r"\1:", cleaned, flags=re.MULTILINE)
        for raw_line in cleaned.splitlines():
            line = raw_line.strip()
            if not line:
                continue
            line = re.sub(r"^-+\s*", "", line)
            if not line or line.endswith(":"):
                continue
            if line.startswith(("###", "####", "====")):
                continue
            if line.startswith(("Obtaining ", "Can be bought", "Can be obtained")):
                continue
            if "Early Access" in line or "Added " in line:
                continue
            if not useful_verbs.search(line):
                continue
            if len(line) > 220:
                line = line[:217].rstrip() + "..."
            if line not in facts:
                facts.append(line)
            if len(facts) >= max_items:
                return facts
    return facts


def is_card_page(title: str, wt: str, expected_color: str) -> bool:
    if not title.startswith("Slay the Spire 2:"):
        return False
    color = wiki.extract_card_color(wt)
    ctype = wiki.extract_card_type(wt)
    if color != expected_color:
        return False
    return ctype in {"Attack", "Skill", "Power", "Curse", "Status"}


def write_codex_card(card: dict[str, Any], output_dir: Path, dry_run: bool) -> dict[str, object]:
    display = str(card["name"])
    ctype = str(card.get("type") or card.get("type_key") or "Unknown")
    rarity = str(card.get("rarity") or card.get("rarity_key") or "Unknown")
    cost = codex_cost(card)
    base = compact_text(str(card.get("description") or card.get("description_raw") or ""))
    upgraded = compact_text(str(card.get("upgrade_description") or ""))
    keywords = codex_keywords(card)
    api_tags = codex_list(card.get("tags"))

    wiki_title, sections, _wt, wiki_stub = get_wiki_card_context(display)
    source_urls = [f"{SPIRE_CODEX_API}/{card['id']}"]
    if wiki_title:
        source_urls.append(wiki.wiki_url(wiki_title))

    numeric_rows = [
        ("Damage", "damage"),
        ("Block", "block"),
        ("Hit count", "hit_count"),
        ("Cards drawn", "cards_draw"),
        ("Energy gain", "energy_gain"),
        ("HP loss", "hp_loss"),
        ("Powers applied", "powers_applied"),
    ]
    numeric_table = "\n".join(
        f"| {label} | {source_value(card.get(key))} |"
        for label, key in numeric_rows
    )

    extra_rows = [
        ("Spawns cards", "spawns_cards"),
        ("Vars", "vars"),
        ("Upgrade", "upgrade"),
        ("Can be generated in combat", "can_be_generated_in_combat"),
        ("Compendium order", "compendium_order"),
    ]
    extra_table = "\n".join(
        f"| {label} | {source_value(card.get(key))} |"
        for label, key in extra_rows
    )

    fm = agent_frontmatter(
        title=display,
        sources=source_urls,
        character="Ironclad",
        type=ctype,
        rarity=rarity,
        cost=cost,
        target=card.get("target") or "Unknown",
        keywords=keywords,
        api_tags=api_tags,
        wiki_stub=wiki_stub,
    )

    upgraded_line = f"\n- Upgraded: {upgraded}" if upgraded else ""
    sources_block = "\n".join(f"- {url}" for url in source_urls)

    content = f"""{fm}

# {display}

## Sources

{sources_block}

## Card Text

- Cost: {cost}
- Type/Rarity: {ctype} / {rarity}
- Target: {card.get("target") or "Unknown"}
- Base: {base or '_Card text not scraped; see source._'}{upgraded_line}

## Structured Fields

| Field | Value |
|---|---|
| ID | {source_value(card.get("id"))} |
| Color | {source_value(card.get("color"))} |
| Type key | {source_value(card.get("type_key"))} |
| Rarity key | {source_value(card.get("rarity_key"))} |
| Target | {source_value(card.get("target"))} |
| Keywords | {source_value(keywords)} |
| API tags | {source_value(api_tags)} |

## Numeric Fields

| Field | Value |
|---|---|
{numeric_table}

## Upgrade And Generation Data

| Field | Value |
|---|---|
{extra_table}
"""

    slug = card_slug_from_name(display)
    path = output_dir / "cards" / "ironclad" / f"{slug}.md"
    wiki.safe_write(path, content, dry_run)
    return {
        "title": display,
        "slug": slug,
        "type": ctype,
        "rarity": rarity,
        "cost": cost,
        "keywords": keywords,
        "api_tags": api_tags,
        "source": source_urls[0],
    }


def write_index(cards: list[dict[str, object]], output_dir: Path, dry_run: bool) -> None:
    cards = sorted(cards, key=lambda c: str(c["title"]).lower())
    rows = [
        "| Card | Cost | Type | Rarity | Keywords | API tags |",
        "|---|---:|---|---|---|---|",
    ]
    for card in cards:
        title = str(card["title"])
        slug = str(card["slug"])
        keywords = ", ".join(card["keywords"]) if isinstance(card.get("keywords"), list) else ""
        api_tags = ", ".join(card["api_tags"]) if isinstance(card.get("api_tags"), list) else ""
        rows.append(
            f"| [{title}](./{slug}.md) | {card['cost']} | {card['type']} | "
            f"{card['rarity']} | {keywords or '—'} | {api_tags or '—'} |"
        )

    content = f"""# Ironclad Cards

Compact Ironclad card data generated from Spire Codex API records, with
wiki.gg source links attached when available. Kept separate from `kb/`.

Total Ironclad cards: {len(cards)}

{chr(10).join(rows)}
"""
    wiki.safe_write(output_dir / "cards" / "ironclad" / "_index.md", content, dry_run)


def write_schema(cards: list[dict[str, object]], output_dir: Path, dry_run: bool) -> None:
    lines = [
        "# kb_new Schema",
        "",
        "This folder is a structured data layer, not a strategy or policy layer.",
        "",
        "## Sources",
        "",
        "- Primary card records come from `https://spire-codex.com/api/cards?color=ironclad`.",
        "- Matching wiki.gg pages are linked when they can be fetched, but generated card pages do not quote wiki strategy prose.",
        "- Existing `kb/` is not modified.",
        "",
        "## Card Page Sections",
        "",
        "- `Sources`: URLs used for the record.",
        "- `Card Text`: normalized base and upgraded text.",
        "- `Structured Fields`: source IDs, type, rarity, target, keywords, and API-provided tags.",
        "- `Numeric Fields`: parsed source numeric fields such as damage, block, draw, energy, and HP loss.",
        "- `Upgrade And Generation Data`: source `vars`, `upgrade`, generated-card, and compendium fields.",
        "",
        f"Total Ironclad card records: {len(cards)}",
        "",
    ]
    content = "\n".join(lines) + "\n"
    wiki.safe_write(output_dir / "cards" / "ironclad" / "_schema.md", content, dry_run)


def write_coverage(cards: list[dict[str, object]], output_dir: Path, dry_run: bool) -> None:
    new_slugs = {str(c["slug"]) for c in cards}
    old_dir = OLD_KB / "cards" / "ironclad"
    old_slugs = {p.stem for p in old_dir.glob("*.md")} if old_dir.exists() else set()
    missing_old = sorted(new_slugs - old_slugs)
    stale_old = sorted(old_slugs - new_slugs)

    lines = [
        "# Ironclad Card Coverage",
        "",
        f"- Existing kb/cards/ironclad files: {len(old_slugs)}",
        f"- kb_new/cards/ironclad files: {len(new_slugs)}",
        "",
        "## Present in kb_new but missing in old kb",
        "",
    ]
    lines.extend(f"- {slug}" for slug in missing_old)
    if not missing_old:
        lines.append("- None")
    lines.extend(["", "## Present in old kb but not generated as Ironclad cards", ""])
    lines.extend(f"- {slug}" for slug in stale_old)
    if not stale_old:
        lines.append("- None")
    lines.append("")

    wiki.safe_write(output_dir / "reports" / "ironclad_card_coverage.md", "\n".join(lines), dry_run)


def build_ironclad_cards(output_dir: Path, dry_run: bool) -> None:
    codex_cards = fetch_spire_codex_ironclad_cards()
    cards: list[dict[str, object]] = []
    for raw_card in codex_cards:
        cards.append(write_codex_card(raw_card, output_dir, dry_run))

    write_index(cards, output_dir, dry_run)
    write_schema(cards, output_dir, dry_run)
    write_coverage(cards, output_dir, dry_run)
    print(f"Wrote {len(cards)} Ironclad card pages to {output_dir / 'cards' / 'ironclad'}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    build_ironclad_cards(args.output_dir, args.dry_run)


if __name__ == "__main__":
    main()
