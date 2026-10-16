# Time

## `time.Clock`

@template Clock

Grade for effectful clock reads.

**Signature:** `time.Clock(&lt;T&gt;: Grade)`

## `time.ElapsedNs`

Nanoseconds elapsed since a previous `InstantNs` reading.

@param {start} - a previous `InstantNs` reading

**Signature:** `time.ElapsedNs(Nat)`

## `time.InstantNs`

Nanoseconds on a monotonic clock.

**Signature:** `time.InstantNs(())`

## `time.NowMs`

Wall-clock milliseconds since the Unix epoch.

**Signature:** `time.NowMs(())`

## `time.elapsed_ns`

**Signature:** `time.elapsed_ns : Nat -&gt; Nat`

## `time.instant_ns`

**Signature:** `time.instant_ns : a -&gt; Nat`

## `time.now_ms`

**Signature:** `time.now_ms : a -&gt; Nat`
