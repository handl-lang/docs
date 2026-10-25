#!/usr/bin/env python3
"""Aggregate every sibling repo's Handl reference into the docs site.

Runs scripts/gen_reference.py once per repo that ships package sources —
a `handl-packages/` tree, a `pkg.hnl` + `src/` one-package-per-repo
layout, or `crates/<crate>/src/*.hnl` substrate packages — then merges the
per-repo `reference.yaml` fragments into the site-wide `reference.yaml`
and `.vitepress/sidebar-reference.mjs`, grouped by repo (ADR-0129 5.3).

`reference/<repo>/` directories left behind by repos that no longer ship
packages (the retired monorepo-era `platform`/`stdlib`/`lang`/
`kit-canonical` fragments, renames, …) are pruned when they carry the
generated `sidebar.json`/`reference.yaml` markers — hand-written pages
under `reference/` are never touched.
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

import yaml

DOCS_ROOT = Path(__file__).resolve().parent.parent
ORG = DOCS_ROOT.parent
HERE = Path(__file__).resolve().parent

sys.path.insert(0, str(HERE))
from gen_reference import package_sources  # noqa: E402
from public_repos import PUBLIC_REPOS


# Only public org repos contribute generated reference pages — this
# mirrors the Pages workflow's `gh repo list --visibility public` clone
# set. Private siblings produce no pages, links, or mentions.


def repos_with_packages() -> list[str]:
    repos = [
        d.name
        for d in sorted(ORG.iterdir())
        if d.is_dir() and d != DOCS_ROOT and d.name in PUBLIC_REPOS
        and package_sources(d, d.name)
    ]
    # host first, then alphabetical
    repos.sort(key=lambda r: (r != "host", r))
    return repos


def prune_stale_fragments(produced: set[str]) -> list[str]:
    """Remove generated `reference/<repo>/` fragments no run produced."""
    removed = []
    for frag in sorted((DOCS_ROOT / "handl" / "reference").iterdir()):
        if not frag.is_dir() or frag.name in produced:
            continue
        if (frag / "sidebar.json").exists() or (frag / "reference.yaml").exists():
            shutil.rmtree(frag)
            removed.append(frag.name)
    return removed


def main() -> int:
    repos = repos_with_packages()
    if not repos:
        print(f"no repos with package sources under {ORG}")
        return 0

    merged_ref: list = []
    merged_sidebar: list = []
    produced: set[str] = set()

    for repo in repos:
        subprocess.run(
            [sys.executable, str(HERE / "gen_reference.py"), "--repo", repo],
            check=True,
        )
        frag = DOCS_ROOT / "handl" / "reference" / repo

        yml = frag / "reference.yaml"
        if yml.exists():
            produced.add(repo)
            data = yaml.safe_load(yml.read_text()) or {}
            merged_ref.extend(data.get("reference") or [])

        sj = frag / "sidebar.json"
        items = json.loads(sj.read_text()) if sj.exists() else []
        if items:
            merged_sidebar.append(
                {"text": repo, "collapsed": False, "items": items}
            )

    removed = prune_stale_fragments(produced)
    if removed:
        print("pruned stale fragments: " + ", ".join(removed))

    (DOCS_ROOT / "reference.yaml").write_text(
        yaml.safe_dump({"reference": merged_ref}, sort_keys=False)
    )
    (DOCS_ROOT / ".vitepress" / "sidebar-reference.mjs").write_text(
        "export default " + json.dumps(merged_sidebar, indent=2) + ";\n"
    )
    print(
        f"merged {len(merged_ref)} packages from {len(repos)} repos: "
        + ", ".join(repos)
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
