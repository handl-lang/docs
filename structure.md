# handl-lang repo structure

~185 repos under `github.com/handl-lang`, checked out as siblings in `~/GitHub/handl-lang/`. Deps are git deps (`branch = "main"`); workspace-root `[patch]` tables resolve them from sibling checkouts (ADR-0128). The public subset is the docs hub's `PUBLIC_REPOS` allowlist (`docs/scripts/public_repos.py`).

## Core layers (bare)

- `host` — runtime, loaders, `plugin-lib-*`/`plugin-ext-*` internals, `plugin-lib-stdlib` (the library-as-data registry)
- `kernel` — `handl-language`, `handl-value`, `handl-ext`, `defining-handl` (self-hosting, ADR-0044 Phase 8), plus substrate ops: `prim`, `prim-handl`, `ops`, `bytes`, `cmp`, `error`, `obj`, `type`, `mood`, `combinators`
- `docs` `automation` `assets` — org-level purpose repos
- `graphopt` `eqsat` `gamekit` `kernelopt` `discovery` `egraph` — the research/product repos (public: `graphopt`, `eqsat`, `gamekit`, `discovery`, `egraph`)
- `c` `web` `research-dts` — public target/research repos (not checked out locally)
- `slidev-theme` `pitch-*` `extension-{neovim,vscode}` — theme, pitch decks, editor extensions

## `engine-*` (16)

`engine` · `engine-{lex,lex-pattern,parse,parse-pratt,exec,exec-tree-walk,exec-bytecode,exec-cranelift,fmt,lint,test,transform,transform-rewrite,typecheck,typecheck-nbe}`

## `compile-*` (7)

`compile-{dot,handl,js,llvm,sexp,term,triton}`

## `sdkgen-*` (5)

`sdkgen-{c,python,webidl,file,cli}` — backends/emitters; generated FFI bindings vendor under `handl-packages/generated/` in the consuming repo (multi-consumer bindings get own repos: `lib-libc`, `lib-curl`, `lib-libz`). `sdkgen-cli` generates SDKs that wrap command-line tools (backend `cli`: `*.clispec.yaml` spec or live `--help` probe; emitter `hnl-cli` → adapters on `lib-cli`'s `cli-c` process-spawn runtime); generated CLI SDKs are committed as spec+gate repos with `generated/` gitignored (`lib-gh`, `lib-cli-gen` for multi-tool SDKs).

## `host-*` (3)

`host-{cli,lsp,tensor}`

## `ext-*` (10)

`ext-{compile,eval,fmt,kit,lint,plugin,sdkgen,test,transform,typecheck}` — `hnl` extensions (`libhnl_ext_*.so` discovered via `HANDL_EXT_DIR`/`~/.handl/ext`).

## `lib-*` (116)

**Rule: one package per repo — `.hnl` codebases only, no Rust** (crates are const-only `*_HNL` exporters; native access via `handl-plugin-ffi`).

- **Ports** (contracts): `lib-concurrent`, `lib-compress`, `lib-fetch`, `lib-ws`, `lib-tls`, `lib-serve`, `lib-ws-frame`, `lib-str`, `lib-math`, `lib-time`, `lib-cli` (two modules — `cli` port + `cli-c` libc backend), …
- **Impls**: `lib-<port>-<backend>` — `lib-time-c`, `lib-str-handl`, `lib-math-js`, `lib-concurrent-epoll`, `lib-fetch-c`, `lib-fetch-js`, `lib-ws-c`, `lib-tls-libssl`, `lib-compress-{gzip,zlib}-c`, `lib-cli` (`cli-c`), …
- **Runtime internals**: `lib-loader`, `lib-desugar`, `lib-tag` (embedded by host crates via `*_HNL` consts)
- **FFI surfaces**: `lib-types` (`types/c/*` aliases), `lib-libc`, `lib-curl`, `lib-libz` (sdkgen bindings)
- `pkg.hnl` declares `{ deps, modules }`; dep keys map to `handl-lang/lib-<dep>`.

## `kit-*` (11)

`kit-{core,data-prelude,ffi,kernel-ir,lang,pkg,prelude,prelude-lang,server,stdlib,test}` — kit declarations and kit infrastructure. `kit-prelude-lang` + `kit-data-prelude` carry the canonical language definition (language-as-data, the successor to the retired `kit-data-canonical`); the rest are kit manifests/manifests-as-data over `lib-*` packages.

## Retired

`meta` (folded into `kernel/crates/defining-handl`), `kit-data-canonical` (crate now lives in `kit-data-prelude`), `kit-canonical` (superseded by the `kit-*` family), `stdlib` (archived — folded into `host/crates`), `bench`, `playground`, `project` (docs moved to per-repo `project` branches, ADR-0129).

## `tool-*`

`tool-archhelper` (at `~/GitHub/9aia`)

## Rules

- Naming: the family prefix *is* the component kind — `engine-*` (language-operation engines), `lib-*` (stdlib `.hnl` packages), `kit-*` (kit declarations/infra), `compile-*` (emitters), `ext-*` (`hnl` dynamic extensions), `host-*` (host binaries), `sdkgen-*` (binding/SDK generators)
- Bare = core layer or purpose repo (host/kernel/docs/…)
- `prefix-*` = one component kind per repo
- Sole-consumer generated bindings vendor into the consumer's `handl-packages/generated/`
- `lib-{port}` = interface contract; `lib-{port}-{impl}` = backend
