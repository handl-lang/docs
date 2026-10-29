#!/usr/bin/env bash
# Collect rustdoc for every sibling repo into api/<repo>/ (ADR-0129 5.3).
#
# Uses `cargo +nightly doc-md` when available (markdown, VitePress-friendly),
# otherwise falls back to `cargo doc` and copies the HTML tree.
set -euo pipefail

DOCS_ROOT=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
ORG=$(dirname "$DOCS_ROOT")
OUT="$DOCS_ROOT/api"
mkdir -p "$OUT"

MODE=doc
if cargo +nightly doc-md --help >/dev/null 2>&1; then MODE=docmd; fi
echo "rustdoc mode: $MODE"

found=0
for dir in "$ORG"/*/; do
  repo=$(basename "$dir")
  [ "$dir" = "$DOCS_ROOT/" ] && continue
  [ -f "$dir/Cargo.toml" ] || continue
  found=$((found + 1))
  echo ">> $repo"
  if [ "$MODE" = docmd ]; then
    ( cd "$dir" && cargo +nightly doc-md --workspace --no-deps \
        --include-private -o "$OUT/$repo" ) || echo "   (failed — skipped)"
  else
    ( cd "$dir" && cargo doc --workspace --no-deps \
        --target-dir "$dir/target/docapi" >/dev/null ) || echo "   (failed — skipped)"
    if [ -d "$dir/target/docapi/doc" ]; then
      rm -rf "$OUT/$repo"
      cp -r "$dir/target/docapi/doc" "$OUT/$repo"
    fi
  fi
done

if [ "$found" = 0 ]; then
  echo "no sibling repos with Cargo.toml found (expected checkouts beside $DOCS_ROOT)"
fi
# Rustdoc writes `Vec<T>` as bare text; VitePress treats `<T>` as a Vue
# component. Escape non-HTML tags so the site builds (same rule as vendor-docs).
python3 "$DOCS_ROOT/scripts/sanitize-md.py" "$OUT"
echo "wrote $OUT"
