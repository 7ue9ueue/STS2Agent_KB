# Ironclad Card Schema

This folder is a structured data layer, not a strategy or policy layer.

## Sources

- Primary card records come from `https://spire-codex.com/api/cards?color=ironclad`.
- Matching wiki.gg pages are linked when they can be fetched, but generated card pages do not quote wiki strategy prose.

## Card Page Sections

- `Sources`: URLs used for the record.
- `Card Text`: normalized base and upgraded text.
- `Structured Fields`: source IDs, type, rarity, target, keywords, and API-provided tags.
- `Numeric Fields`: parsed source numeric fields such as damage, block, draw, energy, and HP loss.
- `Upgrade And Generation Data`: source `vars`, `upgrade`, generated-card, and compendium fields.

Total Ironclad card records: 87


## Merge Notes

- Starter cards are written to `strike_ironclad.md` and `defend_ironclad.md` to preserve existing STS2MCP filenames.
- Old-only files are kept and listed as `legacy-wiki` in `_index.md`.
- Meta-agent notes below each card's divider are preserved during merge.
