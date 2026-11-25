# Libraries

`lib-*` is the largest family in the ecosystem — 130+ repositories of
reusable Handl code. The organizing rule is the **port/impl split**:

- A **port** (`lib-<name>`) is a contract — `.hnl` signatures, axioms,
  and laws every backend must satisfy. Ports are pure data + arrow
  declarations; they never pick a runtime.
- An **impl** (`lib-<name>-<backend>`) satisfies the contract for one
  backend: `-c` over the C FFI, `-js` over the JS interop surface,
  `-handl` as a pure-`.hnl` implementation, `-stub` as a deterministic
  fallback.

One package per repo, `.hnl` sources only — Rust appears solely as
const-only `*_HNL` exporter crates that embed the sources. Each repo
carries a `pkg.hnl` manifest declaring `{ deps, modules }`; dep keys map
to `handl-lang/lib-<dep>` git deps.

## Language and runtime internals

The substrate libraries the host and plugins embed:

| Repo | What it is |
|---|---|
| [lib-loader](https://github.com/handl-lang/lib-loader) | The pure-handl module loader |
| [lib-desugar](https://github.com/handl-lang/lib-desugar) | The `desugar` transform pass source |
| [lib-tag](https://github.com/handl-lang/lib-tag) | Tagged-value helpers |
| [lib-kernel-ir](https://github.com/handl-lang/lib-kernel-ir) | The kernel IR as data — 21 ops with signatures, grades, costs, torch denotations |
| [lib-types](https://github.com/handl-lang/lib-types) | FFI type-alias declarations shared by codegen bindings |
| [lib-ffi](https://github.com/handl-lang/lib-ffi) | FFI decls — `Errno`, call surface |
| [lib-lang-lex](https://github.com/handl-lang/lib-lang-lex) · [lib-lang-parse](https://github.com/handl-lang/lib-lang-parse) · [lib-lang-typecheck](https://github.com/handl-lang/lib-lang-typecheck) · [lib-lang-eval](https://github.com/handl-lang/lib-lang-eval) · [lib-lang-compile](https://github.com/handl-lang/lib-lang-compile) · [lib-lang-run-compiled](https://github.com/handl-lang/lib-lang-run-compiled) | The `lex`/`parse`/`typecheck`/`eval`/`compile`/`run_compiled` meta functions as composable `plugin-lib-*` leaves |
| [lib-js](https://github.com/handl-lang/lib-js) | JavaScript interop surface — `JS` grade, typed call/invoke/await arrows |
| [lib-utils](https://github.com/handl-lang/lib-utils) | Aggregate capability surface (`bool`, `math`, `str` modules) |

## Core values and combinators

| Repo | What it is |
|---|---|
| [lib-option](https://github.com/handl-lang/lib-option) · [lib-result](https://github.com/handl-lang/lib-result) | `Option` / `Result` types |
| [lib-cmp](https://github.com/handl-lang/lib-cmp) | Comparison predicates — eq/lt/gt/clamp/min/max/compare |
| [lib-mood](https://github.com/handl-lang/lib-mood) | Mood (mode-of-data) operations |
| [lib-obj](https://github.com/handl-lang/lib-obj) | Record introspection — keys/values/entries |
| [lib-type](https://github.com/handl-lang/lib-type) · [lib-type-handl](https://github.com/handl-lang/lib-type-handl) | The `type` capability surface + `dependent` indexed families; pure-handl predicates/kind guards |
| [lib-error](https://github.com/handl-lang/lib-error) | `error.raise` primitive |
| [lib-event](https://github.com/handl-lang/lib-event) | User-space event emission + listener registration |
| [lib-pred](https://github.com/handl-lang/lib-pred) · [lib-comb](https://github.com/handl-lang/lib-comb) | Predicate/filter and combinator libraries |
| [lib-query](https://github.com/handl-lang/lib-query) · [lib-command](https://github.com/handl-lang/lib-command) | User-space query/command registration and invocation algebras |
| [lib-mri](https://github.com/handl-lang/lib-mri) | Minimal argv parser (npm `mri` semantics, pure handl) |
| [lib-dedent](https://github.com/handl-lang/lib-dedent) | Multi-line text dedenting |
| [lib-encoding](https://github.com/handl-lang/lib-encoding) | Codec port — `Encoder`/`Decoder`/`Encoding` traits |
| [lib-base64](https://github.com/handl-lang/lib-base64) · [lib-hex](https://github.com/handl-lang/lib-hex) | Base64 / hex codecs over `lib-encoding` |
| [lib-bytes](https://github.com/handl-lang/lib-bytes) | Byte-buffer primitives for the `Bytes` scalar |
| [lib-arrow-iter](https://github.com/handl-lang/lib-arrow-iter) | Arrow iteration over sequences |
| [lib-perlin](https://github.com/handl-lang/lib-perlin) · [lib-simplex](https://github.com/handl-lang/lib-simplex) | Perlin / simplex noise |
| [lib-stats](https://github.com/handl-lang/lib-stats) | `sum`/`avg`/`median`/`stddev` over collections |
| [lib-transform](https://github.com/handl-lang/lib-transform) | Transform utilities |
| [lib-collections](https://github.com/handl-lang/lib-collections) | `vec`/`list`/`queue`/`stack`/`deque`/`hash_map`/`hash_set`/`array`, shipped as sources |
| [lib-crypto](https://github.com/handl-lang/lib-crypto) | `sha1`/`sha256`/`md5` as pure-`.hnl` arrows |
| [lib-archive](https://github.com/handl-lang/lib-archive) · [lib-tar](https://github.com/handl-lang/lib-tar) | Archive reading / tar |
| [lib-kv](https://github.com/handl-lang/lib-kv) · [lib-kv-hashmap](https://github.com/handl-lang/lib-kv-hashmap) · [lib-kv-map](https://github.com/handl-lang/lib-kv-map) | Key-value store trait + `HashMap` backend + pure-functional map |
| [lib-mock](https://github.com/handl-lang/lib-mock) · [lib-test](https://github.com/handl-lang/lib-test) | Spies/stubs/mocks; assert/property/fuzz/snapshot test framework |
| [lib-hello](https://github.com/handl-lang/lib-hello) | The `greet` arrow — canonical first package |

## Text, locale, and time

| Repo | What it is |
|---|---|
| [lib-str](https://github.com/handl-lang/lib-str) | `str` port contract — axioms every backend must satisfy |
| [lib-str-handl](https://github.com/handl-lang/lib-str-handl) · [lib-str-c](https://github.com/handl-lang/lib-str-c) · [lib-str-js](https://github.com/handl-lang/lib-str-js) | Pure-handl / C-ICU / JavaScript backends |
| [lib-char](https://github.com/handl-lang/lib-char) · [lib-char-native](https://github.com/handl-lang/lib-char-native) | Character axioms contract; native `std::char` backend |
| [lib-unicode](https://github.com/handl-lang/lib-unicode) · [lib-unicode-c](https://github.com/handl-lang/lib-unicode-c) | Unicode port + backend |
| [lib-intl](https://github.com/handl-lang/lib-intl) · [lib-intl-c](https://github.com/handl-lang/lib-intl-c) | Intl port; ICU4C backend over codegen bindings |
| [lib-datetime](https://github.com/handl-lang/lib-datetime) | Date/time port |

## Numbers and noise

| Repo | What it is |
|---|---|
| [lib-math](https://github.com/handl-lang/lib-math) | Math surface contracts |
| [lib-math-handl](https://github.com/handl-lang/lib-math-handl) · [lib-math-c](https://github.com/handl-lang/lib-math-c) · [lib-math-js](https://github.com/handl-lang/lib-math-js) | Pure-handl / native / JS backends |
| [lib-tensor](https://github.com/handl-lang/lib-tensor) · [lib-tensor-native](https://github.com/handl-lang/lib-tensor-native) | `.hnl` tensor-op spec (transparent) ↔ native `f64` n-d array backend (opaque atoms) |
| [lib-noise](https://github.com/handl-lang/lib-noise) | Noise port types |
| [lib-noise-handl](https://github.com/handl-lang/lib-noise-handl) · [lib-noise-c](https://github.com/handl-lang/lib-noise-c) · [lib-noise-stub](https://github.com/handl-lang/lib-noise-stub) | Pure-handl / C / stub backends |

## Serialization and formats

| Repo | What it is |
|---|---|
| [lib-serialize](https://github.com/handl-lang/lib-serialize) | Format-agnostic `Serializer`/`Encoder`/`Decoder` port |
| [lib-json](https://github.com/handl-lang/lib-json) | JSON codec + `json.parse`/`stringify` over `lib-serialize` traits |
| [lib-json-handl](https://github.com/handl-lang/lib-json-handl) · [lib-json-c](https://github.com/handl-lang/lib-json-c) · [lib-json-js](https://github.com/handl-lang/lib-json-js) | Pure-handl / C-FFI / JS backends |
| [lib-serialize-toml-c](https://github.com/handl-lang/lib-serialize-toml-c) · [lib-serialize-yaml-c](https://github.com/handl-lang/lib-serialize-yaml-c) | Native TOML / YAML serializer backends |
| [lib-url-rfc](https://github.com/handl-lang/lib-url-rfc) · [lib-url-whatwg](https://github.com/handl-lang/lib-url-whatwg) | URL parsers for the `parse` port — RFC and WHATWG dialects |

## System, process, and CLI

| Repo | What it is |
|---|---|
| [lib-posix](https://github.com/handl-lang/lib-posix) | POSIX.1-2017 contract — fd ops, path, env, time, fs |
| [lib-posix-c](https://github.com/handl-lang/lib-posix-c) · [lib-posix-stub](https://github.com/handl-lang/lib-posix-stub) | C backend / deterministic stub |
| [lib-stdio](https://github.com/handl-lang/lib-stdio) | Standard-stream I/O contract |
| [lib-stdio-c](https://github.com/handl-lang/lib-stdio-c) | libc backend via `ffi.call` |
| [lib-proc](https://github.com/handl-lang/lib-proc) | Process identity contract — `argv`/`exit`/`pid` |
| [lib-cli](https://github.com/handl-lang/lib-cli) | Child-process spawn contract + `cli-c` libc backend |
| [lib-cli-router](https://github.com/handl-lang/lib-cli-router) | CLI ergonomics — compiler + segment trie + `{out,state}` pipeline |
| [lib-command](https://github.com/handl-lang/lib-command) | Command registration/invocation algebra (see Core values) |
| [lib-gh](https://github.com/handl-lang/lib-gh) | Generated handl SDK for the GitHub CLI (`gh.clispec.yaml` is the source of truth) |
| [lib-cli-gen](https://github.com/handl-lang/lib-cli-gen) | Multi-tool generated SDKs — `git`, `docker`, `ffmpeg`, `kubectl`, `aws` |
| [lib-curl](https://github.com/handl-lang/lib-curl) · [lib-libc](https://github.com/handl-lang/lib-libc) · [lib-libz](https://github.com/handl-lang/lib-libz) | Codegen-generated FFI bindings (ports + `c-linux-x86_64` adapters) |

## Networking and serving

| Repo | What it is |
|---|---|
| [lib-fetch](https://github.com/handl-lang/lib-fetch) | `fetch` port — WinterCG-style request/response |
| [lib-fetch-c](https://github.com/handl-lang/lib-fetch-c) · [lib-fetch-js](https://github.com/handl-lang/lib-fetch-js) | libcurl / WebIDL backends |
| [lib-ws](https://github.com/handl-lang/lib-ws) | `ws` port — RFC 6455 client step-surface |
| [lib-ws-c](https://github.com/handl-lang/lib-ws-c) | libcurl-transport WebSocket client for `concurrent-epoll` |
| [lib-ws-whatwg-c](https://github.com/handl-lang/lib-ws-whatwg-c) · [lib-ws-whatwg-wasm](https://github.com/handl-lang/lib-ws-whatwg-wasm) | WHATWG WebSocket surfaces for C / wasm-JS hosts |
| [lib-ws-frame](https://github.com/handl-lang/lib-ws-frame) · [lib-ws-frame-handl](https://github.com/handl-lang/lib-ws-frame-handl) | RFC 6455 frame contract + pure-handl codec |
| [lib-tls](https://github.com/handl-lang/lib-tls) · [lib-tls-libssl](https://github.com/handl-lang/lib-tls-libssl) | TLS step-surface contract; nonblocking libssl primitives |
| [lib-serve](https://github.com/handl-lang/lib-serve) · [lib-serve-epoll](https://github.com/handl-lang/lib-serve-epoll) | HTTP server around a fetch-shaped handler; epoll accept loop |
| [lib-http-rfc](https://github.com/handl-lang/lib-http-rfc) | HTTP/1.1 wire codec in pure handl |
| [lib-route](https://github.com/handl-lang/lib-route) | Transport-agnostic routing + middleware pipeline |
| [lib-http-router](https://github.com/handl-lang/lib-http-router) | HTTP routing layer between `serve` and handler arrows |
| [lib-http-middleware](https://github.com/handl-lang/lib-http-middleware) · [lib-http-ratelimit](https://github.com/handl-lang/lib-http-ratelimit) · [lib-http-static](https://github.com/handl-lang/lib-http-static) | Onion middleware, rate limiting, static file serving |
| [lib-http-openapi](https://github.com/handl-lang/lib-http-openapi) | OpenAPI 3.0.x spec generator over handl records |
| [lib-msg-router](https://github.com/handl-lang/lib-msg-router) | Message/event-envelope dispatcher |
| [lib-ip](https://github.com/handl-lang/lib-ip) | IP address, CIDR, socket primitives |
| [lib-concurrent](https://github.com/handl-lang/lib-concurrent) | Cooperative concurrency contract (step-arrow model) |
| [lib-concurrent-epoll](https://github.com/handl-lang/lib-concurrent-epoll) · [lib-concurrent-js](https://github.com/handl-lang/lib-concurrent-js) | epoll scheduler / JS isomorphic backend |
| [lib-otlp](https://github.com/handl-lang/lib-otlp) | OpenTelemetry/OTLP module surface |
| [lib-otlp-c](https://github.com/handl-lang/lib-otlp-c) · [lib-otlp-std](https://github.com/handl-lang/lib-otlp-std) | Native OTLP exporter / `ureq`-based HTTP exporter |

## Compression

| Repo | What it is |
|---|---|
| [lib-compress](https://github.com/handl-lang/lib-compress) | Compression contract — codec types + backend laws |
| [lib-compress-gzip-c](https://github.com/handl-lang/lib-compress-gzip-c) · [lib-compress-zlib-c](https://github.com/handl-lang/lib-compress-zlib-c) | gzip (zlib `gz*`) / raw-deflate backends over `libz` |

Adding a library follows the same rule as adding a language: declare
the contract as a port, ship at least one impl, and let `pkg.hnl` deps
carry the wiring. The [kits](/ecosystem/kits) curate these into
ready-to-use environments.
