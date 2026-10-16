# Tag

## `tag.construct`

mint a registry-scoped type value (ADR-0054).

**Signature:** `tag.construct : (String, Value) -&gt; Value`

## `tag.is_tag`

test whether a value is a tagged value (inspection).

**Signature:** `tag.is_tag : Value -&gt; Bool`

## `tag.match_type`

dispatch on the type tag of a value (ADR-0054).

**Signature:** `tag.match_type : (Value, Value) -&gt; Value`

## `tag.tag`

mint a tagged value (host capability, ADR-0055).

**Signature:** `tag.tag : (String, Value) -&gt; Value`

## `tag.tag_of`

return the tag name of a tagged value (inspection).

**Signature:** `tag.tag_of : Value -&gt; Value`

## `tag.untag`

return the payload of a tagged value (inspection).

**Signature:** `tag.untag : Value -&gt; Value`
