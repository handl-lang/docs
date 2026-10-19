# String, char, and Unicode package reference

The string stack is split across three concerns, each in its own package. Every package is either a **contract** (axioms, consumed by `parse_contracts`) or an **impl** (a runtime module, registered through `host`'s `plugin-lib-stdlib`).

## Package map

| Package | Kind | Layer | Language | Role |
| ------- | ---- | ----- | -------- | ---- |
| `char/` | contract | 2 — Unicode tables | handl axioms | The irreducible char-primitive floor. Declares `char.is_whitespace`, `char.is_alpha`, `char.is_numeric`, `char.is_alnum`, `char.to_upper`, `char.to_lower`, `char.to_title`, `char.code_point`, `char.from_code_point`, `char.at`, `char.slice`, `char.length`, `char.concat`. |
| `crates/plugin-lib-char-native` | impl | 2 — Unicode tables | Rust (`std::char`) | Backend for `char/` using Rust's embedded UCD subset. Root-locale, codepoint-level. Registered as the `"char"` module. |
| `str/` | contract | 1 — Algorithms | handl axioms | The 45 str-function contracts. `str.upper`, `str.trim`, `str.replace`, `str.levenshtein`, `str.word_wrap`, ... |
| `str-handl/` | impl | 1 — Algorithms | pure handl | Implements `str/` over `char/`; one file per arrow plus a test file (93 files). Registered as the `"str"` module. |
| `unicode/` | contract | 3 — ICU | handl axioms | Text-level Unicode contracts: `is_valid_identifier`, `is_xid_start`, `is_xid_continue`, `code_points`, `code_point_at`, `decode`, `graphemes`, `grapheme_count`, `width`, `casefold`, `nfc`, `nfd`. |
| `unicode-c/` | impl | 3 — ICU | handl over ICU4C FFI | Backend for `unicode/` on the host's `libicuuc`: `ubrk_*` (UAX #29), `unorm2_*` (UAX #15), `u_strFoldCase`, `u_hasBinaryProperty` (UAX #31), East Asian Width (UAX #11). Code-point interop and `decode` are pure handl and need no ICU. Registered as the `"unicode_c"` module. |
| `intl/` | contract | 3 — ICU | handl axioms | ECMA-402-style contracts (collation, number/date/list formatting, segmentation). |
| `intl-c/` | impl | 3 — ICU | handl over ICU4C FFI | Backend for `intl/` on the host's `libicui18n` + `libicuuc`. Registered as the `"intl_c"` module. |
| `time/` + `time-c/` + `time-stub/` | contract + impls | — | handl axioms + ICU4C FFI + pure handl | Clock contracts; `time-c` reads the host clock, `time-stub` returns deterministic zeros for tests and benchmarks. |

`unicode` and `intl` follow the same shape: **a contract package plus a C backend package**, with the runtime module named after the implementation (`unicode_c`, `intl_c`), not the contract. A contract's name is not a module name.

## Layer membership of the 45 str functions

All 45 live in `str-handl/` (Layer 1, pure handl). They call `char/` atoms for any per-character Unicode work.

| Function | Unicode atom it calls (Layer 2) |
| -------- | -------------------------------- |
| `upper`, `lower`, `capitalize`, `title_case` | `char.to_upper`, `char.to_lower` |
| `is_alpha`, `is_numeric`, `is_alphanumeric` | `char.is_alpha`, `char.is_numeric`, `char.is_alnum` |
| `trim`, `trim_start`, `trim_end`, `split_whitespace`, `lines`, `word_wrap`, `slugify` | `char.is_whitespace` |
| `snake_case`, `camel_case`, `pascal_case`, `kebab_case` | `char.is_alpha`, `char.to_lower`, `char.to_upper` |
| `char_at`, `slice`, `length`, `concat` | `char.at`, `char.slice`, `char.length`, `char.concat` |
| `reverse`, `repeat`, `pad_left`, `pad_right`, `strip_prefix`, `strip_suffix`, `split_at`, `truncate` | none (pure index/concat logic) |
| `contains`, `starts_with`, `ends_with`, `find`, `rfind`, `count`, `equals`, `is_empty` | none (pure comparison) |
| `split`, `join`, `replace`, `replace_first` | none (pure scan/replace) |
| `levenshtein`, `similarity` | none (pure DP over chars) |

## Module registration

Impl packages are registered in `host`'s `plugin-lib-stdlib` package table
(`crates/plugin-lib-stdlib/src/packages.rs`):

- `char` → `CharModule` (`plugin-lib-char-native`'s Rust `std::char` atoms).
- `str` → `build_str_handl_module()` (`handl_plugin_lib_handl::build_str_handl_module_with(&StdlibResolver, "tree-walk")`), re-exporting the per-arrow files in `STR_HANDL_SOURCES`. Replaces the former all-FFI `StrModule`.
- `unicode_c` → the `unicode_c` table module from `handl-packages/unicode-c`, built with `module_with` so `ffi`/`char`/`type`/`tag`/`error`/`math` resolve through the kit chain and the `../generated/icu-uc-c-linux-x86_64/*` adapter imports resolve through the table.
- `intl_c` → the `intl_c` table module, same shape.

Contract packages (`char/`, `str/`, `unicode/`, `intl/`) are **not** registered. They are consumed by `plugin-ext-refinement::parse_contracts` and live as the source of truth for the inference engine.

## Backend swap

The contract is the stable interface; the backend is a registration. Two independent swap points:

1. **The ICU layer** (`unicode_c`, `intl_c`) — a different FFI backend can satisfy the same contract. A `unicode-js` backend would use `Intl.Segmenter`, `String.prototype.normalize`, and `\p{ID_Start}` regex classes; callers of `unicode_c` would repoint one import. The code-point interop ops are already backend-neutral (pure handl), so only the table-dependent ops need porting.
2. **The `char` floor** — `char/`'s axioms are the interface; repointing the `char` registration from `CharModule` to another `char` backend changes Unicode/ASCII semantics without touching `str-handl/` or any caller.

## What was deleted

- `handl-packages/utils/str.hnl` — the 45-op FFI monolith.
- `crates/plugin-lib-utils/src/str/` — the 45 `rust_str_*` algorithm impls and the `StrModule` registration. The per-char Unicode lookups inlined inside them were extracted into the `char` floor, not deleted.
- `crates/plugin-lib-unicode-native` — the ICU4X-backed `unicode` ops. Replaced by `unicode-c` (host ICU4C over the generic FFI surface), so the `hnl` binary no longer links ICU4X.
- `handl-packages/unicode-handl` — the coarse pure-handl fallback (code-point `graphemes`/`width`, no `nfc`/`nfd`). Its exact subset is now pure handl inside `unicode-c`, and the table-dependent ops come from ICU4C; a coarse fallback is silently wrong off ASCII, so the contract prefers a loud failure.
- `crates/plugin-lib-unicode` — the `UnicodeLibraryPlugin` the kit `LibraryRegistry` exposed as the `unicode` library.

## Related

- [Why strings, chars, and Unicode live in three layers](../explanation/strings-chars-unicode-layers) — the design rationale.
