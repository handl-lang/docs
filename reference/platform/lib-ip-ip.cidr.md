# Ip.cidr

## `ip.cidr.broadcast`

return the broadcast (last) address of a cidr.

**Signature:** `ip.cidr.broadcast : Value -&gt; String`

## `ip.cidr.contains`

test whether a cidr contains an ip address.

**Signature:** `ip.cidr.contains : (Value, Value) -&gt; Bool`

## `ip.cidr.format`

format a cidr object (or string) into a canonical string.

**Signature:** `ip.cidr.format : Value -&gt; String`

## `ip.cidr.network`

return the network address of a cidr.

**Signature:** `ip.cidr.network : Value -&gt; String`

## `ip.cidr.parse`

parse a CIDR string into a cidr object.

**Signature:** `ip.cidr.parse : String -&gt; Value`
