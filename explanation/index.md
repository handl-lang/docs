# Explanations

Explanations help you understand _why_ handl works the way it does. They are background reading, not step-by-step instructions.

## The language

- [What is handl?](./what-is-handl) — the language's purpose and philosophy.
- [Language overview](./language-overview) — values, expressions, functions, and modules.
- [Runtime](./runtime) — how handl expressions are executed.

## The platform

- [Platform architecture](./platform-architecture) — the crate layers and how they compose.
- [The composable host](./composable-host) — why the platform is built around a single plugin model.
- [Plugins, rules, and operations](./plugins-rules-operations) — how `Plugin`, `RuleAcceptor`, `Operation`, and `Behavior` fit together.
- [Kits and manifests](./kits-and-manifests) — how kits curate plugins and defaults.
- [Options and configuration](./options-and-configuration) — how options are defined, resolved, and used.
- [Security and trust](./security-and-trust) — threat model and recommended practices.

## The calculus

- [The arrow calculus kernel](./arrow-calculus-kernel) — why the six-combinator set is closed.
- [Graded algebraic theory](./graded-algebraic-theory) — the theoretical frame behind the platform.
- [Graded Modal Sanada Arrow Calculus](./graded-modal-sanada-arrow-calculus) — arrows + grades + Sanada's handlers, the canonical execution calculus.

## The standard library

- [Why strings, chars, and Unicode live in three layers](./strings-chars-unicode-layers) — why the string stack is split into algorithms (handl), Unicode tables (Rust floor), and ICU (future swappable backend).

## Papers and background

- [Platform overview](../overview) — the plugin/host model at a glance.
- [The language](../LANG) — the object/arrow kernel's core forms.
- [The runtime](../RUNTIME) — how a host evaluates expressions.
- [Arrow-First Language Kernel](../PAPER) — the kernel paper.
- [Staged Arrow Engines](../SAE) — stackless spatial execution for the kernel's resolvable fragment.
- [Arrow support vs arrow-native](../comparison) — how handl compares to Haskell and other arrow-capable languages.
- [Cross-repo ADR index](../ADR-INDEX) — every decision record, aggregated.

## The research stack (graphopt)

The `graphopt` repo (renamed from `research-mlopt`) — the
categorical optimizer and law-discovery engine:

- [The research stack](./research/) — the section landing, with the rename note.
- [How mlopt works](./research/mechanism) — syntax → structure → search → certificate.
- [Evaluation: the fourth dimension](./research/evaluation) — describe, rank, measure — never decide equivalence.

## Cross-cutting

Concepts that cross repo boundaries:

- [The three costs](./cross-cutting/three-costs) — `dag_cost` guesses, fixtures measure, the verifier proves.
- [The game](./cross-cutting/the-game) — boards, players, episodes, and the learned-policy loop.
- [The gauntlet](./cross-cutting/the-gauntlet) — what a minted law must survive to ship.

## Design notes

Older design notes, merged here from the retired `explanations/` directory:

- [Library API design principles](./ac-lib-api-design-principles)
- [Design principles](./design-principles)
- [Naming: "fields" not "keys"](./fields-not-keys)
- [Name explanation](./lang-name)
- [Per-workspace language variants](./per-workspace-language-variants)
- [handl and other polyglot runtimes](./polyglot-runtimes)
- [Why the language kernel is small](./small-kernel)
- [VS Code extension constraints](./vscode-extension-constraints)

## When to use another section

- If you are new to handl, start with [Tutorials](../tutorials/getting-started).
- For practical instructions, see [How-to guides](../how-to/).
- For function and API listings, see the [Reference](../reference/).
