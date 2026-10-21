# Phase 5.1 — docs inventory & gap analysis

Plan 0032 phase 5. Working document for the org-docs rewrite — **not a
published site page** (excluded via `srcExclude`).

Scope: every page in `handl-lang/docs` plus the public-facing docs in
`research-mlopt` (`docs/*.md`, `README.md`, `paper/`). Owner column names
the *future* repo per the plan's cut map (`handl` = the language/toolchain
org; `eqsat`/`gamekit`/`graphopt` = the three public repos the split
produces — `graphopt` is what `research-mlopt` becomes, so content
currently in `research-mlopt` is tagged `graphopt`).

**Rename note.** `research-mlopt` is the current name; the plan lands
`graphopt` at phase 4. This inventory uses `graphopt` as the owner tag so
the provenance column in DESIGN.md sweeps cleanly. The `catopt` name still
appears in handl docs (kit-manifest worked example) and in the paper draft
title — the project name for the system, not the repo name.

## Stats

| surface | pages | notes |
|---|---|---|
| docs repo — hand-written site pages | 37 | 4 tutorials, 6 how-to, 14 `explanation/`, 10 `explanations/`, 3 hand-written reference, 10 root pages |
| docs repo — generated | ~200 `reference/<repo>/*.md` + `ADR-INDEX.md` | reference is gitignored except `index`/`host-concepts`/`strings-chars-unicode`; ADR-INDEX is generated but committed |
| research-mlopt — `docs/*.md` | 28 | 8 concept/API docs, 14 `results_*.md` evidence docs, 3 generated tables (+`.json` twins), 1 generated `results.md`, 1 completed internal plan |
| research-mlopt — other | `README.md`, `AGENTS.md`, `paper/` (qmd+pdf), `docs/tutorials/course/` (Vite+ app), `bench/{README,RESULTS}.md` | |

## Page inventory — `handl-lang/docs`

### Tutorials (all in nav + sidebar + index — coherent)

| path | quadrant | owner | stale? |
|---|---|---|---|
| `tutorials/index.md` | tutorial | handl | no |
| `tutorials/getting-started.md` | tutorial | handl | no |
| `tutorials/build-a-host.md` | tutorial | handl | overlaps `how-to/build-a-host.md` (same task, different framing — acceptable Diataxis pair, review after split) |
| `tutorials/write-a-plugin.md` | tutorial | handl | same pairing vs `how-to/write-a-plugin.md` |

### How-to (all linked — coherent)

| path | quadrant | owner | stale? |
|---|---|---|---|
| `how-to/index.md` | how-to | handl | no |
| `how-to/install-handl.md` | how-to | handl | clone URL is `github.com/handl-lang/host` — repo is now public, so the instructions work; verify the crate name `-p handl-host-cli` still holds post-ADR-0149 |
| `how-to/write-a-script.md` | how-to | handl | no |
| `how-to/build-a-host.md` | how-to | handl | no |
| `how-to/write-a-plugin.md` | how-to | handl | no |
| `how-to/configure-options.md` | how-to | handl | no |

### `explanation/` — the live Diataxis dir

| path | quadrant | owner | stale? |
|---|---|---|---|
| `explanation/index.md` | explanation | handl | missing entries: `arrow-calculus-kernel`, `graded-algebraic-theory`, `graded-modal-sanada-arrow-calculus` |
| `explanation/what-is-handl.md` | explanation | handl | no |
| `explanation/language-overview.md` | explanation | handl | **self-flagged stale vs ADR-0106** (banner on page) |
| `explanation/runtime.md` | explanation | handl | no |
| `explanation/platform-architecture.md` | explanation | handl | duplicates `explanations/platform-architecture.md` (drifted copies) |
| `explanation/composable-host.md` | explanation | handl | no |
| `explanation/arrow-calculus-kernel.md` | explanation | handl | in sidebar but not index; links into excluded `project/adrs/` |
| `explanation/graded-algebraic-theory.md` | explanation | handl | **orphaned** — not in index or sidebar; links into excluded `project/adrs/` |
| `explanation/graded-modal-sanada-arrow-calculus.md` | explanation | handl | **orphaned** — not in index or sidebar |
| `explanation/plugins-rules-operations.md` | explanation | handl | no |
| `explanation/kits-and-manifests.md` | explanation | handl | **stale paths** — `catopt`'s `lab/handl-spike/dump_fragments.py` (now `research-mlopt`'s `scripts/dump_fragments.py`), `handl-kit-data-canonical` (now `handl-kit-data-prelude`), "eight empty shell files" (now seven) |
| `explanation/options-and-configuration.md` | explanation | handl | no |
| `explanation/security-and-trust.md` | explanation | handl | no |
| `explanation/strings-chars-unicode-layers.md` | explanation | handl | in index but not sidebar |

