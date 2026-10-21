#!/usr/bin/env bash
# paper-build.sh — bupha shell-runner pipeline: rebuild paper/paper.pdf.
#
# bupha's shell runner spawns `bash -c <cmd>` with cwd = the detached
# worktree of the pushed sha (`<worktree.base>-<owner>-<repo>-<sha12>`).
# No per-run env vars are exported by the runner, so the repo is
# identified from the worktree's origin remote (fallback: dirname) —
# same convention as docs-trigger.sh.
#
# Usage:
#   paper-build.sh [REPO_DIR]     # default: $PWD (the bupha worktree)
#
# Behaviour:
#   no paper/paper.qmd            -> exit 0 quietly (repo not on the
#                                  paper pipeline)
#   push didn't touch paper/**    -> exit 0 quietly (per-repo state file
#                                  tracks the last-seen sha, like
#                                  docs-trigger.sh; paper/paper.pdf is
#                                  excluded so our own rebuild commit
#                                  never re-triggers the pipeline)
#   quarto missing                -> fail loudly
#   otherwise                     -> `quarto render paper.qmd --to pdf`
#                                  in paper/, commit paper/paper.pdf
#                                  and push to the repo's main — only
#                                  if the pdf changed

set -euo pipefail

# quarto/TinyTeX/git live outside the systemd unit's default PATH.
export PATH="$HOME/.local/bin:$HOME/.TinyTeX/bin/x86_64-linux:$HOME/.cargo/bin:$PATH"

REPO_DIR="$(cd "${1:-$PWD}" && pwd)"
STATE_DIR="${XDG_STATE_HOME:-$HOME/.local/state}/bupha-paper-build"

# --- identify the pushed repo ----------------------------------------------
url="$(git -C "$REPO_DIR" config --get remote.origin.url 2>/dev/null || true)"
repo="$(basename "$url" .git)"
if [ -z "$repo" ]; then
  # fallback: worktree dirname <base>-<owner>-<repo>-<sha12>
  repo="$(basename "$REPO_DIR" | sed -E 's/-[0-9a-f]{6,12}$//; s/^.*-handl-lang-//')"
fi
sha="$(git -C "$REPO_DIR" rev-parse HEAD)"
echo "[paper-build] repo=$repo sha=${sha:0:12} dir=$REPO_DIR"

# --- opt-out: repos without a paper/ dir aren't on the pipeline ------------
if [ ! -f "$REPO_DIR/paper/paper.qmd" ]; then
  exit 0
fi

# --- does this push touch the paper sources? --------------------------------
mkdir -p "$STATE_DIR"
state="$STATE_DIR/last-$repo"

if [ ! -s "$state" ]; then
  touched=1 # first observed push for this repo — establish a baseline
else
  last="$(cat "$state")"
  if ! git -C "$REPO_DIR" cat-file -e "$last^{commit}" 2>/dev/null; then
    touched=1 # baseline object GC'd / force-pushed away — rebuild to be safe
  elif git -C "$REPO_DIR" diff --name-only "$last" "$sha" -- paper/ ':!paper/paper.pdf' | grep -q .; then
    touched=1
  else
    touched=0
  fi
fi

# advance the diff baseline regardless of outcome — the next push diffs
# against the sha we just saw, not against the last successful build
printf '%s\n' "$sha" > "$state"

if [ "${touched:-0}" != "1" ]; then
  echo "[paper-build] no paper/ source changes — skipping render"
  exit 0
fi

# --- toolchain --------------------------------------------------------------
if ! command -v quarto >/dev/null 2>&1; then
  echo "[paper-build] ERROR: quarto not on PATH" >&2
  echo "[paper-build] install quarto-cli + a LaTeX engine (TinyTeX works):" >&2
  echo "[paper-build]   https://github.com/quarto-dev/quarto-cli/releases" >&2
  exit 1
fi

# --- render ------------------------------------------------------------------
( cd "$REPO_DIR/paper" && quarto render paper.qmd --to pdf )

# --- commit + push iff the pdf changed ----------------------------------------
git -C "$REPO_DIR" add paper/paper.pdf
if git -C "$REPO_DIR" diff --cached --quiet -- paper/paper.pdf; then
  echo "[paper-build] paper.pdf unchanged — nothing to push"
  exit 0
fi

git -C "$REPO_DIR" commit --quiet -m "paper: rebuild pdf (bupha)" -- paper/paper.pdf
git -C "$REPO_DIR" push origin HEAD:main
echo "[paper-build] pushed rebuilt paper.pdf on top of ${sha:0:12}"
