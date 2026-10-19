#!/usr/bin/env python3
"""Generate the VitePress reference docs from handl doc comments.

Regex-based stopgap: the doc comments are *lexed*, not parsed. A proper
extractor will run over the handl parser's AST later; until then this keeps
`docs/reference.yaml` and the sidebar in sync with the package sources.

Package sources live in one of three post-restructure layouts:

  * `handl-packages/<pkg>/*.hnl`   — the original multi-package layout;
    `<pkg>` is the package name and the page slug is `lib-<pkg>`.
  * `pkg.hnl` + `src/**/*.hnl`     — one package per repo (the `lib-*` /
    `host-*` split): the package name is the repo name minus its `lib-` /
    `host-` category prefix, the page slug is the repo name. `src/` is
    scanned recursively; a `src/<group>/` subdirectory names a module
    group (e.g. `src/array/at.hnl` → `array.at`), and `internal/` and
    `generated/` subtrees are skipped like `*.test.hnl` files.
  * `crates/<crate>/src/*.hnl`     — substrate packages embedded in a Rust
    repo (kernel): one package per crate that ships `.hnl` sources,
    slug `lib-<crate>`.

Three declaration forms are covered:

    --- math.abs -- absolute value of a number.      (file-level doc block)
    op "math.abs" : Float -> Float

    --- Applies a transform to a value unless ...
    --- @details ...
    --- @example ...
    export unless :: [value, pred, fn] ~> ...

    -- LAW: concat(graphemes(s)) = s
    axiom unicode.graphemes : String -> List String

A declared name that is already dotted (`math.abs`, `base64.encode`,
`unicode.graphemes`) supplies its own module; a bare `export Name` falls back
to the file layout — a single-export file named after that export is a
one-arrow-per-file package (module = package), anything else is a
module-per-file package (module = file stem).

Outputs: `docs/reference/<repo>/lib-*.md` pages plus per-repo
`reference.yaml` / `sidebar.json` fragments that
`scripts/gen_reference_all.py` merges into the site-wide
`docs/reference.yaml` and `docs/.vitepress/sidebar-reference.mjs`.
Test files and `generated/` / `internal/` subtrees are skipped.
"""
import json
import re
import sys
from pathlib import Path

import yaml

# `docs/` repo root; the site content lives at the root (srcDir ".").
DOCS_ROOT = Path(__file__).resolve().parent.parent
ORG = DOCS_ROOT.parent

# Defaults; overridden per repo by `--repo` / `--packages-dir` / `--out`
# (see scripts/gen_reference_all.py, which aggregates every sibling repo).
ROOT = ORG / 'host'
PKGS = ROOT
REF = DOCS_ROOT / 'reference' / 'host'
URL = '/reference/host'

# --- line patterns ----------------------------------------------------------

DOC_LINE = re.compile(r'^---\s?(.*)$')
LAW_LINE = re.compile(r'^--\s?(.*)$')
NAMED_SUMMARY = re.compile(r'^(?P<name>[\w.]+)\s+--\s+(?P<summary>.+)$')
OP_DECL = re.compile(r'^op\s+"(?P<name>[\w.]+)"\s*:\s*(?P<sig>.*)$')
AXIOM_DECL = re.compile(r'^axiom\s+(?P<name>[\w.]+)\s*:\s*(?P<sig>.*)$')
EXPORT_DECL = re.compile(r'^export\s+(?P<name>[A-Za-z_]\w*)(?P<rest>.*)$')
GENERIC_HEAD = re.compile(r'^(?P<params><[^>]+>)\s*:\s*')
REEXPORT_IMPORT = re.compile(r'^from\s+"(?P<path>[^"]+)"\s+import\s+(?P<orig>[\w.]+)\s+as\s+(?P<alias>\w+)$')


def title_case(slug: str) -> str:
    parts = re.split(r'[-_]', slug)
    return ' '.join(p.capitalize() for p in parts if p)


def norm(name: str) -> str:
    return name.lower().replace('_', '')


def slugify(pkg_dir: str) -> str:
    return pkg_dir.replace('_', '-')


def esc(text: str) -> str:
    return str(text).replace('<', '&lt;').replace('>', '&gt;')


