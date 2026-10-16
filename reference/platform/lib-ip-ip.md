# Ip

## `ip.format`

format an ip object (or string) into a canonical string.

**Signature:** `ip.format : Value -&gt; String`

## `ip.is_link_local`

test whether an ip address is link-local.

**Signature:** `ip.is_link_local : Value -&gt; Bool`

## `ip.is_loopback`

test whether an ip address is a loopback address.

**Signature:** `ip.is_loopback : Value -&gt; Bool`

## `ip.is_multicast`

test whether an ip address is a multicast address.

**Signature:** `ip.is_multicast : Value -&gt; Bool`

## `ip.is_private`

test whether an ip address is in a private range.

**Signature:** `ip.is_private : Value -&gt; Bool`

## `ip.is_unspecified`

test whether an ip address is unspecified (0.0.0.0 / ::).

**Signature:** `ip.is_unspecified : Value -&gt; Bool`

## `ip.parse`

parse an IP address string into an ip object.

**Signature:** `ip.parse : String -&gt; Value`
