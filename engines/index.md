# Engines

Handl engines are **pluggable implementations of the language operations** — lex,
parse, transform, typecheck and eval. A language definition is *data*; an engine
interprets that data. Swapping an engine therefore changes how a language runs,
not what it means.

Every operation follows the same shape: a small **abstraction** crate owns the
contract (`§` marker type, request, trait, shared helpers) and one or more
**engine** crates implement it. The kit decides which engine fills each slot.

## The five operations

| operation | contract | engines |
|---|---|---|
| lex | [engine-lex](/engine-lex/) | [engine-lex-pattern](/engine-lex-pattern/) — data-driven rules |
| parse | [engine-parse](/engine-parse/) | [engine-parse-pratt](/engine-parse-pratt/) — Pratt, grammar rows |
| transform | [engine-transform](/engine-transform/) | [engine-transform-rewrite](/engine-transform-rewrite/) — rule-interpreting |
| typecheck | [engine-typecheck](/engine-typecheck/) | `engine-typecheck-nbe` (NBE; private) + bootstrap in the contract crate |
| eval | [engine-exec](/engine-exec/) | [engine-exec-tree-walk](/engine-exec-tree-walk/) — reference; [engine-exec-bytecode](/engine-exec-bytecode/) — stack VM |

## Shared substrate

- [engine](/engine/) — `Term`, `Model`, and the arena view every engine uses.

## How to read a crate here

Each engine repo publishes the same four quadrants: an **overview** (what it is),
**reference** (the public API), **how-to** (task recipes) and **explanation**
(why it is shaped that way). They carry no tutorials — end-to-end walkthroughs
belong to the product that composes them, the
[Handl platform](/handl/).

## Design invariant

The reference interpreter is the oracle: `engine-exec-bytecode` must produce
results **identical** to `engine-exec-tree-walk`, and its conformance suite
enforces that. Optimisation is allowed to change speed, never meaning. The same
rule holds for the other operations — a data-driven engine must not become a
second definition of the language.