def parse_doc(lines: list[str]) -> dict:
    """Split a `---` doc block into summary/details/returns/examples.

    Untagged lines before the first `@tag` are the summary (first line) and
    details (the rest). Recognised tags: `@details`, `@returns`, `@example`.
    """
    body, tag, buckets = [], None, {'details': [], 'returns': [], 'example': []}
    for line in lines:
        if line.startswith('@details') or line.startswith('@returns') or line.startswith('@example'):
            tag = line[1:].split()[0].rstrip(':')
            continue
        (buckets[tag] if tag else body).append(line)

    body = [b for b in body if b.strip()]
    summary = body[0].strip() if body else ''
    # A file-level block often leads with `<name> -- <summary>`; keep just the
    # summary so the heading does not repeat the full name.
    named = NAMED_SUMMARY.match(summary)
    if named:
        summary = named.group('summary').strip()
    details = ' '.join(b.strip() for b in body[1:]).strip()
    return {
        'summary': summary,
        'details': details,
        'returns': ' '.join(b.strip() for b in buckets['returns']).strip(),
        'examples': [e.strip() for e in buckets['example'] if e.strip()],
    }


def doc_block_above(lines: list[str], i: int, pattern) -> list[str]:
    """Contiguous doc-comment lines directly above line `i`, in order."""
    out = []
    j = i - 1
    while j >= 0:
        m = pattern.match(lines[j])
        if not m:
            break
        out.append(m.group(1))
        j -= 1
    return list(reversed(out))


def split_export(rest: str) -> tuple[str, str | None]:
    """`(signature, re-export alias)` for an `export <name> ...` tail.

    `export abs := __abs` re-exports a binding: the RHS is a name, not a
    type, so it has no signature — the alias is returned so the caller can
    point at the import it came from.  `export f<T>: ...` carries a generic
    parameter list between the name and the signature; it is kept ahead of
    the signature for display.
    """
    body = re.sub(r'^\s*::?=?\s*', '', rest).strip()
    if re.fullmatch(r'[A-Za-z_]\w*', body):
        return '', body
    m = GENERIC_HEAD.match(body)
    if m:
        body = f'{m.group("params")} {body[m.end():]}'.strip()
    for sep in (' ~>', ' :=', ' ::'):
        if sep in body:
            body = body.split(sep)[0].strip()
    # A record-literal export (`export ltensor := { ... }`) has no signature.
    if body.startswith('{') or body.startswith('['):
        body = ''
    return body, None


def module_of(group: str, stem: str, name: str, exports_in_file: list[str]) -> str:
    if '.' in name:
        return name.rsplit('.', 1)[0]
    # `index.hnl` is the package (or module-group) facade
    # (`from "../x" import ... ; export x`), not a module of its own.
    if stem == 'index':
        return group
    if len(exports_in_file) == 1 and norm(name) == norm(stem):
        return group
    return stem


SKIP_DIRS = {'generated', 'internal'}


def package_files(pkg_dir: Path) -> list[Path]:
    """Every documentable `.hnl` under a package dir, recursively.

    Test files (`*.test.hnl`) and `generated/`/`internal/` subtrees are
    skipped — generated bindings vendor upstream surfaces and `internal/`
    is the by-convention home for helpers the package does not expose.
    """
    out = []
    for f in sorted(pkg_dir.rglob('*.hnl')):
        if f.name.endswith('.test.hnl'):
            continue
        if SKIP_DIRS & set(f.relative_to(pkg_dir).parts[:-1]):
            continue
        out.append(f)
    return out


