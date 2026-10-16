# Type

## `type.Bool`

**Signature:** `type.Bool({ "__tag__": "bool", "__registry__": "type", "kind": "primitive" })`

## `type.Bool`

**Signature:** `type.Bool({ "__tag__": "bool", "__registry__": "type", "kind": "primitive" })`

## `type.Float`

**Signature:** `type.Float({ "__tag__": "float", "__registry__": "type", "kind": "primitive" })`

## `type.Float`

**Signature:** `type.Float({ "__tag__": "float", "__registry__": "type", "kind": "primitive" })`

## `type.FloatN`

**Signature:** `type.FloatN(sym(NumberN))`

## `type.FloatN`

**Signature:** `type.FloatN(sym(NumberN))`

## `type.Int`

**Signature:** `type.Int({ "__tag__": "int", "__registry__": "type", "kind": "primitive" })`

## `type.Int`

**Signature:** `type.Int({ "__tag__": "int", "__registry__": "type", "kind": "primitive" })`

## `type.IntN`

**Signature:** `type.IntN(sym(NumberN))`

## `type.IntN`

**Signature:** `type.IntN(sym(NumberN))`

## `type.Nat`

**Signature:** `type.Nat({ "__tag__": "nat", "__registry__": "type", "kind": "primitive" })`

## `type.Nat`

**Signature:** `type.Nat({ "__tag__": "nat", "__registry__": "type", "kind": "primitive" })`

## `type.NatN`

**Signature:** `type.NatN(sym(IntN))`

## `type.NatN`

**Signature:** `type.NatN(sym(IntN))`

## `type.Null`

**Signature:** `type.Null({ "__tag__": "null", "__registry__": "type", "kind": "primitive" })`

## `type.Null`

**Signature:** `type.Null({ "__tag__": "null", "__registry__": "type", "kind": "primitive" })`

## `type.Number`

**Signature:** `type.Number({ "__tag__": "number", "__registry__": "type", "kind": "primitive" })`

## `type.Number`

**Signature:** `type.Number({ "__tag__": "number", "__registry__": "type", "kind": "primitive" })`

## `type.NumberN`

`sym()`; `FloatN` is literally `sym(NumberN)`.

**Signature:** `type.NumberN(sym())`

## `type.NumberN`

## ADR-0106 nominal identities (sym-backed, alongside the legacy tags)

Nominal identities per ADR-0106 §2. `NumberN` is a root nominal (`sym()` -- a fresh object with a unique nominal identity); `IntN` and `FloatN` are children parented to it (`sym(NumberN)`), so the `sym` parent graph *is* the subtyping relation: `FloatN instanceof NumberN` (runtime parent-chain walk) and `FloatN &lt;: NumberN` (the same walk, read statically) with no parallel `Subtype&lt;A, B&gt;` subsystem. `NatN` is parented to `IntN` (`Nat &lt;: Int &lt;: Number`). The legacy `__tag__`-tagged values above (Int/Str/Bool/Null/Float/ Number/Nat) are NOT deleted yet: existing kind predicates and tag checks (`type.is`, `tag.tag_of`, registry equality) match on the `__tag__` string, which a `{"__sym__": ...}` nominal does not carry. Behavior compatibility is preserved by keeping both spellings until consumers migrate. Note the semantic difference: legacy tags compare by structure (two `{__tag__: "int"}` objects are equal) while nominals compare by identity (two `sym()` mints are distinct even with the same presentation name) -- and `instanceof` walks the nominal parent chain, never the `__tag__` string. Surface: `sym()` / `sym(parent)` need no new syntax -- they parse via the existing `call` rule and resolve through the `sym` module (see `SymModule` in `handl-runtime`). `NumberN` below is literally `sym()`; `FloatN` is literally `sym(NumberN)`.

**Signature:** `type.NumberN(sym())`

## `type.Str`

**Signature:** `type.Str({ "__tag__": "str", "__registry__": "type", "kind": "primitive" })`

## `type.Str`

**Signature:** `type.Str({ "__tag__": "str", "__registry__": "type", "kind": "primitive" })`

## `type.coalesce`

NATIVE op: variadic; handl arrows have fixed arity.

**Signature:** `type.coalesce : Value -&gt; Value`

## `type.default`

**Signature:** `type.default : (Value, Value) -&gt; Value`

## `type.identity`

**Signature:** `type.identity : Value -&gt; Value`

## `type.is`

test whether a value matches a kind spelling (canonical tags,

**Signature:** `type.is : (Value, String) -&gt; Bool`

## `type.may`

project a kind (value or null).

**Signature:** `type.may : (Value, String) -&gt; Bool`

## `type.must`

assert a kind ({ok: v} or {err: msg}).

**Signature:** `type.must : (Value, String) -&gt; Value`

## `type.not`

kind complement (value or null).

**Signature:** `type.not : (Value, String) -&gt; Bool`

## `type.of`

NATIVE op: return the kind tag of a value ("null", "bool",

**Signature:** `type.of : Value -&gt; String`

## `type.to_bool`

pure-handl truthiness.

**Signature:** `type.to_bool : Value -&gt; Bool`

## `type.to_number`

**Signature:** `type.to_number : Value -&gt; Number`

## `type.to_string`

**Signature:** `type.to_string : Value -&gt; String`

## `type.type_of`

**Signature:** `type.type_of : Value -&gt; String`

## `type.typeof`

**Signature:** `type.typeof : Value -&gt; String`
