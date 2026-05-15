#!/usr/bin/env python3
"""
build_kb_wiki.py — STS2 wiki scraper for the Ironclad-only playing agent.

Builds kb/ with one Markdown file per entity.  Re-runs are safe (idempotent):
files are only written when content changes, so partial-failure reruns skip
already-complete pages.

Scope
-----
- Cards:   Ironclad + Colorless only (plus universal Status/Curse)
- Relics:  all except those with a non-Ironclad class restriction
- Potions: universal + Ironclad-specific
- Enemies: all (monsters, elites, bosses, ancients)
- Events:  all
- Mechanics: keywords, buffs, debuffs, acts (one file each)

Source: slaythespire.wiki.gg, STS2 namespace (ns=3000) ONLY.
        Every page is verified to start with "Slay the Spire 2:" before writing.

Usage
-----
    python3 scripts/build_kb_wiki.py [--dry-run] [--limit N] [--only CATEGORY]

Requirements: beautifulsoup4, requests
"""

import argparse
import json
import logging
import re
import sys
import time
from pathlib import Path
from typing import Optional

try:
    import requests
    from bs4 import BeautifulSoup, NavigableString, Tag
except ImportError:
    print("Missing deps.  Run:  pip install beautifulsoup4 requests", file=sys.stderr)
    sys.exit(1)

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

BASE_URL  = "https://slaythespire.wiki.gg"
API_URL   = f"{BASE_URL}/api.php"
UA        = "STS2-KB-Builder/1.0 (Ironclad agent research; STS2MCP repo)"
THROTTLE  = 0.5       # seconds between API calls
NS_STS2   = 3000      # MediaWiki namespace id for "Slay the Spire 2"

REPO_ROOT = Path(__file__).parent.parent
KB_DIR    = REPO_ROOT / "kb"

OTHER_CLASSES = {"Silent", "Regent", "Necrobinder", "Defect"}
OUR_CLASSES   = {"Ironclad", "Colorless"}

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s  %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("kb")

# ---------------------------------------------------------------------------
# HTTP helpers
# ---------------------------------------------------------------------------

SESSION = requests.Session()
SESSION.headers["User-Agent"] = UA
_last_request = 0.0


def api_get(params: dict) -> dict:
    global _last_request
    elapsed = time.time() - _last_request
    if elapsed < THROTTLE:
        time.sleep(THROTTLE - elapsed)
    params["format"] = "json"
    resp = SESSION.get(API_URL, params=params, timeout=30)
    resp.raise_for_status()
    _last_request = time.time()
    return resp.json()


def wiki_url(title: str) -> str:
    return f"{BASE_URL}/wiki/{title.replace(' ', '_')}"


def is_sts2_page(title: str) -> bool:
    return title.startswith("Slay the Spire 2:")


def page_slug(title: str) -> str:
    """'Slay the Spire 2:Foo Bar' → 'foo_bar'"""
    name = title.removeprefix("Slay the Spire 2:")
    return re.sub(r'[^a-z0-9]+', '_', name.lower()).strip('_')


# ---------------------------------------------------------------------------
# MediaWiki API queries
# ---------------------------------------------------------------------------

def list_category(category: str, namespace: Optional[int] = None) -> list[str]:
    members, cont = [], {}
    while True:
        params: dict = {
            "action": "query",
            "list": "categorymembers",
            "cmtitle": f"Category:{category}",
            "cmlimit": 500,
        }
        if namespace is not None:
            params["cmnamespace"] = namespace
        params.update(cont)
        d = api_get(params)
        members.extend(m["title"] for m in d["query"]["categorymembers"])
        if "continue" in d:
            cont = d["continue"]
        else:
            break
    return [t for t in members if is_sts2_page(t)]


def get_wikitext(title: str) -> str:
    d = api_get({
        "action": "query", "prop": "revisions",
        "rvprop": "content", "rvslots": "main", "titles": title,
    })
    for pid, pdata in d["query"]["pages"].items():
        if pid == "-1":
            return ""
        revs = pdata.get("revisions", [])
        if revs:
            return revs[0].get("slots", {}).get("main", {}).get("*", "")
    return ""


def get_rendered_html(title: str) -> str:
    d = api_get({"action": "parse", "page": title, "prop": "text"})
    if "parse" not in d:
        return ""
    return d["parse"]["text"]["*"]


def page_categories(title: str) -> list[str]:
    d = api_get({"action": "query", "prop": "categories", "cllimit": 50, "titles": title})
    for _pid, pdata in d["query"]["pages"].items():
        return [c["title"].removeprefix("Category:") for c in pdata.get("categories", [])]
    return []


# ---------------------------------------------------------------------------
# Wikitext parsers
# ---------------------------------------------------------------------------

_COLOR_RE   = re.compile(r'color:(Ironclad|Colorless|Silent|Regent|Necrobinder|Defect)')
_RARITY_RE  = re.compile(r'rarity:(\w+(?:\s\w+)?)')
_TYPE_RE    = re.compile(r'type:(Attack|Skill|Power|Curse|Status)')


def extract_card_color(wt: str) -> Optional[str]:
    m = _COLOR_RE.search(wt)
    return m.group(1) if m else None


def extract_card_rarity(wt: str) -> str:
    m = _RARITY_RE.search(wt)
    return m.group(1) if m else "Unknown"


def extract_card_type(wt: str) -> str:
    m = _TYPE_RE.search(wt)
    return m.group(1) if m else "Unknown"


