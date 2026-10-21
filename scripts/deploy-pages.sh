#!/usr/bin/env bash
# Build the VitePress site and publish .vitepress/dist to the `gh-pages`
# branch. Pages is configured with build_type=branch ("legacy"), so
# pushing gh-pages is the entire deploy — this script runs identically
# in GHA (.github/workflows/pages.yml) and locally (bupha / by hand).
#
# Expects sibling repos checked out at ../<repo> (the workflow clones
# them; locally they already are). Never touches the main worktree —
# all deletion happens inside a detached temporary worktree via
# `rsync --delete`.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

DEPLOY_BRANCH="${DEPLOY_BRANCH:-gh-pages}"
DIST="$REPO_ROOT/.vitepress/dist"

# --- auth -----------------------------------------------------------------
# In GHA the sibling-clone step installs a global URL rewrite carrying
# CI_TOKEN. Drop such rewrites before the push so `git push origin`
# authenticates with the GITHUB_TOKEN that actions/checkout wired into
# the remote (contents: write). Locally this block is a no-op.
if [ "${GITHUB_ACTIONS:-}" = "true" ]; then
  git config --global --get-regexp '^url\..*\.insteadof$' 2>/dev/null \
    | while read -r key _; do
        git config --global --unset "$key" || true
      done || true
fi

# --- build ----------------------------------------------------------------
bun run docs:vendor
bun run docs:gen-ref
# Project Pages live at handl-lang.github.io/docs/ → base must be /docs/.
DOCS_BASE="${DOCS_BASE:-/docs/}" bunx vitepress build .

# Branch deploys still get a Jekyll pass unless .nojekyll is present, and
# Jekyll honours .gitignore — which would drop the generated reference/
# pages this repo ignores.
touch "$DIST/.nojekyll"

# --- publish --------------------------------------------------------------
WT="$(mktemp -d "${TMPDIR:-/tmp}/docs-gh-pages.XXXXXX")"
cleanup() {
  git -C "$REPO_ROOT" worktree remove --force "$WT" 2>/dev/null || true
}
trap cleanup EXIT

REMOTE_HAS_BRANCH=0
if git ls-remote --exit-code --heads origin "$DEPLOY_BRANCH" >/dev/null 2>&1; then
  REMOTE_HAS_BRANCH=1
fi

if [ "$REMOTE_HAS_BRANCH" = 1 ]; then
  git fetch --quiet origin "$DEPLOY_BRANCH"
  if git show-ref --verify --quiet "refs/heads/$DEPLOY_BRANCH"; then
    git worktree add "$WT" "$DEPLOY_BRANCH" >/dev/null
    # gh-pages is publish-only: always mirror origin, discard stale local state.
    git -C "$WT" reset --hard --quiet "origin/$DEPLOY_BRANCH"
  else
    git worktree add -b "$DEPLOY_BRANCH" "$WT" "origin/$DEPLOY_BRANCH" >/dev/null
  fi
else
  # First deploy: no gh-pages yet — orphan it inside the worktree.
  git worktree add --detach "$WT" >/dev/null
  git -C "$WT" checkout --quiet --orphan "$DEPLOY_BRANCH"
  git -C "$WT" rm -rf . >/dev/null 2>&1 || true
fi

# Mirror dist into the worktree root. --delete makes the branch content
# exactly the build output; /.git is excluded (it is the worktree's
# gitdir pointer file, not content).
rsync -a --delete --exclude='/.git' "$DIST"/ "$WT"/

git -C "$WT" add -A
if git -C "$WT" diff --cached --quiet; then
  echo "gh-pages already up to date — nothing to commit"
else
  git -C "$WT" \
    -c "user.name=${DEPLOY_GIT_NAME:-handl-docs deploy}" \
    -c "user.email=${DEPLOY_GIT_EMAIL:-deploy@handl-lang.github.io}" \
    commit --quiet -m "deploy: site build $(date -u +%Y-%m-%dT%H:%M:%SZ)"
fi

git -C "$WT" push origin "HEAD:$DEPLOY_BRANCH"
echo "deployed .vitepress/dist → origin/$DEPLOY_BRANCH"
