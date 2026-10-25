SPECS2 = {}

SPECS2["kit-prelude-lang"] = dict(
    tagline="The canonical eval-path `Language` as data — the ADR-0044 §6 end state.",
    what="""This crate embeds the authored YAML fragment files that *are* the language:
`tokens`, `grammar`, `eval`, `ast`, `globals`, `capabilities` and friends. There is
no Rust grammar and no Rust evaluator here — loading the crate yields a
`Language` value the engines interpret.""",
    modules=[("`data/*.yaml`", "the authored fragments: `ast`, `eval`, `globals`, `capabilities`, `caps`, tokens/grammar"),
             ("crate root", "`include_str!`s the fragments and exposes the assembled `Language`")],
    api=[("`Language` output", "the assembled definition every engine consumes"),
         ("`data/eval.yaml`", "the eval fragment set — scheme per node kind (ADR-0052 v2 kernel)"),
         ("`data/globals.yaml`", "the prelude binding surface"),
         ("`data/capabilities.yaml`, `data/caps.yaml`", "capability declarations the host gates on")],
    howto=[("Change the language",
            "Edit the YAML fragment and rerun the crate's tests: the fragments are the "
            "source of truth, so a semantic change is a data diff that reviewers can read.", ""),
           ("Add a fragment kind",
            "Add the file under `data/` and include it in the crate root; engines pick "
            "new fragment kinds up through `Language`, not through a new Rust API.", "")],
    why="""ADR-0044 ends with the language being *data*, not code: a host loads a
`Language` value, and lexing, parsing, transforming, typechecking and evaluation
are all engines over it. This repo is that end state for the canonical kit —
which is why it is a data crate with almost no Rust in it.""",
    tests="cargo test",
)

SPECS2["egraph"] = dict(
    tagline="The generic e-graph / equality-saturation substrate.",
    what="""`handl-egraph` is the reusable e-graph beneath the research stack: `EGraph`,
`Rewrite`, the compiled matcher, deterministic extraction, and the
applications/provenance machinery. It is a **by-contract** port of the proven
`catopt_core.egraph` Python spec — the Python is the specification, this crate
is the composable Rust substrate.""",
    modules=[("`egraph`", "`EGraph`, `Rewrite`, saturation loop, extraction"),
             ("`matcher`", "the compiled pattern matcher"),
             ("`term`", "`Term`, `TermAttr` and `from_kernel`/`to_kernel` bridges to the kernel")],
    api=[("`EGraph`", "add terms (`AddTermError`), saturate to a `Stop`, extract"),
         ("`Rewrite`", "a rewrite rule with its matcher and cost model"),
         ("`Stop` / `StopReason`", "saturation limit and why it ended"),
         ("`Term` / `TermAttr`", "the term representation with attribute plumbing"),
         ("`from_kernel` / `to_kernel`", "convert to and from the kernel's `Term`/`Value`"),
         ("`dag_cost`", "the extraction cost model"),
         ("`Application` / `Derived`", "provenance: which rule application derived a term")],
    howto=[("Run a saturation",
            "Build an `EGraph`, add rewrite `Rewrite`s, run until `Stop`, then extract; "
            "`StopReason` tells you whether it saturated or hit a limit, so a bounded "
            "run is never mistaken for a proof.", ""),
           ("Carry kernel terms in",
            "Use `from_kernel` so provenance keys stay comparable with the rest of the "
            "platform; `to_kernel` converts back at the boundary.", "")],
    why="""Equality saturation is the workhorse of the optimisation research: it searches
all equivalent programs at once instead of commuting rewrites. Keeping it generic
— and contract-ported from a proven spec rather than re-invented — means the
research stack and the compiler can share one substrate whose behaviour is
checkable against the Python reference.""",
    tests="cargo test",
)