_KW_PATTERNS = [
    ("Innate",    re.compile(r'\{\{KW\|Innate',    re.I)),
    ("Retain",    re.compile(r'\{\{KW\|Retain',    re.I)),
    ("Exhaust",   re.compile(r'\{\{KW\|Exhaust',   re.I)),
    ("Ethereal",  re.compile(r'\{\{KW\|Ethereal',  re.I)),
    ("Unplayable",re.compile(r'\{\{KW\|Unplayable',re.I)),
    ("Fatal",     re.compile(r'\{\{KW\|Fatal',     re.I)),
    ("Replay",    re.compile(r'\{\{KW\|Replay',    re.I)),
    ("Sly",       re.compile(r'\{\{KW\|Sly',       re.I)),
]

def extract_card_keywords(wt: str) -> list[str]:
    return [name for name, pat in _KW_PATTERNS if pat.search(wt)]


def is_stub(wt: str, cats: list[str]) -> bool:
    return "Stubs" in cats or "ToUpdate" in cats


def _template_display(m: re.Match) -> str:
    """
    Extract display text from a STS2 wiki template match.
    Handles: {{R|Name||2}}, {{C|Name||2}}, {{P|Name||2}},
             {{KW|Keyword|Display|2}}, {{QueryLink|...|Display|2}},
             {{2|Page|Display|2}}, {{Icon|...|2}} → '', etc.
    Strategy: take the last non-empty, non-numeric pipe segment.
    """
    content = m.group(1)  # everything inside {{ }}
    parts = [p.strip() for p in content.split('|')]
    if not parts:
        return ''
    name = parts[0].lower()
    # Templates that produce no meaningful text output
    _NO_TEXT = {
        'icon', 'clear', 'asc',
        'relic infobox', 'card infobox', 'enemy infobox', 'power infobox',
        'event header', 'keyword infobox', 'intents',
        'sequel disambiguation', 'navbox', 'hatnote', 'stub',
        'toinfobox', 'toupdate', 'see also',
        'toc_limit', 'toc limit', 'toc', '__toc__', '__notoc__',
    }
    if name in _NO_TEXT or name.endswith(' infobox'):
        return ''
    # Frame = option/button label: {{Frame|Immerse}} → [Immerse]
    if name == 'frame' and len(parts) > 1:
        return f'[{parts[1]}]'
    # TS = typed value: {{TS|positive||2}} → '2', {{TS|negative|3=increasing}} → 'increasing'
    if name == 'ts':
        for part in parts[2:]:
            if part.startswith('3='):
                return part[2:]
        return parts[3] if len(parts) > 3 else ''
    # Int = attack intent: {{Int|EnemyName|AttackName||2}} → AttackName
    if name == 'int' and len(parts) >= 3:
        return parts[2] or parts[1]
    # Find last meaningful part (non-empty, not just digits)
    candidate = None
    for part in reversed(parts):
        if part and not re.fullmatch(r'\d+', part):
            candidate = part
            break
    if candidate is not None and candidate != parts[0]:
        # Non-name display text found (e.g. "Burning Blood" in {{R|Burning Blood||2}})
        return candidate
    if candidate is None:
        # All parts are digits/empty — return first non-empty arg after name
        return next((p for p in parts[1:] if p), '')
    # candidate == parts[0]: template name is the only non-digit token.
    # If there's a numeric value arg, it's likely a quantity template like {{HP|12||2}}
    for part in parts[1:]:
        if part and re.fullmatch(r'\d+', part):
            return part
    # No numeric arg either — fall to exclusion set check
    return parts[0] if parts[0] not in ('R', 'C', 'P', 'KW', '2', 'E', 'BD') else (parts[1] if len(parts) > 1 else '')


def clean_wikitext(text: str) -> str:
    """
    Strip MediaWiki markup and return readable plain text (with Markdown lists/bold).
    Preserves display names from STS2 wiki templates like {{R|Name||2}}.
    """
    if not text:
        return ""
    # Remove HTML comments
    text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)
    # Remove nowiki
    text = re.sub(r'<nowiki>.*?</nowiki>', '', text, flags=re.DOTALL)
    # Remove <ref>
    text = re.sub(r'<ref[^>]*>.*?</ref>', '', text, flags=re.DOTALL)
    text = re.sub(r'<ref[^>]*/>', '', text)
    # Remove category links
    text = re.sub(r'\[\[Category:[^\]]*\]\]', '', text)
    # Remove file/image links
    text = re.sub(r'\[\[(?:File|Image):[^\]]*\]\]', '', text, flags=re.I)
    # Resolve STS2 templates iteratively — extract display text before stripping
    for _ in range(6):
        prev = text
        text = re.sub(r'\{\{([^{}]+?)\}\}', _template_display, text, flags=re.DOTALL)
        if text == prev:
            break
    # Wikilinks [[target|display]] → display
    text = re.sub(r'\[\[(?:[^\]|]*\|)?([^\]]*)\]\]', r'\1', text)
    # External links [url label] → label
    text = re.sub(r'\[https?://\S+ ([^\]]+)\]', r'\1', text)
    text = re.sub(r'\[https?://\S+\]', '', text)
    # Bullets/numbered-lists BEFORE bold (so '''text''' at start of line
    # doesn't get converted to **text** and then confused for a bullet)
    text = re.sub(r'^\*{3}[ \t]*', '      - ', text, flags=re.MULTILINE)
    text = re.sub(r'^\*{2}[ \t]*', '    - ', text, flags=re.MULTILINE)
    text = re.sub(r'^\*[ \t]*', '- ', text, flags=re.MULTILINE)
    # Numbered list (# → 1.)
    text = re.sub(r'^#+\s+', '1. ', text, flags=re.MULTILINE)
    # Bold/italic wiki markup → Markdown
    text = re.sub(r"'''(.+?)'''", r'**\1**', text)
    text = re.sub(r"''(.+?)''", r'_\1_', text)
    # Horizontal rules
    text = re.sub(r'^----+$', '---', text, flags=re.MULTILINE)
    # Level-3/4 wikitext headings that survived section splitting → Markdown headings
    text = re.sub(r'^={4,}\s*(.+?)\s*={4,}\s*$', r'#### \1', text, flags=re.MULTILINE)
    text = re.sub(r'^===\s*(.+?)\s*===\s*$', r'### \1', text, flags=re.MULTILINE)
    # HTML tags
    text = re.sub(r'<br\s*/?>', '\n', text, flags=re.I)
    text = re.sub(r'<[^>]+>', '', text)
    # Trim trailing whitespace per line; collapse excessive blank lines
    lines = [l.rstrip() for l in text.splitlines()]
    text = '\n'.join(lines)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


