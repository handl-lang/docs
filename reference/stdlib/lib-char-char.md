# Char

## `char.at`

LAW: output = input[input.1] as a 1-char string

**Signature:** `char.at : (String * Int) -&gt; String`

## `char.chars`

LAW: LengthEq(output, input) && forall c in output, IsChar(c) && from_chars(chars(s)) = s  (round-trip)

**Signature:** `char.chars : String -&gt; List String`

## `char.code_point`

LAW: output = CodePoint(input); requires input is a single char

**Signature:** `char.code_point : String -&gt; Int`

## `char.code_point_at`

**Signature:** `char.code_point_at : (String * Int) -&gt; Int`

## `char.concat`

LAW: LengthEq(output, input.0 + input.1)

**Signature:** `char.concat : (String * String) -&gt; String`

## `char.from_chars`

LAW: from_chars(chars(s)) = s  (round-trip)

**Signature:** `char.from_chars : List String -&gt; String`

## `char.from_code_point`

LAW: output is the char whose scalar value is input; fails if input is not a valid scalar value in the backend's character set

**Signature:** `char.from_code_point : Int -&gt; String`

## `char.is_alnum`

LAW: output &lt;=&gt; IsAlpha(input) || IsNumeric(input)

**Signature:** `char.is_alnum : String -&gt; Bool`

## `char.is_alpha`

LAW: output &lt;=&gt; IsAlpha(input)  (backend-defined "alphabetic")

**Signature:** `char.is_alpha : String -&gt; Bool`

## `char.is_lowercase`

LAW: output &lt;=&gt; IsLower(input)

**Signature:** `char.is_lowercase : String -&gt; Bool`

## `char.is_numeric`

LAW: output &lt;=&gt; IsNumeric(input)  (backend-defined "numeric")

**Signature:** `char.is_numeric : String -&gt; Bool`

## `char.is_uppercase`

LAW: output &lt;=&gt; IsUpper(input)

**Signature:** `char.is_uppercase : String -&gt; Bool`

## `char.is_whitespace`

LAW: output &lt;=&gt; IsWhitespace(input)  (backend-defined "whitespace")

**Signature:** `char.is_whitespace : String -&gt; Bool`

## `char.length`

LAW: output = number of chars in input

**Signature:** `char.length : String -&gt; Int`

## `char.slice`

LAW: output = input[input.1 .. input.2] (char indices)

**Signature:** `char.slice : (String * (Int * Int)) -&gt; String`

## `char.to_lower`

LAW: IsLower(output)

**Signature:** `char.to_lower : String -&gt; String`

## `char.to_title`

LAW: IsTitle(output); backends without titlecase use to_upper

**Signature:** `char.to_title : String -&gt; String`

## `char.to_upper`

LAW: IsUpper(output)  (backend-defined case map; may expand e.g. ß-&gt;SS)

**Signature:** `char.to_upper : String -&gt; String`
