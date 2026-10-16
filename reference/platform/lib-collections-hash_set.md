# Hash Set

## `hash_set.add`

**Signature:** `hash_set.add : (Array * Value) -&gt; Array`

## `hash_set.difference`

**Signature:** `hash_set.difference : (Array * Array) -&gt; Array`

## `hash_set.from`

**Signature:** `hash_set.from : Array -&gt; Array`

## `hash_set.has`

**Signature:** `hash_set.has : (Array * Value) -&gt; Bool`

## `hash_set.intersection`

**Signature:** `hash_set.intersection : (Array * Array) -&gt; Array`

## `hash_set.is_empty`

**Signature:** `hash_set.is_empty : Array -&gt; Bool`

## `hash_set.len`

**Signature:** `hash_set.len : Array -&gt; Number`

## `hash_set.new`

the `hash_set` module contract.

All ops stay native (see `ops/collections/hash_set.rs`): membership is keyed on a *serialized* value (`value_key`), which distinguishes `1` from `1.0` and therefore differs from handl `==` (cross-numeric equality). A pure-handl port would change `from`/`unique`/`union`/ `intersection`/`difference`/`symmetric_difference`/`without` dedup semantics on mixed int/float inputs. `unique_by` additionally takes an arrow argument, which cannot cross the `HandlFunction` boundary.

**Signature:** `hash_set.new : _ -&gt; Array`

## `hash_set.remove`

**Signature:** `hash_set.remove : (Array * Value) -&gt; Array`

## `hash_set.symmetric_difference`

**Signature:** `hash_set.symmetric_difference : (Array * Array) -&gt; Array`

## `hash_set.to_array`

**Signature:** `hash_set.to_array : Array -&gt; Array`

## `hash_set.union`

**Signature:** `hash_set.union : (Array * Array) -&gt; Array`

## `hash_set.unique`

**Signature:** `hash_set.unique : Array -&gt; Array`

## `hash_set.unique_by`

**Signature:** `hash_set.unique_by : (Array * Fn) -&gt; Array`

## `hash_set.without`

**Signature:** `hash_set.without : (Array * Value...) -&gt; Array`