def extract_sections(wt: str) -> dict[str, str]:
    """
    Parse wikitext into {heading: body} for top-level (==) sections.
    Strips category/file links before returning body text.
    """
    # Strip HTML comments before splitting so cross-section comments don't leak
    wt = re.sub(r'<!--.*?-->', '', wt, flags=re.DOTALL)
    sections: dict[str, str] = {}
    current = "_intro"
    body_lines: list[str] = []

    def flush():
        raw = '\n'.join(body_lines).strip()
        # Strip categories/file links
        raw = re.sub(r'\[\[(?:Category|File|Image):[^\]]*\]\]', '', raw, flags=re.I)
        sections[current] = raw.strip()

    for line in wt.splitlines():
        # Match exactly level-2 headings (== not ===)
        heading = re.match(r'^==(?!=)\s*(.+?)\s*==(?!=)\s*$', line)
        if heading:
            flush()
            current = heading.group(1)
            body_lines = []
        else:
            body_lines.append(line)
    flush()
    return sections


# ---------------------------------------------------------------------------
# HTML parsers (rendered DRUID infobox)
# ---------------------------------------------------------------------------

def _tab_texts(row_div) -> tuple[str, str]:
    """
    Return (base_text, upgraded_text) from a druid-row div that contains
    druid-toggleable-data children.
    """
    tabs = row_div.find_all("div", class_="druid-toggleable-data") if row_div else []
    # 'focused' marks the base tab (left/default)
    base, upgraded = "", ""
    for tab in tabs:
        classes = tab.get("class", [])
        txt = tab.get_text(separator=" ", strip=True)
        if "focused" in classes:
            base = txt
        else:
            upgraded = txt
    if not base and tabs:
        base = tabs[0].get_text(separator=" ", strip=True)
    return base, upgraded


def parse_card_infobox_html(html: str) -> dict:
    """
    Extract card fields from the rendered DRUID infobox HTML.
    Returns dict with: base, upgraded, cost, card_type, rarity, character.
    """
    soup  = BeautifulSoup(html, "html.parser")
    out   = {"base": "", "upgraded": "", "cost": "", "card_type": "",
             "rarity": "", "character": ""}

    # Description
    desc_row = soup.find("div", class_="druid-row-Description")
    if desc_row:
        out["base"], out["upgraded"] = _tab_texts(desc_row)
        if out["upgraded"] == out["base"]:
            out["upgraded"] = ""   # no change on upgrade

    # Cost — card-infobox-cost / druid-row-EnergyCost; read only the Base (focused) tab
    cost_div = soup.find("div", class_="card-infobox-cost")
    if cost_div:
        focused = cost_div.find("div", class_="focused")
        if focused:
            out["cost"] = focused.get_text(strip=True)
        else:
            # Fall back: first druid-toggleable-data child
            first = cost_div.find("div", class_="druid-toggleable-data")
            out["cost"] = first.get_text(strip=True) if first else cost_div.get_text(strip=True)
        if not out["cost"]:
            out["cost"] = "X"

    # Rarity / class row
    rarity_div = soup.find("div", class_="druid-data-RarityClass")
    if rarity_div:
        parts = [s.strip() for s in rarity_div.get_text(separator="|", strip=True).split("|") if s.strip()]
        # Typically ["Common", "Ironclad", "Card"] or ["Ancient", "Colorless", "Card"]
        for p in parts:
            if p in ("Common", "Uncommon", "Rare", "Ancient", "Basic", "Special", "Curse", "Status"):
                out["rarity"] = p
            elif p in ("Ironclad", "Silent", "Regent", "Necrobinder", "Defect", "Colorless"):
                out["character"] = p

    # Type row
    type_div = soup.find("div", class_="druid-data-Type")
    if type_div:
        out["card_type"] = type_div.get_text(strip=True)

    return out


def _render_cell(td) -> str:
    """
    Render a table cell, converting ascension-trigger spans to
    'VALUE (AscN+)' notation instead of concatenating raw text.
    """
    out = []
    for child in td.children:
        if isinstance(child, NavigableString):
            out.append(str(child))
        elif isinstance(child, Tag) and 'ascension-trigger' in (child.get('class') or []):
            label = child.find(class_='ascension-label')
            lvl   = child.find(class_='ascension-superscript')
            if label and lvl:
                out.append(f"{label.get_text(strip=True)} (Asc{lvl.get_text(strip=True)}+)")
            else:
                out.append(child.get_text(separator=" ", strip=True))
        else:
            out.append(child.get_text(separator=" ", strip=True))
    return re.sub(r'\s+', ' ', ''.join(out)).strip()


def _get_data_text(row_div) -> str:
    """Get the text from the druid-data-* child, excluding labels."""
    data = row_div.find("div", class_=lambda x: x and any("druid-data" in c for c in x) if x else False)
    if not data:
        return row_div.get_text(separator=" ", strip=True)
    return data.get_text(separator=" ", strip=True)


