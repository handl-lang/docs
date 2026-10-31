+++
id = "ADR-0080"
title = "ADR-0080: `handl-press` — A VitePress-Class Docs Framework Written In and Configurable Through Handl"
status = "open"
priority = "medium"
+++

---
title: '`handl-press` — A VitePress-Class Docs Framework Written In and Configurable Through Handl'
type: adr
date: 2026-09-04
status: proposed
status_note: |-
  Proposed. Targets the backlog (see `project/BACKLOG.md` → "Low priority").
  Depends on [ADR-0077 — Stdlib Migration to Handl](./0077-stdlib-migration-to-handl.md)
  (`op`/`handl`/`cap` surface, `HandlModule` loader), [ADR-0069 — Arrow-Native
  Modules](./0069-arrow-native-modules.md) (importable `.hnl` modules),
  [ADR-0021 — HMR](./0021-hmr.md) (dev-server hot reload), and
  [ADR-0079 — Unified Dialect](./0079-unify-dialects-no-let-in.md) (graph blocks
  as the configuration surface).
---


# ADR-0080: `handl-press` — A VitePress-Class Docs Framework Written In and Configurable Through Handl

## Decision

1. **Layering — kit, libs, protocol.** kit-press                       (curated plugin list, ADR-0039) ├─ plugin-lib-markdown        (new — block parser, handl-in-md fences) ├─ plugin-lib-docs-config     (new — config schema, validation, defaults) ├─ plugin-lib-docs-theme      (new — theme protocol, slot rendering) ├─ plugin-lib-docs-build      (new — SSG pipeline, asset graph, manifest) ├─ plugin-lib-docs-search     (new — index build + client query, optional) ├─ plugin-lib-tag             (existing — HTML emission) ├─ plugin-lib-fs              (existing — read content, write dist) ├─ plugin-lib-http-server     (existing — dev server) ├─ plugin-lib-http-server-std (existing — dev server impl) ├─ plugin-lib-intl            (existing — i18n) ├─ plugin-lib-utils           (existing) └─ plugin-lib-collections     (existing)
2. **Content format — Markdown with handl fences.** Content files are Markdown. A fence extension allows handl expressions and components inline:
3. **Configuration — a handl program, not a data file.** The site config is a `.hnl` file (`press.config.hnl` by convention). It is a program that returns a `PressConfig` value:
4. **Theme protocol — handl functions returning HTML.** A theme is a `.hnl` module exporting a set of render functions, one per layout slot:
5. **Build pipeline — arrows all the way down.** The build is a handl arrow graph (ADR-0052), not a Rust pipeline:
6. **Dev server — HMR via ADR-0021.** `kit-press dev` runs the build arrow in watch mode (ADR-0021 HMR). Content, config, and theme files are dependencies of the build arrow; on change, the affected sub-graph re-evaluates and the browser reloads only the changed slot. The dev server is `plugin-lib-http-server-std` serving the in-memory render output — no `dist/` write in dev mode. This is the VitePress dev experience, implemented on handl's existing HMR + HTTP server primitives.
7. **Multi-target output.** Because the framework is handl arrows + `op` declarations, the same `press.config.hnl` produces:
8. **Search — optional, capability-gated.** `plugin-lib-docs-search` builds a client-side index (Pagefind-style: content sharded, index in JSON) during the build pass, and ships a query `op` that runs against the index in the browser. The lib declares `cap "search.build"` (build-time) and `cap "search.query"` (runtime); a site that does not enable search simply does not register the build cap, and the index pass is skipped. This keeps search opt-in without conditional imports.
9. **i18n — via `plugin-lib-intl`.** Locale routing and translated UI strings use `plugin-lib-intl` directly. Content translation is per-file (`guide.en.md`, `guide.es.md`); the route table exposes `/en/guide` and `/es/guide` from the same `nav-from-dir` function parameterized by locale. No framework-specific i18n mechanism is invented.

## Why

VitePress is the canonical "docs framework" shape in the frontend ecosystem: Markdown content + a small JS/TS config + Vue components for extensibility, compiled by Vite to a static site (SSG) with a dev server (HMR), client-side routing, theming, search, and i18n. Its success comes from three properties:

## Not doing

- none recorded — legacy record; the design doc lists what was deferred.

## Consequences

- **One language for content, config, theme, and build.** No Vue, no TS
- **Capability-tracked themes and configs.** A theme's I/O is explicit and
- **Multi-target output is inherent.** SSG, SSR, WASM-client, and PDF share
- **The build is a program.** Custom passes (diagrams, link checking,
- **Reuses the stdlib migration end state.** No new runtime mechanism; the

## Enforcement

- Code and tests are named in the design doc.

## Design

The full record (mechanism, tables, proofs, trade-offs): [`design/0080-handl-press-docs-framework.md`](../design/0080-handl-press-docs-framework.md).
