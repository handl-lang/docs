#!/usr/bin/env bash
# Render learn/index.md to a polished print PDF (cover block, styled
# headings, code blocks). Requires pandoc + soffice (LibreOffice).
#
#   scripts/learn-pdf.sh [output.pdf]
#
# Default output: ~/Downloads/handl-type-system-overview.pdf
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="$ROOT/learn/index.md"
OUT="${1:-$HOME/Downloads/handl-type-system-overview.pdf}"
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

pandoc "$SRC" -t html5 -o "$WORK/body.html"

cat > "$WORK/doc.html" <<'HTMLEOF'
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>The Handl type system</title>
<style>
  @page { size: A4; margin: 22mm 20mm 20mm 20mm; }

  html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }

  body {
    font-family: "DejaVu Serif", Georgia, "Times New Roman", serif;
    font-size: 10.5pt;
    line-height: 1.55;
    color: #1a1a1a;
    max-width: 100%;
    margin: 0;
  }

  /* ---- cover block ---- */
  .cover {
    border-bottom: 3px double #1a1a1a;
    padding-bottom: 14pt;
    margin-bottom: 26pt;
  }
  .cover .kicker {
    font-family: "DejaVu Sans", Arial, sans-serif;
    font-size: 8.5pt;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: #6b4fbb;
    margin-bottom: 6pt;
  }
  .cover h1 {
    font-family: "DejaVu Sans", Arial, sans-serif;
    font-size: 30pt;
    font-weight: 700;
    letter-spacing: -0.01em;
    margin: 0 0 6pt 0;
    color: #111;
  }
  .cover .subtitle {
    font-size: 12pt;
    font-style: italic;
    color: #444;
    margin: 0;
  }
  .cover .meta {
    font-family: "DejaVu Sans", Arial, sans-serif;
    font-size: 8.5pt;
    color: #777;
    margin-top: 10pt;
    letter-spacing: 0.04em;
  }

  /* ---- headings ---- */
  h1, h2, h3 {
    font-family: "DejaVu Sans", Arial, sans-serif;
    color: #111;
    page-break-after: avoid;
  }
  h2 {
    font-size: 15pt;
    font-weight: 700;
    margin-top: 26pt;
    margin-bottom: 8pt;
    padding-bottom: 4pt;
    border-bottom: 1px solid #d8d8d8;
  }
  h3 {
    font-size: 11.5pt;
    font-weight: 700;
    margin-top: 18pt;
    margin-bottom: 6pt;
    color: #333;
  }
  h1[id] { display: none; }  /* pandoc h1 duplicates the cover title */
  h4, h5, h6 { font-family: "DejaVu Sans", Arial, sans-serif; }

  p { margin: 0 0 9pt 0; text-align: justify; hyphens: auto; }
  ul, ol { margin: 0 0 9pt 0; padding-left: 20pt; }
  li { margin-bottom: 3pt; }

  /* ---- inline code ---- */
  code {
    font-family: "DejaVu Sans Mono", "Liberation Mono", monospace;
    font-size: 8.8pt;
    background: #f2f0f7;
    border: 1px solid #e2dff0;
    border-radius: 3px;
    padding: 0.5pt 3pt;
    color: #3d2c8d;
  }

  /* ---- code blocks ---- */
  pre {
    font-family: "DejaVu Sans Mono", "Liberation Mono", monospace;
    font-size: 8.6pt;
    line-height: 1.45;
    background: #f7f6fa;
    border: 1px solid #e0ddef;
    border-left: 3px solid #6b4fbb;
    padding: 9pt 11pt;
    margin: 10pt 0 12pt 0;
    white-space: pre-wrap;
    page-break-inside: avoid;
  }
  pre code {
    background: none;
    border: none;
    padding: 0;
    color: #222;
    font-size: inherit;
  }

  /* ---- emphasis / strong ---- */
  strong { color: #111; }
  em { color: #333; }

  a { color: #4a3a8c; text-decoration: none; }

  hr {
    border: none;
    border-top: 1px solid #ccc;
    margin: 22pt 0;
  }

  blockquote {
    border-left: 3px solid #6b4fbb;
    margin-left: 0;
    padding-left: 12pt;
    color: #444;
    font-style: italic;
  }

  table {
    border-collapse: collapse;
    width: 100%;
    font-size: 9.5pt;
    margin: 10pt 0 14pt 0;
    page-break-inside: avoid;
  }
  th, td {
    border: 1px solid #ccc;
    padding: 4pt 7pt;
    text-align: left;
    vertical-align: top;
  }
  th {
    background: #f0eef7;
    font-family: "DejaVu Sans", Arial, sans-serif;
    font-weight: 700;
  }
</style>
</head>
<body>

<div class="cover">
  <div class="kicker">Handl &middot; Language Reference</div>
  <h1>The Handl type system</h1>
  <p class="subtitle">One calculus for programs, proofs, types, effects, and modes</p>
  <div class="meta">Dependent &middot; Cubical &middot; Modal &middot; Effectful &middot; Everything is data</div>
</div>

BODYPLACEHOLDER

</body>
</html>
HTMLEOF

python3 - "$WORK/body.html" "$WORK/doc.html" <<'PYEOF'
import sys, re
body = open(sys.argv[1], encoding="utf-8").read()
# LibreOffice ignores display:none — strip the pandoc h1 (cover has its own).
body = re.sub(r"<h1[^>]*>.*?</h1>\s*", "", body, count=1, flags=re.S)
doc = open(sys.argv[2], encoding="utf-8").read()
open(sys.argv[2], "w", encoding="utf-8").write(doc.replace("BODYPLACEHOLDER", body))
PYEOF

soffice --headless --convert-to pdf --outdir "$WORK" "$WORK/doc.html" >/dev/null 2>&1
mv -f "$WORK/doc.pdf" "$OUT"
echo "wrote $OUT"
