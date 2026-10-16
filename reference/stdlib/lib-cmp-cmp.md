# Cmp

## `cmp.between`

test whether a value is between two bounds (exclusive).

**Signature:** `cmp.between : (Value, Value, Value) -&gt; Bool`

## `cmp.clamp`

clamp a value between a lower and upper bound.

**Signature:** `cmp.clamp : (Value, Value, Value) -&gt; Value`

## `cmp.compare`

compare two values, returning -1, 0, or 1.

**Signature:** `cmp.compare : (Value, Value) -&gt; Number`

## `cmp.eq`

test whether two values are deeply equal.

**Signature:** `cmp.eq : (Value, Value) -&gt; Bool`

## `cmp.ge`

test whether the first value is greater than or equal to the second.

**Signature:** `cmp.ge : (Value, Value) -&gt; Bool`

## `cmp.gt`

test whether the first value is greater than the second.

**Signature:** `cmp.gt : (Value, Value) -&gt; Bool`

## `cmp.in_range`

test whether a value is within a range (alias of between).

**Signature:** `cmp.in_range : (Value, Value, Value) -&gt; Bool`

## `cmp.is_sorted`

test whether an array is sorted in ascending order.

**Signature:** `cmp.is_sorted : Array -&gt; Bool`

## `cmp.is_sorted_desc`

test whether an array is sorted in descending order.

**Signature:** `cmp.is_sorted_desc : Array -&gt; Bool`

## `cmp.le`

test whether the first value is less than or equal to the second.

**Signature:** `cmp.le : (Value, Value) -&gt; Bool`

## `cmp.lt`

test whether the first value is less than the second.

**Signature:** `cmp.lt : (Value, Value) -&gt; Bool`

## `cmp.max`

return the maximum of all arguments.

**Signature:** `cmp.max : Value... -&gt; Value`

## `cmp.max_by`

find the maximum element by a key function.

**Signature:** `cmp.max_by : (Function, Array) -&gt; Value`

## `cmp.min`

return the minimum of all arguments.

**Signature:** `cmp.min : Value... -&gt; Value`

## `cmp.min_by`

find the minimum element by a key function.

**Signature:** `cmp.min_by : (Function, Array) -&gt; Value`

## `cmp.ne`

test whether two values are not equal.

**Signature:** `cmp.ne : (Value, Value) -&gt; Bool`

## `cmp.sort`

sort an array in ascending order.

**Signature:** `cmp.sort : Array -&gt; Array`

## `cmp.sort_by`

sort an array by a key function in ascending order.

**Signature:** `cmp.sort_by : (Function, Array) -&gt; Array`

## `cmp.sort_by_desc`

sort an array by a key function in descending order.

**Signature:** `cmp.sort_by_desc : (Function, Array) -&gt; Array`

## `cmp.sort_desc`

sort an array in descending order.

**Signature:** `cmp.sort_desc : Array -&gt; Array`
