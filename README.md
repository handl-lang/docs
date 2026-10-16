# docs — the `handl-lang` documentation hub

One place to find the language, the platform, and every repo's project docs.
This repo owns the **published** documentation surface; the decision records
themselves live with the repo that made them.

## Layout

```
index.md, tutorials/, how-to/, explanation/, reference/   the VitePress site
.vitepress/                                              site config + theme
ADR-INDEX.md                                             published ADR index
adrs/                                                    pre-split top-level ADRs
scripts/                                                 generators (see below)
project/                                                 project worktree (ADR-0129)
```

The site's `srcDir` is the repo root; `README.md`, `project/**` and
`scripts/**` are excluded.

## Generated content

| script | output | source |
|---|---|---|
| `scripts/gen_reference_all.py` | `reference/<repo>/` + `reference.yaml` + `.vitepress/sidebar-reference.mjs` | every sibling repo's `handl-packages/*.hnl` doc comments |
| `scripts/gen-api.sh` | `api/<repo>/` | each sibling repo's rustdoc (`cargo +nightly doc-md`, else `cargo doc`) |

Both are per-repo: the hub aggregates. `reference/` and `api/` are gitignored
except the three hand-written reference pages (`index.md`,
`host-concepts.md`, `strings-chars-unicode.md`).

```bash
bun run docs:gen-ref     # regenerate the aggregated reference
bun run docs:gen-api     # collect per-repo rustdoc
bun run docs:dev         # local preview
bun run docs:build       # gen-api + gen-ref + vitepress build
```

## Where things live

| what | where |
|---|---|
| ADR index (published, cross-repo) | [`ADR-INDEX.md`](ADR-INDEX.md) |
| ADR registry (canonical) | `platform/project/adrs/INDEX.md` |
| Project principles | `project/principles.md` (this repo's `project` branch) |
| A repo's own docs | that repo's `project` branch, mounted at `<repo>/project/` |

Every repo carries its own docs on a `project` orphan branch, mounted as a
worktree at `<repo>/project` (ADR-0129). `main` stays a clean build tree.
This repo publishes the aggregate.

## History

The site moved here from `platform/docs` in ADR-0128 Phase 12 / ADR-0129 5.3.
