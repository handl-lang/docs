---
title: Decisions
type: index
---

# Decisions

One line per decision rule, generated from each ADR's `## Decision`
section with `host/scripts/gen-decisions.py`. The ADR is the argument;
this is the recall surface (ADR-0161 §8). Superseded records are excluded.

### `handl-press` — A VitePress-Class Docs Framework Written In and Configurable Through Handl

- **SSG** (default): build arrow writes dist/*.html via fs.write — [ADR-0080](adrs/0080-handl-press-docs-framework.md)
- **SSR**: http-server serves rendered HTML per request, in-process eval — [ADR-0080](adrs/0080-handl-press-docs-framework.md)
- **Client-side**: compile the theme + content to WASM (ADR-0077 multi-target — [ADR-0080](adrs/0080-handl-press-docs-framework.md)
- **PDF / single-file**: a custom build arrow pass that serializes the route — [ADR-0080](adrs/0080-handl-press-docs-framework.md)
