# Intl

## `intl.CompareStrings`

Compare two strings under locale-aware collation.

`ok -1 | 0 | 1`, or `err msg`.

**Signature:** `intl.CompareStrings : (String, String, Value, Value) ~[1]~&gt; Result&lt;Int, String&gt;`

## `intl.DisplayName`

Display name for a code (language, region, script) in a locale.

**Signature:** `intl.DisplayName : (Value, Value, Value, Value) ~[1]~&gt; Result&lt;String, String&gt;`

## `intl.FormatDate`

Format a date for a locale with options.

**Signature:** `intl.FormatDate : (Value, Value, Value) ~[1]~&gt; Result&lt;String, String&gt;`

## `intl.FormatDateToParts`

Format a date into named parts.

**Signature:** `intl.FormatDateToParts : (Value, Value, Value) ~[1]~&gt; Result&lt;Value, String&gt;`

## `intl.FormatDuration`

Format a duration for a locale (Intl.DurationFormat): the value is a

{years,…,nanoseconds} record or an elapsed-seconds number; opts.style is "long"|"short"|"narrow"|"digital" (default "short").

**Signature:** `intl.FormatDuration : (Value, Value, Value) ~[1]~&gt; Result&lt;String, String&gt;`

## `intl.FormatList`

Format a list of strings for a locale (`"a, b, and c"`).

**Signature:** `intl.FormatList : (Value, Value, Value) ~[1]~&gt; Result&lt;String, String&gt;`

## `intl.FormatNumber`

Format a number for a locale.

`ok "1,234.5"`, or `err msg`.

**Signature:** `intl.FormatNumber : (Value, Value, Value) ~[1]~&gt; Result&lt;String, String&gt;`

## `intl.FormatNumberToParts`

Format a number into named parts (integer, fraction, group, ...).

**Signature:** `intl.FormatNumberToParts : (Value, Value, Value) ~[1]~&gt; Result&lt;Value, String&gt;`

## `intl.FormatRelativeTime`

Format a value + unit as relative time (`"3 days ago"`).

**Signature:** `intl.FormatRelativeTime : (Value, Value, Value, Value) ~[1]~&gt; Result&lt;String, String&gt;`

## `intl.GetCanonicalLocales`

Canonicalize a locale or list of locales.

**Signature:** `intl.GetCanonicalLocales : (Value) ~[1]~&gt; Result&lt;Value, String&gt;`

## `intl.Locale`

Parse a BCP-47 locale tag into its components.

**Signature:** `intl.Locale : (String, Value) ~[1]~&gt; Result&lt;Value, String&gt;`

## `intl.Segment`

Segment text by granularity (grapheme, word, sentence, line).

**Signature:** `intl.Segment : (String, Value, Value, Value) ~[1]~&gt; Result&lt;Value, String&gt;`

## `intl.SelectPlural`

Select the plural category of a number in a locale.

`ok "one" | "few" | "other" | ...`, or `err msg`.

**Signature:** `intl.SelectPlural : (Value, Value, Value) ~[1]~&gt; Result&lt;String, String&gt;`

## `intl.SupportedLocalesOf`

Filter requested locales to those the backend's data supports.

**Signature:** `intl.SupportedLocalesOf : (Value, Value) ~[1]~&gt; Result&lt;Value, String&gt;`
