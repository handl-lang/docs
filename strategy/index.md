# Strategy

Where Handl is going, what it is for, and the values that shape every
decision in the ecosystem.

## Vision

A programming ecosystem where the mathematics is the substrate. Computation
as arrows, not functions; programs, laws, coherence, and effects as data
you can inspect, rewrite, and execute. Language infrastructure that tools,
libraries, and products can build on without inheriting a hidden runtime.

## Mission

Build **handl-lang**: a modular language infrastructure around a closed
arrow calculus with globular higher-categorical structure.

- The **kernel** defines the computational foundation: arrow calculus, IR,
  value representation, and language schema.
- **Engines** interpret and transform the shared representation:
  compilation, execution, rewriting, and language processing.
- **Libraries** (`lib-*`) provide runtime-agnostic abstractions in
  separate repositories.
- **Kits** (`kit-*`) assemble libraries, engines, and components into
  ready-to-use environments.
- **Tools** (SDK generators, CLI/WebIDL bridges) connect Handl to external
  systems.
- **Hosts** (CLI, LSP) and **extensions** (VS Code, Neovim) expose the
  platform to users and editors.

One principle holds the stack together: composition over application, and
inspectable structure over hidden closures.

See the [paradigm](/paradigm/) for what the calculus buys you and the
[ecosystem](/ecosystem/) for how the repos fit together.

## Values

- **Composition over application.** Arrows compose; nothing needs to be
  unwrapped to be understood.
- **Inspectable structure over hidden closures.** If a tool cannot see it,
  it is not part of the model.
- **The mathematics is the spec.** Laws, coherence, and graded effects are
  data, not folklore in a paper.
- **Runtime independence.** Libraries do not know which engine runs them;
  engines do not know which library called them.
- **Honest work in progress.** Incomplete, unreviewed, and subject to
  change is stated plainly, not hidden behind confidence.

## Where it leads

The same foundation that describes a language also describes its tools,
its libraries, and its products. Research projects like
[research-mlopt](https://github.com/handl-lang/mlopt) are early proof that the
substrate carries real workloads, not just notation.
