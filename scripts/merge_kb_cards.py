#!/usr/bin/env python3
"""Merge data-oriented kb_new Ironclad card pages into kb/.

The merge keeps kb_new as the staging source and writes normalized card pages
under kb/cards/ironclad. It preserves any existing meta-agent notes, maps
starter cards back to the existing STS2MCP filenames, and keeps old-only files
instead of deleting them.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).parent.parent
NEW_DIR = ROOT / "kb_new" / "cards" / "ironclad"
OLD_DIR = ROOT / "kb" / "cards" / "ironclad"

DIVIDER = "---\n<!-- META-AGENT NOTES"
META_TEMPLATE = """---
<!-- META-AGENT NOTES — do not edit above this line -->
## Strategy Notes

<!-- Reserved for the meta-agent. Append lessons, combos, and heuristics here.
     Source facts live above the divider. -->
"""

SLUG_ALIASES = {
    "strike": "strike_ironclad",
    "defend": "defend_ironclad",
}


def split_meta(text: str) -> tuple[str, str]:
    idx = text.find(DIVIDER)
    if idx == -1:
        return text.rstrip(), META_TEMPLATE
    return text[:idx].rstrip(), text[idx:].rstrip() + "\n"


def title_from_page(text: str) -> str:
    for line in text.splitlines():
        if line.startswith("title: "):
            return line.removeprefix("title: ").strip()
    m = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    return m.group(1).strip() if m else "Unknown"


def legacy_notes(text: str, max_items: int = 12) -> list[str]:
    """Extract compact interaction notes from the old wiki scrape."""
    m = re.search(r"## Notes\n\n(.*?)(?:\n## Update History|\n---\n<!-- META)", text, re.DOTALL)
    if not m:
        return []
    useful = re.compile(
        r"\b(trigger|triggers|increase|increases|reduce|reduces|count|counts|"
        r"cause|causes|allow|allows|activate|activates|double|doubles|"
        r"exhaust|vulnerable|replay|damage|block|strength|energy|draw|discard|"
        r"retain|fatal|play|played)\b",
        re.I,
    )
    notes: list[str] = []
    for raw in m.group(1).splitlines():
        line = raw.strip()
        line = re.sub(r"^\*+\s*", "", line)
        line = re.sub(r"^-+\s*", "", line)
        if not line or line == "_None._":
            continue
        if line.startswith(("###", "====", "Obtaining ", "Can be bought", "Can be obtained")):
            continue
        if "Early Access" in line or "Added " in line:
            continue
        if not useful.search(line):
            continue
        line = re.sub(r"^\*\*(.+?)\*\*$", r"\1", line)
        if len(line) > 220:
            line = line[:217].rstrip() + "..."
        if line not in notes:
            notes.append(line)
        if len(notes) >= max_items:
            break
    return notes


def append_legacy_notes(new_body: str, old_text: str | None) -> str:
    if not old_text:
        return new_body.rstrip()
    notes = legacy_notes(old_text)
    if not notes:
        return new_body.rstrip()
    note_block = "\n".join(f"- {note}" for note in notes)
    return f"{new_body.rstrip()}\n\n## Legacy Wiki Notes\n\n{note_block}"


def merge_new_cards() -> list[dict[str, str]]:
    OLD_DIR.mkdir(parents=True, exist_ok=True)
    merged: list[dict[str, str]] = []

    for src in sorted(NEW_DIR.glob("*.md")):
        if src.name.startswith("_"):
            continue
        slug = src.stem
        dest_slug = SLUG_ALIASES.get(slug, slug)
        dest = OLD_DIR / f"{dest_slug}.md"

        new_body, _new_meta = split_meta(src.read_text())
        old_text = dest.read_text() if dest.exists() else None
        _old_body, old_meta = split_meta(old_text) if old_text else ("", META_TEMPLATE)
        body = append_legacy_notes(new_body, old_text)
        dest.write_text(f"{body}\n\n{old_meta}")
        merged.append({
            "title": title_from_page(new_body),
            "slug": dest_slug,
            "source": "spire-codex",
        })

    return merged


def list_old_only(merged_slugs: set[str]) -> list[dict[str, str]]:
    old_only: list[dict[str, str]] = []
    for path in sorted(OLD_DIR.glob("*.md")):
        if path.name.startswith("_"):
            continue
        if path.stem in merged_slugs:
            continue
        text = path.read_text()
        tidy_legacy_file(path, text)
        old_only.append({
            "title": title_from_page(text),
            "slug": path.stem,
            "source": "legacy-wiki",
        })
    return old_only


def tidy_legacy_file(path: Path, text: str) -> None:
    body, meta = split_meta(text)
    body = re.sub(r"\n## Update History\n\n.*$", "", body, flags=re.DOTALL).rstrip()
    body = re.sub(
        r"\n### Obtaining .+?(?=\n### |\n## |\Z)",
        "",
        body,
        flags=re.DOTALL,
    )
    body = re.sub(r"\n{3,}", "\n\n", body)
    path.write_text(f"{body}\n\n{meta}")


def write_index(records: list[dict[str, str]]) -> None:
    records = sorted(records, key=lambda r: r["title"].lower())
    lines = [
        "# Ironclad Cards",
        "",
        "Merged Ironclad card index. `spire-codex` rows come from `kb_new` structured data; `legacy-wiki` rows are old wiki records kept because they were not present in the current Spire Codex Ironclad API result.",
        "",
        f"Total files: {len(records)}",
        "",
        "| Card | File | Source set |",
        "|---|---|---|",
    ]
    for record in records:
        lines.append(f"| {record['title']} | [{record['slug']}](./{record['slug']}.md) | {record['source']} |")
    (OLD_DIR / "_index.md").write_text("\n".join(lines) + "\n")


def write_schema() -> None:
    src_schema = NEW_DIR / "_schema.md"
    text = src_schema.read_text() if src_schema.exists() else "# Ironclad Card Schema\n"
    text = text.replace("# kb_new Schema", "# Ironclad Card Schema")
    text = text.replace("- Existing `kb/` is not modified.\n", "")
    text += "\n## Merge Notes\n\n- Starter cards are written to `strike_ironclad.md` and `defend_ironclad.md` to preserve existing STS2MCP filenames.\n- Old-only files are kept and listed as `legacy-wiki` in `_index.md`.\n- Meta-agent notes below each card's divider are preserved during merge.\n"
    (OLD_DIR / "_schema.md").write_text(text)


def main() -> None:
    merged = merge_new_cards()
    old_only = list_old_only({r["slug"] for r in merged})
    write_index(merged + old_only)
    write_schema()
    print(f"Merged {len(merged)} kb_new card records into {OLD_DIR}")
    print(f"Kept {len(old_only)} legacy-only card records")


if __name__ == "__main__":
    main()
