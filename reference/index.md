# handl API Reference

The reference is generated per repo (`scripts/gen_reference_all.py`) —
each section below links into `reference/<repo>/`, one entry per `lib-*`
package repo, kernel substrate crate, or `handl-packages/` package.

## Platform

- [Host concepts](./host-concepts) — traits, types, and the plugin lifecycle for composable hosts.
- [Tensor](./host-tensor/host-tensor) — host-side dense n-d tensor functions (f64, row-major).

## Kernel substrate (`kernel` repo)

- [Prim](./kernel/lib-prim) — the minimal atom layer for handl's arrow-based stdlib.
- [Bytes](./kernel/lib-bytes) — byte-buffer primitives for the `Bytes` scalar type.
- [Cmp](./kernel/lib-cmp) — deep equality / total ordering.
- [Combinators](./kernel/lib-combinators) — function combinator utilities.
- [Error](./kernel/lib-error) — the error-raising primitive contract.
- [Mood](./kernel/lib-mood) — mood (mode-of-data) operations.
- [Obj](./kernel/lib-obj) — record introspection primitives.
- [Type](./kernel/lib-type) — type coercion, predicates, and utilities.

## Research stack (`research-mlopt` → `graphopt`)

The frozen public surface of the research stack — bound to
`research-mlopt:docs/public_api.md` (`API_VERSION = "0.1.0"`):

- [The frozen API](./research/frozen-api) — the contracts the repo split must not break, tagged per destination repo (`eqsat`/`gamekit`/`graphopt`).
- [Discovery scorecard](./research/scorecard) — can the engine derive each named optimization, certify it, and beat the registered floor? *(generated upstream, vendored)*
- [Player leaderboard](./research/leaderboard) — every registered player on every board under one paired protocol. *(generated upstream, vendored)*
- [Limits table](./research/limits) — the delivered form vs every registered baseline, honest losses included. *(generated upstream, vendored)*

## Contracts and implementations (`lib-*` repos — internal)

::: warning Internal — links are local-only
This section is generated from **private** sibling `lib-*` repos. The
deployed site clones public repos only, so every link below **404s on
the published site** and renders only in a local checkout. The real
fix (publish or drop the section) belongs to the repo split.
:::

- [Base64](./lib-base64/lib-base64) — base64 encoding/decoding.
- [Char](./strings-chars-unicode) — the `char`/`str`/`unicode` package map: contracts, impls, layer membership, backend swap.
  - [Char](./lib-char/lib-char) · [Char (native)](./lib-char-native/lib-char-native)
- [Collections](./lib-collections/lib-collections) — vec/list/queue/stack/deque/hash_map/hash_set/array.
- [Comb](./lib-comb/lib-comb) — call a function with an array of arguments.
- [Compress](./lib-compress/lib-compress) — compression contract.
  - [Gzip (C)](./lib-compress-gzip-c/lib-compress-gzip-c) · [Zlib (C)](./lib-compress-zlib-c/lib-compress-zlib-c)
- [Concurrent](./lib-concurrent/lib-concurrent) — cooperative concurrency contract (step-arrow model).
  - [Epoll](./lib-concurrent-epoll/lib-concurrent-epoll)
- [Crypto](./lib-crypto/lib-crypto) — SHA-256 and friends.
- [Dedent](./lib-dedent/lib-dedent) — strip a shared leading-whitespace prefix.
- [Encoding](./lib-encoding/lib-encoding) — generic encoding to/from string forms.
- [Fetch](./lib-fetch/lib-fetch) — HTTP client contract (WinterCG `fetch` surface).
  - [fetch-c](./lib-fetch-c/lib-fetch-c) · [fetch-js](./lib-fetch-js/lib-fetch-js)
- [FFI](./lib-ffi/lib-ffi) — objects and arrows for foreign function calls.
- [Grade](./lib-grade/lib-grade) — the `Grade` kind for effect-graded arrows.
- [Hex](./lib-hex/lib-hex) — hexadecimal encoding/decoding.
- [HTTP (RFC)](./lib-http-rfc/lib-http-rfc) — HTTP/1.1 wire codec in pure Handl.
- [Intl](./lib-intl/lib-intl) — internationalization contract.
  - [Intl (C/ICU)](./lib-intl-c/lib-intl-c)
