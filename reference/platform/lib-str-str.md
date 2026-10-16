# Str

## `str.camel_case`

**Signature:** `str.camel_case : String -&gt; String`

## `str.capitalize`

**Signature:** `str.capitalize : String -&gt; String`

## `str.char_at`

**Signature:** `str.char_at : (String * Int) -&gt; String`

## `str.concat`

LAW: LengthEq(output, input.0 + input.1) (sum not expressible; length is monotone in each part)

**Signature:** `str.concat : (String * String) -&gt; String`

## `str.contains`

**Signature:** `str.contains : (String * String) -&gt; Bool`

## `str.count`

LAW: Le(0, output) && CountEq(input.0, input.1, output)

**Signature:** `str.count : (String * String) -&gt; Int`

## `str.ends_with`

LAW: output &lt;=&gt; IsSuffix(input.1, input.0)

**Signature:** `str.ends_with : (String * String) -&gt; Bool`

## `str.equals`

LAW: output &lt;=&gt; CharEq(input.0, input.1)

**Signature:** `str.equals : (String * String) -&gt; Bool`

## `str.find`

**Signature:** `str.find : (String * String) -&gt; Int`

## `str.is_alpha`

LAW: output &lt;=&gt; AllSatisfy(input, IsAlpha)

**Signature:** `str.is_alpha : String -&gt; Bool`

## `str.is_alphanumeric`

LAW: output &lt;=&gt; AllSatisfy(input, IsAlnum)

**Signature:** `str.is_alphanumeric : String -&gt; Bool`

## `str.is_empty`

LAW: output &lt;=&gt; IsEmpty(input)

**Signature:** `str.is_empty : String -&gt; Bool`

## `str.is_numeric`

LAW: output &lt;=&gt; AllSatisfy(input, IsNumeric)

**Signature:** `str.is_numeric : String -&gt; Bool`

## `str.join`

**Signature:** `str.join : (List String * String) -&gt; String`

## `str.kebab_case`

**Signature:** `str.kebab_case : String -&gt; String`

## `str.length`

**Signature:** `str.length : String -&gt; Int`

## `str.levenshtein`

LAW: Le(0, output) && EditDistance(input.0, input.1, output)

**Signature:** `str.levenshtein : (String * String) -&gt; Int`

## `str.lines`

**Signature:** `str.lines : String -&gt; List String`

## `str.lower`

LAW: IsLower(output) && LengthEq(output, input)

**Signature:** `str.lower : String -&gt; String`

## `str.pad_left`

**Signature:** `str.pad_left : (String * (Int * String)) -&gt; String`

## `str.pad_right`

**Signature:** `str.pad_right : (String * (Int * String)) -&gt; String`

## `str.pascal_case`

**Signature:** `str.pascal_case : String -&gt; String`

## `str.repeat`

**Signature:** `str.repeat : (String * Int) -&gt; String`

## `str.replace`

LAW: NoOccurrence(output, input.1.0)

**Signature:** `str.replace : (String * (String * String)) -&gt; String`

## `str.replace_first`

LAW: CountEq(output, input.1.0, Count(input, input.1.0) - 1)

**Signature:** `str.replace_first : (String * (String * String)) -&gt; String`

## `str.reverse`

LAW: IsReversed(output, input) && IsPerm(output, input)

**Signature:** `str.reverse : String -&gt; String`

## `str.rfind`

**Signature:** `str.rfind : (String * String) -&gt; Int`

## `str.similarity`

LAW: Le(0, output) && Le(output, 1) && Similarity(input.0, input.1, output) (typed Int since Float is not a base type; ratio in [0, 1])

**Signature:** `str.similarity : (String * String) -&gt; Int`

## `str.slice`

**Signature:** `str.slice : (String * (Int * Int)) -&gt; String`

## `str.slugify`

LAW: IsSlug(output)

**Signature:** `str.slugify : String -&gt; String`

## `str.snake_case`

**Signature:** `str.snake_case : String -&gt; String`

## `str.split`

**Signature:** `str.split : (String * String) -&gt; List String`

## `str.split_at`

**Signature:** `str.split_at : (String * Int) -&gt; List String`

## `str.split_whitespace`

**Signature:** `str.split_whitespace : String -&gt; List String`

## `str.starts_with`

LAW: output &lt;=&gt; IsPrefix(input.1, input.0)

**Signature:** `str.starts_with : (String * String) -&gt; Bool`

## `str.strip_prefix`

**Signature:** `str.strip_prefix : (String * String) -&gt; String`

## `str.strip_suffix`

**Signature:** `str.strip_suffix : (String * String) -&gt; String`

## `str.title_case`

**Signature:** `str.title_case : String -&gt; String`

## `str.trim`

LAW: IsTrimmed(output) && LengthLe(output, input)

**Signature:** `str.trim : String -&gt; String`

## `str.trim_end`

LAW: IsTrimmedEnd(output) && LengthLe(output, input)

**Signature:** `str.trim_end : String -&gt; String`

## `str.trim_matches`

LAW: IsTrimmed(output) && LengthLe(output, input.0)

**Signature:** `str.trim_matches : (String * String) -&gt; String`

## `str.trim_start`

LAW: IsTrimmedStart(output) && LengthLe(output, input)

**Signature:** `str.trim_start : String -&gt; String`

## `str.truncate`

**Signature:** `str.truncate : (String * Int) -&gt; String`

## `str.upper`

LAW: IsUpper(output) && LengthEq(output, input)

**Signature:** `str.upper : String -&gt; String`

## `str.word_wrap`

**Signature:** `str.word_wrap : (String * Int) -&gt; String`
