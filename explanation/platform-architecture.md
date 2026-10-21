# Platform architecture

The handl platform is a workspace of Rust crates organised around one goal: every concept in the language is a `Plugin`, and every tool is a `Host` that composes plugins.

## Crate layers

```text
handl-host-cli, handl-host-lsp     # executable hosts
handl-ext-fmt, handl-ext-lint,    # concrete operations
  handl-ext-lexer, handl-ext-parser,
  hnl-engine-typecheck, handl-ext-cli,
  handl-ext-lsp, handl-ext-doc,
  handl-ext-eval
handl-plugin-*                    # rule and library plugins
handl-kit-*                       # curated kit manifests
handl-target-*                    # runtime targets
handl-platform                    # Plugin, Host, and composition primitives
```

| Layer            | Responsibility                                                                                                          |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `handl-platform` | `Host`, `Plugin`, `RuleAcceptor`, `Operation`, `Behavior`, `ContributionContext`, `Options`, `AstNode`, and resolution. |
| `handl-ext-*`    | Concrete operations such as `Format`, `Lint`, `Parser`, `Lexer`, `Typecheck`, `Eval`, `Cli`, `Lsp`, and `Doc`.          |
| `handl-plugin-*` | Rule plugins that contribute `Behavior`s and `OptionSchema`s, and library plugins that register more plugins.           |
| `handl-kit-*`    | Curated manifests of plugins and default option values. A kit is not executable.                                        |
| `handl-target-*` | Target plugins that register runtime backends.                                                                          |
| `handl-host-*`   | Executable hosts that load kits and execute `Cli` or `Lsp` capabilities.                                                |

## The per-crate map

The layer table is the contract; the concrete crates fill it in:

| Crate/module                    | Responsibility |
| ------------------------------- | -------------- |
| `handl-platform`                | `Host`, `Plugin`, `RuleAcceptor`, `Operation`, `Behavior`, `ContributionContext`, `Options`, `AstNode`, `DataTypes`, resolution, manifests. |
| `handl-ext-fmt`                 | `Format` operation, `FormatBehavior`, `FormatContext`, `BasicFormatter` `RuleAcceptor` plugin. |
| `handl-ext-lint`                | `Lint` operation, `LintBehavior`, `LintContext`, `BasicLinter` `RuleAcceptor` plugin. |
| `handl-ext-lexer`               | `Lexer` operation, `LexerBehavior`, `BasicLexer` `RuleAcceptor` plugin. |
| `handl-ext-parser`              | `Parser` operation, `ParserBehavior`, `BasicParser` `RuleAcceptor` plugin. |
| `hnl-engine-typecheck`          | Typecheck abstraction: `Typecheck` operation marker, `TypecheckRequest`/`TypecheckResult`, `TypecheckEngine` trait, `check_module` entry point. Engine impl: `hnl-engine-typecheck-handl` (Handl-authored model, ADR-0105). |
| `handl-ext-eval`                | `Eval` operation, `EvalBehavior`, `EvalContext`. |
| `handl-target-rust-interpreter` | Default `Eval` interpreter `RuleAcceptor` target plugin. |
| `handl-ext-doc`                 | `Doc` operation, `DocBehavior`, `BasicDoc` `RuleAcceptor` plugin. |
| `handl-ext-cli`                 | `Cli` operation, `CliCommand`, `BasicCli` `RuleAcceptor` plugin. |
| `handl-ext-lsp`                 | `Lsp` operation, `LspHandler`, `BasicLsp` `RuleAcceptor` plugin. |
| `handl-plugin-lib-*`            | `Library` plugins that register the standard library pieces. |
| `handl-target-*`                | `Target` plugins that register runtime backends (e.g. `handl-target-wasm`, `handl-target-llvm`, `handl-target-js-native`, `handl-target-rust-interpreter`). |
| `handl-plugin-*`                | Rule plugins that contribute `Behavior`s and `OptionSchema`s to operations. |
| `handl-kit-*`                   | Curated manifest of plugins and default option overrides (not an executable) (e.g. `handl-kit-prelude`, `handl-kit-server`, `handl-kit-sandbox`). |
| `handl-kit-prelude-lang`        | The canonical eval-path `Language` as data — YAML fragment merge (`tokens`/`grammar`/`eval`/`types`/`ast`/`caps`/`options`/`lexer_rules`/`transforms`/`globals`) for consumers that only lex/parse/desugar/eval `.hnl`. `handl-kit-data-prelude` composes it and layers the tooling fragments (`lints`, `lsp`) + kit manifests on top. |
| `handl-host-cli`                | Executable `Host` that loads multiple kits, applies excludes, and runs `Cli`. |
| `handl-host-lsp`                | Executable `Host` that loads multiple kits, applies excludes, and runs `Lsp`. |

