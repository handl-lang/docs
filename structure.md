# handl-lang repo structure

## Architecture — platform / tenant / edge (P-011, accepted 2026-11-24)

```
PLATFORM (this toolchain — the product)
  categorical IR + verified-rewrite machinery (laws, e-graph,
  minted records, gauntlet admission — proof-carrying rewrites)
  toolchain: engine/exec/tool/ext · lib/kit · tensor runtime · host

TENANTS (domains built ON the platform — applications, not families)
  mlopt stack: eqsat (substrate) · gamekit (RL players) ·
  mlopt-{discovery,carriers,torch,pipeline,product} · kernelopt ·
  discoverykit · research-mlopt · bench

EDGES (foreign runtimes ↔ platform)
  tool-codegen-* emitters + generated typed surfaces
  (python→hnl SDK gen, hnl→python compile — both directions)
  + thin runtime shims (e.g. kit-mlopt's `python -m mlopt stage`
  JSON protocol — hnl orchestrates, python measures)
```

Conventions:

- **Prefix = ecosystem role, never language/content** — `.hnl` is the only language target; language-named cohorts (`kit-python`) are the bug P-010 audits.
- **Domain machinery stays in domain repos** — only ports/contracts promote to toolchain (catalog: project T-119).
- **Edges are generated, not hand-written** — foreign surfaces become typed hnl decls via `tool-codegen-*`; thin shims only where the foreign side is runtime-coupled (torch autograd/CUDA). `interop-*` as a family was scaffolding.
- **Native components pair with `.hnl` specs** — `lib-tensor` (spec) ↔ native impl is the pattern: spec gives rewrites structure, impl gives speed.
- **Compilers**: `tool-compile-{handl,js,llvm,dot,sexp,term,tensor}` = canonical/debug targets; `tool-compile-{cuda,triton,python}` = performance/interop exits. LLVM is the escape hatch; verified-rewrite integration only exists in own backends.

~200 repos under `github.com/handl-lang`, checked out as siblings in `~/GitHub/handl-lang/` (202 local checkouts). Deps are git deps (`branch = "main"`); workspace-root `[patch]` tables resolve them from sibling checkouts (ADR-0128). The public subset is the docs hub's `PUBLIC_REPOS` allowlist (`docs/scripts/public_repos.py`).

## Core layers (bare)

- `host` — runtime, loaders, `plugin-lib-*`/`plugin-ext-*` internals, `plugin-lib-stdlib` (the library-as-data registry)
- `kernel` — `handl-calculus` (`Term`/`Model`), `handl-language`, `handl-value`, `handl-ops` (op ABI), `handl-ext`, `defining-handl` (self-hosting corpus, ADR-0044 Phase 8), plus the remaining substrate ops: `ops`, `prim`, `prim-handl` (the rest of the floor libs — `bytes`, `cmp`, `combinators`, `error`, `mood`, `obj`, `type` — are their own `lib-*` repos)
- `docs` `workspace` `assets` — org-level purpose repos (`workspace` absorbed the retired `automation` repo)
- `research-mlopt` `eqsat` `gamekit` `kernelopt` `discovery` `egraph` `mlopt-product` — the research/product repos (public: `research-mlopt`, `eqsat`, `gamekit`, `discovery`, `egraph`)
- `c` `web` `research-dts` — public target/research repos (not checked out locally)
- `slidev-theme-handl` `pitch-*` `extension-{neovim,vscode}` — theme, pitch decks, editor extensions
- `discoverykit` `source-onnx` `test` — additional bare repos (Python discovery package, ONNX tooling, test crate)

## `engine-*` / `exec-*` / `tool-*` (the operation layer)

`engine` · `engine-eqsat` stay `engine-*` — the genuine engines (the `hnl-engine`
arrow-calculus substrate and the e-graph search engine). Everything else split:

- `exec` · `exec-{tree-walk,bytecode,cranelift}` — the eval backends (`hnl-exec*`)
- `tool-{lex,lex-pattern,parse,parse-pratt,transform,transform-rewrite,typecheck,typecheck-handl,typecheck-nbe,fmt,lint,test,watch,codemod}` — the on-demand toolchain instruments (`hnl-tool-*`)

plus the emitters below.

## `tool-compile-*` (10)

`tool-compile-{cuda,dot,handl,js,llvm,python,sexp,tensor,term,triton}`

