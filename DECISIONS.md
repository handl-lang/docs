---
title: Decisions
type: index
---

# Decisions

One line per decision rule, generated from each ADR's `## Decision`
section with `host/scripts/gen-decisions.py`. The ADR is the argument;
this is the recall surface (ADR-0161 §8). Superseded records are excluded.

### `handl-press` — A VitePress-Class Docs Framework Written In and Configurable Through Handl

- **Layering — kit, libs, protocol.** kit-press (curated plugin list, ADR-0039) ├─ plugin-lib-markdown (new — block… — [ADR-0080](adrs/0080-handl-press-docs-framework.md)
- **Content format — Markdown with handl fences.** Content files are Markdown. A fence extension allows handl expressions… — [ADR-0080](adrs/0080-handl-press-docs-framework.md)
- **Configuration — a handl program, not a data file.** The site config is a .hnl file (press.config.hnl by convention).… — [ADR-0080](adrs/0080-handl-press-docs-framework.md)
- **Theme protocol — handl functions returning HTML.** A theme is a .hnl module exporting a set of render functions, one… — [ADR-0080](adrs/0080-handl-press-docs-framework.md)
- **Build pipeline — arrows all the way down.** The build is a handl arrow graph (ADR-0052), not a Rust pipeline: — [ADR-0080](adrs/0080-handl-press-docs-framework.md)
- **Dev server — HMR via ADR-0021.** kit-press dev runs the build arrow in watch mode (ADR-0021 HMR). Content, config,… — [ADR-0080](adrs/0080-handl-press-docs-framework.md)
- **Multi-target output.** Because the framework is handl arrows + op declarations, the same press.config.hnl produces: — [ADR-0080](adrs/0080-handl-press-docs-framework.md)
- **Search — optional, capability-gated.** plugin-lib-docs-search builds a client-side index (Pagefind-style: content… — [ADR-0080](adrs/0080-handl-press-docs-framework.md)
- **i18n — via plugin-lib-intl.** Locale routing and translated UI strings use plugin-lib-intl directly. Content… — [ADR-0080](adrs/0080-handl-press-docs-framework.md)
