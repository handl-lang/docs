# Str

## `str.camel_case`

convert a string to camelCase.

**Signature:** `str.camel_case : String -&gt; String`

## `str.capitalize`

capitalize the first character of a string.

**Signature:** `str.capitalize : String -&gt; String`

## `str.char_at`

get the character at a given index.

**Signature:** `str.char_at : (String * Float) -&gt; String`

## `str.concat`

concatenate two or more strings.

**Signature:** `str.concat : (String * String) -&gt; String`

## `str.contains`

test whether a string contains a substring.

**Signature:** `str.contains : (String * String) -&gt; Bool`

## `str.count`

count non-overlapping occurrences of a substring.

**Signature:** `str.count : (String * String) -&gt; Float`

## `str.ends_with`

test whether a string ends with a suffix.

**Signature:** `str.ends_with : (String * String) -&gt; Bool`

## `str.equals`

test whether two strings are equal.

**Signature:** `str.equals : (String * String) -&gt; Bool`

## `str.find`

find the char index of the first occurrence of a substring.

**Signature:** `str.find : (String * String) -&gt; Float`

## `str.is_alpha`

test whether a string contains only alphabetic characters.

**Signature:** `str.is_alpha : String -&gt; Bool`

## `str.is_alphanumeric`

test whether a string contains only alphanumeric characters.

**Signature:** `str.is_alphanumeric : String -&gt; Bool`

## `str.is_empty`

test whether a string is empty.

**Signature:** `str.is_empty : String -&gt; Bool`

## `str.is_numeric`

test whether a string contains only numeric characters.

**Signature:** `str.is_numeric : String -&gt; Bool`

## `str.join`

join a list of strings with a separator.

**Signature:** `str.join : ((List String) * String) -&gt; String`

## `str.kebab_case`

convert a string to kebab-case.

**Signature:** `str.kebab_case : String -&gt; String`

## `str.length`

count the characters in a string.

**Signature:** `str.length : String -&gt; Float`

## `str.levenshtein`

compute the Levenshtein edit distance between two strings.

**Signature:** `str.levenshtein : (String * String) -&gt; Float`

## `str.lines`

split a string into a list of lines.

**Signature:** `str.lines : String -&gt; (List String)`

## `str.lower`

convert a string to lowercase.

**Signature:** `str.lower : String -&gt; String`

## `str.pad_left`

pad a string on the left to a target length.

**Signature:** `str.pad_left : (String * Float * String) -&gt; String`

## `str.pad_right`

pad a string on the right to a target length.

**Signature:** `str.pad_right : (String * Float * String) -&gt; String`

## `str.pascal_case`

convert a string to PascalCase.

**Signature:** `str.pascal_case : String -&gt; String`

## `str.repeat`

repeat a string a given number of times.

**Signature:** `str.repeat : (String * Float) -&gt; String`

## `str.replace`

replace all occurrences of a substring.

**Signature:** `str.replace : (String * String * String) -&gt; String`

## `str.replace_first`

replace the first occurrence of a substring.

**Signature:** `str.replace_first : (String * String * String) -&gt; String`

## `str.reverse`

reverse the characters of a string.

**Signature:** `str.reverse : String -&gt; String`

## `str.rfind`

find the char index of the last occurrence of a substring.

**Signature:** `str.rfind : (String * String) -&gt; Float`

## `str.similarity`

compute a normalized similarity ratio between two strings.

**Signature:** `str.similarity : (String * String) -&gt; Float`

## `str.slice`

extract a substring by char-index range.

**Signature:** `str.slice : (String * Float * Float) -&gt; String`

## `str.slugify`

convert a string to a URL-safe slug.

**Signature:** `str.slugify : String -&gt; String`

## `str.snake_case`

convert a string to snake_case.

**Signature:** `str.snake_case : String -&gt; String`

## `str.split`

split a string by a separator into a list.

**Signature:** `str.split : (String * String) -&gt; (List String)`

## `str.split_at`

split a string at a char index into two parts.

**Signature:** `str.split_at : (String * Float) -&gt; (List String)`

## `str.split_whitespace`

split a string on whitespace into a list.

**Signature:** `str.split_whitespace : String -&gt; (List String)`

## `str.starts_with`

test whether a string starts with a prefix.

**Signature:** `str.starts_with : (String * String) -&gt; Bool`

## `str.strip_prefix`

remove a leading prefix if present.

**Signature:** `str.strip_prefix : (String * String) -&gt; String`

## `str.strip_suffix`

remove a trailing suffix if present.

**Signature:** `str.strip_suffix : (String * String) -&gt; String`

## `str.title_case`

capitalize the first character of each word.

**Signature:** `str.title_case : String -&gt; String`

## `str.trim`

strip leading and trailing whitespace.

**Signature:** `str.trim : String -&gt; String`

## `str.trim_end`

strip trailing whitespace.

**Signature:** `str.trim_end : String -&gt; String`

## `str.trim_matches`

strip leading/trailing characters matching a set.

**Signature:** `str.trim_matches : (String * String) -&gt; String`

## `str.trim_start`

strip leading whitespace.

**Signature:** `str.trim_start : String -&gt; String`

## `str.truncate`

truncate a string to a max length with an optional suffix.

**Signature:** `str.truncate : (String * Float) -&gt; String`

## `str.upper`

convert a string to uppercase.

**Signature:** `str.upper : String -&gt; String`

## `str.word_wrap`

wrap text to a given line width.

**Signature:** `str.word_wrap : (String * Float) -&gt; String`
