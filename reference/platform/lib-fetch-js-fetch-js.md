# Fetch Js

## `fetch-js.fetch`

Start a fetch. `input` is a URL string or Request object; `init`

follows the WebIDL RequestInit shape (method, headers, body, ...). Returns `{ ok: { promise } }` or `{ err: JsError }` — the result tag of the generated adapter, unwrapped one level.

**Signature:** `fetch-js.fetch((input, init))`
