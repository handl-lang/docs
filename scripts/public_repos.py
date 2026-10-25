#!/usr/bin/env python3
"""Canonical set of repos whose content this hub publishes.

One list, imported by `vendor-docs.py`, `gen-docs-index.py` and
`gen_reference_all.py`; it mirrors the Pages clone set (`--visibility public`).
Keeping it in one place is the point — the three generators had drifted (a repo
could be public, publish ADRs, and still be absent from the reference build).

Membership rule: the repo is **public on GitHub** *and* its content is
publishable. `lib-char`, `lib-char-native`, `lib-desugar`, `lib-loader` and
`lib-str-handl` are public but document the unreleased Handl language surface
(syntax / standard library), which `docs/README.md` keeps out of the hub until
the language is released — add them here (and drop that paragraph) when it is.

`.github` is not a product repo and never appears.
"""

PUBLIC_REPOS = {
    # platform / engine family
    "engine",
    "engine-exec",
    "engine-exec-bytecode",
    "engine-exec-tree-walk",
    "engine-lex",
    "engine-lex-pattern",
    "engine-parse",
    "engine-parse-pratt",
    "engine-transform",
    "engine-transform-rewrite",
    "engine-typecheck",
    "kernel",
    "host",
    # products
    "graphopt",
    "eqsat",
    "gamekit",
    "host-tensor",
    "kit-prelude-lang",
    # research / tooling / this hub
    "discovery",
    "egraph",
    "research-dts",
    "slidev-theme",
    "docs",
}