### `explanations/` — a second, orphaned dir (no index, no nav, no sidebar)

These ten pages predate or bypass the `explanation/` dir. Only inbound
link in the whole site: `explanation/arrow-calculus-kernel.md` →
`explanations/small-kernel.md`. All owner = handl.

| path | quadrant | stale? |
|---|---|---|
| `explanations/ac-lib-api-design-principles.md` | explanation | no |
| `explanations/crate-architecture.md` | explanation | overlaps `explanation/platform-architecture.md` |
| `explanations/design-principles.md` | explanation | describes the field/expression kernel — pre-ADR-0106 framing |
| `explanations/fields-not-keys.md` | explanation | no |
| `explanations/lang-name.md` | explanation | no |
| `explanations/per-workspace-language-variants.md` | explanation | no |
| `explanations/platform-architecture.md` | explanation | **drifted duplicate** of `explanation/platform-architecture.md` |
| `explanations/polyglot-runtimes.md` | explanation | no |
| `explanations/small-kernel.md` | explanation | 2 broken links (`../../docs/LANG.md`); links into excluded `project/adrs/` |
| `explanations/vscode-extension-constraints.md` | explanation | no |

### Reference

| path | quadrant | owner | stale? |
|---|---|---|---|
| `reference/index.md` | reference | handl | links `reference/lib-*/` sections generated from **private** sibling repos — CI clones public repos only, so those links 404 on the deployed site |
| `reference/host-concepts.md` | reference | handl | no |
| `reference/strings-chars-unicode.md` | reference | handl | no |
| `reference/<repo>/*.md` (~200) | reference | handl | generated per sibling; locally covers private `lib-*` repos that Pages never sees |
| `reference.yaml`, `.vitepress/sidebar-reference.mjs` | reference | handl | generated inputs |

### Root pages

| path | quadrant | owner | stale? |
|---|---|---|---|
| `index.md` | meta (landing) | handl | no |
| `overview.md` | explanation | handl | linked from `explanation/index.md` (f589b2b); overlaps `explanation/platform-architecture.md`; ADR links now github URLs |
| `LANG.md` | explanation (stub landing) | handl | linked from `explanation/index.md`; ADR links now github URLs |
| `RUNTIME.md` | explanation (stub landing) | handl | linked from `explanation/index.md` |
| `PAPER.md` | explanation (paper) | handl | dead link **fixed (4314dd7)** — now points at `github.com/handl-lang/host/blob/main/research/PAPER.md`; still reachable only via `explanation/index.md` |
| `SAE.md` | explanation (paper) | handl | linked from `explanation/index.md` |
| `comparison.md` | explanation | handl | linked from `explanation/index.md` |
| `dialect-removal-plan.md` | internal plan | handl | **deleted (4314dd7)** — the plan was done, page was not site material |
| `ADR-INDEX.md` | reference | cross-repo | in nav + linked from `explanation/index.md` (4314dd7); header regenerated — `host` is public now |
| `api-examples.md` | scaffold | — | **deleted (4314dd7)** |
| `markdown-examples.md` | scaffold | — | **deleted (4314dd7)** |

## Page inventory — `research-mlopt` (public-facing; future `graphopt`)

