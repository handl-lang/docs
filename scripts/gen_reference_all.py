#!/usr/bin/env python3
"""Aggregate every sibling repo's Handl reference into the docs site.

Runs scripts/gen_reference.py once per repo that has a `handl-packages/`
directory, then merges the per-repo `reference.yaml` fragments into the
site-wide `reference.yaml` and `.vitepress/sidebar-reference.mjs`, grouped by
repo (ADR-0129 5.3).
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import yaml

DOCS_ROOT = Path(__file__).resolve().parent.parent
ORG = DOCS_ROOT.parent
HERE = Path(__file__).resolve().parent


def repos_with_packages() -> list[str]:
    repos = [
        d.name
        for d in sorted(ORG.iterdir())
        if d.is_dir() and d != DOCS_ROOT and (d / "handl-packages").is_dir()
    ]
    # platform first, then alphabetical
    repos.sort(key=lambda r: (r != "platform", r))
    return repos


def main() -> int:
    repos = repos_with_packages()
    if not repos:
        print(f"no repos with handl-packages/ under {ORG}")
        return 0

    merged_ref: list = []
    merged_sidebar: list = []

    for repo in repos:
        subprocess.run(
            [sys.executable, str(HERE / "gen_reference.py"), "--repo", repo],
            check=True,
        )
        frag = DOCS_ROOT / "reference" / repo

        yml = frag / "reference.yaml"
        if yml.exists():
            data = yaml.safe_load(yml.read_text()) or {}
            merged_ref.extend(data.get("reference") or [])

        sj = frag / "sidebar.json"
        items = json.loads(sj.read_text()) if sj.exists() else []
        if items:
            merged_sidebar.append(
                {"text": repo, "collapsed": False, "items": items}
            )

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
