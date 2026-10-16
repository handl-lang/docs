# Intl C

## `intl-c.available`

## `intl-c.compare_strings`

Compare two strings under `locale` collation (null = ICU default).

`opts`: { sensitivity: "base"|"accent"|"case"|"variant", caseFirst: "upper"|"lower"|"false", numeric: bool }.

**Signature:** `intl-c.compare_strings((a, b, locale, opts))`

## `intl-c.display_name`

Display name for `code` of `name_type` ("language", "region", "script",

"locale", "key", or a unicode key like "currency"/"calendar") in `locale`.

**Signature:** `intl-c.display_name((code, name_type, locale, opts))`

## `intl-c.format_date`

Format a date — epoch-ms number or "YYYY-MM-DD[THH:mm[:ss][Z|±hh:mm]]".

`opts`: { dateStyle, timeStyle: "full"|"long"|"medium"|"short", timeZone: "UTC" }.

**Signature:** `intl-c.format_date((v, locale, opts))`

## `intl-c.format_date_to_parts`

Like `format_date` but returns `[{type, value}]` parts

(year, month, day, weekday, dayPeriod, timeZoneName, literal, …).

**Signature:** `intl-c.format_date_to_parts((v, locale, opts))`

## `intl-c.format_duration`

Intl.DurationFormat: `v` is a {years,…,nanoseconds} record (integer fields,

consistent sign) or an elapsed-seconds number (extension). `opts`: { style: "long"|"short"|"narrow"|"digital" (default "short"), fractionalDigits: 0-9 } — "digital" gives "1:46:40", textual styles give "1 hr, 46 min and 40 sec" via CLDR unit + list patterns.

**Signature:** `intl-c.format_duration((v, locale, opts))`

## `intl-c.format_list`

Format a list of strings ("a, b, and c") via CLDR listPattern data.

`opts`: { type: "and"|"or"|"unit", style: "wide"|"short"|"narrow" }.

**Signature:** `intl-c.format_list((items, locale, opts))`

## `intl-c.format_number`

Format `n` under `locale` (null = ICU default).

`opts`: { style: "decimal"|"currency"|"percent"|"scientific"|"spellout"| "ordinal"|"duration", currency: "EUR", useGrouping: bool, minimum/maximumFractionDigits, minimum/maximumIntegerDigits }.

**Signature:** `intl-c.format_number((n, locale, opts))`

## `intl-c.format_number_to_parts`

Like `format_number` but returns `[{type, value}]` parts

(integer, fraction, group, currency, percentSign, minusSign, literal, …).

**Signature:** `intl-c.format_number_to_parts((n, locale, opts))`

## `intl-c.format_relative_time`

`n` of `unit` ("day", "hour", …) as relative time ("3 days ago").

`opts`: { style: "long"|"short"|"narrow", numeric: "auto"|"always" }.

**Signature:** `intl-c.format_relative_time((n, unit, locale, opts))`

## `intl-c.get_canonical_locales`

Canonicalize a tag or list of tags → same shape back.

**Signature:** `intl-c.get_canonical_locales(v)`

## `intl-c.icu_version`

## `intl-c.locale`

Parse a BCP-47 `tag` → {tag, locale_id, base_name, language, script,

region, variant, canonical}.

**Signature:** `intl-c.locale((t, opts))`

## `intl-c.segment`

Segment `text` by `granularity` ("grapheme", "word", "sentence", "line")

→ `[{index, segment}]`; "word" adds `isWordLike`. Indices are UTF-16 units.

**Signature:** `intl-c.segment((text, granularity, locale, opts))`

## `intl-c.select_plural`

Plural category of `n` in `locale`; `opts`: { type: "cardinal"|"ordinal" }.

**Signature:** `intl-c.select_plural((n, locale, opts))`

## `intl-c.supported_locales_of`

Filter requested tag(s) to those covered by ICU's locale data

(canonicalized; prefix fallback counts — "en" covers "en-US").

**Signature:** `intl-c.supported_locales_of((requested, opts))`