## Plugins are the only unit

`handl-platform` does not distinguish between a component, an extension, a library, a target, and a capability. The only real distinction is whether a plugin implements `RuleAcceptor` and, if so, what rule it accepts. `handl-plugin-*` crates contribute rules; `handl-kit-*` crates curate sets of plugins; `handl-host-*` crates run them.

## Why this split

The platform crate intentionally stays small. It defines the composition primitives and nothing else. Concrete operations, library rules, and targets live in separate crates because they can be added, swapped, or excluded without changing the core. This lets a host be as small as a formatter or as large as a language server.

A new crate is added only when it represents a distinct dependency or consumer boundary. If two crates are always consumed together, they belong in one crate. If one can be used without the other, they stay split. Every crate boundary should correspond to a real dependency, target, or consumer boundary.

Because the platform layer is the only shared contract, dependency direction is always clear, and new operations and commands can be added in new `handl-ext-*` or `handl-plugin-*` crates without changing `handl-platform`. Tools share the same composition model, from the CLI to the LSP server to the test runner.

## The host as composer

A `Host` starts empty and ends as a fully composed tool. It does this by:

1. Loading `HostConfig` from a `HostApplier`.
2. Merging kit manifests into `PluginRegistry`.
3. Resolving `requires` and `optional` dependencies.
4. Running `Plugin::contribute` in topological order.
5. Repeating steps 3–4 until no new plugins appear.
6. Resolving `Options` from merged schemas and overrides.

After this, `Host::execute` dispatches a `CapabilityRequest` to the plugin that provides the requested capability.

## Adding a new operation

To add a new operation such as `Hover`:

1. Create `handl-ext-hover`.
2. Define a `Hover` marker type implementing `Operation`.
3. Define `HoverBehavior` implementing `Behavior<Hover>`.
4. Provide `BasicHover` as a `RuleAcceptor<Rule = HoverBehavior>`.
5. Register `BasicHover` in the host.

No `handl-platform` change is required.

## How a new plugin becomes a command

A rule plugin can contribute a `CliCommand` to the `Cli` `RuleAcceptor`. The `handl-ext-cli` crate defines the `Cli` operation and the `BasicCli` plugin that accepts those commands. The `handl-host-cli` host loads the kit, runs `contribute`, and then executes the `cli` capability.

```rust
// handl-plugin-lint
impl Plugin for LintPlugin {
    fn id(&self) -> &str { "lint" }

    fn contribute(&self, ctx: &mut ContributionContext) -> Result<(), PlatformError> {
        ctx.contribute::<Cli>(CliCommand {
            name: "lint",
            about: "Run the linter",
            run: Box::new(|host, matches| {
                host.execute(&"lint".into(), json!({
                    "path": matches.get_one::<String>("path"),
                }))
            }),
        })?;

        ctx.contribute::<Linter>(Box::new(NoUnusedImports))?;
        Ok(())
    }
}
```

`handl-host-cli` does not know `lint` exists. The `LintPlugin` contributed the command and the rule, and the host ran them.
