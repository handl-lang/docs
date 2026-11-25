# Extensions

`ext-*` crates package Handl operations as **dynamic extensions** —
`libhnl_ext_*.so`/`.dylib`/`.dll` shared libraries discovered at runtime
via `HANDL_EXT_DIR` or `~/.handl/ext`. Each extension wraps one tool
family so `hnl` stays a dumb host: the CLI links the extension, the
extension links the engine.

| Extension | Provides |
|---|---|
| [ext-eval](https://github.com/handl-lang/ext-eval) | `hnl run` / `hnl eval` — program evaluation |
| [ext-compile](https://github.com/handl-lang/ext-compile) | `hnl compile` — compiler front end |
| [ext-transform](https://github.com/handl-lang/ext-transform) | `hnl transform` — transform runner |
| [ext-typecheck](https://github.com/handl-lang/ext-typecheck) | `hnl typecheck` / `hnl check` |
| [ext-fmt](https://github.com/handl-lang/ext-fmt) | `hnl fmt` — formatter |
| [ext-lint](https://github.com/handl-lang/ext-lint) | `hnl lint` — canonical linter |
| [ext-test](https://github.com/handl-lang/ext-test) | `hnl test` — test runner |
| [ext-codegen](https://github.com/handl-lang/ext-codegen) | `hnl codegen` — SDK/FFI generation pipeline |
| [ext-codemod](https://github.com/handl-lang/ext-codemod) | `hnl codemod` — declarative codemod pipeline |
| [ext-kit](https://github.com/handl-lang/ext-kit) | `hnl kit` + `hnl gen-grammar` — kit tooling |
| [ext-plugin](https://github.com/handl-lang/ext-plugin) | `hnl plugin` — plugin management |

The same operation also exists as a `tool-*` engine crate — the
extension is a thin packaging of it. Building an extension is a normal
Rust crate implementing the `hnl-ext` ABI; dropping the built library
into the ext dir is the entire install step.
