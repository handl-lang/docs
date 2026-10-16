# Comb

## `comb.apply`

Calls a function with an array of arguments.

**Signature:** `comb.apply([f, args])`

**Examples:**

```handl
`[[x, y] ~> x + y, [1, 2]] >>> comb.apply`
-- => 3
```

## `comb.choice`

Selects between two branches based on a predicate.

**Signature:** `comb.choice([value, pred, true_fn, false_fn])`

**Examples:**

```handl
`[4, x ~> x % 2 == 0, x ~> "even", x ~> "odd"] >>> comb.choice`
-- => "even"
```

## `comb.compose`

Composes a list of functions right-to-left, returning a single arrow.

**Signature:** `comb.compose(fs)`

**Examples:**

```handl
`inc :: x ~> x + 1`
`dbl :: x ~> x * 2`
`f :: [inc, dbl] >>> comb.compose`
`3 >>> f`
-- => 7
`id :: [] >>> comb.compose`
`42 >>> id`
-- => 42
```

## `comb.constantly`

Returns an arrow that ignores its input and always yields `c`.

**Signature:** `comb.constantly(c)`

**Examples:**

```handl
`f :: 0 >>> comb.constantly`
`999 >>> f`
-- => 0
```

## `comb.converge`

Applies several branches to one value and folds the results with a combiner.

**Signature:** `comb.converge(args)`

**Examples:**

```handl
`[6, [a, b] ~> a + b, x ~> x * 2, x ~> x * 3] >>> comb.converge`
-- => 30
```

## `comb.fanout`

Applies several functions to one value and collects the results.

**Signature:** `comb.fanout(args)`

**Examples:**

```handl
`[3, x ~> x + 1, x ~> x * 2] >>> comb.fanout`
-- => [4, 6]
```

## `comb.fanout_fn`

Returns an arrow that splits its input across several functions.

**Signature:** `comb.fanout_fn(fs)`

**Examples:**

```handl
`f :: [x ~> x + 1, x ~> x * 2] >>> comb.fanout_fn`
`3 >>> f`
-- => [4, 6]
```

## `comb.flip`

Returns an arrow that calls `f` with its first two arguments swapped.

**Signature:** `comb.flip(f)`

**Examples:**

```handl
`sub :: [a, b] ~> a - b`
`[10, 3] >>> (sub >>> comb.flip) >>> comb.apply`
-- => -7
```

## `comb.flow`

Composes a list of functions left-to-right, returning a single arrow.

**Signature:** `comb.flow(fs)`

**Examples:**

```handl
`inc :: x ~> x + 1`
`dbl :: x ~> x * 2`
`f :: [inc, dbl] >>> comb.flow`
`3 >>> f`
-- => 8
```

## `comb.partial`

Partially applies the leading argument(s) of a function.

**Signature:** `comb.partial([f, bound])`

**Examples:**

```handl
`add3 :: [a, b, c] ~> a + b + c`
`add_from_10 :: [add3, [10, 20]] >>> comb.partial`
`5 >>> add_from_10`
-- => 35
```

## `comb.pipe`

Pipes a value through a sequence of functions, left-to-right.

**Signature:** `comb.pipe(args)`

**Examples:**

```handl
`[3, x ~> x + 1, x ~> x * 2] >>> comb.pipe`
-- => 8
```

## `comb.tap`

Runs a side-effect function on a value, then returns the value unchanged.

**Signature:** `comb.tap([f, x])`

**Examples:**

```handl
`[x ~> print(x), 42] >>> comb.tap`
-- => 42
```

## `comb.unless`

Applies a transform to a value unless a predicate holds for it.

**Signature:** `comb.unless([value, pred, fn])`

**Examples:**

```handl
`[4, x ~> x % 2 == 0, x ~> x * 10] >>> comb.unless`
-- => 4
```

## `comb.when`

Applies a transform to a value only when a predicate holds for it.

**Signature:** `comb.when([value, pred, fn])`

**Examples:**

```handl
`[4, x ~> x % 2 == 0, x ~> x * 10] >>> comb.when`
-- => 40
```
