#!/usr/bin/env python3
"""Escape non-HTML `<tag` in generated Markdown so Vue can compile it.

Rustdoc emits `Vec<T>`, `Option<T>` and friends as bare text; VitePress treats
`<T>` as an unclosed Vue component and the build dies. This escapes only
angle-bracket tags that are **not** HTML elements, outside code fences and
inline code spans — the same rule the docs hub applies to vendored pages.

Usage:
    python3 scripts/sanitize-md.py api            # rewrite api/**/*.md in place
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

FENCE = re.compile(r"```.*?```", re.DOTALL)
INLINE = re.compile(r"`[^`\n]*`")
TAG = re.compile(r"<(/?)([a-zA-Z][a-zA-Z0-9-]*)")
FRONT = re.compile(r"\A---[ \t]*\r?\n.*?\r?\n---[ \t]*\r?\n", re.S)
HTML_TAGS = {
    "a", "abbr", "address", "article", "aside", "b", "blockquote", "br",
    "caption", "cite", "code", "col", "colgroup", "details", "dd", "del",
    "dfn", "div", "dl", "dt", "em", "figcaption", "figure", "footer", "h1",
    "h2", "h3", "h4", "h5", "h6", "header", "hr", "i", "img", "ins", "kbd",
    "li", "main", "mark", "nav", "ol", "p", "pre", "s", "samp", "section",
    "small", "span", "strong", "sub", "summary", "sup", "table", "tbody",
    "td", "tfoot", "th", "thead", "tr", "u", "ul", "var",
}


def escape_tags(segment: str) -> str:
    return TAG.sub(
        lambda m: m.group(0) if m.group(2) in HTML_TAGS
        else f"&lt;{m.group(1)}{m.group(2)}",
        segment,
    )


def escape_outside_code(segment: str) -> str:
    """Escape non-HTML tags, leaving inline code spans untouched."""
    codes: list[str] = []

    def stash(m: re.Match) -> str:
        codes.append(m.group(0))
        return f"\x00{len(codes) - 1}\x00"

    guarded = INLINE.sub(stash, segment)
    guarded = escape_tags(guarded)
    for i, code in enumerate(codes):
        guarded = guarded.replace(f"\x00{i}\x00", code)
    return guarded


def sanitize(text: str) -> str:
    head = ""
    if (m := FRONT.match(text)):
        head, text = text[:m.end()], text[m.end():]
    parts = FENCE.split(text)
    fences = FENCE.findall(text)
    out: list[str] = []
    for i, seg in enumerate(parts):
        out.append(escape_outside_code(seg))
        if i < len(fences):
            out.append(fences[i])
    return head + "".join(out)


def main(argv: list[str]) -> int:
    root = Path(argv[0] if argv else ".")
    files = changed = 0
    for path in sorted(root.rglob("*.md")):
        files += 1
        text = path.read_text(encoding="utf-8", errors="replace")
        new = sanitize(text)
        if new != text:
            path.write_text(new, encoding="utf-8")
            changed += 1
    print(f"sanitized {changed}/{files} markdown files under {root}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
