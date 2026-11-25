# Tooling and SDK generation

Beyond the language-operation engines, the `tool-*` family includes the
**codegen pipeline**: the machinery that turns foreign interfaces —
C headers, WebIDL specs, OpenAPI documents, command-line tools — into
typed Handl surfaces. This is the edge of the ecosystem: generated,
not hand-written, bindings are how Handl talks to the outside world.

## The codegen kernel

- [tool-codegen](https://github.com/handl-lang/tool-codegen) —
  `hnl-tool-codegen`, the desired-state codegen kernel. The pipeline is
  `Lift → Transform → Emit`: lift a foreign spec into an intermediate
  representation, transform it, emit typed Handl modules.

## Backends (spec → IR)

Each backend parses one foreign spec language:

| Repo | Spec it lifts |
|---|---|
| [tool-codegen-c](https://github.com/handl-lang/tool-codegen-c) | C headers via libclang |
| [tool-codegen-webidl](https://github.com/handl-lang/tool-codegen-webidl) | WebIDL — browser/worker APIs |
| [tool-codegen-openapi](https://github.com/handl-lang/tool-codegen-openapi) | OpenAPI documents |
| [tool-codegen-cli](https://github.com/handl-lang/tool-codegen-cli) | CLI tools — `*.clispec.yaml` specs or live `--help` probes |

## Emitters (IR → Handl)

| Repo | What it emits |
|---|---|
| [tool-codegen-file](https://github.com/handl-lang/tool-codegen-file) | `.hnl` module files (`hnl-file` emitter) |
| [tool-codegen-python](https://github.com/handl-lang/tool-codegen-python) | Python `ctypes` SDKs for C headers |

Generated output lands as `handl-packages/generated/` bindings inside
the consuming repo; multi-consumer bindings graduate to their own
`lib-*` repos — [lib-libc](https://github.com/handl-lang/lib-libc),
[lib-curl](https://github.com/handl-lang/lib-curl),
[lib-libz](https://github.com/handl-lang/lib-libz) are the canonical
examples, and the generated CLI SDKs
([lib-gh](https://github.com/handl-lang/lib-gh),
[lib-cli-gen](https://github.com/handl-lang/lib-cli-gen)) follow the
same spec-plus-gate pattern.

## Codemods

- [tool-codemod](https://github.com/handl-lang/tool-codemod) — the
  declarative codemod engine's spec/model layer; rewrite rules as data,
  same philosophy as the transform engines. Packaged for `hnl` as the
  `ext-codemod` extension (see [Extensions](/ecosystem/extensions)).

The design rule across the family: foreign surfaces become *typed Handl
declarations* — specs are the source of truth, generated code is
rebuilt, never hand-edited.
