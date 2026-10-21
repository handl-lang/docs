# The research stack — mlopt

<!-- provenance: research-mlopt:README.md@eea02f6 -->

::: info Rename note
`research-mlopt` is the current repo name; the plan renames it
**`graphopt`** at the phase-4 split (the `eqsat` substrate and the
`gamekit` game layer are carved out at the same time). Until then the
`research/` sections of this site point at `research-mlopt`.
:::

**mlopt** is a categorical optimizer for neural-network computation
graphs — and a machine that writes its own rewrite rules, certifies
them, and learns to play the game they create. Programs, rules, and
derivations are all values in one calculus (n-morphisms), so a minted
rule re-enters the bank as a legal move and discovery closes into a
self-modifying game under a certifying referee.

- [How mlopt works](./mechanism) — syntax → structure → search → certificate.
- [Evaluation: the fourth dimension](./evaluation) — describe, rank, measure — never decide equivalence.

## Cross-cutting concepts

These pages explain the pieces that cross repo boundaries:

- [The three costs](../cross-cutting/three-costs) — `dag_cost` guesses, fixtures measure, the verifier proves.
- [The game](../cross-cutting/the-game) — boards, players, episodes, and the learned-policy loop.
- [The gauntlet](../cross-cutting/the-gauntlet) — what a minted law must survive to ship.

## Learn by doing

The [research tutorial track](../../tutorials/research/) walks install
→ first `search()` → first minted law → the scorecard. The contract
surface is [the frozen API reference](../../reference/research/frozen-api);
upstream, the repository's own docs live at
[`handl-lang/research-mlopt/docs/`](https://github.com/handl-lang/research-mlopt/tree/main/docs).
