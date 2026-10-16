# Frame

## `frame.decode`

read one frame off the front of `buf`. Returns

`option.none` (need more bytes) while `buf` is a strict prefix of the frame -- truncated header, extended length, mask key, or payload alike -- and `option.some` with `{frame, rest}` once the whole frame is present, where `rest` is whatever trails it.

**Signature:** `frame.decode(Decode)`

## `frame.encode`

serialize `{fin, op, payload, mask_key}` to wire bytes.

`mask_key` empty emits an unmasked frame; 4 bytes emits a masked one with the payload XORed against the key (RFC 6455 §5.1, §5.3).

**Signature:** `frame.encode(Encode)`
