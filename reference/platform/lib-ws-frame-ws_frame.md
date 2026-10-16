# Ws Frame

## `ws_frame.all_need_more`

decode every buffer in `bs`; `true` when each one

comes back `None`.

**Signature:** `ws_frame.all_need_more((decode: Decode, bs))`

## `ws_frame.complete`

decode consumes exactly one frame: a lone encoded frame leaves an

empty rest. Coalesced frames are therefore peeled one at a time by feeding `rest` back to `decode`.

**Signature:** `ws_frame.complete((encode: Encode, decode: Decode))`

## `ws_frame.Decode`

read one frame off the front of a buffer. `None` means the

buffer holds only a strict prefix (need more bytes); `Some` returns the frame and the unconsumed `rest`.

**Signature:** `ws_frame.Decode((Bytes))`

## `ws_frame.DecodeOut`

The `decode` success record: the decoded `frame` plus `rest`, the

unconsumed bytes trailing it. Named separately so the `Option` application in `Decode` takes a var (a record literal does not round-trip through the formatter in generic-argument position).

**Signature:** `ws_frame.DecodeOut({ frame: Frame, rest: Bytes })`

## `ws_frame.empty`

the constantly-empty-buffer arrow, named so `complete` can

mention it.

**Signature:** `ws_frame.empty((x))`

## `ws_frame.Encode`

serialize a frame.

**Signature:** `ws_frame.Encode((input: EncodeIn))`

## `ws_frame.EncodeIn`

The `encode` input record: a `Frame` plus `mask_key` -- empty to

emit an unmasked frame, 4 bytes to emit a masked one (the caller owns key entropy and length). Named separately because an arrow parameter must be a (possibly annotated) var, so the record shape cannot appear inline in `Encode`.

**Signature:** `ws_frame.EncodeIn({ fin: Nat, op: Nat, payload: Bytes, mask_key: Bytes })`

## `ws_frame.Frame`

A decoded frame. `fin` is 1 (final fragment) or 0 (continuation);

`op` is the 4-bit opcode -- use the `Op*` constants; `payload` is always unmasked (the wire mask bit and key do not surface here).

**Signature:** `ws_frame.Frame({ fin: Nat, op: Nat, payload: Bytes })`

## `ws_frame.frame_in`

the `Frame` an `Encode` input describes (`mask_key` is

encode-only; it does not survive a decode round-trip).

**Signature:** `ws_frame.frame_in((r))`

## `ws_frame.frame_of`

project the frame out of a `Some` decode result.

**Signature:** `ws_frame.frame_of((o))`

## `ws_frame.OpBinary`

**Signature:** `ws_frame.OpBinary(2)`

## `ws_frame.OpClose`

**Signature:** `ws_frame.OpClose(8)`

## `ws_frame.OpContinuation`

RFC 6455 §5.2 opcode constants.

**Signature:** `ws_frame.OpContinuation(0)`

## `ws_frame.OpPing`

**Signature:** `ws_frame.OpPing(9)`

## `ws_frame.OpPong`

**Signature:** `ws_frame.OpPong(10)`

## `ws_frame.OpText`

**Signature:** `ws_frame.OpText(1)`

## `ws_frame.prefix`

need_more on every strict prefix: no proper truncation of an encoded

frame decodes to a frame -- incremental decoding is honest.

**Signature:** `ws_frame.prefix((encode: Encode, decode: Decode))`

## `ws_frame.prefixes`

every strict prefix of a buffer, shortest first. The

`prefix` law quantifies over all truncations through this helper.

**Signature:** `ws_frame.prefixes((b))`

## `ws_frame.rest_of`

project the unconsumed tail out of a `Some` decode

result.

**Signature:** `ws_frame.rest_of((o))`

## `ws_frame.roundtrip`

decode is a left inverse of encode up to the mask: decoding what a

conforming encoder produced returns the input frame (the mask key is consumed on the wire). Quantified over the contract signatures so any implementation can be checked against it.

**Signature:** `ws_frame.roundtrip((encode: Encode, decode: Decode))`
