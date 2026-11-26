# Kits

A **kit** is a curated environment: a `kit.hnl` v1 manifest
(`{ name, description, license, libs }`) that assembles `lib-*`
packages into a ready-to-use surface for a domain — CLI apps, HTTP
servers, browser interop, testing, or the mlopt research stack. Kits
are pure curation: no plugins, no entry glue; each listed package's own
`pkg.hnl` deps pull its contracts and transitive backends.

## Application kits

| Kit | What it assembles |
|---|---|
| [kit-cli-app](https://github.com/handl-lang/kit-cli-app) | Build CLI applications — argv parsing (`mri`), stdio, POSIX fs/env/time, child processes, JSON, collections |
| [kit-web-server](https://github.com/handl-lang/kit-web-server) | Serve HTTP from handl — epoll accept loop, HTTP/1.1 codec + routing, TLS, WebSocket, JSON |
| [kit-test](https://github.com/handl-lang/kit-test) | In-language test surface — test/property/benchmark/fuzz/snapshot/assert plus deterministic rand and posix stubs |
| [kit-pkg](https://github.com/handl-lang/kit-pkg) | The package kit — `.handl.toml` project discovery and dependency wiring |

## Interop kits

| Kit | What it assembles |
|---|---|
| [kit-web-browser-iterop](https://github.com/handl-lang/kit-web-browser-iterop) | Browser/client-side JS interop — call/invoke/await into JS, fetch and WebSocket over generated WebIDL bindings, JSON + JS str backend |
| [kit-web-worker-iterop](https://github.com/handl-lang/kit-web-worker-iterop) | Web Worker interop for handl-on-JS — JS call/invoke/await surface plus data plumbing (JSON, serialize port, str-js backend) |

## MLOpt kits

The `mlopt` research game (see [Products](/ecosystem/#10-products)) has
its own kit family — domain kits that wire tensor, carrier, and
discovery machinery:

| Kit | What it assembles |
|---|---|
| [kit-torch](https://github.com/handl-lang/kit-torch) | PyTorch integration for the mlopt game |
| [kit-cuda](https://github.com/handl-lang/kit-cuda) | CUDA-graph delivery mechanism for the mlopt game |
| [kit-carriers](https://github.com/handl-lang/kit-carriers) | Semantic carriers — online-softmax monoids |
| [kit-discovery](https://github.com/handl-lang/kit-discovery) | Law-discovery engine — census, proposal, verification |

Kits are data, so composing one is editing a manifest: pick the libs,
let `pkg.hnl` deps resolve the rest. The kits that bootstrap the
toolchain itself ship with the platform layer.
