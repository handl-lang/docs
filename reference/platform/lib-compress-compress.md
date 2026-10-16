# Compress

## `compress.absorb`

Derived form: compress absorbs a trailing decompress ∘ compress

round-trip. Follows from `roundtrip` by right-composition with compress.

**Signature:** `compress.absorb((compress: Compress, decompress: Decompress))`

## `compress.Compress`

**Signature:** `compress.Compress : (Bytes) ~[1]~&gt; Bytes`

## `compress.Decompress`

**Signature:** `compress.Decompress : (Bytes) ~[1]~&gt; Bytes`

## `compress.id`

The identity arrow, named so the laws can mention it.

**Signature:** `compress.id((x))`

## `compress.roundtrip`

decompress is a left inverse of compress: decoding what a conforming

encoder produced returns the input bytes. Quantified over the contract signatures so any backend can be checked against it.

**Signature:** `compress.roundtrip((compress: Compress, decompress: Decompress))`
