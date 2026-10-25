SPECS = {}

SPECS["engine"] = dict(
    tagline="Foundation types for every pluggable engine: `Term`, `Model`, and the arena view.",
    what="""The substrate every other `engine-*` crate builds on. It defines the **`Term`**
algebra used to express eval schemes, the **`Model`** trait an engine implements,
and a minimal, object-safe **arena view** (`AstRef` / `AstNode` / `LanguageView`)
that lets a model inspect an AST without depending on `handl-language` — which
would be a dependency cycle, since `handl-language` already depends on
`hnl-engine` for `Term`.""",
    modules=[("`term`", "`Term`, `ArrSource`, `Side`, `RewriteWitness`, handler elimination"),
             ("`term_data`", "`TermData` — the owned, inspectable form of a term"),
             ("`term_interpreter`", "`interpret` — the generic scheme interpreter"),
             ("`nbe`", "normalization-by-evaluation helpers shared by the typecheckers")],
    api=[("`Term`", "the arrow-calculus term algebra every scheme is written in"),
         ("`Model` / `ModelCtx`", "the trait an engine implements, and the context it is handed"),
         ("`LanguageView`", "object-safe read-only view over a language definition (ADR-0081)"),
         ("`AstRef` / `AstNode`", "arena handle + placeholder node — cycle-free by construction"),
         ("`interpret`", "interpret a `Term` against a `Model`"),
         ("`EvalError` / `LangError`", "failure kinds surfaced by interpretation")],
    howto=[("Add a new engine",
            "Implement `Model` for your engine type and let `interpret` drive it; the "
            "`engine-*` crates are the worked examples — no per-kind Rust branching.",
            """struct MyModel;
impl Model for MyModel {
    // resolve the scheme's term for a node kind;
    // `interpret` then executes it generically.
}"""),
           ("Inspect an AST without a cycle",
            "Take `AstRef` + `LanguageView` instead of `handl_language::Ast`; the view "
            "resolves child positions by named role (ADR-0081).", "")],
    why="""Engines are *data-driven*: a language definition supplies schemes and the
engine interprets them (ADR-0044, «language as data»). That needs one shared term
algebra — otherwise every engine invents its own node enum and kits can no longer
swap engines. `hnl-engine` is that algebra, kept dependency-free so both the
kernel (`handl-language`, `handl-value`) and every engine can sit above it
without cycles.""",
    tests=None,
)

SPECS["engine-exec"] = dict(
    tagline="The eval-operation contract: `Eval`, `EvalRequest`, `EvalEngine`.",
    what="""The **abstraction crate** for the eval operation (ADR-0044 §3, §4, §7):
the `Eval` operation marker, the `EvalRequest` an engine receives, and the
`EvalEngine` trait it implements. **No interpreter lives here.** The concrete
engines are `engine-exec-tree-walk` (reference interpreter) and
`engine-exec-bytecode` (stack VM), which must agree value-for-value.""",
    modules=[("`io`", "the `IO` effect surface: handler frames, resume, accumulation"),
             ("`native_ops`", "the native operation table an engine dispatches to"),
             ("`pattern_match`", "`try_pattern` — shared pattern matching on a growable stack")],
    api=[("`Eval`", "zero-sized operation marker that namespaces the eval stage"),
         ("`EvalRequest`", "the AST + language + context an engine is asked to evaluate"),
         ("`EvalEngine`", "the trait an eval engine implements"),
         ("`JOURNAL_FRAME_KEY`, `RESUME_KEY`, `HANDLER_ACC_KEY`", "value keys carrying resumable-handler state (ADR-0158)"),
         ("`Num`, `OpService`", "numeric helpers and the operation-dispatch service"),
         ("`apply_native_op`, `apply_handler_impl`", "the shared dispatch path both engines use")],
    howto=[("Implement an eval engine",
            "Implement `EvalEngine` and register it under the kit's `eval` operation "
            "slot. The shipped engines are thin: they reuse this crate's dispatch and "
            "differ only in how they walk or execute the scheme.", ""),
           ("Pattern-match deep values safely",
            "Use `pattern_match::try_pattern`; it grows the stack at `STACK_RED_ZONE` "
            "instead of overflowing, so deeply nested values are bounded by total "
            "growable stack rather than the platform stack.", "")],
    why="""Splitting eval into *abstraction* (`engine-exec`) and *engines*
(`…-tree-walk`, `…-bytecode`) is what makes the backend swappable: a kit registers
an engine under one operation name and the same language definition runs on the
interpreter or the VM. The abstraction owns the parts that must not diverge —
handler/journal keys, native dispatch, pattern matching — so conformance between
backends is structural rather than coincidental.""",
    tests=None,
)