| path | quadrant | owner | stale? |
|---|---|---|---|
| `README.md` | explanation (landing/pitch) | graphopt | doc table omits `api.md`, `public_api.md`, `cost-model.md`, `evaluation.md`, the scorecard/leaderboard/limits trio |
| `AGENTS.md` | how-to (dev reference) | graphopt | no — maintained with the code |
| `docs/api.md` | how-to/reference (walkthrough) | graphopt | overlaps `public_api.md`; no pointer to the frozen surface |
| `docs/public_api.md` | **reference** | graphopt → eqsat/gamekit split tags | the phase-1 frozen manifest; already carries per-destination tags — this is the binding contract for the org-site reference section |
| `docs/cost-model.md` | **explanation** | eqsat+graphopt (cross-cutting) | the three-costs model — a cross-cutting org page |
| `docs/mechanism.md` | explanation | graphopt | no |
| `docs/evaluation.md` | explanation | graphopt | no |
| `docs/paper_draft.md` | explanation (paper) | graphopt | title still says "Catopt" — the project name; reconcile naming at split |
| `docs/product_landing_page.md` | meta (marketing) | graphopt | no |
| `docs/lab_dissolution_plan.md` | internal plan (complete) | graphopt | status: complete — archive, not site material |
| `docs/results.md` | reference (generated) | graphopt | generated by `python -m bench results` |
| `docs/results_curated.md`, `results_tooling.md` | reference (hand-maintained inserts) | graphopt | appended into `results.md` verbatim — edit-here files |
| `docs/results_{learned_baseline,learned_ablations,learned_rl,macro_bake2,macro_moves,player_meta_arm,player_on_board,richer_features,schema_leaderboard,stop_advantage,stop_calibrated,stop_policy,stop_valuelabel,wholemodel_gap}.md` | reference (evidence docs) | graphopt | per-driver result documents |
| `docs/scorecard.md` + `.json` | reference (generated) | graphopt | generated discovery scorecard |
| `docs/leaderboard_players.md` + `.json` | reference (generated) | graphopt → gamekit content | generated player leaderboard |
| `docs/limits_table.md` + `.json` | reference (generated) | graphopt | generated limits table |
| `docs/tutorials/course/` | tutorial | graphopt | **interactive Vite+ app, not markdown** — builds standalone (`vp run -r build`) but has no published deployment; decision: **linked as unpublished** from `tutorials/research/index.md` with local-run commands |
| `paper/` (`paper.qmd`, `paper.pdf`, `references.bib`, `README.md`) | explanation (paper) | graphopt | no |
| `bench/README.md`, `bench/RESULTS.md` | how-to + reference | graphopt | no |

## Gap list

1. ~~**No end-to-end tutorial path.**~~ **Done (913e4ed)** —
   `tutorials/research/` is the learn-by-doing path: install → first
   `search()` → mint-a-law → scorecard. `research-mlopt/docs/tutorials/course/`
   stays a separate unpublished app, now linked as such from the track
   index.
2. ~~**research-mlopt has no how-to section at all**~~ **Done (phase
   5.3 cont.)** — `how-to/research/` ships the four DESIGN recipes:
   `optimize-a-model` (from `docs/api.md`), `add-a-board`, `register-
   a-player`, `admit-a-law` (from `docs/public_api.md` + the code).
   Upstream `docs/api.md` stays the working walkthrough; the how-to
   links out to it.
3. ~~**The org site documents only handl.**~~ **Done (913e4ed)** —
   `tutorials/research/`, `how-to/research/`, `explanation/research/` +
   `cross-cutting/`, and `reference/research/` give the research stack
   a section in every quadrant; ADR-INDEX has a nav entry.
4. ~~**`explanation/` vs `explanations/` split.**~~ **Done (f589b2b)** —
   merged into `explanation/`; `platform-architecture` deduped, every
   page now in index + sidebar.
5. ~~**Explanation content scattered across root.**~~ **Mostly done
   (f589b2b/913e4ed)** — the six root pages are reachable from
   `explanation/index.md` (a "papers & longer reads" group). A
   dedicated `papers.md`/`explanation/papers/` grouping is still on
   the DESIGN map.
6. ~~**Dead links are masked.**~~ **Fixed (4314dd7)** — `ignoreDeadLinks`
   stays on, but the known classes are repointed: `project/adrs/*`
   links now go to `github.com/handl-lang/host/blob/project/adrs/…`
   (ADRs live on the host repo's `project` *branch*), `PAPER.md` →
   `…/blob/main/research/PAPER.md`, `small-kernel.md`'s
   `../../docs/LANG.md` → `./LANG`. The `reference/lib-*` links remain
   local-only by design — marked "(internal repo)" in `reference/
   index.md` (913e4ed); real fix belongs to the split.
7. ~~**Missing index/sidebar entries in `explanation/`.**~~ **Fixed
   (4314dd7/f589b2b)** — every `explanation/` page is in both index and
   sidebar.
8. ~~**ADR-INDEX.md is published but orphaned**~~ **Fixed (4314dd7)** —
   nav entry + `explanation/index.md` link; regenerated header no longer
   calls `host` private.
9. ~~**No per-repo reference for research-mlopt.**~~ **Done (913e4ed)** —
   `reference/research/frozen-api.md` vendors `docs/public_api.md` at
   `eea02f6`; scorecard/leaderboard/limits vendor the generated tables.
10. ~~**Stale singletons**~~ **Fixed (4314dd7/f589b2b)** —
    `kits-and-manifests` paths updated, `dialect-removal-plan` deleted,
    `small-kernel` merged into `explanation/` keeping its pre-ADR-0106
    caveat.
