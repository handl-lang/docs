#!/usr/bin/env python3
"""Canonical set of repos whose content this hub publishes.

One list, imported by `vendor-docs.py`, `gen-docs-index.py` and
`gen_reference_all.py`; it mirrors the Pages clone set (`--visibility public`).
Keeping it in one place is the point — the three generators had drifted (a repo
could be public, publish ADRs, and still be absent from the reference build).

Membership rule: the repo is **public on GitHub**. That is the whole rule — the
allowlist is what the org actually publishes, so a repo becoming public is what
admits it here. (Until this sweep the five `lib-*` repos above were public but
withheld on the theory that the language surface was unreleased; publishing docs
for a public repo cannot leak anything its code does not, so they are
included.)

`.github` is not a product repo and never appears.
"""

PUBLIC_REPOS = {
    # platform / engine family
    "engine",
    "engine-exec",
    "engine-exec-bytecode",
    "engine-exec-cranelift",
    "engine-exec-tree-walk",
    "engine-fmt",
    "engine-lex",
    "engine-lex-pattern",
    "engine-lint",
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
    "lib-char",
    "lib-char-native",
    "lib-desugar",
    "lib-loader",
    "lib-str-handl",
    # research / tooling / this hub
    "discovery",
    "egraph",
    "research-dts",
    "slidev-theme",
    "docs",
}
