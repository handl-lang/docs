# Phase 5.2 — target structure for the org docs site

Plan 0032 phase 5. Working document — **not a published page** (excluded
via `srcExclude`). Builds on `ANALYSIS.md`.

Design constraints:

- The site aggregates **public** repos only (the Pages workflow clones
  with `--visibility public`). Private sibling repos produce **no**
  pages, links, or mentions anywhere in this repo — including the
  private split-out the plan carves off; it is absent by construction.
- Repo names in flight: `research-mlopt` → `graphopt`; `eqsat` and
  `gamekit` are extracted at phase 4. Every page carries a **provenance**
  tag (see below) so a rename is a sweep, not a rewrite.
- Reference is bound to `research-mlopt/docs/public_api.md` — the
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
discovery — currently `research-mlopt`), **eqsat** (e-graph substrate —
post-phase-4), **gamekit** (the game layer — post-phase-4). Until the
split lands, the eqsat/gamekit rows read "lives in `research-mlopt`
today" — the provenance column makes that explicit rather than silent.

## Page map with provenance

Provenance = *where the source of truth lives*, written as
`repo:path@rev-pin`. When a repo renames, every page whose provenance
starts with `research-mlopt:` sweeps to `graphopt:`. Pages authored
fresh for this site carry `docs:`.

### Tutorials — the end-to-end path

Order matters; each step links to the next. This is the gap-1 fix.

| page | purpose | provenance |
|---|---|---|
| `tutorials/index.md` | the two paths: handl track, research track | docs: |
| `tutorials/getting-started.md` | handl: install `hnl`, first expression | docs: (exists) |
| `tutorials/build-a-host.md` | handl: host binary + kit | docs: (exists) |
| `tutorials/write-a-plugin.md` | handl: `Plugin` + a rule | docs: (exists) |
| `tutorials/research/setup.md` | install research-mlopt (`uv sync`, `.venv`) | `research-mlopt:README.md`, `AGENTS.md` |
| `tutorials/research/first-search.md` | first `search()` — a model in, a cheaper certified form out | `research-mlopt:docs/api.md`, `mlopt_orchestrator.search` (frozen) |
| `tutorials/research/mint-a-law.md` | watch a law get minted and survive the gauntlet | `research-mlopt:mlopt_discovery` mint machinery, `docs/mechanism.md` |
| `tutorials/research/run-the-scorecard.md` | regenerate `docs/scorecard.md`, read a row | `research-mlopt:bench`, `docs/scorecard.md` |

### How-to — per-repo groups

| page | purpose | provenance |
|---|---|---|
| `how-to/install-handl.md` … (6 existing) | handl toolchain recipes | docs: |
| `how-to/research/optimize-a-model.md` | `Optimizer`/`search` + runners + `engine=` | `research-mlopt:docs/api.md` (promote; api.md becomes this how-to) |
| `how-to/research/add-a-board.md` | write a `Domain` + `Board` | `research-mlopt:docs/public_api.md` (game + domain contracts) |
| `how-to/research/register-a-player.md` | `PlayerSpec` + registry | `research-mlopt:docs/public_api.md` |
| `how-to/research/admit-a-law.md` | `verify_law` → gauntlet → `MACHINE_SHIPPED` | `research-mlopt:docs/public_api.md`, AGENTS.md law-bank notes |

### Explanation — per-repo groups + cross-cutting

| page | purpose | provenance |
|---|---|---|
| `explanation/` (14 existing) | handl concepts | docs: |
| `explanations/` → merged into `explanation/` | handl design notes | docs: (dedupe `platform-architecture`, merge `crate-architecture` content) |
| `explanation/research/mechanism.md` | syntax → structure → search → certificate | `research-mlopt:docs/mechanism.md` |
| `explanation/research/evaluation.md` | the fourth dimension | `research-mlopt:docs/evaluation.md` |
| `explanation/cross-cutting/three-costs.md` | **the three costs** — `dag_cost` guess / measured pay / delivered measurement | `research-mlopt:docs/cost-model.md` |
| `explanation/cross-cutting/the-game.md` | boards, players, episodes, the learned policy loop | `research-mlopt:gamekit.engine`, `docs/results_player_on_board.md` |
| `explanation/cross-cutting/the-gauntlet.md` | numeric oracle → typed-pay gate → adversarial sweep → certificate | `research-mlopt:mlopt_discovery.verifier`, `docs/public_api.md` |
| `papers.md` (or `explanation/papers/`) | PAPER.md, SAE.md, `research-mlopt:docs/paper_draft.md` + `paper/` | docs: + repo pointers |

### Reference — bound to the frozen surface

| page | purpose | provenance |
|---|---|---|
| `reference/index.md` | per-repo index — handl groups (existing) **plus** a research group | docs: |
| `reference/kernel/`, `reference/host-tensor/` | generated from public siblings | generated (existing pipeline) |
| `reference/research/frozen-api.md` | the frozen surface, rendered — one section per destination tag (`eqsat`/`gamekit`/`graphopt`) | `research-mlopt:docs/public_api.md` — bind at `API_VERSION`; either vendored with a "synced at \<sha\>" header or generated by a script that reads the file |
| `reference/research/{scorecard,leaderboard,limits}.md` | the three generated tables, republished with their provenance headers | `research-mlopt:docs/{scorecard,leaderboard_players,limits_table}.md` (generated there, vendored here — **never hand-edited**) |
| `ADR-INDEX.md` | keep; add nav entry | generated (existing) |

The `reference/lib-*` sections are generated from private sibling repos
and 404 on the deployed site — either they move behind "internal"
marking, or `reference/index.md` only lists groups whose repos are
public. Cheap interim fix: mark them "(internal repo)" and accept the
local-only rendering; real fix belongs to the split.

## Sequencing (the update lane, phase 5.3+)

1. Cheap fixes now: stale `lab/`/crate paths, dead links
   (`project/adrs/*`, `../research/PAPER.md`, `../../docs/LANG.md`),
   missing index/sidebar entries, scaffold pages, README/api pointers.
2. Add the research skeleton: `tutorials/research/`, `how-to/research/`,
   `explanation/research/` + `cross-cutting/` stubs that *link out* to
   the repo docs rather than vendoring prose.
3. On phase-4 extraction: sweep `research-mlopt:` → `graphopt:`, split
   `frozen-api.md` by destination tag into `reference/eqsat/` +
   `reference/gamekit/` + `reference/graphopt/`.