def _get_hp_text(row_div) -> str:
    """
    Get HP and ascension HP from druid-row-HP.
    The data div contains: base_hp<br/>asc_trigger(asc_hp Asc N)
    """
    data = row_div.find("div", class_=lambda x: x and "druid-data-HP" in (x or []) if x else False)
    if not data:
        return _get_data_text(row_div)

    # Grab the full raw text, then extract numeric ranges and ascension info
    raw = data.get_text(separator="|", strip=True)
    # Remove the label if it leaked in (e.g. "HP|40-44|...")
    raw = re.sub(r'^HP\|?', '', raw)

    # Find ascension label spans
    asc_parts = []
    for asc in data.find_all(class_='ascension-trigger'):
        label = asc.find(class_='ascension-label')
        lvl   = asc.find(class_='ascension-superscript')
        if label and lvl:
            asc_parts.append(f"Asc{lvl.get_text(strip=True)}+: {label.get_text(strip=True)}")

    # Base HP: first token in raw that looks like a number or range
    m = re.search(r'(\d[\d\-]*)', raw)
    base_hp = m.group(1) if m else raw.split("|")[0].strip()

    if asc_parts:
        return f"{base_hp} ({'; '.join(asc_parts)})"
    return base_hp


def parse_enemy_stats_html(html: str) -> str:
    """
    Extract HP, powers, and attack table from rendered enemy HTML.
    Returns a formatted Markdown block, empty string if nothing found.
    """
    soup  = BeautifulSoup(html, "html.parser")
    parts = []

    # There may be multiple enemy infoboxes (e.g. Kaiser Crab has two)
    for cont in soup.find_all("div", class_="druid-container-enemy-infobox"):
        name_div = cont.find("div", class_="druid-title")
        label    = name_div.get_text(strip=True) if name_div else ""

        hp_row  = cont.find("div", class_="druid-row-HP")
        hp_text = _get_hp_text(hp_row) if hp_row else ""

        debut_row  = cont.find("div", class_="druid-row-Debut")
        debut_text = _get_data_text(debut_row) if debut_row else ""

        powers_row = cont.find("div", class_="druid-row-Powers")
        # Powers data contains icon images — get link title text or span text
        powers_text = ""
        if powers_row:
            data_div = powers_row.find("div", class_=lambda x: x and "druid-data" in " ".join(x) if x else False)
            if data_div:
                # Collect text from spans and links, skip pure-image elements
                pwr_parts = []
                for child in data_div.find_all(["a", "span"]):
                    t = child.get_text(strip=True)
                    if t and not re.fullmatch(r'\d+', t):
                        pwr_parts.append(t)
                powers_text = ", ".join(dict.fromkeys(pwr_parts))  # deduplicate

        header = f"### {label}" if label else "### Stats"
        block_lines = [header]
        if hp_text:
            block_lines.append(f"- **HP**: {hp_text}")
        if powers_text:
            block_lines.append(f"- **Powers**: {powers_text}")
        if debut_text:
            block_lines.append(f"- **Appears in**: {debut_text}")
        parts.append("\n".join(block_lines))

    # Parse attack tables (wikitable class)
    for table in soup.find_all("table", class_="wikitable"):
        rows = table.find_all("tr")
        if not rows:
            continue
        headers = [th.get_text(strip=True) for th in rows[0].find_all(["th", "td"])]
        if not any(h.lower() in ("name", "effect", "intent") for h in headers):
            continue

        table_md   = ["| " + " | ".join(headers) + " |",
                      "| " + " | ".join("---" for _ in headers) + " |"]
        seen_names: set[str] = set()
        prev_name  = ""

        for row in rows[1:]:
            tds = row.find_all(["td", "th"])
            if not tds:
                continue
            # Ascension-variant rows have fewer cells than the header (typically 1 cell)
            if len(tds) < len(headers):
                asc_text = " ".join(_render_cell(td) for td in tds).strip()
                if asc_text and prev_name:
                    table_md.append(f"| _(Asc variant)_ | | {asc_text} |")
                continue
            cells = [_render_cell(td) for td in tds]
            name_cell = cells[0].strip()
            if not name_cell or name_cell in seen_names:
                continue
            seen_names.add(name_cell)
            prev_name = name_cell
            while len(cells) < len(headers):
                cells.append("")
            table_md.append("| " + " | ".join(cells[:len(headers)]) + " |")

        parts.append("### Attacks\n\n" + "\n".join(table_md))

    return "\n\n".join(parts)


def parse_relic_infobox_html(html: str) -> dict:
    """Extract relic fields from rendered HTML."""
    soup = BeautifulSoup(html, "html.parser")
    out  = {"effect": "", "rarity": "", "class": "Any"}

    # DRUID infobox for relics
    infobox = soup.find("div", class_="druid-infobox")
    if not infobox:
        return out

    # Effect — first meaningful text block after title
    all_text = infobox.get_text(separator="\n", strip=True)
    lines = [l.strip() for l in all_text.splitlines() if l.strip()]
    # Usually: [Name, rarity, class, effect...]
    if len(lines) > 3:
        out["effect"] = " ".join(lines[3:6])

    # Rarity from druid-data-RarityClass or similar
    rarity_div = soup.find("div", class_=lambda x: x and "RarityClass" in x if x else False)
    if rarity_div:
        parts = [s.strip() for s in rarity_div.get_text(separator="|").split("|") if s.strip()]
        for p in parts:
            if p in ("Starter", "Common", "Uncommon", "Rare", "Ancient", "Boss", "Event", "Shop"):
                out["rarity"] = p

    return out


