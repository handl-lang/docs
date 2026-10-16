# Bytes

## `bytes.at`

the byte at `index` (error when out of bounds).

**Signature:** `bytes.at : (Bytes * Int) -&gt; Int`

## `bytes.concat`

concatenate two Bytes buffers.

**Signature:** `bytes.concat : (Bytes * Bytes) -&gt; Bytes`

## `bytes.from_list`

build a Bytes buffer from a list of ints (each must be 0..=255).

**Signature:** `bytes.from_list : (List Int) -&gt; Bytes`

## `bytes.len`

byte length of a Bytes buffer.

**Signature:** `bytes.len : Bytes -&gt; Int`

## `bytes.slice`

copy out the `len`-byte window at `offset`, clamped to the buffer.

**Signature:** `bytes.slice : (Bytes * Int * Int) -&gt; Bytes`

## `bytes.to_list`

project a Bytes buffer to a list of ints.

**Signature:** `bytes.to_list : Bytes -&gt; (List Int)`

## `bytes.utf8_decode`

UTF-8 decode Bytes into a String (error on invalid UTF-8).

**Signature:** `bytes.utf8_decode : Bytes -&gt; String`

## `bytes.utf8_encode`

UTF-8 encode a String into Bytes.

**Signature:** `bytes.utf8_encode : String -&gt; Bytes`
