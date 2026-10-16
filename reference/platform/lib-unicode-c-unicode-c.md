# Unicode C

## `unicode-c.available`

Whether the host `libicuuc` was found and its symbol suffix resolved.

## `unicode-c.casefold`

Full case fold of `s` (CaseFolding.txt).

**Signature:** `unicode-c.casefold(s)`

## `unicode-c.code_point_at`

Code point at index `i`, or null past the end (exact; needs no ICU).

**Signature:** `unicode-c.code_point_at((s, i))`

## `unicode-c.code_points`

Code points of `s` (exact; needs no ICU).

**Signature:** `unicode-c.code_points(s)`

## `unicode-c.decode`

UTF-8 `[byte_offset, code_point]` pairs (pure handl; needs no ICU).

**Signature:** `unicode-c.decode(s)`

## `unicode-c.from_code_points`

Inverse of `code_points` (exact; needs no ICU).

**Signature:** `unicode-c.from_code_points(xs)`

## `unicode-c.grapheme_count`

Number of grapheme clusters in `s`.

**Signature:** `unicode-c.grapheme_count(s)`

## `unicode-c.graphemes`

Grapheme clusters of `s` (UAX #29, UBRK_CHARACTER).

**Signature:** `unicode-c.graphemes(s)`

## `unicode-c.icu_version`

The detected ICU major version (0 when unavailable).

## `unicode-c.is_ascii`

Whether every scalar of `s` is ASCII (exact; needs no ICU).

**Signature:** `unicode-c.is_ascii(s)`

## `unicode-c.is_valid_identifier`

Whether `s` is a valid Unicode identifier (UAX #31).

**Signature:** `unicode-c.is_valid_identifier(s)`

## `unicode-c.is_xid_continue`

Whether the first scalar of `s` is XID_Continue.

**Signature:** `unicode-c.is_xid_continue(s)`

## `unicode-c.is_xid_start`

Whether the first scalar of `s` is XID_Start.

**Signature:** `unicode-c.is_xid_start(s)`

## `unicode-c.nfc`

NFC-normalized `s` (UAX #15).

**Signature:** `unicode-c.nfc(s)`

## `unicode-c.nfd`

NFD-normalized `s` (UAX #15).

**Signature:** `unicode-c.nfd(s)`

## `unicode-c.width`

Terminal display width of `s` (UAX #11).

**Signature:** `unicode-c.width(s)`