def parse_enemy_html(html: str) -> dict:
    """Extract HP, moves from Enemy Infobox rendered HTML."""
    soup = BeautifulSoup(html, "html.parser")
    out  = {"hp": "", "asc_hp": ""}

    # Enemy infobox — look for HP values
    for div in soup.find_all("div", class_=lambda x: x and "enemy" in " ".join(x).lower() if x else False):
        txt = div.get_text(separator=" | ", strip=True)
        hp_m = re.search(r'HP[:\s]+(\d+(?:\s*\(\s*\d+\s*\))?)', txt, re.I)
        if hp_m:
            out["hp"] = hp_m.group(1)
            break

    # Also scan page text for HP patterns
    page_text = soup.get_text(separator="\n")
    hp_m = re.search(r'HP[:\s]+(\d+)(?:\s*\((\d+)[^)]*\))?', page_text, re.I)
    if hp_m and not out["hp"]:
        out["hp"] = hp_m.group(1)
        if hp_m.group(2):
            out["asc_hp"] = hp_m.group(2)

    return out


# ---------------------------------------------------------------------------
# File writing
# ---------------------------------------------------------------------------

META_AGENT_DIVIDER = (
    "---\n"
    "<!-- META-AGENT NOTES — do not edit above this line -->\n"
    "## Strategy Notes\n\n"
    "<!-- Reserved for the meta-agent. Append lessons, combos, and heuristics here.\n"
    "     Wiki facts live above the divider. -->"
)


def safe_write(path: Path, content: str, dry_run: bool = False) -> bool:
    """Write only if content changed. Returns True when file was written."""
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.read_text() == content:
        return False
    if dry_run:
        log.info("[DRY-RUN] Would write %s", path)
        return True
    path.write_text(content)
    return True


def frontmatter(**fields) -> str:
    lines = ["---"]
    for k, v in fields.items():
        if isinstance(v, list):
            lines.append(f"{k}: [{', '.join(str(x) for x in v)}]")
        elif isinstance(v, bool):
            lines.append(f"{k}: {'true' if v else 'false'}")
        else:
            lines.append(f"{k}: {v}")
    lines.append("---")
    return '\n'.join(lines)


def stub_banner(stub: bool) -> str:
    if stub:
        return "**[STUB]** Wiki page is marked incomplete — verify numbers at source before relying on them.\n\n"
    return ""


# ---------------------------------------------------------------------------
# Card scraper
# ---------------------------------------------------------------------------

def scrape_card(title: str, dry_run: bool) -> str:
    """Returns 'ironclad', 'colorless', 'status', 'skip', or 'error'."""
    log.info("Card: %s", title)
    wt = get_wikitext(title)
    if not wt:
        log.warning("  Empty wikitext for %s", title)
        return "error"

    color  = extract_card_color(wt)
    ctype  = extract_card_type(wt)
    rarity = extract_card_rarity(wt)

    if color in OTHER_CLASSES:
        return "skip"

    if color is None:
        if ctype in ("Curse", "Status"):
            color = "status"
        elif "color:Colorless" in wt:
            color = "Colorless"
        else:
            log.debug("  No color in %s — skipping", title)
            return "skip"

    cats     = page_categories(title)
    stub     = is_stub(wt, cats)
    keywords = extract_card_keywords(wt)

    # Rendered HTML for infobox fields
    html = get_rendered_html(title)
    box  = parse_card_infobox_html(html)

    # Prefer HTML-parsed values; fall back to wikitext
    cost  = box["cost"] or "?"
    ctype = box["card_type"] or ctype
    rarity = box["rarity"] or rarity
    char_label = box["character"] or (color if color in OUR_CLASSES else "Status/Curse")

    base_text     = box["base"]
    upgraded_text = box["upgraded"]

    # Wikitext sections for notes
    sections = extract_sections(wt)

    notes_md = []
    for h in ("Notes", "Interactions", "Synergies", "Anti-Synergies",
               "Obtaining " + title.removeprefix("Slay the Spire 2:"), "Trivia"):
        body = clean_wikitext(sections.get(h, ""))
        if body:
            notes_md.append(f"### {h}\n\n{body}")

    update_hist = clean_wikitext(sections.get("Update History", ""))

    short = title.removeprefix("Slay the Spire 2:")

    if color == "Ironclad":
        subdir = "ironclad"
    elif color == "Colorless":
        subdir = "colorless"
    else:
        subdir = "status"

    fm = frontmatter(
        title=short,
        source=wiki_url(title),
        character=char_label,
        type=ctype,
        rarity=rarity,
        cost=cost,
        keywords=keywords,
        stub=stub,
    )

    card_text_block = ""
    if base_text:
        card_text_block += f"**Base**: {base_text}\n\n"
    if upgraded_text:
        card_text_block += f"**Upgraded**: {upgraded_text}\n"
    if not card_text_block:
        card_text_block = "_Card text not scraped — see source._"

    notes_block = "\n\n".join(notes_md) if notes_md else "_None._"

    content = f"""{fm}

# {short}

{stub_banner(stub)}| Field | Value |
|-------|-------|
| Type | {ctype} |
| Rarity | {rarity} |
| Cost | {cost} |
| Character | {char_label} |
| Keywords | {', '.join(keywords) if keywords else '—'} |

## Card Text

{card_text_block}

## Notes

{notes_block}

## Update History

{update_hist or '_None._'}

{META_AGENT_DIVIDER}
"""

    slug = page_slug(title)
    path = KB_DIR / "cards" / subdir / f"{slug}.md"
    safe_write(path, content, dry_run)
    return subdir


# ---------------------------------------------------------------------------
# Relic scraper
# ---------------------------------------------------------------------------

