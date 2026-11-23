# Engines

Handl engines are **pluggable implementations of the language operations** — lex,
parse, transform, typecheck and eval. A language definition is *data*; an engine
interprets that data. Swapping an engine therefore changes how a language runs,
not what it means.

Every operation follows the same shape: a small **abstraction** crate owns the
contract (`§` marker type, request, trait, shared helpers) and one or more
**engine** crates implement it. The kit decides which engine fills each slot.

This section covers the `engine-*` family only. The wider org families —
`tool-compile-*` (emitters), `ext-*` (`hnl` extensions), most `kit-*`,
`host-cli`/`host-lsp`, `tool-codegen-*` and most `lib-*` — are private; the
public exceptions (`host-tensor`, `kit-prelude-lang`, `lib-char`,
`lib-char-native`, `lib-desugar`, `lib-loader`, `lib-str-handl`) have
their own sections. See the [platform architecture](/handl/explanation/platform-architecture)
for the full repo map.

Two private repos landed recently and are named here so the family map
stays honest:

- `engine-eqsat` — the e-graph **search** interpretation over kernel
  `Term`s (ADR-0174 phase P2, contracts per ADR-0177). It is an engine
  in the same sense as the exec backends — saturation and extraction
  over `hnl_engine::Term` via `handl-egraph`, with `optimize` /
  `saturate` / `extract_best` as the public surface and laws, guards,
  and cost specs moving to kit data.
- `tool-compile-cuda` — an `tool-compile-*` emitter (a compiler
  backend, outside this section's engine scope) that lowers `lib-kernel-ir` terms to real CUDA C++:
  one templated `__global__` kernel plus an `extern "C"` launcher,
  declining uncovered ops by name rather than emitting stubs.

## The five operations

| operation | contract | engines |
|---|---|---|
| lex | [tool-lex](/tool-lex/) | [tool-lex-pattern](/tool-lex-pattern/) — data-driven rules |
| parse | [tool-parse](/tool-parse/) | [tool-parse-pratt](/tool-parse-pratt/) — Pratt, grammar rows |
| transform | [tool-transform](/tool-transform/) | [tool-transform-rewrite](/tool-transform-rewrite/) — rule-interpreting |
| typecheck | [tool-typecheck](/tool-typecheck/) | `tool-typecheck-nbe` (NBE; private) + bootstrap in the contract crate |
| eval | [exec](/exec/) | [exec-tree-walk](/exec-tree-walk/) — reference; [exec-bytecode](/exec-bytecode/) — stack VM; [exec-cranelift](/exec-cranelift/) — JIT/object (see Tools) |

## Shared substrate

- [engine](/engine/) — `Term`, `Model`, and the arena view every engine uses.

## Tools

These are `engine-*` repos that are **not** operation slots — they are
rule-based tools over the same `Language` data:

| tool | what it does |
|---|---|
| [tool-fmt](/tool-fmt/) | data-driven AST formatter (`FormattingRule` / `PostProcessRule` seams) |
| [tool-lint](/tool-lint/) | rule-based linter (`lang.lints` + named native checks) |
| [exec-cranelift](/exec-cranelift/) | Cranelift eval backend (JIT / object file) |

`tool-test` is the test runner; it stays private while its corpus harness
depends on the private kit closure.

## How to read a crate here

Each engine repo publishes the same four quadrants: an **overview** (what it is),
**reference** (the public API), **how-to** (task recipes) and **explanation**
(why it is shaped that way). They carry no tutorials — end-to-end walkthroughs
belong to the product that composes them, the
[Handl platform](/handl/).

## Design invariant

The reference interpreter is the oracle: `exec-bytecode` must produce
results **identical** to `exec-tree-walk`, and its conformance suite
enforces that. Optimisation is allowed to change speed, never meaning. The same
rule holds for the other operations — a data-driven engine must not become a
second definition of the language.
