# The paradigm

Handl is a categorical language: computation is described as **arrows**,
not applied as functions.

In a functional language, you write `f(x)`: a function is applied to a
value, produces a value, and whatever effects it has are hidden inside the
closure. In Handl, you compose arrows: `f >>> g` feeds the output of one
computation into the next, `f &&& g` runs two computations side by side,
`f ||| g` chooses between them, and `loop` feeds output back as input. The
result is a structure you can inspect, not a black box you can only call.

## The closed arrow calculus

The kernel's computation model is a closed arrow calculus in the
Lindley-Wadler-Yallop tradition, extended with graded effects and
higher-categorical structure. Six combinators are enough:

- `arr`: lift a pure value into an arrow
- `>>>`: sequential composition
- `first`: apply an arrow to the first component of a pair
- `choice`: alternative composition (the `|||` surface form)
- `loop`: feedback
- `app`: application

No lambda, no variables-as-functions, no sugar hiding the structure. What
you see is what executes.

## Everything is data

The deeper bet is representation. Programs are 1-morphisms; laws and
rewrites are 2-morphisms; higher transformations extend the structure into
higher dimensions. Composition is dimension-indexed, with explicit
boundaries, rewriting rules, and coherence conditions, so higher-dimensional
structures compose consistently.

Because arrows are data, computation becomes:

- **inspectable**: you can read, diff, and search a program's structure
- **transformable**: rewrites and optimizations are themselves arrows
- **serializable**: an arrow survives a round trip through JSON, YAML, or
  any engine's memory model
- **interpretable**: tree-walk, bytecode, Cranelift, LLVM, Triton, and CUDA
  backends all consume the same representation

## Language as data

A language in Handl is not hardcoded into an engine. It is a declarative
`Language` value: syntax, grammar, AST shapes, evaluation schemes, type
rules, and transformations, described as data. Engines are generic
interpreters of that data, which is what makes new languages and new
backends cheap to add.

## Graded effects

Effects are first-class but disciplined. The kernel implements the Graded
Modal Sanada Arrow Calculus: operations carry grades, handlers interpret
them, and the grade system tracks what a computation is allowed to do.
Effects are algebraic (Sanada 2024) and handlers are where meaning is
supplied. Grades generalize further into **modes**: an MTT-style axis
where grades, coeffects, and effect rows are all mode-algebra instances
over ordinary data.

## Why it matters

Most language infrastructure forces a trade-off: expressiveness lives in
the syntax, but the semantics is locked inside a runtime you cannot
inspect. Handl removes the trade-off. The mathematics (arrows, effects,
handlers, higher categories) is the substrate; tooling, libraries, and
products are layers on top.

**Architectural principle:** the Kernel defines a compositional,
higher-categorical computational model. Engines interpret and transform its
representations. Libraries provide runtime-agnostic abstractions, while
Kits assemble them into usable environments. Tools bridge Handl with
external systems, and Hosts expose the ecosystem to users and development
environments.

For the full type system that sits on this substrate (dependent types,
cubical equality, effect signatures, and modes), see the
[type system overview](/learn/).

The [story](/story/) covers where this comes from; the
[bibliography](/ecosystem/bibliography) lists the papers; the
[ecosystem](/ecosystem/) shows how the repos fit together.