SPECS["engine-lex"] = dict(
    tagline="The lex-operation contract: `LexerEngine`, `LexerRequest`, `Lexer`.",
    what="""The **abstraction crate** for the lex operation (ADR-0044 §1, §3): the
`LexerEngine` trait, the `LexerRequest` describing what to tokenize, and a
`Lexer` handle. It contains **no lexing logic** — the data-driven implementation
is `engine-lex-pattern`.""",
    modules=[],
    api=[("`LexerEngine`", "the trait a lexer implements"),
         ("`LexerRequest`", "source text + language + position, as handed to an engine"),
         ("`Lexer`", "handle over an engine; `new` / `with_options` construct it")],
    howto=[("Implement a lexer",
            "Implement `LexerEngine`; return tokens plus the advanced position. Keep "
            "policy — patterns, priority, block forms — in `Language` data rather than "
            "in the engine, as `engine-lex-pattern` does.", "")],
    why="""Lexing is the first place a language definition has to *be* data: token shapes
are declared per language and swapping the lexer must be a data change, not a
recompile. The abstraction is deliberately tiny so alternative lexers
(regex-based, hand-rolled, streaming) stay possible.""",
    tests=None,
)

SPECS["engine-parse"] = dict(
    tagline="The parse-operation contract: `ParserEngine`, `ParserRequest`, `ParserContext`.",
    what="""The **abstraction crate** for the parse operation (ADR-0044 §3): the
`ParserEngine` trait, the `ParserRequest`/`ParserContext` an engine receives, and a
`Parser` cursor helper. **No grammar logic lives here** — the concrete engine is
`engine-parse-pratt`, which reads grammar rows from the language definition.""",
    modules=[],
    api=[("`ParserEngine`", "the trait a parser implements"),
         ("`ParserRequest`", "tokens + language the engine parses"),
         ("`ParserContext`", "per-parse state: arena, position, diagnostics"),
         ("`Parser`", "lexed-token cursor: `advance`, `peek`, `pos`, `tokens`, `expression`")],
    howto=[("Implement a parser",
            "Implement `ParserEngine` and produce an `Ast` arena. Follow "
            "`engine-parse-pratt`'s root-node convention so downstream passes can "
            "rely on it.", "")],
    why="""Parsing is where the grammar-as-data story pays off: `engine-parse-pratt`
drives a Pratt loop from `GrammarRow`s rather than from hard-coded Rust methods,
so a language changes its operator precedence table without a rebuild.""",
    tests=None,
)

SPECS["engine-transform"] = dict(
    tagline="The AST-transform contract: `TransformEngine`, `TransformMode`, arena helpers.",
    what="""The **abstraction crate** for the AST transform operation (ADR-0094):
`TransformEngine`, `TransformMode`, and the arena navigation helpers (`node_ref`,
`child_ref`, `descendant_ref`, `child_is_kind`, `contains`) that implementations
share. The rule-interpreting implementation is `engine-transform-rewrite`.""",
    modules=[],
    api=[("`TransformEngine`", "the trait a pass engine implements"),
         ("`TransformMode`", "how a pass applies: rewrite vs overlay"),
         ("`install_transform_overlay`", "install a rewritten arena as the new AST"),
         ("`node_ref`, `child_ref`, `descendant_ref`, `child_is_kind`, `contains`", "arena navigation without holding borrows"),
         ("`declined`, `out`, `ast`, `lang`", "result and context accessors")],
    howto=[("Write a transform pass",
            "Implement `TransformEngine`, or reuse `engine-transform-rewrite`'s rule "
            "loop; return `declined` when nothing matched so the caller can skip "
            "re-running.", ""),
           ("Replace the AST safely",
            "Use `install_transform_overlay`: it keeps the old arena alive for nodes "
            "the pass did not rewrite.", "")],
    why="""Desugaring, lowering and rewrite passes all want the same thing: walk an arena
bottom-up, remap changed nodes, hand back a new root. Extracting that shape once
(ADR-0094) turned the legacy `desugar_pass` into a reusable engine and made
passes registerable data.""",
    tests=None,
)

