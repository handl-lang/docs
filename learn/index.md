# The Handl type system

One calculus for programs, proofs, types, effects, and modes, where
equality, transport, and univalence all *compute*, and the typechecker
itself is a program in the same language it checks.

Everything on this page is ordinary Handl: types are values, proofs are
witnesses, judgments are data. There is no separate type-theoretic
subsystem. Dependent structure, equality, effects, and modes are all
cells in the same arrow calculus.

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

## Effects: ambient modes

```hnl
printLn : (Str ~> Str) @ {io: {puts: Str}}
readFile : (Str ~> Str) @ {io: {fs: Path}}
greet   : Str @ {io: {puts: Str}} := perform puts "hi"

f : (Str ~> Str) @ {io: {puts}}
g : (Str ~> Str) @ {io: {fs}}
h := g >>> f     -- : (Str ~> Str) @ {io: {puts, fs}}

puts_handler : Str ~> Unit := s ~> print(s)
handled : (Str ~> Str) @ {} :=
  handle printLn with {puts: puts_handler}
```

`perform` extends the ambient mode `μ`; `handle` is a modality
`μ → μ'` whose residual row is `(S ∖ S_h) ∪ {op ↦ ret}` — covered
ops take their handler's return type, uncovered ops survive. Row
union, unit, and subsumption are the `Effects` algebra's
`compose`/`unit`/`order`, so `>>>` *computes* the mode exactly like
`Cost(2) >>> Cost(5)` computes a grade.

The mode is a record because modes are a *product* of independent
dimensions: `{io: {puts}, cost: 3, session: net}` ascribes effects,
cost, and session simultaneously, and each field's value selects its
own algebra (`Effects`, `Cost`, `Session`) for `mode_compose` — the
same call-head selection `Cost(3)` uses for a single dimension.

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

## Modes: MTT arrows

Modes unify grades, coeffects, and effects onto one axis. A mode is an arbitrary Handl data value; an algebra is an ordinary
type, a record of `compose`/`unit`/`order` functions, declared once and
selected by the mode's call head:

```hnl
Cost := new Algebra(Nat) {
  compose: (a, b) ~> a + b,
  unit:    0,
  order:   (a, b) ~> a <= b
}

f : A ~[Cost(2)]~> B
g : B ~[Cost(5)]~> C
h := g >>> f        -- : A ~[Cost(7)]~> C
```

`Cost(2)` composed with `Cost(5)` dispatches to the `Cost` instance's
`compose`, so composition *computes* the mode. Subsumption is the
algebra's `order`: an arrow usable at `Cost(3)` is accepted where
`Cost(5)` is expected. Modes are data, so algebras are computable:
transformers, products, and mode expressions like `Cost(3) +
Session(p)` are ordinary functions returning algebra records.

```hnl
mapM : (m : Mode) ~> (f : A ~[m]~> B) ~> List(A) ~[m]~> List(B)
costed := mapM(Cost(1), double)     -- mode polymorphism by substitution
```

`~>[n]` remains the dimension arrow: globular structure, a different
axis from modes.

## The meta layer: everything is data

The typechecker is itself a Handl program: types are `type.*` values,
proofs are witnesses stored in the evaluation state, unification
records its `via` paths, and algebras are records the checker
interprets. Aliases are transparent expansions; `forall` is Pi-sugar;
judgments are serializable, cacheable, parallelizable data.

Because types and terms share one evaluator, **typechecking already
runs your computations**: normalizing `Vec(2, Bool)` evaluates indices,
transport along `ua(e)` applies the equivalence, and `mode_compose`
evaluates the governing algebra. The checker's normalization cache is a
demand-driven partial evaluator whose results the runtime can inherit.
Pure computations verified once at typecheck time are replayable at run
time, and the purity boundary is itself typed: graded arrows mark
exactly which computations may cross it.

---

**One line:** programs, proofs, types, effects, and modes are cells in
one calculus, and equality, transport, univalence, and grading all
*compute*.

The academic groundwork behind each layer is collected in the
[bibliography](/ecosystem/bibliography): arrows and categorical
semantics, graded and quantitative type theory, modal type theory,
dependent and inductive types, cubical type theory and univalence, and
effects and handlers.
