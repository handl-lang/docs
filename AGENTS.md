# docs — the `handl-lang` documentation hub

One place to find the platform's published docs — the kernel, the
engines, the composable host, and the research stack — plus every
public repo's project docs. This repo owns the **published**
documentation surface; the decision records themselves live with the
repo that made them.

## Layout

| path | role |
| --- | --- |
| `index.md`, `adrs/`, `handl/`, `api/`, `paradigm/`, `ecosystem/`, `engines/`, `members/` | the VitePress site (org level) + generated reference output |
| `scripts/` | generators: `gen_reference_all.py`, `gen-api.sh`, `gen-docs-index.py`, `vendor-docs.py` |
| `scripts/public_repos.py` | the publish allowlist — all three generators import it (single source of truth) |
| `ci/` | trigger/deploy scripts (`docs-trigger.sh`, `trigger.sh`, `paper-build.sh`) |
| `package.json` / `bun.lock` | bun + VitePress (`next`) site |

## Contract

- **Publication boundary:** every public repo (204 today) gets docs;
  private repos (`host-lsp`, `extension-*`, `pitch-*`, `project`,
  `playground`, …) produce no pages, links, or mentions. Membership
  rule: public on GitHub.
- `research-mlopt` publishes under the `mlopt` slug.

## Verification

```bash
bun install
bun run docs:dev        # vendor + vitepress dev
bun run docs:build      # vendor + vitepress build
bun run docs:gen-ref    # regenerate reference pages
bun run docs:gen-api    # regenerate API pages
```

<!-- myco:agent-awareness -->

## Agent awareness

- Session start / any work discussion: run `myco status --prompt`
  before proposing next steps — know the board first.
- User describes new work → offer to capture it (`myco todo add`,
  `issue new`, `proposal new`). Don't wait to be asked.
- Picking up a task: `myco resume <ID>` is the briefing.
- Wrapping up: `myco handoff <ID>` anything resumable; keep statuses
  honest (claimed → in-progress → blocked/done).

<!-- /myco:agent-awareness -->
