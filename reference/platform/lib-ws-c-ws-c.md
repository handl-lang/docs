# Ws C

## `ws-c.active_socket`

the fd curl uses for this connection (CURLINFO_ACTIVESOCKET) -- what

the scheduler parks on.

**Signature:** `ws-c.active_socket((h))`

## `ws-c.close`

close frame (best effort) then release the handle.

**Signature:** `ws-c.close((h))`

## `ws-c.curle_again`

no complete frame yet (or the send buffer is full).

Not an error: the caller waits for the socket.

**Signature:** `ws-c.curle_again(81)`

## `ws-c.prepare`

prepare(url, init) -&gt; easy handle in WebSocket mode.

init: { insecure?: Bool } -- skip TLS peer/host verification.

**Signature:** `ws-c.prepare((url, init))`

## `ws-c.recv_step`

one non-blocking frame read. `again` = no complete frame buffered.

**Signature:** `ws-c.recv_step((h))`

## `ws-c.send_binary`

send a binary frame.

**Signature:** `ws-c.send_binary((h, b))`

## `ws-c.send_step`

one non-blocking frame write. `flags` is `CURLWS_TEXT`/`CURLWS_BINARY`/

`CURLWS_CLOSE`/...; `again` = the socket is not writable yet.

**Signature:** `ws-c.send_step((h, buf, flags))`

## `ws-c.send_text`

send a text frame.

**Signature:** `ws-c.send_text((h, s))`
