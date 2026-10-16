# Rand

## `rand.Binomial`

Generate a binomial-distributed integer in `[0, n]` with `n` trials

and success probability `p`.

**Signature:** `rand.Binomial((Number, Number))`

## `rand.Bool`

Generate a random boolean.

**Signature:** `rand.Bool(())`

## `rand.Bytes`

Generate `n` random bytes in `[0, 255]`.

**Signature:** `rand.Bytes(Number)`

## `rand.Choice`

Choose `count` elements from an array with replacement.

**Signature:** `rand.Choice((Array, Number))`

## `rand.Exponential`

Generate an exponentially distributed non-negative number with `lambda`.

**Signature:** `rand.Exponential(Number)`

## `rand.Float`

Generate a random float in `[0, max)`.

**Signature:** `rand.Float(Number)`

## `rand.Gauss`

Generate a normally distributed number with `mean` and `stddev`.

**Signature:** `rand.Gauss((Number, Number))`

## `rand.Int`

Generate a random integer in `[0, max]`.

**Signature:** `rand.Int(Number)`

## `rand.Pick`

Pick one random element from a non-empty array.

**Signature:** `rand.Pick(Array)`

## `rand.Poisson`

Generate a Poisson-distributed non-negative integer with `lambda`.

**Signature:** `rand.Poisson(Number)`

## `rand.Random`

@template Random

Grade for effectful randomness generation.

**Signature:** `rand.Random(&lt;T&gt;: Grade)`

## `rand.Sample`

Sample `count` elements from an array without replacement.

**Signature:** `rand.Sample((Array, Number))`

## `rand.SeededBool`

Generate a seeded random boolean.

**Signature:** `rand.SeededBool(Number)`

## `rand.SeededChoice`

Choose `count` seeded elements from an array with replacement.

**Signature:** `rand.SeededChoice((Number, Array, Number))`

## `rand.SeededFloat`

Generate a seeded random float in `[0, max)`.

**Signature:** `rand.SeededFloat((Number, Number))`

## `rand.SeededGauss`

Generate a seeded normally distributed number with `mean` and `stddev`.

**Signature:** `rand.SeededGauss((Number, Number, Number))`

## `rand.SeededInt`

Generate a seeded random integer in `[0, max]`.

**Signature:** `rand.SeededInt((Number, Number))`

## `rand.SeededPick`

Pick one seeded random element from a non-empty array.

**Signature:** `rand.SeededPick((Number, Array))`

## `rand.SeededSample`

Sample `count` seeded elements from an array without replacement.

**Signature:** `rand.SeededSample((Number, Array, Number))`

## `rand.SeededShuffle`

Shuffle an array with a seeded RNG.

**Signature:** `rand.SeededShuffle((Number, Array))`

## `rand.SeededString`

Generate a seeded random string of `len` characters from `charset`.

**Signature:** `rand.SeededString((Number, Number, String))`

## `rand.Shuffle`

Shuffle an array in random order.

**Signature:** `rand.Shuffle(Array)`

## `rand.String`

Generate a random string of `len` characters from `charset`.

**Signature:** `rand.String((Number, String))`

## `rand.WeightedPick`

Pick one random element from weighted arrays.

**Signature:** `rand.WeightedPick((Array, Array))`
