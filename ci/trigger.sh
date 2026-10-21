#!/usr/bin/env bash
# bupha pipeline entry point — one runner per repo, fans out to the
# self-filtering jobs: paper rebuild (paper/) and docs site rebuild
# (docs/site/). Each job exits quietly when its paths didn't change.
set -uo pipefail

CI_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

bash "$CI_DIR/paper-build.sh" "$@" || echo "paper-build: failed ($?) — continuing"
bash "$CI_DIR/docs-trigger.sh" "$@" || echo "docs-trigger: failed ($?) — continuing"
