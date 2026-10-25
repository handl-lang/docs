# docs — the `handl-lang` documentation hub

One place to find the platform's published docs — the kernel, the engines,
the composable host, and the research stack — plus every public repo's
project docs. This repo owns the **published** documentation surface; the
decision records themselves live with the repo that made them.

**Publication boundary.** Only **public** repos are published, and the allowlist
lives in exactly one place: [`scripts/public_repos.py`](scripts/public_repos.py)
(all three generators import it — they had drifted apart). Public today:
`kernel`, the `engine-*` family, `host`, `host-tensor`, `kit-prelude-lang`,
`egraph`, `discovery`, `graphopt`, `eqsat`, `gamekit`, `research-dts`,
`slidev-theme`, and this repo. `lib-char`, `lib-char-native`, `lib-desugar`,
`lib-loader` and `lib-str-handl` are public too but document the **unreleased
Handl language surface**, so they stay out until the language ships — add them
to that module when it does. Every other repo (`ext-*`, `kit-*` other than
`kit-prelude-lang`, `compile-*`, `host-cli`, `host-lsp`, …) is private and
produces no pages, links, or mentions.

## Layout

```
index.md, adrs/                                        the VitePress site (org level)
handl/                                                   generated reference output only
                                                         (gen_reference*.py writes
                                                         handl/reference/<repo>/;
                                                         gitignored — the Handl
                                                         product pages are vendored)
.vitepress/                                              site config + theme
vendored/                                                product docs vendored from
                                                         <repo>/docs/site/ (generated)
scripts/                                                 generators (see below)
project/                                                 project worktree (ADR-0129)
```

ADRs are **never** at a repo root — every repo keeps them on its `project`
branch under `project/adrs/`, and this hub publishes the aggregate.

The site's `srcDir` is the repo root; `README.md`, `project/**` and
`scripts/**` are excluded.

## Generated content

| script | output | source |
|---|---|---|
| `scripts/gen-docs-index.py` | `adrs/{index,handl,graphopt}.md` | every sibling's `project/adrs/` worktree + the `project` repo's retired-shell subtrees (+ `host/project/docs-split.yaml` for split/local metadata) |
| `scripts/gen_reference_all.py` | `handl/reference/<repo>/` + `reference.yaml` + `.vitepress/sidebar-reference.mjs` | every sibling repo's package sources — `handl-packages/<pkg>/`, `pkg.hnl`+`src/`, or `crates/<crate>/src/*.hnl` doc comments |
| `scripts/vendor-docs.py` | `vendored/<product>/` | each public product repo's `docs/site/` + `docs/site.yaml` |
| `scripts/vendor-docs.py` (sidebars) | `.vitepress/sidebar-products.mjs` | the vendored tree — one sidebar per product, so a repo that starts shipping `docs/site/` is navigable without editing `config.mjs` |
| `scripts/gen-api.sh` | `api/<repo>/` | each sibling repo's rustdoc (`cargo +nightly doc-md`, else `cargo doc`) |

Both are per-repo: the hub aggregates **public repos only** (the
`PUBLIC_REPOS` allowlist in each generator mirrors the Pages workflow's
`--visibility public` clone set). `handl/` and `api/` are gitignored —
`handl/` on disk holds only generated reference output; every
hand-written product page lives in its repo's `docs/site/` and is
vendored.

```bash
bun run docs:gen-ref     # regenerate the aggregated reference
bun run docs:gen-api     # collect per-repo rustdoc
bun run docs:dev         # local preview
bun run docs:build       # gen-api + gen-ref + vitepress build
```

## Where things live

| what | where |
|---|---|
| ADR indexes (published, per-product) | [`adrs/index.md`](adrs/index.md), [`adrs/handl.md`](adrs/handl.md), [`adrs/graphopt.md`](adrs/graphopt.md) |
| ADR registry (canonical) | `host/project/adrs/INDEX.md` |
| Project principles | `project/principles.md` (this repo's `project` branch) |
| A repo's own docs | that repo's `project` branch, mounted at `<repo>/project/` |

Every repo carries its own docs on a `project` orphan branch, mounted as a
worktree at `<repo>/project` (ADR-0129). `main` stays a clean build tree.
This repo publishes the aggregate.

## History

The site moved here from `host/docs` in ADR-0128 Phase 12 / ADR-0129 5.3.
