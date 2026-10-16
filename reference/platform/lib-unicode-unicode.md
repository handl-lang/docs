# Unicode

## `unicode.casefold`

LAW: output = full case fold (CaseFolding.txt); casefold(casefold(s)) = casefold(s) (idempotent) && IsLower(output) under Unicode

**Signature:** `unicode.casefold : String -&gt; String`

## `unicode.code_point_at`

LAW: output = char.code_point_at(input.0, input.1); out-of-range index yields a backend-defined null/0 sentinel

**Signature:** `unicode.code_point_at : (String * Int) -&gt; Int`

## `unicode.code_points`

LAW: output = map char.code_point (char.chars input) && LengthEq(output, char.length input)

**Signature:** `unicode.code_points : String -&gt; List Int`

## `unicode.decode`

LAW: output = [byte_offset, code_point] pairs decoding input's UTF-8 bytes; LengthEq(output, 2 * char.length input) for ASCII

**Signature:** `unicode.decode : String -&gt; List Int`

## `unicode.from_code_points`

LAW: output = char.from_chars (map char.from_code_point input); fails if any element is not a valid scalar value LAW: code_points(from_code_points(input)) = input  (round-trip)

**Signature:** `unicode.from_code_points : List Int -&gt; String`

## `unicode.grapheme_count`

LAW: output = LengthEq(graphemes(input))

**Signature:** `unicode.grapheme_count : String -&gt; Int`

## `unicode.graphemes`

LAW: concat(graphemes(input)) = input  (covering) && LengthEq(output, grapheme_count(input))

**Signature:** `unicode.graphemes : String -&gt; List String`

## `unicode.is_ascii`

LAW: output &lt;=&gt; forall c in char.chars(input), code_point(c) &lt; 128

**Signature:** `unicode.is_ascii : String -&gt; Bool`

## `unicode.is_valid_identifier`

LAW: output &lt;=&gt; input is a valid Unicode identifier (UAX #31: XID_Start followed by XID_Continue*)

**Signature:** `unicode.is_valid_identifier : String -&gt; Bool`

## `unicode.is_xid_continue`

LAW: output &lt;=&gt; first char of input is in XID_Continue

**Signature:** `unicode.is_xid_continue : String -&gt; Bool`

## `unicode.is_xid_start`

LAW: output &lt;=&gt; first char of input is in XID_Start

**Signature:** `unicode.is_xid_start : String -&gt; Bool`

## `unicode.nfc`

LAW: IsNormalized(output, NFC) && nfc(nfc(s)) = nfc(s) (idempotent) && nfc(char.concat(a, nfc(b))) = nfc(char.concat(a, b))

**Signature:** `unicode.nfc : String -&gt; String`

## `unicode.nfd`

LAW: IsNormalized(output, NFD) && nfd(nfd(s)) = nfd(s) (idempotent) && nfc(nfd(s)) = nfc(s)  (round-trip through composition)

**Signature:** `unicode.nfd : String -&gt; String`

## `unicode.width`

LAW: output = sum of per-grapheme display widths (UAX #11) && Le(grapheme_count(input), output) for ASCII-visible text

**Signature:** `unicode.width : String -&gt; Int`