## `tool-codegen-*` (9)

`tool-codegen-{aten,c,cli,ffi,file,onnx,openapi,python,webidl}` — backends/emitters; generated FFI bindings vendor under `handl-packages/generated/` in the consuming repo (multi-consumer bindings get own repos: `lib-libc`, `lib-curl`, `lib-libz`). `tool-codegen-cli` generates SDKs that wrap command-line tools (backend `cli`: `*.clispec.yaml` spec or live `--help` probe; emitter `hnl-cli` → adapters on `lib-cli`'s `cli-c` process-spawn runtime); generated CLI SDKs are committed as spec+gate repos with `generated/` gitignored (`lib-gh`, `lib-cli-gen` for multi-tool SDKs).

## `host-*` (2+)

`host-{cli,lsp}` (+ `host-tensor` native component pending rename per P-010/P-011)

## `ext-*` (11)

`ext-{codegen,codemod,compile,eval,fmt,kit,lint,plugin,test,transform,typecheck}` — `hnl` extensions (`libhnl_ext_*.so` discovered via `HANDL_EXT_DIR`/`~/.handl/ext`).

## `lib-*` (120)

**Rule: one package per repo — `.hnl` codebases only, no Rust** (crates are const-only `*_HNL` exporters; native access via `handl-plugin-ffi`).

- **Ports** (contracts): `lib-concurrent`, `lib-compress`, `lib-fetch`, `lib-ws`, `lib-tls`, `lib-serve`, `lib-ws-frame`, `lib-str`, `lib-math`, `lib-posix` (incl. the folded `lib-time` clock surface), `lib-cli` (two modules — `cli` port + `cli-c` libc backend), …
- **Impls**: `lib-<port>-<backend>` — `lib-posix-c` (clock impl folded in from `lib-time-c`), `lib-str-handl`, `lib-math-js`, `lib-concurrent-epoll`, `lib-fetch-c`, `lib-fetch-js`, `lib-ws-c`, `lib-tls-libssl`, `lib-compress-{gzip,zlib}-c`, `lib-cli` (`cli-c`), …
- **Runtime internals**: `lib-loader`, `lib-desugar`, `lib-tag` (embedded by host crates via `*_HNL` consts)
- **FFI surfaces**: `lib-types` (`types/c/*` aliases), `lib-libc`, `lib-curl`, `lib-libz` (codegen bindings)
- `pkg.hnl` declares `{ deps, modules }`; dep keys map to `handl-lang/lib-<dep>`.

## `kit-*` (10) + mlopt cohort

`kit-{cli-app,cuda,host-tensor,onnx,pkg,py-smoke,test,web-browser-interop,web-server,web-worker-interop}` — kit declarations and kit infrastructure. The mlopt domain packages were renamed `kit-*`→`mlopt-*` (P-010 cohort migration, in flight): `mlopt-{carriers,discovery,pipeline,product,torch}` plus tenant repos `eqsat`, `gamekit`, `kernelopt`, `discoverykit`, `research-mlopt`, `bench`. `kit-{cuda,host-tensor,onnx}` await the same dissolution (blocked on parity work).

## Retired

`meta` (folded into `kernel/crates/defining-handl`), `kit-data-canonical` (crate now lives in `kit-data-prelude`), `kit-canonical` (superseded by the `kit-*` family), `stdlib` (archived — folded into `host/crates`), `playground`, `ext-sdkgen` (dead after PL-004), `lib-grade` (retired — `Grade` promoted to the `type` surface, T-113). `bench` and `project` are live again (tenant repo / ledger repo respectively).

## `tool-*`

`tool-archhelper` (at `~/GitHub/9aia`)

## Rules

- Naming: the family prefix *is* the component kind — `engine-*`/`exec-*`/`tool-*` (language-operation engines, exec backends, and on-demand toolchain instruments), `lib-*` (stdlib `.hnl` packages), `kit-*` (kit declarations/infra), `tool-compile-*` (emitters), `ext-*` (`hnl` dynamic extensions), `host-*` (host binaries), `tool-codegen-*` (binding/SDK generators)
- Bare = core layer or purpose repo (host/kernel/docs/…)
- `prefix-*` = one component kind per repo
- Sole-consumer generated bindings vendor into the consumer's `handl-packages/generated/`
- `lib-{port}` = interface contract; `lib-{port}-{impl}` = backend
