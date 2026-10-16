# Combinators

## `combinators.apply`

apply a function to an array of arguments.

**Signature:** `combinators.apply : (Value * Value) -&gt; Value`

## `combinators.choice`

conditional branching: apply one of two functions based on a predicate.

**Signature:** `combinators.choice : (Value * Value * Value * Value) -&gt; Value`

## `combinators.compose`

compose functions right-to-left into a single inlined function.

**Signature:** `combinators.compose : Value -&gt; Value`

## `combinators.constantly`

return a function that always yields a fixed value.

**Signature:** `combinators.constantly : Value -&gt; Value`

## `combinators.converge`

apply branches to a value, then combine the results with a combiner.

**Signature:** `combinators.converge : (Value * Value * Value) -&gt; Value`

## `combinators.count_by`

count elements of a list grouped by a key function.

**Signature:** `combinators.count_by : (Value * Value) -&gt; Value`

## `combinators.every`

test whether all elements of a list satisfy a predicate.

**Signature:** `combinators.every : (Value * Value) -&gt; Value`

## `combinators.fanout`

apply a value to each of several functions, collecting results into a list.

**Signature:** `combinators.fanout : (Value * Value) -&gt; Value`

## `combinators.fanout_fn`

lazy fanout: return a function that splits its input across branches.

**Signature:** `combinators.fanout_fn : Value -&gt; Value`

## `combinators.find`

find the first element of a list satisfying a predicate.

**Signature:** `combinators.find : (Value * Value) -&gt; Value`

## `combinators.flat_map`

map a function over a list and flatten the results.

**Signature:** `combinators.flat_map : (Value * Value) -&gt; Value`

## `combinators.flip`

swap the first two parameters of a function.

**Signature:** `combinators.flip : Value -&gt; Value`

## `combinators.flow`

compose functions left-to-right into a single inlined function.

**Signature:** `combinators.flow : Value -&gt; Value`

## `combinators.group_by`

group elements of a list by a key function.

**Signature:** `combinators.group_by : (Value * Value) -&gt; Value`

## `combinators.match`

pattern-match a value against a sequence of pattern/handler branches.

**Signature:** `combinators.match : (Value * Value) -&gt; Value`

## `combinators.partial`

partially apply a function by binding its leading arguments.

**Signature:** `combinators.partial : (Value * Value) -&gt; Value`

## `combinators.partition`

split a list into matching and non-matching elements.

**Signature:** `combinators.partition : (Value * Value) -&gt; Value`

## `combinators.pipe`

pipe a value through a sequence of functions left-to-right.

**Signature:** `combinators.pipe : (Value * Value) -&gt; Value`

## `combinators.some`

test whether any element of a list satisfies a predicate.

**Signature:** `combinators.some : (Value * Value) -&gt; Value`

## `combinators.tap`

call a function for its side effect, returning the original value.

**Signature:** `combinators.tap : (Value * Value) -&gt; Value`

## `combinators.unless`

apply a transform unless a predicate holds, otherwise return the value unchanged.

**Signature:** `combinators.unless : (Value * Value * Value) -&gt; Value`

## `combinators.when`

apply a transform when a predicate holds, otherwise return the value unchanged.

**Signature:** `combinators.when : (Value * Value * Value) -&gt; Value`
