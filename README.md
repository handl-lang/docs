# docs — the `handl-lang` documentation hub

One place to find the platform's published docs — the kernel, the engines,
the composable host, and the research stack — plus every public repo's
project docs. This repo owns the **published** documentation surface; the
decision records themselves live with the repo that made them.

**Publication boundary.** Public repos are published, and the allowlist lives in
exactly one place: [`scripts/public_repos.py`](scripts/public_repos.py) (all three
generators import it — they had drifted apart). That is **every public repo** (204 today):
`kernel`, the `engine`/`engine-eqsat` + `exec-*`/`tool-*` operation families, `host`, `host-tensor`, the `c`
and `web` targets, `research-mlopt` (published under the `mlopt` slug — formerly
`graphopt`/`mlopt` until its `docs/site.yaml` `site_path` flipped), `eqsat`, `gamekit`, `kit-prelude-lang`,
`egraph`, `discovery`, `research-dts`, `slidev-theme-handl`, `lib-char`,
`lib-char-native`, `lib-desugar`, `lib-loader`, `lib-str-handl`, the `ext-*`/`tool-compile-*`/`tool-codegen-*` families,
`host-cli`, the `kit-*`/`lib-*` package repos, and this
repo. Membership rule: public on GitHub. (An earlier
revision withheld the `lib-*` repos on the theory that the language surface was
unreleased; publishing docs for a public repo cannot disclose more than its
source does, so they are in.) Repos still private (`host-lsp`, `extension-*`, `pitch-*`,
`project`, `playground`, …) produce no pages, links, or
mentions.

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
project/                                                 project worktree
```

ADRs are **never** at a repo root — every repo keeps them on its `project`
branch under `project/adrs/`, and this hub publishes the aggregate.

The site's `srcDir` is the repo root; `README.md`, `project/**` and
`scripts/**` are excluded.

## Generated content

| script | output | source |
|---|---|---|
| `scripts/gen-docs-index.py` | `adrs/{index,handl,mlopt,eqsat,gamekit}.md` | every sibling's `project/adrs/` worktree + the `project` repo's retired-shell subtrees (+ `host/project/docs-split.yaml` for split/local metadata) |
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
bun run docs:gen-ref     # regenerate the aggregated reference (parked, see below)
bun run docs:gen-api     # collect per-repo rustdoc (parked, see below)
bun run docs:dev         # local preview
bun run docs:build       # vendor + vitepress build
```

Note: `handl/reference/` and `api/` output is currently **generated but
not published**: both trees are gitignored and `srcExclude`d in
`.vitepress/config.mjs`, and `sidebar-reference.mjs` is not wired into
the nav. Treat the reference/api pipeline as parked until it is
connected (or drop `docs:gen-ref`/`docs:gen-api` from
`scripts/deploy-pages.sh`).

## Where things live

| what | where |
|---|---|
| ADR indexes (published, per-product) | [`adrs/index.md`](adrs/index.md), [`adrs/handl.md`](adrs/handl.md), [`adrs/mlopt.md`](adrs/mlopt.md) |
| ADR registry (canonical) | `host/project/registry/INDEX.md` |
| Project principles | `project/principles.md` (this repo's `project` branch) |
| A repo's own docs | that repo's `project` branch, mounted at `<repo>/project/` |

Every repo carries its own docs on a `project` orphan branch, mounted as a
worktree at `<repo>/project`. `main` stays a clean build tree.
This repo publishes the aggregate.

## License

MIT.
