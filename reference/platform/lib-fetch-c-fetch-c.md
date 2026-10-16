# Fetch C

## `fetch-c.fetch`

**Signature:** `fetch-c.fetch((url, init))`

## `fetch-c.fetch_task`

step-arrow task form for concurrent-epoll:

run(fetch_task, { url: "...", init: { method: "POST", ... } }) or `enter`/`spawn` it from another task. The task suspends on `curl_perform`; the scheduler drives the transfer through a shared CURLM + epoll and resumes it with `{ code: CURLcode }`.

**Signature:** `fetch-c.fetch_task((s))`
