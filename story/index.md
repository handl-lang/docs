# The story of Handl

How a line of research in category theory became a programming language
infrastructure, and where Handl picks it up.

## A short history of arrows

The lineage below runs left to right: monads and premonoidal categories
converge on Hughes's arrows, which then split into a syntax-sugar branch
and a categorical-semantics branch before Sanada's work on effects and
handlers funnels everything into Handl. Click any node for the details of
that era.

<StoryGraph />

See the full [bibliography](/ecosystem/bibliography).

## Where Handl picks up

Every step above stayed inside a host language: arrows were syntax sugar in
Haskell, effects were a thin layer, and the interesting structure (laws,
rewrites, graded effects) was invisible to tools.

Handl inverts that. The arrow calculus isn't syntax over something else; it
**is the IR**. Programs are 1-morphisms, laws and rewrites are
2-morphisms, and transformations are data like everything else. That gives
us:

- **Inspectable computation**: arrows serialize, diff, and transform.
- **Language as data**: a `Language` is declarative syntax + grammar +
  eval scheme + type rules, not hardcoded engine logic.
- **Graded effects**: the Graded Modal Sanada Arrow Calculus, with graded
  operations and handlers.
- **Interchangeable engines**: lex, parse, transform, typecheck, exec
  (tree-walk, bytecode, Cranelift, LLVM, Triton, CUDA) all consume the same
  representation.

The vision: a language infrastructure where the mathematics is the
substrate, and everything (tools, libraries, hosts, products) is built
on top of it.

- [The paradigm](/paradigm/): what the calculus buys you.
- [The Handl ecosystem](/ecosystem/): how the repos fit together.
