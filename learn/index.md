# The Handl type system

One calculus for programs, proofs, types, effects, and modes. There is
no separate type-theoretic subsystem and no second language for specs
or checks: **everything is data**, the same evaluator computes types
and terms, and the typechecker itself is a program in the language it
checks. Equality, transport, univalence, composition, and mode
arithmetic all *compute* — and the same computation runs at typecheck
time and at run time.

Every judgement has the form `t : A @ μ`: a type `A` plus an ambient
mode `μ`, a set of applications of declared algebras (`[]` is pure).
Modes are the unifying frame — grades, coeffects, and effects are all
instances of the same mechanism, developed in the Modes section. The
sections before it are type structure; the sections after it are
specializations.

## Core: one binder, one arrow

```hnl
x := 42
id : Nat ~> Nat := n ~> n
pair := [1, "two"]
rec := { name: "luis", age: 30 }
```

`:=` is the only binder. `~>` is the only arrow: terms and types share
it, and data declarations are `new` expressions. Module forms such as
`export` control visibility only; they play no role in typing.

## Inductive families

```hnl
Nat := new Inductive {
  zero : Nat,
  succ : (pred : Nat) ~> Nat
}

Vec<n : Nat, a : Type> := new Inductive {
  vnil  : Vec(0, a),
  vcons : (x : a, xs : Vec(n, a)) ~> Vec(n + 1, a)
}

v1 : Vec<2, Bool> := vcons(true, vcons(false, vnil))
```

`<n : Nat, a : Type>` declares indexed families. `Vec(2, Bool)` is a
`family_app` whose indices **compute**: `Vec<1+1>` is `Vec<2-0>` is
`Vec<2*1>`, and all check against the same value.

## Inductives as data

An inductive specification is itself a value: an `inductive.spec`
record of constructor signatures as owned type expressions. Specs can be
computed, composed, inspected, and passed to generic eliminators; the
same spec drives `match` refinement and `F.rec`-style folds. Positivity
is a checker judgment over the spec value, not a parse-time native.

## Dependent types: Π and Σ

```hnl
-- Π: a typed-binder arrow in type position
idp : (x : Nat) ~> Nat := x ~> x
curried : (x : Nat, y : Bool) ~> Nat := x ~> y ~> x

-- Σ: a typed-binder list with no arrow is a dependent pair
one_vec : (m : Nat, v : Vec(m, Bool)) := [succ(zero), vcons(true, vnil)]
prod : (x : Bool, y : String) := [true, "hi"]
```

## Dependent elimination: match

```hnl
vtail<n, a> : Vec<n + 1, a> ~> Vec<n, a> :=
  v ~> match v { vcons(x, xs): xs }

vhead<n, a> : Vec<succ n, a> ~> a :=
  v ~> match v { vcons(x, xs): x }

is_nil : Vec<n, a> ~> Bool :=
  v ~> match v { vnil: true, vcons(x, xs): false }
```

Under `vcons`, the checker refines `n ≡ ?k+1`, binds `xs : Vec<?k, a>`,
and records a proof-relevant `eq_n` path witness. Impossible arms are
decided: `vnil: absurd` checks iff the branch's index equations are
unsatisfiable.

## Eliminators and motives

Family eliminators are visible to the checker:

```hnl
len_via_rec : Nat := Vec.rec(null, zero, step)(2, Bool, v1)
```

And motives can be stated explicitly:

```hnl
id_vec : (n : Nat) ~> (v : Vec(n + 0, Bool)) ~> Vec(n + 0, Bool) :=
  n ~> v ~> match v return (i, w) ~> Vec(i, Bool) with {
    vnil:    J eq_n, (i2, w2) ~> Vec(i2, Bool), v,
    vcons(x, xs): eq_n # v
  }
```

## Equality: paths are data

```hnl
p : Path(1, 1) := refl
moved : Nat := p # zero
transported : Nat := transport(p, zero)

tt : Path(Nat, zero, succ(succ(zero))) := trans pt, qt
st := symm(tt)
jv : Vec<2, Bool> := J p22, (i, w) ~> Vec(i, Bool), v2
```

Unification itself consumes in-scope paths: `P[frm]` against `P[to]`
succeeds when a `Path` bound in the environment justifies the rewrite.
Equality is weak and proof-relevant, never erased: transport along a
path *is* substitution.

## Cubical structure

Paths are not an axiomatized identity type; they are terms over an
interval `I`, and the Kan operations that make them compute are
ordinary primitives:

```hnl
cp : Path(Bool, true, true) := i ~> true
t1 := transp Pi(I, i ~> Bool), i0, fF, true
h1 : Bool := hcomp Bool, i0, fF, true, false
y : unglue(Glue(Bool, fF, Pi(I, i ~> Bool))) := true
pfB : isFibrant(Bool) := fibrant Bool
```

`transp` is transport in a type family along a dimension, partial on a
face; `hcomp` is homogeneous composition over a single type; `Glue` and
`unglue` glue types along equivalences; `fibrant` is the fibrancy
predicate the Kan structure is stated over.

## Univalence computes

```hnl
eBN : Equiv(Bool, Nat) := { to: x ~> zero, fro: y ~> true }
tv : Nat := ua(eBN) # true        -- transport applies `to` and reduces
tb : Bool := symm(ua(eBN)) # zero
```

`ua(e)` mints a path over the interval carrying the recorded equivalence;
transport along it applies the equivalence's functions. Univalence is a
value, not an axiom.

## Higher categories: dimension arrows

