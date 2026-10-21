#!/usr/bin/env python3
"""Vendor product docs from sibling repos into the site tree (ADR-0129 next).

Each public product repo may ship a published-site subtree at
`<repo>/docs/site/` plus a `docs/site.yaml` declaring its site path:

    site_path: graphopt        # -> vendored/graphopt/, served at /graphopt/

The vendored tree lands in `vendored/<site_path>/` (gitignored); VitePress
`rewrites` map `vendored/**` to site-root paths. Sibling dirs are resolved
by their git remote basename, so a checkout named differently from the
repo (e.g. `research-mlopt` -> `graphopt`) still matches.

Private repos, repos without `docs/site/`, and repos not in
`PUBLIC_REPOS` produce nothing — same rule as the Pages clone set.

Run from the docs repo: `python3 scripts/vendor-docs.py`.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

import yaml

DOCS_ROOT = Path(__file__).resolve().parent.parent
ORG = DOCS_ROOT.parent
VENDORED = DOCS_ROOT / "vendored"

PUBLIC_REPOS = {
    "discovery", "docs", "egraph", "engine", "engine-exec",
    "engine-exec-tree-walk", "engine-lex", "engine-lex-pattern",
    "engine-parse", "engine-parse-pratt", "engine-transform", "host",
    "host-tensor", "kernel", "kit-prelude-lang", "research-dts",
    "graphopt", "slidev-theme", "project",
}

# Repo -> site subtree it feeds (fallback: repo name via site.yaml site_path).
# `host` docs vendored under /handl/ is the product mapping; everything
# else defaults to its repo name.
SITE_PATH = {"host": "handl"}


def remote_name(repo_dir: Path) -> str | None:
    try:
        url = subprocess.run(
            ["git", "-C", str(repo_dir), "remote", "get-url", "origin"],
            capture_output=True, text=True, check=True,
        ).stdout.strip()
    except subprocess.CalledProcessError:
        return None
    name = url.rsplit("/", 1)[-1]
    return name[:-4] if name.endswith(".git") else name


def main() -> int:
    if VENDORED.exists():
        shutil.rmtree(VENDORED)
    VENDORED.mkdir()

    vendored: list[str] = []
    for d in sorted(ORG.iterdir()):
        if not d.is_dir() or d == DOCS_ROOT:
            continue
        repo = remote_name(d)
        if repo not in PUBLIC_REPOS:
            continue
        site_dir = d / "docs" / "site"
        if not site_dir.is_dir():
            continue
        meta = {}
        yml = d / "docs" / "site.yaml"
        if yml.exists():
            meta = yaml.safe_load(yml.read_text()) or {}
        dest_name = meta.get("site_path") or SITE_PATH.get(repo) or repo
        shutil.copytree(site_dir, VENDORED / dest_name)
        vendored.append(f"{repo} -> /{dest_name}/")

    if vendored:
        print("vendored: " + ", ".join(vendored))
    else:
        print("no product docs vendored (no public sibling ships docs/site/)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
