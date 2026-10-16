# handl API Reference

## Platform

- [Host concepts](./host-concepts) — traits, types, and the plugin lifecycle for composable hosts.

## Standard library

- [Archive](./lib-archive) — Archive abstractions and entry types.
  - [Archive (Tar)](./lib-archive-tar) — TAR archive reader support.
- [Char](./strings-chars-unicode) — The `char`/`str`/`unicode` package map: contracts, impls, layer membership, backend swap.
- [Collections](./lib-collections) — Extended collection types for handl values.
- [Compress](./lib-compress) — Compression traits and error types.
  - [Compress (Gzip)](./lib-compress-gzip) — Gzip compression and decompression.
- [Crypto](./lib-crypto) — Cryptographic hash functions.
- [DateTime](./lib-datetime) — Date and time operations.
- [Encoding](./lib-encoding) — Text encoding utilities.
  - [Base64](./lib-base64) — Base64 encoding and decoding.
  - [Hex](./lib-hex) — Hexadecimal encoding and decoding.
- [HTTP Client](./lib-http-client) — HTTP client types and stubs.
  - [HTTP Client (Std)](./lib-http-client-std) — Standard-library HTTP client implementation.
- [HTTP Server](./lib-http-server) — HTTP server framework and types.
  - [HTTP Server (Std)](./lib-http-server-std) — Standard-library HTTP server runtime.
- [Intl](./lib-intl) — Internationalization and locale support.
- [IP](./lib-ip) — IP address, CIDR and socket types.
- [KV](./lib-kv) — Key/value store interface.
  - [KV (Hashmap)](./lib-kv-hashmap) — In-memory key/value store backend.
- [OS](./lib-os) — Operating-system interfaces for handl.
  - [OS (Std)](./lib-os-std) — Standard-library OS runtime bindings.
- [OTLP](./lib-otlp) — OpenTelemetry protocol support.
  - [OTLP (Std)](./lib-otlp-std) — Standard-library OTLP export backend.
- [Parse](./lib-parse) — Generic parser framework and types.
- [Random](./lib-rand) — Random value generation.
- [Serialize](./lib-serialize) — Serializer framework and traits.
  - [JSON](./lib-json) — JSON serializer for the handl runtime.
  - [TOML](./lib-toml) — TOML serializer for the handl runtime.
  - [YAML](./lib-yaml) — YAML serializer for the handl runtime.
- [Stats](./lib-stats) — Statistical functions.
- [Test](./lib-test) — Testing, assertion and benchmark helpers.
- [Unicode](./lib-unicode) — Unicode identifier and decode utilities.
- [URL (RFC 3986)](./lib-url-rfc) — Strict RFC 3986 URI parsing.
  - [URL (WHATWG)](./lib-url-whatwg) — WHATWG URL Standard parsing.
- [Utils](./lib-utils) — Standard utility modules for the handl runtime.
- [WebSocket](./lib-websocket) — WebSocket frame and message handling.
