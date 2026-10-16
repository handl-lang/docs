# Host concepts

This reference describes the core types, traits, and components that make up a composable host. It is intended to be read while working with the `handl-platform` API.

## Traits

| Trait | Role |
| --- | --- |
| `Plugin` | The universal, object-safe base trait. Every loaded component implements this. |
| `RuleAcceptor` | A sub-trait of `Plugin` for components that accept contributions. `RuleAcceptor::Rule` is the associated contribution type. |
| `Operation` | A marker trait for a cross-cutting concern such as `Format`, `Lint`, or `Cli`. |
| `Behavior<Op>` | A rule that contributes to a specific `Operation` for a specific `AstNode.kind`. |
| `Host` | The composer that owns the `PluginRegistry` and drives loading. |
| `HostApplier` | Reads external configuration and applies it to a `Host` as a `HostConfig`. |
| `Contribution` | Base trait for rules such as `OptionSchema` and `DataType`. |

## Core types

| Type | Description |
| --- | --- |
| `PluginRegistry` | Stores `Box<dyn Plugin>` and resolves capabilities and dependencies. |
| `ContributionContext` | Passed to `Plugin::contribute`. Provides `register_plugin` and `contribute::<P: RuleAcceptor>(rule)`. |
| `PluginContext` | Passed to `Plugin::run`. Gives the plugin access to the host while running a capability. |
| `CapabilityRequest` | A request to execute a capability, carrying the capability id and a JSON payload. |
| `CapabilityResponse` | The result of executing a capability. |
| `CapabilityId` | The string identifier for a capability. |
| `AstNode` | A generic AST node with `kind`, `span`, and `payload`. |
| `Kit` | A manifest of plugins to load, plus metadata. |
| `KitManifest` | The on-disk or embedded TOML manifest for a kit. |
| `HostConfig` | In-memory description of kits to load, plugins to include or exclude, and option overrides. |
| `OptionSchema` | A plugin-contributed option definition with id, scope, default, and allowed values. |
| `ResolvedOptions` | The merged and validated option values available during `run` and `Behavior::apply`. |
| `DataType` | A plugin-contributed runtime data type. |

## Plugin lifecycle

1. **Register** — plugins are added to `PluginRegistry` from kits, direct registration, or another plugin's `contribute`.
2. **Resolve dependencies** — the host topologically sorts plugins by `requires` and `optional`.
3. **Contribute** — `Plugin::contribute` is called for each plugin, passing a `ContributionContext`.
4. **Fixed point** — if a `contribute` step registers new plugins, the host returns to step 2 until no new plugins appear.
5. **Resolve options** — the `Options` plugin merges defaults, kit, host, and user values and validates them.
6. **Run** — `Host::execute` dispatches a `CapabilityRequest` to the plugin that provides the requested capability.

## Operation categories

| Operation | Crate | Typical `RuleAcceptor` |
| --- | --- | --- |
| `Format` | `handl-ext-fmt` | `BasicFormatter` accepts `Behavior<Format>`. |
| `Lint` | `handl-ext-lint` | `BasicLinter` accepts `Behavior<Lint>`. |
| `Lexer` | `handl-ext-lexer` | `BasicLexer` accepts `Behavior<Lexer>`. |
| `Parser` | `handl-ext-parser` | `BasicParser` accepts `Behavior<Parser>`. |
| `Typecheck` | `handl-ext-type` | `BasicTypechecker` accepts `Behavior<Typecheck>`. |
| `Eval` | `handl-ext-eval` | `handl-target-rust-interpreter` provides `Behavior<Eval>`. |
| `Cli` | `handl-ext-cli` | `BasicCli` accepts `CliCommand` rules. |
| `Lsp` | `handl-ext-lsp` | `BasicLsp` accepts `LspHandler` rules. |
| `Doc` | `handl-ext-doc` | `BasicDoc` accepts `Behavior<Doc>`. |
| `Options` | `handl-platform` | `Options` accepts `OptionSchema` rules. |
| `DataTypes` | `handl-platform` | `DataTypes` accepts `DataType` rules. |

## Common plugin kinds

| Kind | What it does in `contribute` |
| --- | --- |
| Library plugin | Calls `ContributionContext::register_plugin` to load more plugins. |
| Target plugin | Registers target-specific operations and contributes `OptionSchema` values. |
| Rule plugin | Calls `ContributionContext::contribute::<P>(rule)` to add a rule to an existing `RuleAcceptor`. |
| Operation plugin | Accepts rules and executes them when a capability is requested. |
| Executable host | Loads kits, applies config, and calls `Host::execute` for `Cli` or `Lsp`. |