def scan_package(pkg_dir: Path, pkg: str | None = None, slug: str | None = None) -> dict | None:
    """Collect documented declarations of one package, grouped by module.

    `pkg` defaults to the package directory's name (`handl-packages/<pkg>`);
    a repo-level `src/` package overrides it with the repo-derived name.
    `slug` is the page-name prefix (`lib-<pkg>` for the old layouts, the
    repo name for a one-package-per-repo `src/` package).
    """
    pkg = pkg or pkg_dir.name
    slug = slug or f'lib-{slugify(pkg)}'
    modules: dict[str, list[dict]] = {}
    description = ''

    files = package_files(pkg_dir)
    for path in files:
        lines = path.read_text().splitlines()
        # The file's leading `---` block (index 0 upward).
        header = []
        for line in lines:
            m = DOC_LINE.match(line)
            if not m:
                break
            header.append(m.group(1))
        header_doc = parse_doc(header) if header else {'summary': '', 'details': '', 'returns': '', 'examples': []}
        named = {}
        for line in header:
            m = NAMED_SUMMARY.match(line.strip())
            if m:
                named[m.group('name')] = m.group('summary').strip()
        if not description and header_doc['summary']:
            description = header_doc['summary']

        exports = [EXPORT_DECL.match(l).group('name') for l in lines if EXPORT_DECL.match(l)]
        # `export abs := __abs` is a facade re-export; the import line above
        # says where it comes from, which is the only documentation it has.
        origins = {
            m.group('alias'): (m.group('path'), m.group('orig'))
            for m in (REEXPORT_IMPORT.match(l) for l in lines)
            if m
        }
        decl_count = sum(
            1 for l in lines if OP_DECL.match(l) or AXIOM_DECL.match(l) or EXPORT_DECL.match(l)
        )
        stem = path.stem

        for i, line in enumerate(lines):
            entry = None
            for decl, kind in ((OP_DECL, 'op'), (AXIOM_DECL, 'axiom'), (EXPORT_DECL, 'export')):
                m = decl.match(line)
                if not m:
                    continue
                name = m.group('name')
                alias = None
                if kind == 'export':
                    sig, alias = split_export(m.group('rest'))
                else:
                    sig = m.group('sig').strip()
                block = doc_block_above(lines, i, DOC_LINE)
                if kind == 'axiom':
                    # A contract axiom carries its body *below* as `-- LAW:`
                    # comments (with an optional `guarantee:` line).
                    below, j = [], i + 1
                    while j < len(lines):
                        m = LAW_LINE.match(lines[j])
                        if not m:
                            break
                        below.append(m.group(1).strip())
                        j += 1
                    doc = {
                        'summary': named.get(name, ''),
                        'details': ' '.join(b for b in below if b),
                        'returns': '',
                        'examples': [],
                    }
                elif block:
                    doc = parse_doc(block)
                else:
                    # A file-level block documents the whole file: it is the
                    # doc of a one-declaration file, but a facade's header
                    # (`--- math -- numeric surface facade.`) must not become
                    # every re-export's summary.
                    fallback = named.get(name, header_doc['summary'] if decl_count == 1 else '')
                    doc = {'summary': fallback, 'details': '', 'returns': '', 'examples': []}
                origin = origins.get(alias) if alias else None
                entry = {'name': name, 'sig': sig, 'kind': kind, 'origin': origin, **doc}
                break
            if not entry:
                continue
            # A `src/<group>/*.hnl` file belongs to the `<group>` module;
            # top-level files default to the package itself.
            rel = path.parent.relative_to(pkg_dir)
            group = pkg if str(rel) == '.' else '.'.join(rel.parts)
            module = module_of(group, stem, entry['name'], exports)
            leaf = entry['name'].rsplit('.', 1)[-1]
            entry['full'] = f'{module}.{leaf}'
            modules.setdefault(module, []).append(entry)

    modules = {m: sorted(v, key=lambda e: e['name'].lower()) for m, v in modules.items() if v}
    if not modules:
        return None
    return {'pkg': pkg, 'slug': slug, 'description': description, 'modules': modules}


def write_module_page(out: Path, module: str, entries: list[dict]) -> None:
    md = [f'# {title_case(module)}', '']
    for e in entries:
        md.append(f'## `{esc(e["full"])}`')
        md.append('')
        if e['summary']:
            md.append(esc(e['summary']))
            md.append('')
        if e['details']:
            md.append(esc(e['details']))
            md.append('')
        if e['origin']:
            path, orig = e['origin']
            md.append(f'Re-export of `{esc(orig)}` from `{esc(path)}`.')
            md.append('')
        elif e['sig']:
            # `[f, args]` / `s` are parameter patterns; `A -> B` / `A ~[n]~> B`
            # are type signatures.
            if '->' in e['sig'] or '~>' in e['sig']:
                md.append(f'**Signature:** `{esc(e["full"])} : {esc(e["sig"])}`')
            else:
                md.append(f'**Signature:** `{esc(e["full"])}({esc(e["sig"])})`')
            md.append('')
        if e['returns']:
            md.append(f'**Returns:** {esc(e["returns"])}')
            md.append('')
        if e['examples']:
            md.append('**Examples:**')
            md.append('')
            md.append('```handl')
            md.extend(e['examples'])
            md.append('```')
            md.append('')
    out.write_text('\n'.join(md).rstrip() + '\n')


REPO_PREFIXES = ('lib-', 'host-', 'ext-', 'kit-', 'sdkgen-', 'compile-', 'engine-')


def package_name(repo: str) -> str:
    """The hnl package name for a one-package-per-repo checkout."""
    for prefix in REPO_PREFIXES:
        if repo.startswith(prefix):
            return repo[len(prefix):]
    return repo


