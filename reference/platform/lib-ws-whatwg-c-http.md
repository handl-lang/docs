# Http

## `http.accept_key`

the expected `Sec-WebSocket-Accept` value for a client

nonce: `base64(sha1(key ++ GUID))` (RFC 6455 section 1.3). `crypto.sha1` returns hex, so the digest is decoded to bytes before the pure `b64_encode`. @param {key} - the Sec-WebSocket-Key the client sent

**Signature:** `http.accept_key((key))`

## `http.b64_encode`

standard base64 (RFC 4648, `+/` alphabet with `=`

padding) over a list of byte ints. @param {bs} - the input bytes as a list of ints

**Signature:** `http.b64_encode((bs))`

## `http.build_101_resp`

the server half of the handshake: the raw

`101 Switching Protocols` response head for a client nonce (RFC 6455 section 1.3 / 4.2.2), `Sec-WebSocket-Accept` computed with `accept_key`. @param {key} - the Sec-WebSocket-Key the client sent

**Signature:** `http.build_101_resp((key))`

## `http.GUID`

The RFC 6455 section 1.3 magic GUID appended to the client key

before hashing.

**Signature:** `http.GUID("258EAFA5-E914-47DA-95CA-C5AB0DC85B11")`

## `http.Head`

A parsed response head: the numeric status plus the header list.

**Signature:** `http.Head({ status: Int, headers: [Header] })`

## `http.head_end`

the index just past the first `"\r\n\r\n"` terminator

in a byte buffer, or -1 while the head is still incomplete. Pure byte scan so the (possibly binary) frame bytes trailing the head are never UTF-8 decoded. @param {buf} - the Bytes accumulated so far

**Signature:** `http.head_end((buf))`

## `http.Header`

A single response header; `name` is stored lowercased.

**Signature:** `http.Header({ name: String, value: String })`

## `http.header_get`

case-insensitive header lookup over a `parse_head`

header list; returns the value or null when absent. @param {headers} - the [{name, value}] list from parse_head @param {name} - the header name to find (any case)

**Signature:** `http.header_get((headers, name))`

## `http.header_has_token`

whether a comma-list header (e.g. `Connection`)

carries `token`, case-insensitively. RFC 9110 section 7.3 field lists: `Connection: keep-alive, Upgrade` must match `upgrade`. @param {headers} - the [{name, value}] list from parse_head @param {name} - the header name to find (any case) @param {token} - the list token to look for (any case)

**Signature:** `http.header_has_token((headers, name, token))`

## `http.hex_decode`

decode a hex string (any mix of upper/lowercase) into

a list of byte ints. Pairs are consumed left to right; a trailing half-pair is dropped. @param {s} - the hex string

**Signature:** `http.hex_decode((s))`

## `http.parse_head`

parse a raw HTTP response head: the status line

`HTTP/1.1 &lt;code&gt; &lt;reason&gt;` plus colon-separated header lines into `{status, headers}` with header names lowercased. Lines without a colon (including the blank terminator) are skipped. @param {s} - the raw response head

**Signature:** `http.parse_head((s))`

## `http.parse_req_head`

`parse_head` for the request side: the request

line `&lt;METHOD&gt; &lt;target&gt; &lt;proto&gt;` plus colon-separated header lines into `{method, headers}` with header names lowercased. Lines without a colon (including the blank terminator) are skipped. @param {s} - the raw request head

**Signature:** `http.parse_req_head((s))`

## `http.parse_url`

read a `ws://`/`wss://host[:port][/path]` URL into

`{host, port, path, scheme}`. Port defaults to 80 for `ws://` and 443 for `wss://`, path to `"/"`. Raises on any other scheme, an empty host, or a non-numeric/out-of-range port. @param {s} - the URL string

**Signature:** `http.parse_url((s))`

**Returns:** scheme: String }}

## `http.ReqHead`

A parsed request head: the method (uppercased) plus the header

list. `server.accept` consumes this shape.

**Signature:** `http.ReqHead({ method: String, headers: [Header] })`

## `http.upgrade_req`

build the RFC 6455 section 1.2 client upgrade

request for `{host, port, path}` and the base64 nonce `key`. @param {u} - { host: String, port: Int, path: String } @param {key} - the base64 Sec-WebSocket-Key nonce

**Signature:** `http.upgrade_req((u, key))`

## `http.UrlIn`

The `{host, port, path, scheme}` record `parse_url` produces and

`upgrade_req` consumes. `scheme` is "ws" or "wss" -- `connect` reads it to decide whether to wrap the socket in TLS.

**Signature:** `http.UrlIn({ host: String, port: Int, path: String, scheme: String })`
