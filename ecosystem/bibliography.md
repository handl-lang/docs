# Bibliography

These academic works are a major inspiration for Handl. There is already a
substantial body of mathematical groundwork for arrows via category theory:
that is what we are drawing on.

Foundational work behind the arrow calculus and the categorical semantics the
kernel is built on.

## Arrows

- **John Hughes**: [*Generalising Monads to Arrows*](https://doi.org/10.1016/S0167-6423(99)00023-4)
  (2000, *Science of Computer Programming*). Introduced arrows and their core
  combinators (`arr`, `>>>`, `first`).
- **Ross Paterson**: [*A New Notation for Arrows*](https://doi.org/10.1145/507635.507664)
  (2001, ICFP). Formalized proc notation, algebraic laws, and categorical
  correspondences.
- **Sam Lindley, Philip Wadler & Jeremy Yallop**: [*The Arrow Calculus*](https://doi.org/10.1017/S095679680999027X)
  (2010, *Journal of Functional Programming*). Defined a formal typed
  calculus and equational semantics for arrows.

## Categorical semantics

- **Eugenio Moggi**: [*Notions of Computation and Monads*](https://doi.org/10.1016/0890-5401(91)90052-4)
  (1991, *Information and Computation*). Monads as notions of computation.
- **John Power & Edmund Robinson**: [*Premonoidal Categories and Notions
  of Computation*](https://doi.org/10.1017/S0960129597002375) (1997,
  *Mathematical Structures in Computer Science*).
- **John Power & Hayo Thielecke**: [*Closed Freyd- and
  κ-categories*](https://doi.org/10.1007/3-540-48523-6_59) (1999, ICALP).
  Freyd and premonoidal categories, the canonical categorical model
  separating pure values from effectful computations.
- **Paul Levy**: *Call-by-push-value* (PhD thesis, Queen Mary and Westfield
  College, University of London, 2001). Value/computation discipline that
  premonoidal models are built on.

## Monads in Prof

- **Chris Heunen & Bart Jacobs**: [*Arrows, like Monads, are
  Monoids*](https://doi.org/10.1016/j.entcs.2006.04.012) (2006, ENTCS).
  Arrows as monoids in categories of bifunctors.
- **Bart Jacobs, Chris Heunen & Ichiro Hasuo**: [*Categorical Semantics
  for Arrows*](https://doi.org/10.1017/S0956796809007308) (2009, *Journal of
  Functional Programming*). Denotational semantics via Eilenberg–Moore and
  Kleisli constructions ("arrows are Freyd categories").
- **Kazuyuki Asada**: [*Arrows are Strong
  Monads*](https://doi.org/10.1145/1863597.1863607) (2010, MSFP; [PDF](https://www.riec.tohoku.ac.jp/~asada/papers/arrStrMnd.pdf)).
  Identifies `first` with strength: arrows are strong monads (promonads) in
  `Prof`.

## Higher categories

Handl's IR is globular and higher-categorical: programs are 1-morphisms,
laws and rewrites are 2-morphisms, and transformations extend upward. These
are the foundations that make "all data, all dimensions" coherent.

- **Michael A. Batanin**: [*Monoidal Globular Categories as a Natural
  Environment for the Theory of Weak n-Categories*](https://doi.org/10.1006/aima.1998.1724)
  (1998, *Advances in Mathematics*). Globular operads and weak
  ω-categories: the canonical setting for globular higher structure.
- **Tom Leinster**: [*Higher Operads, Higher
  Categories*](https://doi.org/10.1017/CBO9780511525896) (2004, Cambridge).
  The standard reference for generalized operads and n-categorical
  structures.
- **Eugenia Cheng & Aaron Lauda**: [*Higher-Dimensional Categories: an
  Illustrated Guide Book*](https://eugeniacheng.com/wp-content/uploads/2017/02/cheng-lauda-guidebook.pdf)
  (2004, IMA workshop notes). A friendly tour of the competing definitions
  of n-category.
- **Jacob Lurie**: [*Higher Topos Theory*](https://people.math.harvard.edu/~lurie/papers/HTT.pdf)
  (2009). ∞-categories via quasi-categories: the modern foundation for
  infinite-dimensional composition and coherence.

## Graded type theory

Handl's graded effects descend from graded monads and graded algebraic
theories: the grade on an operation is what the type-level literature calls
a coeffect/grade.

- **Dominic Orchard, Vilem-Benjamin Liepelt & Harley Eades III**:
  [*Quantitative Program Reasoning with Graded Modal
  Types*](https://doi.org/10.1145/3341714) (2019, PACMPL 3(ICFP), Article
  110). Graded modal types as the type-level counterpart of graded
  effects.
- **Satoshi Kura**: [*Graded Algebraic
  Theories*](https://doi.org/10.1007/978-3-030-45231-5_21) (2020, FoSSaCS;
  [arXiv:2002.06784](https://arxiv.org/abs/2002.06784)). Graded algebraic
  and Lawvere theories, equivalent to finitary graded monads.
- **Jeff Egger, Rasmus Ejlers Møgelberg & Alex Simpson**: [*The Enriched
  Effect Calculus: Syntax and
  Semantics*](https://doi.org/10.1093/logcom/exs025) (2014, *Journal of
  Logic and Computation* 24(3)). Effect calculi enriched with linear logic
  primitives.
- **Benjamin Moon, Harley Eades III & Dominic Orchard**: [*Graded Modal
  Dependent Type Theory*](https://doi.org/10.1007/978-3-030-72019-3_17)
  (2021, ESOP). Graded analysis of dataflow in a dependent type theory;
  grades applied to both terms and types.
- **Robert Atkey**: [*Syntax and Semantics of Quantitative Type
  Theory*](https://doi.org/10.1145/3209108.3209189) (2018, LICS; pp.
  56–65). Usage quantities tracked per variable in the judgement, with a
  realizability semantics via quantitative categories with families;
  the semantic foundation for graded/usage modes.

## Modal type theory

Handl's mode arrows generalize grades, coeffects, and effects onto one
axis in the spirit of modal type theory: a mode annotates how a term may
be used, and algebras govern how modes combine.

- **Daniel Gratzer, Georgios A. Kavvos, Andreas Nuyts & Lars Birkedal**:
  [*Multimodal Dependent Type Theory*](https://doi.org/10.46298/lmcs-17(3:11)2021)
  (2021, *Logical Methods in Computer Science* 17(3); also LICS 2020).
  MTT proper: a dependent type theory parametrized by a mode theory of
  modes, modalities, and transformations between them; the direct
  ancestor of Handl's mode-algebra approach.
- **Aleksandar Nanevski, Frank Pfenning & Brigitte Pientka**:
  [*Contextual Modal Type Theory*](https://doi.org/10.1145/1352582.1352591)
  (2008, *ACM Transactions on Computational Logic* 9(3)). Modal type
  theory with explicitly specified contexts; the canonical treatment of
  modes as context structure.
- **Daan Leijen**: [*Koka: Programming with Row-Polymorphic Effect
  Types*](https://doi.org/10.4204/EPTCS.153.8) (2014, MSFP; EPTCS 153,
  pp. 100–126). Effects as row-polymorphic signatures on function types;
  the model for Handl's `IO<sig>` codomain formers and residual-effect
  reasoning.

## Dependent type theory

- **Per Martin-Löf**: *Intuitionistic Type Theory* (Bibliopolis, 1984).
  The original dependent type theory: universes, identity types,
  well-founded trees.
- **Peter Dybjer**: [*Inductive Families*](https://doi.org/10.1007/BF01211308)
  (1994, *Formal Aspects of Computing* 6(4), pp. 440–465). Indexed
  inductive families in Martin-Löf type theory with a general
  positivity criterion and elimination-rule derivation; the reference
  for Handl's `Vec<n, a>`-style families and the inductives-as-data
  representation.

## Cubical type theory and univalence

Handl's equality is cubical: paths are interval-indexed terms,
transport computes, and univalence is a value rather than an axiom.

- **Cyril Cohen, Thierry Coquand, Simon Huber & Anders Mörtberg**:
  [*Cubical Type Theory: A Constructive Interpretation of the Univalence
  Axiom*](https://doi.org/10.4230/LIPIcs.TYPES.2015.5) (TYPES 2015;
  published in LIPIcs vol. 69, 2018). Dependent type theory interpreted
  in cubical sets: `transp`, `hcomp`, `Glue`, and a *provable*
  univalence axiom with judgmental computation.
- **The Univalent Foundations Program**: [*Homotopy Type
  Theory: Univalent Foundations of Mathematics*](https://homotopytypetheory.org/book/)
  (2013). The book-length development of identity types as paths,
  function extensionality, and the univalence axiom.

## Effects and handlers for arrows

- **Takahiro Sanada**: [*Algebraic Effects and Handlers for
  Arrows*](https://doi.org/10.1017/S0956796824000066) (2024, *Journal of
  Functional Programming*; also [ICFP 2024](https://icfp24.sigplan.org/details/icfp-2024-jfp-first-papers/1/Algebraic-effects-and-handlers-for-arrows)).
  Extended the arrow calculus with algebraic effects and handlers via
  algebras over strong promonads.
- **Takahiro Sanada, Keisuke Hoshino, Kenshin Hirai & Shin-ya Katsumata**:
  [*Programming Backpropagation with Reverse Handlers for
  Arrows*](https://doi.org/10.1145/3828704) (2026, PACMPL 10(ICFP), Article
  306; also [arXiv:2602.18090](https://arxiv.org/abs/2602.18090)). Modeled
  neural networks and backpropagation via linear reverse effect handlers,
  combining strong promonads with Cartesian reverse differential
  categories.

## Tooling and implementation

The engineering techniques behind the engine and library families.

- **Nelson Niu, Chandrakana Nandi, Andrew Rice, Antoine Yang & Adam
  Chlipala**: [*egg: Fast and Extensible Equality
  Saturation*](https://doi.org/10.1145/3434290) (2021, POPL). E-graphs
  and equality saturation — the technique `engine-eqsat` implements
  over Handl `Term`s.
- **Andreas Abel, Thierry Coquand & Peter Dybjer**: [*Normalization by
  Evaluation for Martin-Löf Type Theory*](https://doi.org/10.1016/j.entcs.2007.01.012)
  (2007, TYPES; ENTCS 174). NbE — the evaluation strategy
  `tool-typecheck-nbe` uses to decide conversion.
- **Vaughan R. Pratt**: [*Top Down Operator Precedence*
  ](https://doi.org/10.1145/512927.512931) (1973, SOAP). Precedence
  climbing — the parsing technique behind `tool-parse-pratt`.
