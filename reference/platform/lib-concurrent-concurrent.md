# Concurrent

## `concurrent.Run`

A backend's entry point: drive `task(init)` and every spawned

descendant to completion. Returns `{ main: v, results: [{id, v}] }` on success or `{ deadlock: [id] }` when live tasks can never wake.

**Signature:** `concurrent.Run : (Task, Value) ~[1]~&gt; Value`

## `concurrent.run_done`

A finished task runs to its result: running `(s) ~&gt; { out: v }`

hands `v` back as the main result. Quantified over backends so any conforming scheduler can be checked against it.

**Signature:** `concurrent.run_done((run: Run))`

## `concurrent.Task`

**Signature:** `concurrent.Task((Value))`