SPECS2["discovery"] = dict(
    tagline="The pure-compute legs of catopt's discovery/gauntlet machinery.",
    what="""`handl-discovery` is the domain-free half of `catopt_discovery` (`oracle`,
`evidence`) and `catopt_core.rulecache`, composed over `handl-egraph`'s saturation
substrate. The port is **by contract, not by translation**: the Python is the
spec, this is the composable Rust version.""",
    modules=[("`oracle`", "site proposals, admission and scoring"),
             ("`evidence`", "attribute/tagged-value bridges and guard composition"),
             ("`rulecache`", "cache keys and memoised candidate enumeration")],
    api=[("`admit` / `SiteOutcome`", "whether a proposed rewrite site is admitted, and why"),
         ("`combos_at_sum`", "enumerate candidate combinations at a given sum"),
         ("`binding_envs`, `binding_envs_capped`", "binding environments for a pattern (optionally bounded)"),
         ("`compose_guards`", "combine guards into one predicate"),
         ("`cache_key`", "stable key for memoising rule-cache entries"),
         ("`dec_reexpr`, `dec_rule`", "decode re-expressions / rules from data"),
         ("`attr_from_data`, `attr_from_tagged`, `attr_to_data`", "attribute marshalling across the boundary")],
    howto=[("Bound a discovery search",
            "Use `binding_envs_capped` and a `Stop`-style budget so an open-ended "
            "enumeration cannot hang a run; the cap is part of the result, not a silent "
            "truncation.", ""),
           ("Reuse the rule cache",
            "Key entries with `cache_key` so identical rule sets across runs hit the "
            "same slots — the key is stable by construction, which is what makes "
            "cross-run reuse sound.", "")],
    why="""Discovery (proposing rewrite sites) is where research throughput comes from,
and it must be reproducible: the same seeds must yield the same candidates. The
pure-compute half is therefore split from the domain half (`catopt`) and ported by
contract, so the search semantics stay identical to the spec while the substrate
stays reusable.""",
    tests="cargo test",
)

SPECS2["host-tensor"] = dict(
    tagline="Host-side `tensor.*` functions: a dense n-d `f64` array for `.hnl` runtimes.",
    what="""Runtimes compose this component to give `.hnl` code tensor operations: a
dense n-dimensional `f64` array (row-major) behind the `tensor.*` op surface.
`src/index.hnl` is the single source of truth for the surface — the Rust side
implements exactly what that file declares. Catopt is the first consumer.""",
    modules=[("`src/index.hnl`", "the declared op surface — the contract the Rust implements"),
             ("`src/ops/`", "the Rust implementations (forward and backward passes)")],
    api=[("`tensor.from_list`, `tensor.ones`", "construction"),
         ("`tensor.add`, `tensor.mul`, `tensor.div`, `tensor.matmul`", "elementwise and matrix arithmetic"),
         ("`tensor.reshape`, `tensor.concat`", "shape manipulation"),
         ("`tensor.conv`, `tensor.max_pool`, `tensor.batch_norm`", "the layer ops"),
         ("`*_backward` variants", "gradients for every differentiable op"),
         ("`tensor.derive`", "run a backward pass given the upstream gradient")],
    howto=[("Add a tensor op",
            "Declare it in `src/index.hnl` first, then implement it in `src/ops/` and add "
            "its backward pass — the declaration is the contract the runtime loads.", ""),
           ("Wire tensors into a host",
            "Compose the plugin crate into the host's plugin list; `.hnl` code then calls "
            "`tensor.*` like any other host function.", "")],
    why="""Tensor code is the first real numerical workload on the platform, and it
belongs *outside* the language: a host composes the tensor component only if it
needs it, and the `.hnl` surface stays the same whether the backend is Rust f64
arrays or something faster later. Declaring the surface in `.hnl` keeps the
documentation and the implementation from drifting apart.""",
    tests="cargo test",
)

