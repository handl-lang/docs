# Serve Epoll

## `serve-epoll.listener_task`

accept forever; spawn a conn_task per connection.

**Signature:** `serve-epoll.listener_task((s))`

## `serve-epoll.serve`

serve(handler, { port, host?, tls?: { cert, key } }) -- listen and

run the accept loop forever (blocks; this IS the process main loop).

**Signature:** `serve-epoll.serve((handler, opts))`

## `serve-epoll.serve_task`

serve_task(handler, opts) -- handler is a step-arrow: it is

`enter`ed per request and may suspend on any scheduler op.

**Signature:** `serve-epoll.serve_task((handler, opts))`

## `serve-epoll.tls_ctx_server`

exported so callers can build a shared SSL_CTX for `opts.tls`.

**Signature:** `serve-epoll.tls_ctx_server(tlsp.ctx_server)`