SPECS["engine-typecheck"] = dict(
    tagline="The typecheck contract (`TypecheckEngine`) plus the bootstrap checker.",
    what="""The **abstraction crate** for the typecheck operation (ADR-0054 §3):
`Typecheck`, `TypecheckRequest`, `TypecheckResult`/`TypecheckReport`,
`TypecheckEngine`, and the `check_module` entry point `hnl typecheck` calls.

Unlike the other abstraction crates this one *does* ship a checker — a small
**bootstrap** implementation used when no engine is registered. The production
engine is `engine-typecheck-nbe`, registered by the canonical kit as `"nbe"`.""",
    modules=[("`bootstrap`", "the bootstrap checker: structure + obvious type errors only")],
    api=[("`TypecheckEngine`", "the trait a checker implements"),
         ("`TypecheckRequest` / `TypecheckResult`", "input (AST, language, options) and output (diagnostics, accepted AST)"),
         ("`TypecheckReport` / `TypecheckDiagnostic`", "structured, renderable diagnostics"),
         ("`check_module`, `check_module_with_prelude`", "convenience entry points, optionally seeding a prelude"),
         ("`CheckError`, `is_clean`", "failure kind, and the quick «no diagnostics» test")],
    howto=[("Run the checker from Rust",
            "Call `check_module(&ast, &lang, options)`; the report's diagnostics carry "
            "spans, which is how `hnl typecheck` renders `file:line:col`.",
            """let report = hnl_engine_typecheck::check_module(&ast, &lang, options);
if !report.is_clean() {
    for d in &report.diagnostics { eprintln!("{d}"); }
}"""),
           ("Register a real engine",
            "Publish the engine under the `typecheck` operation slot in the kit "
            "manifest; `hnl typecheck` then prefers it over the bootstrap.", "")],
    why="""Typechecking must work before a language has registered a checker — otherwise
`hnl typecheck` on a fresh kit produces nothing at all. The bootstrap is
deliberately shallow (structure and obvious mismatches) and exists to be
*replaced*: dependent types, instance search and handler typing live in the NBE
engine.""",
    tests="cargo test",
)

SPECS["engine-lex-pattern"] = dict(
    tagline="The data-driven lexer: every pattern comes from the language definition.",
    what="""A lexer engine with **no Rust lexing logic**. It collects `LexerRuleDef`
fragments from the `Language`, sorts them by `priority` ascending, and applies
them: literals, character classes, numbers and delimited blocks are all data.
Swapping the lexer is a change to `lexer_rules`, not a recompile (ADR-0044
§1, §3).""",
    modules=[],
    api=[("`LexerRuleDef` input", "rule fragments read from `Language::lexer_rules`"),
         ("priority ordering", "lowest `priority` wins first; ties keep declaration order"),
         ("`LexerEngine` impl", "the `engine-lex` contract, satisfied without hard-coded patterns")],
    howto=[("Add a token kind",
            "Add a `LexerRuleDef` fragment with a `priority` below the catch-all rules; "
            "no Rust change is needed.", ""),
           ("Debug a tokenization surprise",
            "Dump the collected rules sorted by priority — most surprises are an "
            "ordering tie, not a missing rule.", "")],
    why="""Hand-written lexers put grammar knowledge in Rust, so every language variant
needs a fork. Reading the rules from data keeps one engine for all languages and
makes grammar reviewable as data.""",
    tests="cargo test",
)

SPECS["engine-parse-pratt"] = dict(
    tagline="The Pratt parser: top-down operator precedence driven by grammar data.",
    what="""The parse engine used by the canonical kit. It looks up `GrammarRow`s by
`(token, position)` and drives a classic top-down operator-precedence loop. It
never calls a Rust `rule.prefix(token, ctx)`: prefix/infix kind, binding powers and
child shape are read from the descriptor and executed (ADR-0044 §3).""",
    modules=[],
    api=[("`GrammarRow` input", "prefix/infix descriptors keyed by token and position"),
         ("`Ast` output", "arena of nodes; the **root node is the last node** of the arena"),
         ("`ParserEngine` impl", "the `engine-parse` contract")],
    howto=[("Add an operator",
            "Add grammar rows for the token with its left/right binding power; a "
            "precedence change is a data edit, not a code edit.", ""),
           ("Consume the parse result",
            "Read the root as the arena's **last** node — this engine appends children "
            "before their parents.",
            """let ast = engine.parse(&request)?;
let root = ast.last().expect("parser always emits a root");""")],
    why="""Pratt parsing is compact and handles precedence without a rule per level;
driving it from `GrammarRow` data keeps precedence in the language definition,
where grammar readers can see it.""",
    tests="cargo test",
)