SPECS2["lib-char"] = dict(
    tagline="The character-library contract: the irreducible floor every backend satisfies.",
    what="""`char` is an **abstraction contract**, not an implementation: the axioms and
laws that every character backend must satisfy. All `str-handl` algorithms are
written on top of it, so swapping the backend (`char-native` on Rust
`std::char`, an ASCII-only one, a JS one, a future ICU one) changes semantics —
Unicode vs ASCII vs locale — without touching a single string algorithm.""",
    modules=[("`char`", "the contract module: predicates, transforms, indexing, code points")],
    api=[("`is_whitespace`, `is_alpha`, `is_alphanumeric`, `is_numeric`", "the predicates, named semantically"),
         ("`to_upper`, `to_lower`", "character transforms"),
         ("`at(s, i)`", "the i-th **character** — indices are never byte offsets"),
         ("`length`, `slice`, `concat`", "sequence operations"),
         ("`code_point` / `from_code_point`", "the only scalar-value access; backends may bound the range"),
         ("characters", "represented as 1-char strings — handl has no separate char type")],
    howto=[("Write a backend",
            "Implement the contract over your encoding and document which reading of "
            "`is_whitespace`/`is_alpha` you mean; do not special-case callers.", ""),
           ("Read an algorithm on top",
            "Assume only what the axioms state — char indices, 1-char strings, semantic "
            "predicate names — so the same `str-handl` code runs on every backend.", "")],
    why="""A string library written against `std::char` is welded to Rust. Writing it
against an axiom set makes the *semantics* a choice of backend: ASCII-only and
full-Unicode are both legitimate, they are simply different `char`
implementations. The contract says nothing about encoding (UTF-8/16/32) or about
Unicode vs ASCII vs locale on purpose — that is the backend's decision to
document.""",
    tests="hnl test (pure-handl contract; laws are exercised by the backends)",
)

SPECS2["lib-char-native"] = dict(
    tagline="The Rust `std::char` backend for the `char` contract.",
    what="""`char-native` implements the `char` contract over Rust's `std::char`, i.e. it
is the **Unicode-capable** backend: `is_whitespace`, `is_alpha` and friends are
read per the Unicode Character Database rather than per ASCII.""",
    modules=[("`handl-packages/`", "the Handl package that exposes the native ops to `.hnl` code"),
             ("`src/`", "the Rust implementations behind those ops")],
    api=[("`char.*` ops", "the contract surface, implemented over `std::char`"),
         ("Unicode semantics", "predicates and case transforms follow the Unicode Character Database"),
         ("`code_point` / `from_code_point`", "expose scalar values across the FFI boundary")],
    howto=[("Swap character semantics",
            "Replace this backend with an ASCII-only one and `str-handl` behaviour "
            "changes with it — no string algorithm needs editing.", ""),
           ("Add a native char op",
            "Extend the contract first (`lib-char`), then implement it here; the contract "
            "is what other backends must also satisfy.", "")],
    why="""The platform needs to run the same string library with different notions of
«letter»: a host may want ASCII for speed or Unicode for correctness. Keeping the
Rust `std::char` reading in a plugin makes that a composition decision instead of
a fork of the library.""",
    tests="cargo test",
)

