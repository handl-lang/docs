# Http Rfc

## `http_rfc.alen`

(while, not recursion: self-recursive arrows lose their own

binding when a task env is serialized -- runtime limitation)

**Signature:** `http_rfc.alen((xs))`

## `http_rfc.find_head_end`

**Signature:** `http_rfc.find_head_end((b))`

## `http_rfc.fold_hdrs`

**Signature:** `http_rfc.fold_hdrs((ks, hs, acc))`

## `http_rfc.fold_header`

one "Name: value" header line into the accumulator

**Signature:** `http_rfc.fold_header((acc, line))`

## `http_rfc.nat_of`

digit string to Int, -1 when any char is not a digit

(mirrors ws-whatwg-c/http.hnl).

**Signature:** `http_rfc.nat_of((s))`

## `http_rfc.parse_head`

parse the head block into { method, target, version, headers }

**Signature:** `http_rfc.parse_head((text))`

## `http_rfc.reason`

**Signature:** `http_rfc.reason((code))`

## `http_rfc.serialize_response`

render { status?, headers?, body?|body_bytes? } to wire bytes.

Always emits Content-Length and `connection: close`; `head_only` drops the body for HEAD responses.

**Signature:** `http_rfc.serialize_response((resp, head_only))`

## `http_rfc.split_target`

split "path?query" on the first '?'

**Signature:** `http_rfc.split_target((t))`

## `http_rfc.try_decode_chunked`

decode a chunked body starting at `p`. Returns { body, end } (end =

one past the terminating CRLF), { bad: true } on a malformed stream, or null when the buffer needs more bytes. Trailers are skipped: the stream ends at the first "\r\n\r\n" after the 0-size chunk line.

**Signature:** `http_rfc.try_decode_chunked((buf, p))`

## `http_rfc.try_parse_request`

try to decode a full request from accumulated bytes. Returns

{ req, consumed }, { req: null, consumed } for a bad head, or null when the buffer needs more data.

**Signature:** `http_rfc.try_parse_request((buf))`
