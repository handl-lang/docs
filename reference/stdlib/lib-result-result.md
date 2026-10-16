# Result

## `result.err`

Construct an Err result wrapping an error value.

@param {error} - the error value of type E

**Signature:** `result.err : &lt;T, E&gt;: E ~[1]~&gt; Result&lt;T, E&gt;`

## `result.ok`

Construct an Ok result wrapping a success value.

@param {value} - the success value of type T

**Signature:** `result.ok : &lt;T, E&gt;: T ~[1]~&gt; Result&lt;T, E&gt;`

## `result.Result`

@template T - the success value type

@template E - the error value type The `Result&lt;T, E&gt;` type.

**Signature:** `result.Result(&lt;T, E&gt;)`