def scrape_relic(title: str, dry_run: bool) -> str:
    """Returns 'wrote', 'skip', or 'error'."""
    log.info("Relic: %s", title)
    wt = get_wikitext(title)
    if not wt:
        return "error"

    # Detect class restriction from Spawn Restrictions section
    restriction = None
    sections = extract_sections(wt)
    spawn_text = sections.get("Spawn Restrictions", "") + wt
    m = re.search(r'Can only be obtained by (?:the )?\{\{2\|(\w+)\}\}', spawn_text)
    if not m:
        m = re.search(r'Can only be obtained by (?:the )?([A-Z][a-z]+)\.', spawn_text)
    if m:
        restriction = m.group(1)

    if restriction and restriction in OTHER_CLASSES:
        log.debug("  Skipping %s (restricted to %s)", title, restriction)
        return "skip"

    cats   = page_categories(title)
    stub   = is_stub(wt, cats)
    rarity = extract_card_rarity(wt)   # reuse rarity regex — works for relics too

    html = get_rendered_html(title)
    box  = parse_relic_infobox_html(html)
    rarity = box["rarity"] or rarity

    short = title.removeprefix("Slay the Spire 2:")

    # Collect useful sections
    notes_md = []
    for h in ("Sources", f"Obtaining {short}", "Notes", "Interactions",
               "Synergies", "Anti-Synergies", "Trivia"):
        body = clean_wikitext(sections.get(h, ""))
        if body:
            notes_md.append(f"### {h}\n\n{body}")

    intro       = clean_wikitext(sections.get("_intro", ""))
    update_hist = clean_wikitext(sections.get("Update History", ""))
    class_label = restriction or "Any"

    fm = frontmatter(
        title=short,
        source=wiki_url(title),
        rarity=rarity,
        **{"class": class_label},
        stub=stub,
    )

    content = f"""{fm}

# {short}

{stub_banner(stub)}| Field | Value |
|-------|-------|
| Rarity | {rarity} |
| Class | {class_label} |

## Description

{intro or '_See source._'}

## Notes

{chr(10).join(notes_md) if notes_md else '_None._'}

## Update History

{update_hist or '_None._'}

{META_AGENT_DIVIDER}
"""

    slug = page_slug(title)
    path = KB_DIR / "relics" / f"{slug}.md"
    safe_write(path, content, dry_run)
    return "wrote"


# ---------------------------------------------------------------------------
# Potion scraper — from Potions_List page
# ---------------------------------------------------------------------------

def scrape_potions_list(dry_run: bool) -> int:
    """
    Write one file per potion from the Potions_List page.
    Returns the count of files written.
    """
    title = "Slay the Spire 2:Potions_List"
    log.info("Potions list: %s", title)
    html = get_rendered_html(title)
    if not html:
        log.warning("Could not fetch potions list HTML")
        return 0

    soup = BeautifulSoup(html, "html.parser")
    count, seen = 0, set()

    # Each potion is typically in a table row or definition list
    tables = soup.find_all("table")
    for table in tables:
        rows = table.find_all("tr")
        if not rows:
            continue
        # Header row — determine column indices
        headers = [th.get_text(strip=True).lower()
                   for th in rows[0].find_all(["th", "td"])]

        def col(cells, name):
            try:
                idx = next(i for i, h in enumerate(headers) if name in h)
                return cells[idx].get_text(separator=" ", strip=True) if idx < len(cells) else ""
            except StopIteration:
                return ""

        for row in rows[1:]:
            cells = row.find_all(["td", "th"])
            if not cells:
                continue
            name = col(cells, "name") or col(cells, "potion") or cells[0].get_text(strip=True)
            name = name.strip()
            if not name or name.lower() in ("name", "potion name", ""):
                continue
            if name in seen:
                continue
            seen.add(name)

            effect  = col(cells, "effect") or col(cells, "description") or ""
            char    = col(cells, "character") or "Any"
            rarity  = col(cells, "rarity") or col(cells, "type") or ""

            slug = re.sub(r'[^a-z0-9]+', '_', name.lower()).strip('_')
            path = KB_DIR / "potions" / f"{slug}.md"

            fm = frontmatter(
                title=name,
                source=wiki_url("Slay_the_Spire_2:Potions_List"),
                character=char,
                rarity=rarity,
                stub=False,
            )
            content = f"""{fm}

# {name}

| Field | Value |
|-------|-------|
| Character | {char} |
| Rarity | {rarity} |

## Effect

{effect or '_See source._'}

{META_AGENT_DIVIDER}
"""
            if safe_write(path, content, dry_run):
                count += 1

    # If no tables found, fall back to a placeholder
    if count == 0:
        log.warning("No potion tables found — writing placeholder")
        path = KB_DIR / "potions" / "_index.md"
        content = (f"---\ntitle: Potions Index\n"
                   f"source: {wiki_url('Slay_the_Spire_2:Potions_List')}\n"
                   f"stub: true\n---\n\n"
                   f"# Potions\n\n**[STUB]** Could not parse potion tables — see source.\n\n"
                   f"{META_AGENT_DIVIDER}\n")
        safe_write(path, content, dry_run)
        count = 1

    return count


# ---------------------------------------------------------------------------
# Enemy scraper
# ---------------------------------------------------------------------------

_ACT_RE = re.compile(r'\b(Overgrowth|Underdocks|Hive|Glory)\b', re.IGNORECASE)


def detect_act(wt: str) -> str:
    """Return the first act name found in wikitext, lower-cased, or 'unknown'."""
    m = _ACT_RE.search(wt)
    return m.group(1).lower() if m else "unknown"


def enemy_category(cats: list[str]) -> str:
    if "Ancients" in cats:
        return "ancients"
    if "Bosses" in cats:
        return "bosses"
    if "Elites" in cats:
        return "elites"
    return "regular"


