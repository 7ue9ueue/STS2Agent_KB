#!/usr/bin/env python3
"""Rebuild kb/events as structured event data.

Primary source: https://spire-codex.com/api/events

This intentionally omits event/page narrative descriptions and dialogue. For
agent play, the useful facts are event identity, act/preconditions, and the
available option IDs/effects.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

import requests

ROOT = Path(__file__).parent.parent
EVENT_DIR = ROOT / "kb" / "events"
API_URL = "https://spire-codex.com/api/events"
UA = "STS2MCP Event KB Builder"

DIVIDER = "---\n<!-- META-AGENT NOTES"
META_TEMPLATE = """---
<!-- META-AGENT NOTES — do not edit above this line -->
## Strategy Notes

<!-- Reserved for the meta-agent. Append lessons, combos, and heuristics here.
     Source facts live above the divider. -->
"""


def slugify(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_")


def clean_text(text: object) -> str:
    if text is None:
        return ""
    out = str(text)
    out = re.sub(r"\[/?(?:red|green|blue|gold|purple|orange|aqua|gray|sine|jitter|b|i)\]", "", out)
    out = re.sub(r"\[energy:(\d+)\]", r"\1 Energy", out)
    out = re.sub(r"\s+", " ", out).strip()
    return out


def yaml_list(values: list[str]) -> str:
    if not values:
        return "[]"
    escaped = [v.replace("]", "\\]") for v in values]
    return "[" + ", ".join(escaped) + "]"


def frontmatter(**fields: object) -> str:
    lines = ["---"]
    for key, value in fields.items():
        if isinstance(value, list):
            lines.append(f"{key}: {yaml_list([str(v) for v in value])}")
        elif isinstance(value, bool):
            lines.append(f"{key}: {'true' if value else 'false'}")
        elif value is None:
            lines.append(f"{key}: null")
        else:
            lines.append(f"{key}: {value}")
    lines.append("---")
    return "\n".join(lines)


def split_meta(text: str) -> tuple[str, str]:
    idx = text.find(DIVIDER)
    if idx == -1:
        return text.rstrip(), META_TEMPLATE
    return text[:idx].rstrip(), text[idx:].rstrip() + "\n"


def source_value(value: object) -> str:
    if value is None:
        return "—"
    if isinstance(value, (dict, list)):
        return f"`{json.dumps(value, sort_keys=True)}`"
    text = clean_text(value)
    return text if text else "—"


def option_rows(options: list[dict[str, Any]] | None) -> list[str]:
    if not options:
        return []
    rows = []
    for option in options:
        rows.append(
            "| "
            + " | ".join(
                [
                    source_value(option.get("id")),
                    source_value(option.get("title")),
                    source_value(option.get("description")),
                ]
            )
            + " |"
        )
    return rows


def page_option_rows(pages: list[dict[str, Any]] | None) -> list[str]:
    if not pages:
        return []
    rows = []
    for page in pages:
        page_id = source_value(page.get("id"))
        for option in page.get("options") or []:
            rows.append(
                "| "
                + " | ".join(
                    [
                        page_id,
                        source_value(option.get("id")),
                        source_value(option.get("title")),
                        source_value(option.get("description")),
                    ]
                )
                + " |"
            )
    return rows


def relic_rows(relics: object) -> list[str]:
    if not isinstance(relics, list):
        return []
    rows = []
    for relic in relics:
        if isinstance(relic, dict):
            rows.append(
                "| "
                + " | ".join(
                    [
                        source_value(relic.get("id")),
                        source_value(relic.get("name")),
                        source_value(relic.get("description") or relic.get("effect")),
                    ]
                )
                + " |"
            )
        else:
            rows.append(f"| — | {source_value(relic)} | — |")
    return rows


def event_content(event: dict[str, Any], meta: str) -> str:
    preconditions = [clean_text(p) for p in event.get("preconditions") or []]
    fm = frontmatter(
        title=event.get("name"),
        source=API_URL,
        id=event.get("id"),
        type=event.get("type"),
        act=event.get("act"),
        preconditions=preconditions,
        stub=False,
    )

    initial = option_rows(event.get("options"))
    initial_block = (
        "\n".join(["| ID | Title | Effect |", "|---|---|---|", *initial])
        if initial
        else "_No initial options in source record._"
    )

    page_rows = page_option_rows(event.get("pages"))
    page_block = (
        "\n".join(["| Page ID | Option ID | Title | Effect |", "|---|---|---|---|", *page_rows])
        if page_rows
        else "_No page-transition options in source record._"
    )

    relics = relic_rows(event.get("relics"))
    relic_block = (
        "\n".join(["| ID | Name | Effect |", "|---|---|---|", *relics])
        if relics
        else "_No relic list in source record._"
    )

    pre_block = "\n".join(f"- {p}" for p in preconditions) if preconditions else "_None in source record._"

    body = f"""{fm}