```hnl
comp_assoc := (a,b,c) ~> ((a >>>[2] b) >>>[2] c)
                    ~>[3]~> (a >>>[2] (b >>>[2] c))

interchange := (al,al2,be,be2) ~>
  ((al =>| al2) =>> (be =>| be2)) ~>[3]~>
  ((al =>> be) =>| (al2 =>> be2))
```

`~>[n]` is the dimension-n arrow `Hom(n, ·, ·)`, consistent with
`>>>[k]` composing k-cells. `Path` itself is defined as a Sigma of
2-cells, their inverses, and coherence 3-cells; associativity,
unitality, and interchange are *typechecked equations*, verified
definitionally by normalization.

## Modes: the unifying frame

Modes unify grades, coeffects, and effects onto one axis — the same
mechanism the judgement form `t : A @ μ` introduced above. Every mode
ascription is `@ [Algebra(payload), …]`: a **set** of applications of
declared algebras. An algebra is an ordinary type, a record of
`compose`/`unit`/`order` functions:

```hnl
Cost := new Algebra(Nat) {
  compose: (a, b) ~> a + b,
  unit:    0,
  order:   (a, b) ~> a <= b
}

double : (Nat ~> Nat) @ [Cost(2)]
f : (Nat ~> Nat) @ [Cost(3)]
g : (Nat ~> Nat) @ [Cost(5)]
h := g >>> f        -- : (Nat ~> Nat) @ [Cost(8)]
```

Each element's head selects its algebra: `Cost(3)` composed with
`Cost(5)` dispatches to the `Cost` instance's `compose`, so
composition *computes* the mode. The set holds one element per
algebra — order is irrelevant and duplicate heads are rejected.
Subsumption is one judgement-level `order` check per algebra, shared
by every mode dimension alike. Modes are data, so algebras are
computable: transformers, products, and mode expressions are ordinary
functions returning algebra records.

```hnl
mapM : (m : Mode) ~> (f : (A ~> B) @ m) ~> (List(A) ~> List(B)) @ m
costed := mapM([Cost(1)], double)   -- mode polymorphism by substitution
```

`~>[n]` remains the dimension arrow: globular structure, a different
axis from modes. A cell type takes `@` like any type —
`e : (f ~[2]~> g) @ [Cost(3)]` is a cost-graded 2-cell.

## Effects: the `Effects` algebra

Effects are not a separate system — they are one algebra instance on
the mode axis:

```hnl
printLn : (Str ~> Str) @ [Effects({ puts: Str ~> Unit })]
readFile : (Str ~> Str) @ [Effects({ fs: Path ~> Str })]
greet   : Str @ [Effects({ puts: Str ~> Unit })] := perform puts "hi"

f : (Str ~> Str) @ [Effects({ puts: Str ~> Unit })]
g : (Str ~> Str) @ [Effects({ fs: Path ~> Str })]
h := g >>> f
-- h : (Str ~> Str) @ [Effects({ puts: Str ~> Unit, fs: Path ~> Str })]

puts_handler : Str ~> Unit := s ~> print(s)
handled : (Str ~> Str) @ [] :=
  handle printLn with { puts: puts_handler }
```

`perform` extends the ambient mode `μ`; `handle` is a modality
`μ → μ'` whose residual row is `(S ∖ S_h) ∪ { op ↦ ret }` — covered
ops take their handler's return type, uncovered ops survive. Every
row entry is an operation type `name : A ~> B`, one shape whether
the op was declared or performed. Row union, unit, and subsumption
are the `Effects` algebra's `compose`/`unit`/`order`, so `>>>`
*computes* the mode exactly like `Cost(2) >>> Cost(5)` computes a
grade.

## Instances and evidence

```hnl
Eq := new Constraint(Type) {
  evidence : a ~> a ~> Bool
}

instance Eq(Nat) := { evidence: (x, y) ~> x == y }

eqv<a, ev : Eq(a)> : a ~> a ~> Bool :=
  x ~> y ~> ev.evidence(x, y)
nat_eq : Bool := eqv(zero)(zero)
```

`new` is the single declaration form for checker registries:
`Inductive` (constructors and eliminators), `Algebra` (mode
composition), `Constraint` (evidence dictionaries). An `instance`
fills a registry slot; `ev : Eq(a)` binders are evidence-implicit,
resolved by unification-driven dictionary search with
declaration-time no-overlap coherence.

## Everything computes

The typechecker is itself a Handl program: types are `type.*` values,
proofs are witnesses stored in the evaluation state, unification
records its `via` paths, and algebras are records the checker
interprets. Aliases are transparent expansions; `forall` is Pi-sugar;
judgments are serializable, cacheable, parallelizable data.

Because types and terms share one evaluator, **typechecking already
runs your computations**: normalizing `Vec(2, Bool)` evaluates indices,
transport along `ua(e)` applies the equivalence, and `mode_compose`
evaluates the governing algebra. The checker's normalization cache is a
demand-driven partial evaluator whose results the runtime inherits —
the same compute is reused, never run twice. And the same language
spans every domain: the checker, the libraries it checks, the proofs
it records, and the algebras it interprets are all ordinary Handl. The
purity boundary is itself typed: modes mark exactly which computations
may cross it.

---

**One line:** programs, proofs, types, effects, and modes are cells in
one calculus — everything is data, everything computes, and equality,
transport, univalence, and mode arithmetic are all the same evaluator
at work.

The academic groundwork behind each layer is collected in the
[bibliography](/ecosystem/bibliography): arrows and categorical
semantics, graded and quantitative type theory, modal type theory,
dependent and inductive types, cubical type theory and univalence, and
effects and handlers.
