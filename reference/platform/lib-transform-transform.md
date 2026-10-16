# Transform

## `transform.filter`

Keeps the elements of a list that satisfy a predicate.

**Signature:** `transform.filter(do {)`

**Examples:**

```handl
`[[1, 2, 3, 4], x ~> x % 2 == 0] >>> transform.filter`
-- => [2, 4]
```

## `transform.map`

Maps a function over a list, preserving order.

**Signature:** `transform.map(do {)`

**Examples:**

```handl
`[[1, 2, 3], x ~> x * 2] >>> transform.map`
-- => [2, 4, 6]
```

## `transform.reduce`

Folds a list from the left with an initial accumulator.

**Signature:** `transform.reduce([xs, init, f])`

**Examples:**

```handl
`[[1, 2, 3], 0, [acc, x] ~> acc + x] >>> transform.reduce`
-- => 6
`[[], "seed", [acc, x] ~> acc] >>> transform.reduce`
-- => "seed"
```

## `transform.filter`

filter a list by a predicate.

**Signature:** `transform.filter : (Value * Value) -&gt; Value`

## `transform.map`

map a function over a list.

**Signature:** `transform.map : (Value * Value) -&gt; Value`

## `transform.reduce`

fold a list with a function and an initial value.

**Signature:** `transform.reduce : (Value * Value * Value) -&gt; Value`
