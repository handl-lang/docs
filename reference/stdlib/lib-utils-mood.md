# Mood

## `mood.cnd`

conditional: extract the matching component or return a default.

**Signature:** `mood.cnd : (Value * Value * Value) -&gt; Value`

## `mood.ind`

strict projection: extract the matching component or error.

**Signature:** `mood.ind : (Value * Value) -&gt; Value`

## `mood.int`

intersection: test whether a value matches a kind.

**Signature:** `mood.int : (Value * Value) -&gt; Bool`

## `mood.neg`

complement: extract the non-matching component or null.

**Signature:** `mood.neg : (Value * Value) -&gt; Value`

## `mood.norm`

normalized projection: wrap the result in an ok/err record.

**Signature:** `mood.norm : (Value * Value) -&gt; Value`

## `mood.pot`

potential extraction: extract the matching component or null.

**Signature:** `mood.pot : (Value * Value) -&gt; Value`
