# Time C

## `time-c.elapsed_ns`

Nanoseconds elapsed since a previous `instant_ns` reading.

**Signature:** `time-c.elapsed_ns(ElapsedNs)`

**Examples:**

```handl
```hnl
from "time" import { instant_ns, elapsed_ns }
start = instant_ns()
elapsed_ns(start)
```
```

## `time-c.instant_ns`

Nanoseconds on a monotonic clock.

**Signature:** `time-c.instant_ns(InstantNs)`

**Examples:**

```handl
```hnl
from "time" import { instant_ns }
instant_ns()
```
```

## `time-c.now_ms`

Wall-clock milliseconds since the Unix epoch.

**Signature:** `time-c.now_ms(NowMs)`

**Examples:**

```handl
```hnl
from "time" import { now_ms }
now_ms()
-- 1789238129361
```
```
