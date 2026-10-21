#!/usr/bin/env bash
# docs-trigger.sh — bupha shell-runner pipeline for the handl docs site.
#
# bupha's shell runner spawns `bash -c <cmd>` with cwd = the detached
# worktree of the pushed sha (`<worktree.base>-<owner>-<repo>-<sha12>`).
# No per-run env vars are exported by the runner, so the repo is
# identified from the worktree's origin remote (fallback: dirname).
#
# Behaviour:
#   handl-lang/docs            -> always rebuild + deploy
#   host/graphopt/eqsat/gamekit-> deploy iff `docs/site/**` or
#                                 `docs/site.yaml` changed since the last
#                                 push bupha ran for that repo
#
# bupha does not pass the webhook's before/after range to the runner, so
# the "previous pushed sha" is kept in a per-repo state file
# ($STATE_DIR/last-<repo>). The deploy itself is a full rebuild —
# scripts/deploy-pages.sh vendors every sibling's docs/site fresh — so
# the diff only decides whether to run, never what to ship.
#
# The deploy always runs out of the docs repo's *main checkout*
# (scripts/deploy-pages.sh resolves its own REPO_ROOT). The worktree is
# only used for repo identification + the diff — nothing builds in it,
# so concurrent bupha worktrees can't clobber the deploy.

set -euo pipefail

# bun/python3/rsync/git live outside the systemd unit's default PATH.
export PATH="$HOME/.bun/bin:$HOME/.local/bin:$HOME/.cargo/bin:$PATH"

DOCS_DIR="${DOCS_DIR:-/home/luis/GitHub/handl-lang/docs}"
DEPLOY="$DOCS_DIR/scripts/deploy-pages.sh"
STATE_DIR="${XDG_STATE_HOME:-$HOME/.local/state}/bupha-docs-watch"

# --- identify the pushed repo ----------------------------------------------
url="$(git config --get remote.origin.url 2>/dev/null || true)"
repo="$(basename "$url" .git)"
if [ -z "$repo" ]; then
  # fallback: worktree dirname <base>-<owner>-<repo>-<sha12>
  repo="$(basename "$PWD" | sed -E 's/-[0-9a-f]{6,12}$//; s/^.*-handl-lang-//')"
fi
sha="$(git rev-parse HEAD)"
echo "[docs-trigger] repo=$repo sha=${sha:0:12} cwd=$PWD"

# --- does this push touch the published docs? -------------------------------
mkdir -p "$STATE_DIR"
state="$STATE_DIR/last-$repo"

if [ "$repo" = "docs" ]; then
  touched=1 # the docs repo itself: every push to main rebuilds
elif [ ! -s "$state" ]; then
  touched=1 # first observed push for this repo — establish a baseline
else
  last="$(cat "$state")"
  if ! git cat-file -e "$last^{commit}" 2>/dev/null; then
    touched=1 # baseline object GC'd / force-pushed away — deploy to be safe
  elif git diff --name-only "$last" "$sha" -- docs/site docs/site.yaml | grep -q .; then
    touched=1
  else
    touched=0
  fi
fi

# advance the diff baseline regardless of outcome — the next push diffs
# against the sha we just saw, not against the last successful deploy
printf '%s\n' "$sha" > "$state"

if [ "${touched:-0}" != "1" ]; then
  echo "[docs-trigger] no docs/site or docs/site.yaml changes — skipping deploy"
  exit 0
fi

# --- freshen the checkouts the build vendors from ---------------------------
# scripts/vendor-docs.py reads sibling checkouts on disk, not this
# worktree, so a push made elsewhere would otherwise deploy stale docs.
# Fast-forward only, and only a clean checkout on main — a dirty or
# detached checkout is left untouched (logged, non-fatal).
sync_checkout() {
  local dir="$1" label="$2" br
  [ -d "$dir/.git" ] || { echo "[docs-trigger] $label: no checkout at $dir"; return 0; }
  git -C "$dir" fetch --quiet origin main 2>/dev/null \
    || { echo "[docs-trigger] $label: fetch failed — vendored docs may lag"; return 0; }
  br="$(git -C "$dir" symbolic-ref --quiet --short HEAD 2>/dev/null || true)"
  [ "$br" = "main" ] \
    || { echo "[docs-trigger] $label: on '$br' — leaving checkout alone"; return 0; }
  git -C "$dir" diff --quiet && git -C "$dir" diff --cached --quiet \
    || { echo "[docs-trigger] $label: dirty checkout — vendored docs may lag"; return 0; }
  if git -C "$dir" merge --ff-only --quiet origin/main 2>/dev/null; then
    echo "[docs-trigger] $label: checkout fast-forwarded to origin/main"
  else
    echo "[docs-trigger] $label: not fast-forwardable — vendored docs may lag"
  fi
}

case "$repo" in
  host | graphopt | eqsat | gamekit)
    sync_checkout "/home/luis/GitHub/handl-lang/$repo" "$repo"
    ;;
esac
sync_checkout "$DOCS_DIR" "docs"

# --- deploy -----------------------------------------------------------------
echo "[docs-trigger] running $DEPLOY"
bash "$DEPLOY"
