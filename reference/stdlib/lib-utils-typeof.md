# Typeof

## `typeof.any`

the type.any tag constant.

**Signature:** `typeof.any : Value -&gt; String`

## `typeof.arr`

the type.arr tag constant.

**Signature:** `typeof.arr : Value -&gt; String`

## `typeof.array`

the type.array tag constant.

**Signature:** `typeof.array : Value -&gt; String`

## `typeof.bool`

the type.bool tag constant.

**Signature:** `typeof.bool : Value -&gt; String`

## `typeof.coalesce`

return the first non-null value from a list of arguments.

**Signature:** `typeof.coalesce : Value -&gt; Value`

## `typeof.default`

return the value if non-null, otherwise a fallback.

**Signature:** `typeof.default : (Value * Value) -&gt; Value`

## `typeof.identity`

return the value unchanged.

**Signature:** `typeof.identity : Value -&gt; Value`

## `typeof.is`

test whether a value matches a kind.

**Signature:** `typeof.is : (Value * Value) -&gt; Bool`

## `typeof.may`

potential extraction: extract the matching component or null.

**Signature:** `typeof.may : (Value * Value) -&gt; Value`

## `typeof.must`

strict projection: wrap the result in an ok/err record.

**Signature:** `typeof.must : (Value * Value) -&gt; Value`

## `typeof.not`

complement: extract the non-matching component or null.

**Signature:** `typeof.not : (Value * Value) -&gt; Value`

## `typeof.null`

the type.null tag constant.

**Signature:** `typeof.null : Value -&gt; String`

## `typeof.num`

the type.num tag constant.

**Signature:** `typeof.num : Value -&gt; String`

## `typeof.number`

the type.number tag constant.

**Signature:** `typeof.number : Value -&gt; String`

## `typeof.obj`

the type.obj tag constant.

**Signature:** `typeof.obj : Value -&gt; String`

## `typeof.object`

the type.object tag constant.

**Signature:** `typeof.object : Value -&gt; String`

## `typeof.str`

the type.str tag constant.

**Signature:** `typeof.str : Value -&gt; String`

## `typeof.string`

the type.string tag constant.

**Signature:** `typeof.string : Value -&gt; String`

## `typeof.to_bool`

coerce a value to a boolean.

**Signature:** `typeof.to_bool : Value -&gt; Bool`

## `typeof.to_number`

coerce a value to a number.

**Signature:** `typeof.to_number : Value -&gt; Float`

## `typeof.to_string`

coerce a value to a string.

**Signature:** `typeof.to_string : Value -&gt; String`

## `typeof.type_of`

get the type name of a value.

**Signature:** `typeof.type_of : Value -&gt; String`

## `typeof.typeof`

alias for type_of.

**Signature:** `typeof.typeof : Value -&gt; String`

## `typeof.unknown`

the type.unknown tag constant.

**Signature:** `typeof.unknown : Value -&gt; String`

## `typeof.when`

conditional: extract the matching component or return a default.

**Signature:** `typeof.when : (Value * Value * Value) -&gt; Value`
