# Phase 5.2 — target structure for the org docs site

Plan 0032 phase 5. Working document — **not a published page** (excluded
via `srcExclude`). Builds on `ANALYSIS.md`.

Design constraints:

- The site aggregates **public** repos only (the Pages workflow clones
  with `--visibility public`). Private sibling repos produce **no**
  pages, links, or mentions anywhere in this repo — including the
  private split-out the plan carves off; it is absent by construction.
- Repo rename landed: `research-mlopt` is now `graphopt`; the phase-4
  extraction landed too — `eqsat` and `gamekit` are public repos.
  Every page carries a **provenance** tag (see below) so a rename is a
  sweep, not a rewrite.
- Reference is bound to `graphopt/docs/public_api.md` — the
  phase-1 frozen surface (`API_VERSION = "0.1.0"`). Only frozen names
  get reference pages; the doc already tags each contract with its
  destination repo.

## Target top level

```
index.md                       landing — org-level: language platform + research stack
tutorials/                     end-to-end lesson paths, ordered
how-to/                        task recipes, grouped by repo section
explanation/                   concepts, grouped by repo section + cross-cutting
reference/                     generated + frozen-API pages, grouped by repo
ADRs                           (ADR-INDEX.md, linked from nav)
```

Per-repo sections appear inside each quadrant (not as four parallel site
trees). The nav stays four entries; each quadrant index groups by
domain: **handl** (language + toolchain), **graphopt** (tensor-law
discovery — renamed from `research-mlopt`), **eqsat** (e-graph
substrate), **gamekit** (the game layer). The phase-4 split landed:
`eqsat`/`gamekit` are public repos with their own site sections.

## Page map with provenance

Provenance = *where the source of truth lives*, written as
`repo:path@rev-pin`. When a repo renames, every page whose provenance
starts with the old name sweeps to the new one (`research-mlopt:` →
`graphopt:` landed). Pages authored fresh for this site carry `docs:`.

### Tutorials — the end-to-end path

Order matters; each step links to the next. This is the gap-1 fix.

| page | purpose | provenance |
|---|---|---|
| `tutorials/index.md` | the two paths: handl track, research track | docs: |
| `tutorials/getting-started.md` | handl: install `hnl`, first expression | docs: (exists) |
| `tutorials/build-a-host.md` | handl: host binary + kit | docs: (exists) |
| `tutorials/write-a-plugin.md` | handl: `Plugin` + a rule | docs: (exists) |
| `tutorials/research/setup.md` | install graphopt (`uv sync`, `.venv`) | `graphopt:README.md`, `AGENTS.md` |
| `tutorials/research/first-search.md` | first `search()` — a model in, a cheaper certified form out | `graphopt:docs/api.md`, `mlopt_orchestrator.search` (frozen) |
| `tutorials/research/mint-a-law.md` | watch a law get minted and survive the gauntlet | `graphopt:mlopt_discovery` mint machinery, `docs/mechanism.md` |
| `tutorials/research/run-the-scorecard.md` | regenerate `docs/scorecard.md`, read a row | `graphopt:bench`, `docs/scorecard.md` |

### How-to — per-repo groups

| page | purpose | provenance | status |
|---|---|---|---|
| `how-to/install-handl.md` … (6 existing) | handl toolchain recipes | docs: | shipped |
| `how-to/research/optimize-a-model.md` | `Optimizer`/`search` + runners + `engine=` | `graphopt:docs/api.md` | **shipped** (phase 5.3 cont.) |
| `how-to/research/add-a-board.md` | write a `Domain` + `Board` | `graphopt:gamekit.engine` + `mlopt_discovery.play` | **shipped** (phase 5.3 cont.) |
| `how-to/research/register-a-player.md` | `PlayerSpec` + registry | `graphopt:gamekit.players.registry` | **shipped** (phase 5.3 cont.) |
| `how-to/research/admit-a-law.md` | `verify_law` → gauntlet → `MACHINE_SHIPPED` | `graphopt:mlopt_discovery.{pipeline,verifier,emit}` + `mlopt_core.laws.provenance` | **shipped** (phase 5.3 cont.) |

### Explanation — per-repo groups + cross-cutting

