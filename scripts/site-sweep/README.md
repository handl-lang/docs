# site-sweep — the generator behind the 27-product docs

`emit.py` + `specs*.py` are what authored `docs/site/` in 23 public repos (the
other four already had sites and only got README pointers). They are kept here
so the files stay reproducible: the per-repo specs hold the *content* that the
emitter lays out into the four Diátaxis quadrants.

```bash
# from a checkout of the org root (all repos side by side)
python3 emit.py <repo>...        # no args = every spec
```

Each spec carries: `tagline`, `what`, `modules`, `api` (the reference table),
`howto` (title/prose/optional code), `why` (the explanation), and `tests`. The
reference rows are derived from the crate's module docs and public items — that
is the part worth keeping accurate when a crate changes.

`emit.py` is idempotent: re-running replaces the README's `## Documentation`
block instead of appending a second one.
