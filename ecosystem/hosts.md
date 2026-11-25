# Hosts

Hosts are the distribution layer — the programs that embed the Handl
platform and expose it to users. The platform itself is a Cargo
workspace plus `.hnl` packages; a host decides which engines fill the
operation slots and which extensions are loaded.

## Public hosts

| Repo | What it is |
|---|---|
| [host](https://github.com/handl-lang/host) | The reference Rust platform — runtime, loaders, `plugin-lib-*`/`plugin-ext-*` internals, and `plugin-lib-stdlib`, the library-as-data registry |
| [host-cli](https://github.com/handl-lang/host-cli) | The `hnl` CLI — a *dumb host* that links exactly one sibling engine set and dispatches to the `ext-*` dynamic extensions |

The `hnl` binary is deliberately thin: `hnl run`, `hnl eval`, `hnl fmt`,
`hnl lint`, `hnl typecheck`, `hnl test`, `hnl compile`, `hnl codegen`,
`hnl transform`, `hnl plugin`, `hnl kit`, `hnl codemod` are each a
separate `ext-*` shared library discovered via `HANDL_EXT_DIR` /
`~/.handl/ext` — see [Extensions](/ecosystem/extensions). This keeps
the core small and lets deployments ship only the operations they need.

Additional hosts exist for editor and language-server surfaces; they
are part of the private platform layer.