- [IP](./lib-ip/lib-ip) — IP address, CIDR and socket types.
- [JS](./lib-js/lib-js) — grades, types and arrows for JavaScript interop.
- [KV (Hashmap)](./lib-kv-hashmap/lib-kv-hashmap) — in-memory key/value store.
- [Math](./lib-math/lib-math) — numeric surface.
  - [math-c](./lib-math-c/lib-math-c) · [math-handl](./lib-math-handl/lib-math-handl)
- [Noise](./lib-noise/lib-noise) — deterministic lattice-noise contract.
  - [Perlin](./lib-perlin/lib-perlin) · [Simplex](./lib-simplex/lib-simplex)
- [Option](./lib-option/lib-option) — Option type and constructors.
- [OS](./lib-os-c/lib-os-c) — libc-backed OS primitives.
  - [OS (stub)](./lib-os-stub/lib-os-stub)
- [OTLP](./lib-otlp/lib-otlp) — OpenTelemetry protocol support.
  - [OTLP (std)](./lib-otlp-std/lib-otlp-std)
- [Parse](./lib-parse/lib-parse) — generic string parsing.
- [Query](./lib-query/lib-query) — user-space query algebra. Also: [Command](./lib-command/lib-command), [Event](./lib-event/lib-event).
- [Rand](./lib-rand/lib-rand) — randomness generation contract.
  - [rand-c](./lib-rand-c/lib-rand-c)
- [Result](./lib-result/lib-result) — Result type and constructors.
- [Serialize](./lib-serialize/lib-serialize) — generic serialization to/from strings.
- [Serve](./lib-serve/lib-serve) — HTTP server around a fetch-shaped handler.
  - [serve-epoll](./lib-serve-epoll/lib-serve-epoll)
- [Stats](./lib-stats/lib-stats) — canonical statistical aggregates.
- [Str](./lib-str/lib-str) — the string contract.
  - [str-handl](./lib-str-handl/lib-str-handl)
- [Tag](./lib-tag/lib-tag) — tagged values (host capability).
- [Tar](./lib-tar/lib-tar) — pack `{path, contents}` objects into a base64 tar archive.
- [Tensor (spec)](./lib-tensor/lib-tensor) — transparent `.hnl` spec of the `tensor.*` surface.
- [Test](./lib-test/lib-test) — assertion, benchmark, fuzz, property, snapshot helpers.
- [Time](./lib-time/lib-time) — wall-clock and monotonic clocks.
  - [time-c](./lib-time-c/lib-time-c) · [time-stub](./lib-time-stub/lib-time-stub)
- [TLS](./lib-tls/lib-tls) — nonblocking TLS contract.
  - [tls-libssl](./lib-tls-libssl/lib-tls-libssl)
- [Transform](./lib-transform/lib-transform) — sequence transforms.
- [Type (indexed families)](./lib-type/lib-type) — dependent structure (ADR-0120).
- [Types](./lib-types/lib-types) — transparent aliases for the C type vocabulary.
- [Unicode](./lib-unicode/lib-unicode) — unicode contract.
  - [unicode-c](./lib-unicode-c/lib-unicode-c)
- [URL (RFC 3986)](./lib-url-rfc/lib-url-rfc) — strict URI parsing.
  - [URL (WHATWG)](./lib-url-whatwg/lib-url-whatwg)
- [Utils](./lib-utils/lib-utils) — boolean utilities.
- [UUID](./lib-uuid/lib-uuid) — unique identifier generation.
- [WebSocket](./lib-ws/lib-ws) — WebSocket client contract (RFC 6455).
  - [ws-c](./lib-ws-c/lib-ws-c) · [ws-frame](./lib-ws-frame/lib-ws-frame) · [ws-frame-handl](./lib-ws-frame-handl/lib-ws-frame-handl) · [ws-whatwg-c](./lib-ws-whatwg-c/lib-ws-whatwg-c)