# {event.get('name')}

## Sources

- {API_URL}

## Structured Fields

| Field | Value |
|---|---|
| ID | {source_value(event.get('id'))} |
| Type | {source_value(event.get('type'))} |
| Act | {source_value(event.get('act'))} |
| Epithet | {source_value(event.get('epithet'))} |
| Image URL | {source_value(event.get('image_url'))} |

## Preconditions

{pre_block}

## Initial Options

{initial_block}

## Page Transition Options

{page_block}

## Relics

{relic_block}
"""
    return f"{body.rstrip()}\n\n{meta}"


def fetch_events() -> list[dict[str, Any]]:
    response = requests.get(API_URL, headers={"User-Agent": UA}, timeout=30)
    response.raise_for_status()
    events = response.json()
    if not isinstance(events, list):
        raise RuntimeError("Unexpected events API response")
    return events


def write_index(events: list[dict[str, Any]], old_only: list[Path]) -> None:
    rows = ["| Event | Act | Type | File |", "|---|---|---|---|"]
    for event in sorted(events, key=lambda e: str(e.get("name", "")).lower()):
        name = str(event.get("name"))
        slug = slugify(name)
        rows.append(
            f"| {name} | {source_value(event.get('act'))} | {source_value(event.get('type'))} | [{slug}](./{slug}.md) |"
        )
    for path in old_only:
        rows.append(f"| {path.stem} | legacy | legacy-wiki | [{path.stem}](./{path.stem}.md) |")

    content = "\n".join(
        [
            "# Events",
            "",
            "Structured event option data. Narrative dialogue and update-history sections are intentionally omitted.",
            "",
            f"API event records: {len(events)}",
            f"Legacy-only files kept: {len(old_only)}",
            "",
            *rows,
            "",
        ]
    )
    (EVENT_DIR / "_index.md").write_text(content)


def write_schema() -> None:
    content = """# Event Schema

Primary source: `https://spire-codex.com/api/events`.

Generated event pages intentionally omit narrative descriptions, dialogue, and update history. The retained fields are meant for agent navigation:

- `Structured Fields`: event identity, type, act, epithet, image URL.
- `Preconditions`: source-provided preconditions.
- `Initial Options`: options available on the initial event screen.
- `Page Transition Options`: option effects exposed on later event pages.
- `Relics`: source-provided relic lists when present.

Meta-agent notes below each file's divider are preserved across rebuilds.
"""
    (EVENT_DIR / "_schema.md").write_text(content)


def main() -> None:
    EVENT_DIR.mkdir(parents=True, exist_ok=True)
    events = fetch_events()
    api_slugs = set()

    for event in events:
        slug = slugify(str(event.get("name")))
        api_slugs.add(slug)
        path = EVENT_DIR / f"{slug}.md"
        old_text = path.read_text() if path.exists() else ""
        _old_body, meta = split_meta(old_text)
        path.write_text(event_content(event, meta))

    old_only = [
        path for path in sorted(EVENT_DIR.glob("*.md"))
        if not path.name.startswith("_") and path.stem not in api_slugs
    ]
    write_index(events, old_only)
    write_schema()
    print(f"Wrote {len(events)} structured event records to {EVENT_DIR}")
    print(f"Kept {len(old_only)} legacy-only event files")


if __name__ == "__main__":
    main()
