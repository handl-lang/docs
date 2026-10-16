# Concurrent Epoll

## `concurrent-epoll.run`

run tasks until the main task (id 1) completes: drain the runq;

when it empties fire due timers; when nothing can wake the parked tasks that's a deadlock; otherwise block in epoll_wait. Spawned daemon tasks (e.g. an accept loop) may still be live when main finishes -- run abandons them.

**Signature:** `concurrent-epoll.run((task, init))`

## `concurrent-epoll.tcp_close`

**Signature:** `concurrent-epoll.tcp_close((fd))`

## `concurrent-epoll.tcp_connect`

initiate a nonblocking connect. Returns { fd, pending } -- when

`pending` is true the handshake is in flight; a task completes it with { call: { name: "connect_wait", fd } }.

**Signature:** `concurrent-epoll.tcp_connect((addr))`

## `concurrent-epoll.tcp_listen`

bind+listen. `addr` = { host: "0.0.0.0"|dotted-quad, port: Int }.

**Signature:** `concurrent-epoll.tcp_listen((addr))`