def scrape_enemy(title: str, dry_run: bool) -> str:
    log.info("Enemy: %s", title)
    wt = get_wikitext(title)
    if not wt:
        return "error"

    cats  = page_categories(title)
    stub  = is_stub(wt, cats)
    cat   = enemy_category(cats)
    act   = detect_act(wt)
    short = title.removeprefix("Slay the Spire 2:")

    # Regular enemies go under their act folder; elites/bosses/ancients keep their category.
    subdir = act if cat == "regular" else cat

    sections = extract_sections(wt)
    intro    = clean_wikitext(sections.get("_intro", ""))

    # Rendered HTML for HP and attack tables
    html       = get_rendered_html(title)
    stats_md   = parse_enemy_stats_html(html)

    skip_h = {"Update History", "Version History", "_intro"}
    body_parts = []
    for h, body in sections.items():
        if h in skip_h:
            continue
        cleaned = clean_wikitext(body)
        # Level-3 subsections remain as raw ===text=== in body; promote to ### headings
        cleaned = re.sub(r'^===+\s*(.+?)\s*===+\s*$', r'### \1', cleaned, flags=re.MULTILINE)
        if cleaned:
            body_parts.append(f"## {h}\n\n{cleaned}")

    update_hist = clean_wikitext(
        sections.get("Update History") or sections.get("Version History", "")
    )

    fm = frontmatter(
        title=short,
        source=wiki_url(title),
        category=cat,
        act=act,
        stub=stub,
    )

    stats_section = f"## Stats\n\n{stats_md}" if stats_md else ""

    content = f"""{fm}

# {short}

{stub_banner(stub)}## Overview

{intro or '_No overview — see source._'}

{stats_section}

{chr(10).join(body_parts)}

## Update History

{update_hist or '_None._'}

{META_AGENT_DIVIDER}
"""

    slug = page_slug(title)
    path = KB_DIR / "enemies" / subdir / f"{slug}.md"
    safe_write(path, content, dry_run)
    return "wrote"


# ---------------------------------------------------------------------------
# Event scraper
# ---------------------------------------------------------------------------

def scrape_event(title: str, dry_run: bool) -> str:
    log.info("Event: %s", title)
    wt = get_wikitext(title)
    if not wt:
        return "error"

    cats  = page_categories(title)
    stub  = is_stub(wt, cats)
    short = title.removeprefix("Slay the Spire 2:")

    sections = extract_sections(wt)
    intro    = clean_wikitext(sections.get("_intro", ""))

    # Detect act from intro
    act_m = re.search(
        r'(?:found (?:exclusively )?in (?:the )?)(Overgrowth|Underdocks|Hive|Glory)',
        wt, re.IGNORECASE
    )
    act = act_m.group(1) if act_m else "Unknown"

    options = clean_wikitext(sections.get("Options", ""))

    # Extra sections (Notes, Trivia…)
    skip_h = {"Options", "Dialogue", "Update History", "Version History", "_intro"}
    extras = []
    for h, body in sections.items():
        if h in skip_h:
            continue
        cleaned = clean_wikitext(body)
        if cleaned:
            extras.append(f"## {h}\n\n{cleaned}")

    fm = frontmatter(
        title=short,
        source=wiki_url(title),
        act=act,
        stub=stub,
    )

    content = f"""{fm}

# {short}

{stub_banner(stub)}**Act**: {act}

{intro}

## Options

{options or '_No structured options found in wiki scrape. Prefer scripts/build_kb_events.py for event data._'}

{chr(10).join(extras)}

{META_AGENT_DIVIDER}
"""

    slug = page_slug(title)
    path = KB_DIR / "events" / f"{slug}.md"
    safe_write(path, content, dry_run)
    return "wrote"


# ---------------------------------------------------------------------------
# Mechanics pages
# ---------------------------------------------------------------------------

MECHANICS_PAGES: dict[str, tuple[str, str]] = {
    "Slay the Spire 2:Keywords":      ("keywords",      "mechanics"),
    "Slay the Spire 2:Buffs":         ("buffs",         "mechanics"),
    "Slay the Spire 2:Debuffs":       ("debuffs",       "mechanics"),
    "Slay the Spire 2:Acts":          ("acts",          "mechanics"),
    "Slay the Spire 2:Map_Locations": ("map_locations", "mechanics"),
    "Slay the Spire 2:Mechanics":     ("core_mechanics","mechanics"),
    "Slay the Spire 2:Ascension":     ("ascension",     "mechanics"),
}


def scrape_mechanics_page(title: str, slug: str, subdir: str, dry_run: bool) -> str:
    log.info("Mechanics: %s", title)
    wt = get_wikitext(title)
    if not wt:
        return "error"

    cats  = page_categories(title)
    stub  = is_stub(wt, cats)
    short = title.removeprefix("Slay the Spire 2:").replace("_", " ")

    sections = extract_sections(wt)
    parts    = []
    intro    = clean_wikitext(sections.get("_intro", ""))
    if intro:
        parts.append(intro)
    for h, body in sections.items():
        if h == "_intro":
            continue
        cleaned = clean_wikitext(body)
        if cleaned:
            parts.append(f"## {h}\n\n{cleaned}")

    fm = frontmatter(
        title=short,
        source=wiki_url(title),
        stub=stub,
    )

    content = f"""{fm}

# {short}

{stub_banner(stub)}{chr(10).join(parts) or '_No content scraped — see source._'}

{META_AGENT_DIVIDER}
"""

    path = KB_DIR / subdir / f"{slug}.md"
    safe_write(path, content, dry_run)
    return "wrote"