| page | purpose | provenance |
|---|---|---|
| `explanation/` (14 existing) | handl concepts | docs: |
| `explanations/` → merged into `explanation/` | handl design notes | docs: (dedupe `platform-architecture`, merge `crate-architecture` content) |
| `explanation/research/mechanism.md` | syntax → structure → search → certificate | `graphopt:docs/mechanism.md` |
| `explanation/research/evaluation.md` | the fourth dimension | `graphopt:docs/evaluation.md` |
| `explanation/cross-cutting/three-costs.md` | **the three costs** — `dag_cost` guess / measured pay / delivered measurement | `graphopt:docs/cost-model.md` |
| `explanation/cross-cutting/the-game.md` | boards, players, episodes, the learned policy loop | `graphopt:gamekit.engine`, `docs/results_player_on_board.md` |
| `explanation/cross-cutting/the-gauntlet.md` | numeric oracle → typed-pay gate → adversarial sweep → certificate | `graphopt:mlopt_discovery.verifier`, `docs/public_api.md` |
| `papers.md` (or `explanation/papers/`) | PAPER.md, SAE.md, `graphopt:docs/paper_draft.md` + `paper/` | docs: + repo pointers |

### Reference — bound to the frozen surface

| page | purpose | provenance |
|---|---|---|
| `reference/index.md` | per-repo index — handl groups (existing) **plus** a research group | docs: |
| `reference/kernel/`, `reference/host-tensor/` | generated from public siblings | generated (existing pipeline) |
| `reference/research/frozen-api.md` → split at phase 5.4 into `graphopt/reference/frozen-api` (vendored, domain rows) + `eqsat/reference/frozen-api` + `gamekit/reference/frozen-api` (docs-repo slices) | the frozen surface, rendered — one slice per destination repo | `graphopt:docs/public_api.md` — bind at `API_VERSION`; vendored with a "synced at \<sha\>" header |
| `reference/research/{scorecard,leaderboard,limits}.md` | the three generated tables, republished with their provenance headers | `graphopt:docs/{scorecard,leaderboard_players,limits_table}.md` (generated there, vendored here — **never hand-edited**) |
| `ADR-INDEX.md` | keep; add nav entry | generated (existing) |

The `reference/lib-*` sections are generated from private sibling repos
and 404 on the deployed site — either they move behind "internal"
marking, or `reference/index.md` only lists groups whose repos are
public. Cheap interim fix: mark them "(internal repo)" and accept the
local-only rendering; real fix belongs to the split.

## Sequencing (the update lane, phase 5.3+)

1. ~~Cheap fixes now~~ — **done (4314dd7)**: stale paths, dead links
   (`project/adrs/*` → `host@project` branch URLs, `PAPER.md` →
   `host@main` `research/PAPER.md`, `../../docs/LANG.md`), index/sidebar
   entries, scaffold pages.
2. ~~Add the research skeleton~~ — **done (913e4ed + cont.)**:
   `tutorials/research/` (4 steps + index), `explanation/research/` +
   `cross-cutting/` (3 pages), `reference/research/` (frozen-api +
   3 vendored tables), `how-to/research/` (4 recipes). The
   `docs/tutorials/course/` app is linked as unpublished from the track
   index — it builds standalone (`vp run -r build`) but has no
   deployment; wiring a published path is deferred (separate toolchain,
   separate site).
3. ~~On phase-4 extraction~~ — **done (phase 5.4)**: the split landed
   (`graphopt` + public `eqsat`/`gamekit`). `frozen-api.md` is split by
   destination tag: `eqsat/reference/frozen-api.md` (substrate rows) and
   `gamekit/reference/frozen-api.md` (game rows) are docs-repo pages
   synced from `graphopt:docs/public_api.md@fb00089`; the domain rows
   stay in the vendored `graphopt/reference/frozen-api`. New tracked
   sections `eqsat/` + `gamekit/` carry the repo-scoped stubs
   (egraph/certificates/ports; board/players/kernel) — the vendored
   `graphopt/docs/site/` pages still carry pre-split provenance tags
   (`graphopt:gamekit.*` paths) that now resolve to the
   `gamekit`/`eqsat` repos; the upstream sweep is the follow-up.
4. Remaining open items: the `papers.md` / `explanation/papers/`
   grouping (PAPER.md, SAE.md, `paper_draft.md`, `paper/`); the
   `reference/lib-*` internal-repo treatment on the deployed site
   (currently marked "(internal repo)" — real fix at the split).
