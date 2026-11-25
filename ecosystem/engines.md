# Engines

Engines are the pluggable implementations of Handl's language operations.
A language definition is *data* — syntax, grammar, AST shapes, eval
schemes, and type rules live in `Language` records, not in engine code.
An engine interprets that data, so swapping one changes how a language
runs, not what it means.

Every operation follows the same shape: a small **abstraction** crate
owns the contract (marker type, request, trait, shared helpers) and one
or more **engine** crates implement it. The kit decides which engine
fills each slot.

## The operations

| Operation | Contract | Engines |
|---|---|---|
| lex | `tool-lex` | `tool-lex-pattern` — data-driven rules |
| parse | `tool-parse` | `tool-parse-pratt` — Pratt, grammar rows |
| transform | `tool-transform` | `tool-transform-rewrite` — rule-interpreting |
| typecheck | `tool-typecheck` | `tool-typecheck-nbe` — normalization by evaluation |
| eval | `exec` | `exec-tree-walk` (reference), `exec-bytecode` (stack VM), `exec-cranelift` (JIT/object) |

Two further families sit alongside: `tool-compile-*` lowers `Term`s to
concrete targets (see [Compiler backends](#compiler-backends)), and the
`ext-*` crates package the same operations as dynamic `hnl` extensions
(see [Extensions](/ecosystem/extensions)).

## Shared substrate

- [engine](https://github.com/handl-lang/engine) — `Term`, `Model`, and
  the arena view every engine uses.
- [engine-eqsat](https://github.com/handl-lang/engine-eqsat) — the
  e-graph **search** interpretation over kernel `Term`s: saturation and
  extraction via `handl-egraph`, with laws, guards, and cost specs as
  kit data.

## Tooling instruments

The `tool-*` family beyond the five core operations:

- [tool-fmt](https://github.com/handl-lang/tool-fmt) — data-driven AST
  formatter; renders an `Ast` using only language data, no hardcoded
  kinds.
- [tool-lint](https://github.com/handl-lang/tool-lint) — rule-based
  linter over a `lang.lints` table plus named native checks.
- [tool-test](https://github.com/handl-lang/tool-test) — bootstrap test
  runner: discovery, tag/filter predicates, scheduling.
- [tool-watch](https://github.com/handl-lang/tool-watch) —
  cross-platform filesystem watcher: typed events, filters, debounce.
- [tool-codemod](https://github.com/handl-lang/tool-codemod) — the
  spec/model layer of the declarative codemod engine.

## Compiler backends

`tool-compile-*` emitters lower Handl `Term` arrow graphs to concrete
targets. Canonical/debug targets round-trip the IR itself; the
performance targets emit real code.

| Repo | Target |
|---|---|
| [tool-compile-term](https://github.com/handl-lang/tool-compile-term) | `Term` JSON — canonical form |
| [tool-compile-handl](https://github.com/handl-lang/tool-compile-handl) | Handl source (Hughes arrow dialect) |
| [tool-compile-sexp](https://github.com/handl-lang/tool-compile-sexp) | S-expressions |
| [tool-compile-dot](https://github.com/handl-lang/tool-compile-dot) | Graphviz DOT graphs |
| [tool-compile-js](https://github.com/handl-lang/tool-compile-js) | JavaScript |
| [tool-compile-llvm](https://github.com/handl-lang/tool-compile-llvm) | LLVM IR — the escape hatch to native code |
| [tool-compile-triton](https://github.com/handl-lang/tool-compile-triton) | Triton kernels (GPU) |
| [tool-compile-cuda](https://github.com/handl-lang/tool-compile-cuda) | CUDA C++ — templated `__global__` + `extern "C"` launcher |

Emitters decline uncovered ops by name rather than emitting stubs — a
compile failure is explicit, never silent.

## References

The design lineage is academic: equality saturation comes from the
e-graph literature (egg/egglog), normalization-by-evaluation from the
type-checking literature, and Pratt/precedence parsing from classical
parser theory. See the [bibliography](/ecosystem/bibliography) for the
foundations; implementation-specific references are collected under
"Tooling and implementation" there.