SPECS2["lib-str-handl"] = dict(
    tagline="The `str` library, written in pure handl over the `char` floor.",
    what="""`str-handl` implements the string library **in handl itself**, one module per
function, over the `char` contract. Because the `char` floor decides what counts
as whitespace, alphabetic or uppercase, this library inherits Unicode-vs-ASCII
semantics from the composed backend rather than hard-coding one.""",
    modules=[("one module per function", "`capitalize`, `trim`, `split`, `replace`, `slugify`, …"),
             ("`*.test.hnl`", "each module ships its own tests")],
    api=[("`length`, `char_at`, `slice`, `concat`, `repeat`", "core access and construction"),
         ("`trim`/`trim_start`/`trim_end`/`trim_matches`, `strip_prefix`/`strip_suffix`", "edge handling"),
         ("`split`, `split_at`, `split_whitespace`, `lines`, `join`", "splitting and joining"),
         ("`find`, `rfind`, `contains`, `starts_with`, `ends_with`, `count`, `replace`, `replace_first`", "search"),
         ("`upper`, `lower`, `camel_case`, `snake_case`, `kebab_case`, `pascal_case`, `title_case`, `slugify`", "case and naming"),
         ("`pad_left`, `pad_right`, `truncate`, `word_wrap`", "presentation"),
         ("`levenshtein`, `similarity`", "distance")],
    howto=[("Add a string function",
            "Add `src/<name>.hnl` plus `src/<name>.test.hnl`; depend only on `char` "
            "operations so every backend keeps working.", ""),
           ("Use it in a project",
            "Declare the dependency (`str-handl = { … }`) and import the function's "
            "module; each function is its own module, so imports stay narrow.", "")],
    why="""Implementing the library in handl is the point: it dogfoods the language on a
real workload, and because it targets the `char` contract rather than Rust, the
same source runs on every backend. Swapping `char-native` for an ASCII backend
changes `slugify`'s output without editing `slugify`.""",
    tests="hnl test src/ (each module ships `*.test.hnl`)",
)

SPECS2["lib-desugar"] = dict(
    tagline="The `desugar` transform-pass source, embedded by `plugin-lib-handl`.",
    what="""This repo carries the **desugar pass as handl data**: the `TransformDef`s the
runtime applies to surface syntax before evaluation. It is not a library a user
imports — `plugin-lib-handl` embeds it and hands the rules to
`engine-transform-rewrite`, so the pass can change without a runtime rebuild.""",
    modules=[("`src/index.hnl`", "the transform definitions (the pass source)"),
             ("`src/lib.rs`", "the embedding shim that exposes the source to the plugin")],
    api=[("transform definitions", "the rules themselves — data, reviewed as data"),
         ("`desugar` pass", "the named pass the rewrite engine runs before eval")],
    howto=[("Change a desugaring",
            "Edit the transform definitions and rerun `plugin-lib-handl`'s tests; the "
            "engine needs no change, and the diff shows the rule that moved.", ""),
           ("Debug a surprising expansion",
            "Run the pass alone and diff the AST before/after — the rewritten arena "
            "names the rule that fired.", "")],
    why="""Desugaring used to live inside the runtime, so changing it meant changing
Rust. Moving the pass source into its own repo (ADR-0128 split) makes the pass
inspectable and versionable, and keeps the runtime a consumer of passes rather
than their owner.""",
    tests="cargo test (embedding) + the plugin's transform tests",
)

SPECS2["lib-loader"] = dict(
    tagline="The pure-handl module loader, embedded by `plugin-lib-handl`.",
    what="""`loader.hnl` resolves module imports at runtime — the module chain, import
splicing and name resolution — implemented in handl itself. Like the desugar
pass it is embedded by `plugin-lib-handl` rather than imported by users.""",
    modules=[("`src/index.hnl`", "the loader: module discovery, import resolution, name binding")],
    api=[("module resolution", "map an import path to the module that satisfies it"),
         ("import splicing", "bind `import`/`from … import` names into the module scope"),
         ("module chain", "walk the resolved dependency chain deterministically")],
    howto=[("Follow an import",
            "Trace the loader's resolution for a concrete path — a resolution "
            "surprise is almost always a name mapping, not a missing file.", ""),
           ("Change resolution rules",
            "Edit `loader.hnl` and rerun the plugin's tests; the loader is data the "
            "runtime evaluates, so no Rust rebuild of the loader is needed.", "")],
    why="""A loader written in the language it loads keeps the module system inside the
same semantics as user code: resolution is evaluated, not special-cased in Rust.
Separating it into its own repo makes that surface small enough to review.""",
    tests="hnl test / plugin integration tests",
)

