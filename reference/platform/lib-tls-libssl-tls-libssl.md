# Tls Libssl

## `tls-libssl.close`

SSL_shutdown + SSL_free.

**Signature:** `tls-libssl.close((ssl))`

## `tls-libssl.ctx_client`

SSL_CTX_new(TLS_client_method()) with default CA paths.

**Signature:** `tls-libssl.ctx_client((_u))`

## `tls-libssl.ctx_free`

**Signature:** `tls-libssl.ctx_free((ctx))`

## `tls-libssl.ctx_server`

SSL_CTX_new(TLS_server_method()) with cert chain + key loaded.

**Signature:** `tls-libssl.ctx_server((cert, key))`

## `tls-libssl.free`

**Signature:** `tls-libssl.free((ssl))`

## `tls-libssl.handshake_step`

one nonblocking SSL_accept / SSL_connect attempt.

**Signature:** `tls-libssl.handshake_step((ssl, is_server))`

## `tls-libssl.read_step`

one nonblocking SSL_read attempt (64KiB window).

**Signature:** `tls-libssl.read_step((ssl))`

## `tls-libssl.wrap_client`

client wrap: fd + SNI + peer hostname verification.

**Signature:** `tls-libssl.wrap_client((ctx, fd, host))`

## `tls-libssl.wrap_server`

SSL_new + SSL_set_fd; no handshake driven yet.

**Signature:** `tls-libssl.wrap_server((ctx, fd))`

## `tls-libssl.write_step`

one nonblocking SSL_write attempt.

**Signature:** `tls-libssl.write_step((ssl, buf))`