# ---------------------------------------------------------------------------
# Main orchestrator
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--limit", type=int, default=0,
                        help="Stop after N pages (0 = unlimited)")
    parser.add_argument(
        "--only",
        choices=["cards", "relics", "potions", "enemies", "events", "mechanics"],
        help="Scrape only one category",
    )
    parser.add_argument(
        "--output-dir",
        metavar="DIR",
        help="Write output to DIR instead of the default kb/ directory (useful for staging runs)",
    )
    args = parser.parse_args()

    # Override KB_DIR if --output-dir is specified
    global KB_DIR
    if args.output_dir:
        KB_DIR = Path(args.output_dir)
        KB_DIR.mkdir(parents=True, exist_ok=True)
        log.info("Output directory overridden to: %s", KB_DIR)

    log.info("=== STS2 KB builder starting (dry_run=%s, limit=%d) ===",
             args.dry_run, args.limit)

    stats: dict[str, int | list] = {
        "cards_ironclad": 0, "cards_colorless": 0, "cards_status": 0, "cards_skipped": 0,
        "relics_wrote": 0,   "relics_skipped": 0,
        "potions": 0,
        "enemies": 0,
        "events": 0,
        "mechanics": 0,
        "errors": [],
    }
    processed = 0

    def at_limit() -> bool:
        return bool(args.limit) and processed >= args.limit

    # ---- Cards ----
    if not args.only or args.only == "cards":
        log.info("--- Cards ---")
        card_titles = [
            t for t in list_category("Cards", namespace=NS_STS2)
            if "list" not in t.lower().replace(" ", "").replace("_", "")
        ]
        log.info("Found %d card pages", len(card_titles))
        for title in card_titles:
            if at_limit():
                break
            result = scrape_card(title, args.dry_run)
            processed += 1
            if result == "ironclad":
                stats["cards_ironclad"] += 1
            elif result == "colorless":
                stats["cards_colorless"] += 1
            elif result == "status":
                stats["cards_status"] += 1
            elif result == "skip":
                stats["cards_skipped"] += 1
            else:
                stats["errors"].append(title)  # type: ignore[union-attr]

    # ---- Relics ----
    if not args.only or args.only == "relics":
        log.info("--- Relics ---")
        relic_titles = [
            t for t in list_category("Relics", namespace=NS_STS2)
            if "list" not in t.lower().replace(" ", "").replace("_", "")
        ]
        log.info("Found %d relic pages", len(relic_titles))
        for title in relic_titles:
            if at_limit():
                break
            result = scrape_relic(title, args.dry_run)
            processed += 1
            if result == "wrote":
                stats["relics_wrote"] += 1
            elif result == "skip":
                stats["relics_skipped"] += 1
            else:
                stats["errors"].append(title)  # type: ignore[union-attr]

    # ---- Potions ----
    if not args.only or args.only == "potions":
        if not at_limit():
            log.info("--- Potions ---")
            n = scrape_potions_list(args.dry_run)
            stats["potions"] = n
            processed += 1

    # ---- Enemies ----
    if not args.only or args.only == "enemies":
        log.info("--- Enemies ---")
        seen: set[str] = set()
        enemy_titles: list[str] = []
        for cat in ["Monsters", "Elites", "Bosses", "Ancients"]:
            for t in list_category(cat, namespace=NS_STS2):
                if t not in seen and "list" not in t.lower().replace(" ", ""):
                    seen.add(t)
                    enemy_titles.append(t)
        log.info("Found %d enemy pages", len(enemy_titles))
        for title in enemy_titles:
            if at_limit():
                break
            result = scrape_enemy(title, args.dry_run)
            processed += 1
            if result == "wrote":
                stats["enemies"] += 1
            else:
                stats["errors"].append(title)  # type: ignore[union-attr]

    # ---- Events ----
    if not args.only or args.only == "events":
        log.info("--- Events ---")
        event_titles = [
            t for t in list_category("Events", namespace=NS_STS2)
            if "list" not in t.lower().replace(" ", "")
        ]
        log.info("Found %d event pages", len(event_titles))
        for title in event_titles:
            if at_limit():
                break
            result = scrape_event(title, args.dry_run)
            processed += 1
            if result == "wrote":
                stats["events"] += 1
            else:
                stats["errors"].append(title)  # type: ignore[union-attr]

    # ---- Mechanics ----
    if not args.only or args.only == "mechanics":
        log.info("--- Mechanics ---")
        for title, (slug, subdir) in MECHANICS_PAGES.items():
            if at_limit():
                break
            result = scrape_mechanics_page(title, slug, subdir, args.dry_run)
            processed += 1
            if result == "wrote":
                stats["mechanics"] += 1
            else:
                stats["errors"].append(title)  # type: ignore[union-attr]

    # ---- Summary ----
    print("\n" + "=" * 62)
    print("  KB BUILD SUMMARY")
    print("=" * 62)
    print(f"  Cards — Ironclad:       {stats['cards_ironclad']}")
    print(f"  Cards — Colorless:      {stats['cards_colorless']}")
    print(f"  Cards — Status/Curse:   {stats['cards_status']}")
    print(f"  Cards — Skipped:        {stats['cards_skipped']}  (other-class cards)")
    print(f"  Relics — Written:       {stats['relics_wrote']}")
    print(f"  Relics — Skipped:       {stats['relics_skipped']}  (other-class exclusive)")
    print(f"  Potions:                {stats['potions']}")
    print(f"  Enemies:                {stats['enemies']}")
    print(f"  Events:                 {stats['events']}")
    print(f"  Mechanics pages:        {stats['mechanics']}")
    print(f"  Errors:                 {len(stats['errors'])}")  # type: ignore[arg-type]
    if stats["errors"]:
        print("\n  Failed pages:")
        for e in stats["errors"]:  # type: ignore[union-attr]
            print(f"    {e}")

    if not args.dry_run:
        stub_count = sum(1 for md in KB_DIR.rglob("*.md")
                         if "stub: true" in md.read_text())
        print(f"\n  Stub files (stub: true): {stub_count}")
        print(f"  → rg 'stub: true' kb/  to list them all")

    print("=" * 62 + "\n")


if __name__ == "__main__":
    main()
