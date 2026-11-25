#!/usr/bin/env bash
# Render learn/index.md to a professional print PDF via Quarto/LaTeX.
# Requires: quarto + a LaTeX toolchain (xelatex).
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

QMD="$WORK/learn-pdf.qmd"
{
cat <<'YAMLEOF'
---
title: "The Handl type system"
subtitle: "One calculus for programs, proofs, types, effects, and modes"
author: "Handl"
date: ""
format:
  pdf:
    documentclass: article
    classoption: [11pt]
    papersize: a4
    geometry: margin=2.3cm
    toc: false
    number-sections: false
    colorlinks: true
    linkcolor: "NavyBlue"
    urlcolor: "NavyBlue"
    citecolor: "NavyBlue"
    highlight-style: tango
    mainfont: "Liberation Serif"
    monofont: "Liberation Mono"
    monofontoptions: "Scale=0.85"
    header-includes:
      - \usepackage{microtype}
      - \usepackage{fancyhdr}
      - \pagestyle{fancy}
      - \fancyhf{}
      - \fancyhead[L]{\small\itshape The Handl type system}
      - \fancyhead[R]{\small\thepage}
      - \renewcommand{\headrulewidth}{0.4pt}
---

YAMLEOF
# Strip the markdown H1 (the title block covers it) and remap the
# `hnl` fence to `agda` for reasonable keyword highlighting.
sed -e '1{/^# /d}' -e 's/^```hnl$/```agda/' "$SRC"
} > "$QMD"

# --output takes a basename only; quarto drops the PDF next to the .qmd
# (or the resolved project dir). Render from $WORK and collect it.
( cd "$WORK" && quarto render "$QMD" --to pdf --output learn-pdf.pdf )
PDF="$(find "$WORK" "$ROOT" -maxdepth 1 -name 'learn-pdf.pdf' -newer "$QMD" | head -1)"
[ -n "$PDF" ] || { echo "learn-pdf.sh: quarto did not produce learn-pdf.pdf" >&2; exit 1; }
mv -f "$PDF" "$OUT"
rm -f "$ROOT/learn-pdf.pdf"
echo "wrote $OUT"
