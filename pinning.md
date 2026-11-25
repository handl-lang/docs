# Dependency pinning & release convention (T-121)

Status: phase 1 — tags exist, convention documented. Fleet dep-pin
migration is phased (see [Migration](#migration)).

Companion to [structure.md](./structure.md) (repo map) and the
P-011 architecture section there.

## Problem

Every inter-repo dependency in the fleet is a git dep on
`branch = "main"` (`Cargo.toml` `[dependencies]`/`[patch]`,
`pyproject.toml` `[tool.uv.sources]`). Nothing records *which* commit a
consumer was built against, so the fleet floats: a green build today can
silently change tomorrow when a platform repo lands on `main`. There is
no reproducible pin and no release point to bump to deliberately.

Precedent: `kernelopt` and `mlopt-product` already pin
`[tool.uv.sources]` entries to `tag = "vX.Y.Z"` on `eqsat`, `gamekit`,
`mlopt-torch`, etc., and their AGENTS.md files state the rule: *"Bump the
pin deliberately."*

## Tag scheme

- Tags are `v<semver>` lightweight tags on `main` HEAD at release
  points: `git tag vX.Y.Z origin/main && git push origin vX.Y.Z`.
- Tags are **immutable once pushed** — never move or delete a published
  tag; cut the next patch instead (`v0.1.0` → `v0.1.1`).
- `0.x` tags track the crate `version` in `Cargo.toml` /
  `pyproject.toml`/`pkg.hnl` where one exists; when they diverge, the
  tag is authoritative for dep pins.
- A tag asserts "this commit is a known-good platform state" — cut it
  after the repo's gate (`bupha`/`ci.sh`, `pytest`, etc.) is green, not
  mid-flight.

### What gets tagged (platform-core first)

Phase-1 tagged set (all at `v0.1.0` unless noted):

- `kernel` — `handl-calculus`/`handl-language`/`handl-value`/`handl-ops`/`handl-ext`
- `engine`, `engine-eqsat`
- `exec`, `exec-tree-walk`, `exec-bytecode`, `exec-cranelift`
- `host`, `host-cli` (`v0.1.1` — `v0.1.0` predates this convention),
  `host-lsp`
- `tool-lex`, `tool-parse`, `tool-typecheck`, `tool-transform`,
  `tool-codegen`, `tool-codemod`, `tool-fmt`, `tool-lint`, `tool-test`
- `ext-eval`, `ext-typecheck`

Remaining `tool-*`/`exec-*`/`ext-*`/`host-*` repos, then `lib-*`,
`kit-*`, and the mlopt/tenant repos tag on the same scheme as they
stabilize. Tenants already using `v*` tags (`eqsat`, `gamekit`,
`mlopt-*`, `discoverykit`, `benchkit` per kernelopt/mlopt-product
`[tool.uv.sources]`) continue unchanged.

## Dep-pin forms

### Cargo

```toml
# canonical: tag selector
handl-language = { git = "https://github.com/handl-lang/kernel", tag = "v0.1.0" }

# equivalent for an immutable commit (what scripts/pin-git-revs.py emits)
handl-language = { git = "https://github.com/handl-lang/kernel", rev = "<full-sha>" }
```

Prefer `tag` for hand-maintained pins (readable, matches uv). `rev =
"<sha>"` is the machine-pinned form — `host/scripts/pin-git-revs.py`
already rewrites `branch = "main"` selectors to `rev` at release time
and `--check` reports drift; reproduce pinned builds with
`cargo build --locked`.

`branch = "main"` remains the day-to-day selector during active
development; `[patch]` tables keep resolving siblings from local
checkouts (ADR-0128), so local builds don't hit the network.

### uv / pyproject

```toml
[tool.uv.sources]
mlopt-core = { git = "https://github.com/handl-lang/eqsat.git",
               subdirectory = "packages/mlopt-core", tag = "v0.1.14" }
```

`tag` is preferred over `rev` here too. Note the kernelopt lesson:
declare each git-sourced package directly in `[project] dependencies`
so its `[tool.uv.sources]` entry actually applies — uv does not
always propagate sources to transitive-only requirements.

## The deliberate-bump rule

1. **Platform repos tag releases** — a tag is cut on green `main` HEAD.
2. **Consumers pin tags** — a consumer's manifest names a `vX.Y.Z` it
   was verified against.
3. **Bumps are explicit commits** — moving a pin from `v0.1.0` to
   `v0.1.1` is a deliberate, reviewable change in the consumer repo
   ("bump the pin deliberately"), never a side effect of `cargo update`
   or `uv lock` against `branch = "main"`.
4. **Breaking upstream changes surface as pin-bump diffs**, not silent
   main-float breakage — e.g. kernelopt binds the frozen
   `spec_domain`/`register_player` seam and an upstream break shows up
   as an import-time failure at bump time.

## Migration

- **Phase 1 (done, T-121):** `v0.1.0` tags exist on the platform-core
  repos above; this convention is documented; pilot consumer
  `tool-lex` pins `handl-language` to `tag = "v0.1.0"` (verified via
  `cargo metadata` — resolves `git+…/kernel?tag=v0.1.0`).
- **Phase 2:** high-value consumers pin — repos whose gates are
  load-bearing or that already pretend to be stable (`host`,
  `host-cli`, `host-lsp`, `kit-*`, `mlopt-product`, `kernelopt`
  already-pinned set). Each pin is an explicit commit per the rule
  above.
- **Phase 3:** fleet-wide — `lib-*`/`kit-*`/tenant manifests migrate
  from `branch = "main"` to tags repo-by-repo; `branch = "main"`
  remains only for repos still in active unscheduled flux.

Fleet-wide dep-URL rewriting is explicitly **out of scope** for T-121 —
tracked as a follow-up task in `project/TODO.md`.