def package_sources(repo_dir: Path, repo: str) -> list[tuple[str, Path, str]]:
    """`(pkg name, source dir, page slug)` for each package a repo ships.

    Three layouts (see module docstring): the multi-package
    `handl-packages/` tree, the one-package-per-repo `pkg.hnl` + `src/`
    layout, and `crates/<crate>/src/*.hnl` substrate packages.
    """
    out: list[tuple[str, Path, str]] = []
    hp = repo_dir / 'handl-packages'
    if hp.is_dir():
        out += [
            (d.name, d, f'lib-{slugify(d.name)}')
            for d in sorted(hp.iterdir())
            if d.is_dir() and d.name != 'generated'
        ]
    if (repo_dir / 'pkg.hnl').is_file() and (repo_dir / 'src').is_dir():
        out.append((package_name(repo), repo_dir / 'src', repo))
    if not out and (repo_dir / 'crates').is_dir():
        out += [
            (c.name, c / 'src', f'lib-{slugify(c.name)}')
            for c in sorted((repo_dir / 'crates').iterdir())
            if (c / 'src').is_dir() and package_files(c / 'src')
        ]
    return out


def main(argv: list[str] | None = None) -> int:
    import argparse

    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('--repo', default='host',
                    help='repo label (used for the output dir + URL prefix)')
    ap.add_argument('--packages-dir', type=Path, default=None,
                    help='directory of .hnl packages (default: resolve <org>/<repo> layout)')
    ap.add_argument('--out', type=Path, default=None,
                    help='output dir for this repo (default: <docs>/reference/<repo>)')
    args = ap.parse_args(argv)

    global PKGS, REF, URL
    if args.packages_dir is not None:
        sources = [
            (d.name, d, f'lib-{slugify(d.name)}')
            for d in sorted(args.packages_dir.iterdir())
            if d.is_dir() and d.name not in SKIP_DIRS
        ]
    else:
        sources = package_sources(ORG / args.repo, args.repo)
    if not sources:
        print(f'gen_reference: no package sources for {args.repo}')
        return 0
    PKGS = ORG / args.repo
    REF = args.out or (DOCS_ROOT / 'reference' / args.repo)
    URL = f'/reference/{args.repo}'

    packages = [p for p in (scan_package(d, pkg=n, slug=s) for n, d, s in sources) if p]
    # Guard: never overwrite the hand-maintained index with an empty one.
    if not packages:
        print('gen_reference: no documented declarations found in the package sources')
        print('  refusing to overwrite docs/reference.yaml with an empty index.')
        return 0

    REF.mkdir(parents=True, exist_ok=True)

    written = set()
    reference, sidebar = [], []
    for pkg in packages:
        mod_links = []
        for module, entries in pkg['modules'].items():
            page = f'{pkg["slug"]}-{module}'
            write_module_page(REF / f'{page}.md', module, entries)
            written.add(f'{page}.md')
            mod_links.append((title_case(module), page))

        index = [f'# {title_case(pkg["pkg"])}', '']
        if pkg['description']:
            index += [esc(pkg['description']), '']
        index += ['## Modules', '']
        index += [f'- [{t}](./{p})' for t, p in mod_links]
        (REF / f'{pkg["slug"]}.md').write_text('\n'.join(index).rstrip() + '\n')
        written.add(f'{pkg["slug"]}.md')

        reference.append({
            'title': title_case(pkg['pkg']),
            'slug': pkg['slug'],
            'description': pkg['description'],
            'include': [{'package': pkg['pkg']}],
        })
        sidebar.append({
            'text': title_case(pkg['pkg']),
            'collapsed': False,
            'link': f'{URL}/{pkg["slug"]}',
            'items': [
                {'text': t, 'link': f'{URL}/{p}'} for t, p in mod_links
            ],
        })

    # Drop pages this run did not produce — `<slug>*.md` and the legacy
    # `lib-*.md` pages are generator output; hand-written pages in the same
    # dir (index.md, host-concepts.md, …) are left alone.
    slugs = {p['slug'] for p in packages}
    for stale in REF.glob('*.md'):
        if stale.name in written:
            continue
        if stale.name.startswith('lib-') or any(
            stale.name.startswith(s) for s in slugs
        ):
            stale.unlink()

    # Per-repo fragments; scripts/gen_reference_all.py merges them into the
    # site-wide reference.yaml + .vitepress/sidebar-reference.mjs.
    (REF / 'reference.yaml').write_text(
        yaml.safe_dump({'reference': reference}, sort_keys=False)
    )
    (REF / 'sidebar.json').write_text(json.dumps(sidebar, indent=2) + '\n')
    print(f'Generated {len(packages)} packages, {len(written)} reference pages, sidebar.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