SPECS2["kernel"] = dict(
    tagline="The arrow-calculus substrate: language schema, tagged values, extension ABI, floor libs.",
    what="""The kernel is the platform's smallest layer (ADR-0040): the `Language` data
schema and staged `lex`/`parse`/`eval` dispatch signatures (ADR-0044, language as
data), the tagged `Value` representation the engines share, the dynamic extension
ABI (`hnl` extensions, ADR-0149), and the `handl-lib-*` floor packages.

What is *not* kernel: engines, emitters, kits, plugins and hosts. They live in the
`engine-*`, `kit-*` and `host` repos and depend on the kernel, never the reverse.""",
    modules=[("`crates/handl-language`", "the `Language` schema + staged lex/parse/eval dispatch signatures"),
             ("`crates/handl-value`", "the tagged `Value` representation shared by engines"),
             ("`crates/handl-ext`", "the shared ABI for dynamic `hnl` extensions (ADR-0149)"),
             ("`crates/defining-handl`", "self-hosting infrastructure (ADR-0044 phase 8)"),
             ("`crates/{bytes,cmp,combinators,error,mood,obj,ops,prim,prim-handl,type}`", "the `handl-lib-*` substrate packages")],
    api=[("`handl_language::Language`", "the language value: tokens, grammar, eval schemes, globals, capabilities"),
         ("`handl_language::Ast` / `AstRef`", "the arena and its handle"),
         ("`handl_value::Value` / `TaggedValue`", "the tagged value representation"),
         ("`hnl_engine::LanguageView`", "the object-safe view engines use (`handl-language` implements it)"),
         ("`handl_lib_*` packages", "the floor libraries every host gets for free")],
    howto=[("Consume the kernel",
            "Depend on `handl-lang/kernel` at branch `main`; for local development the "
            "consumer's `[patch]` table points at `../kernel` (regenerated by "
            "`host/scripts/dev-link.sh`).", ""),
           ("Add a language fragment",
            "Extend the `Language` schema in `handl-language`, then teach the engines — "
            "the schema is the contract, so an engine change is expected to follow a "
            "schema change, not the other way round.", "")],
    why="""Everything above the kernel has to agree on what a language *is* and what a
value *is*; the kernel is that agreement and nothing else. It was extracted from
the `host` workspace (ADR-0128) so a consumer can pin the substrate without
pulling the whole host, and it depends only on `hnl-engine` — which is why the
dependency arrows all point downwards.""",
    tests="cargo test --workspace",
)

SPECS2["slidev-theme"] = dict(
    tagline="A Slidev theme in the handl docs look.",
    what="""`slidev-theme-handl` is a Slidev theme matching this documentation site:
Source Sans 3 / Source Code Pro, an oklch green ramp on black and white, square
corners and the `>>>` prompt motif. Forked from `slidev-theme-lfds`.""",
    modules=[("`layouts/`", "slide layouts (cover, section, two-column, quote, ...)"),
             ("`components/`", "theme components"),
             ("`styles/`", "the palette and typography"),
             ("`setup/`", "theme setup (fonts, shiki config)")],
    api=[("`theme: handl`", "the frontmatter switch that selects this theme"),
         ("layouts", "named layouts usable as `layout: <name>`"),
         ("styles", "oklch green ramp, square corners, `>>>` prompt motif"),
         ("fonts", "Source Sans 3 (text), Source Code Pro (code)")],
    howto=[("Use the theme",
            "Install from GitHub and set `theme: handl` in the deck frontmatter.",
            "npm i -D github:handl-lang/slidev-theme"),
           ("Match the docs exactly",
            "Reuse the same font pairing and palette as the site: the theme is the "
            "single place those tokens live, so a deck cannot drift from the docs look.", "")],
    why="""Talks about the platform kept being restyled by hand; a theme makes the
presentation look a property of the project rather than of whoever prepared the
slides. It is a thin fork on purpose — only the tokens differ.""",
    tests="slidev build (see package.json scripts)",
)