SPECS["engine-exec-tree-walk"] = dict(
    tagline="The reference interpreter for the eval operation.",
    what="""The **reference** eval engine. It interprets the arrow-calculus `Term` kernel
directly: look up `lang.eval[node.kind]` → `EvalSchemeDef` → `Term`, then
interpret the scheme. Entirely data-driven, and the oracle the bytecode engine is
conformance-tested against (ADR-0044 §3, §4; ADR-0052).""",
    modules=[],
    api=[("value shapes", "tagged JSON pair `__pair__` and friends — the values combinators operate on"),
         ("`EvalEngine` impl", "the `engine-exec` contract"),
         ("handler support", "resumable `handle`/`perform` via the shared journal keys (ADR-0158)")],
    howto=[("Trace an evaluation",
            "Dispatch is `kind → scheme → interpret`, so log the scheme term for the "
            "node kind before interpreting it — the term names the exact rule applied.", ""),
           ("Keep backend parity",
            "Change evaluation semantics here first and let the bytecode conformance "
            "tests follow: this engine is the reference.", "")],
    why="""A reference interpreter without compilation keeps the semantics legible: if a
language definition and this engine disagree, the definition is wrong. The
bytecode engine exists for speed and must match this one exactly — that pairing
is what lets the platform optimise without redefining the language.""",
    tests="cargo test",
)

SPECS["engine-exec-bytecode"] = dict(
    tagline="The bytecode eval engine: compile `Term` to bytecode, run it on a stack VM.",
    what="""Compiles `Term` (the v2 arrow-calculus kernel, ADR-0052) to a bytecode
representation and executes it on a stack-based VM. It shares the `Term`
vocabulary with `engine-exec-tree-walk`, and conformance tests require both to
produce **identical results** (ADR-0044 §4, §7).""",
    modules=[("`vm`", "the stack machine: frames, resumable `perform`, accumulated handlers (ADR-0158)"),
             ("`compile`", "`Term` → bytecode, erasing per-node data dispatch")],
    api=[("`EvalEngine` impl", "the `engine-exec` contract"),
         ("bytecode compilation", "scheme lookup happens at compile time, not per node"),
         ("conformance suite", "shared cases asserting parity with the tree-walk engine")],
    howto=[("Add an instruction",
            "Add the opcode, its compile case and its VM case, then extend the "
            "conformance suite so the tree-walk engine stays the oracle.", ""),
           ("Debug a divergence",
            "Run the failing case on both engines and diff the produced values: a "
            "mismatch means the compile step erased semantics the VM does not restore.", "")],
    why="""The tree-walk pays for `lang.eval[node.kind]` on every node. Compiling to
bytecode moves that dispatch to compile time, which is where the speedup comes
from — but only if the VM reproduces the interpreter exactly, which the shared
conformance tests enforce.""",
    tests="cargo test",
)

SPECS["engine-transform-rewrite"] = dict(
    tagline="The rule-interpreting transform engine (ADR-0094).",
    what="""The first `TransformEngine` implementation: it walks a pass's `TransformDef`s
bottom-up over the `Ast` arena with a `remap` old→new index table — the proven
`apply_desugar` algorithm generalised to any named pass. Dispatch is a
`kind → Vec<TransformDef>` table built once per pass; there are no `kind ==`
checks in the engine core.""",
    modules=[],
    api=[("`RewriteEngine::run_pass`", "run one named pass over the arena"),
         ("`TransformRule::Native(name)`", "dispatch a rule to a wired `NativeRewrite`"),
         ("`with_desugar_natives`", "install the built-in desugar native rules"),
         ("`RuleSource`", "where a pass's `TransformDef`s come from")],
    howto=[("Add a rewrite pass",
            "Declare `TransformDef`s in the language/kit data and run them through "
            "`run_pass`; keep natives for what data cannot express.", ""),
           ("Write a native rule",
            "Implement `NativeRewrite` and register it with `with_desugar_natives` (or "
            "your own set); rules stay addressable by name from data.", "")],
    why="""The desugarer was a one-off; most later passes had the same shape (bottom-up,
remap, replace root). Generalising it into an engine turned passes into data and
let kits compose them, while natives stayed the escape hatch for host-side
operations.""",
    tests="cargo test",
)
