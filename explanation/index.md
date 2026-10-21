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

## Design notes

Older design notes live in `explanations/` (a merge into this section is
planned — see `DESIGN.md`):

- [Library API design principles](../explanations/ac-lib-api-design-principles)
- [Crate architecture](../explanations/crate-architecture)
- [Design principles](../explanations/design-principles)
- [Naming: "fields" not "keys"](../explanations/fields-not-keys)
- [Name explanation](../explanations/lang-name)
- [Per-workspace language variants](../explanations/per-workspace-language-variants)
- [Platform architecture (earlier draft)](../explanations/platform-architecture)
- [handl and other polyglot runtimes](../explanations/polyglot-runtimes)
- [Why the language kernel is small](../explanations/small-kernel)
- [VS Code extension constraints](../explanations/vscode-extension-constraints)

## When to use another section

- If you are new to handl, start with [Tutorials](../tutorials/getting-started).
- For practical instructions, see [How-to guides](../how-to/).
- For function and API listings, see the [Reference](../reference/).
