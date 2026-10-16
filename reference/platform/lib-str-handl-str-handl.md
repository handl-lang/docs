# Str Handl

## `str-handl.camel_case`

Converts `s` to `camelCase`.

**Signature:** `str-handl.camel_case((s))`

**Examples:**

```handl
`str.camel_case("hello_world-again")`
-- => "helloWorldAgain"
```

## `str-handl.capitalize`

Uppercases the first character of `s` and lowercases the rest.

@param {s} - the input string

**Signature:** `str-handl.capitalize((s))`

**Examples:**

```handl
`str.capitalize("hELLO")`
-- => "Hello"
```

## `str-handl.char_at`

The character of `s` at index `i`.

**Signature:** `str-handl.char_at((s, i))`

**Examples:**

```handl
`str.char_at("hello", 1)`
-- => "e"
```

## `str-handl.concat`

Concatenates `a` and `b`.

@param {a} - the left string @param {b} - the right string

**Signature:** `str-handl.concat((a, b))`

**Examples:**

```handl
`str.concat("foo", "bar")`
-- => "foobar"
```

## `str-handl.contains`

Whether `pat` occurs anywhere in `s`.

@param {s} - the haystack @param {pat} - the needle

**Signature:** `str-handl.contains((s, pat))`

**Examples:**

```handl
`str.contains("hello", "ell")`
-- => true
```

## `str-handl.count`

The number of non-overlapping occurrences of `pat` in `s`.

**Signature:** `str-handl.count((s, pat))`

**Examples:**

```handl
`str.count("aXbXc", "X")`
-- => 2
```

## `str-handl.ends_with`

Whether `s` ends with `pat`.

@param {s} - the input string @param {pat} - the suffix to test

**Signature:** `str-handl.ends_with((s, pat))`

**Examples:**

```handl
`str.ends_with("hello", "lo")`
-- => true
```

## `str-handl.equals`

Whether `a` and `b` are character-for-character equal.

@param {a} - the left string @param {b} - the right string

**Signature:** `str-handl.equals((a, b))`

**Examples:**

```handl
`str.equals("a", "a")`
-- => true
```

## `str-handl.find`

The char index of the first occurrence of `pat` in `s`, or `-1`.

**Signature:** `str-handl.find((s, pat))`

**Examples:**

```handl
`str.find("hello", "ll")`
-- => 2
```

## `str-handl.is_alpha`

Whether every character of `s` is alphabetic.

**Signature:** `str-handl.is_alpha((s))`

**Examples:**

```handl
`str.is_alpha("abc")`
-- => true
```

## `str-handl.is_alphanumeric`

Whether every character of `s` is alphanumeric.

**Signature:** `str-handl.is_alphanumeric((s))`

**Examples:**

```handl
`str.is_alphanumeric("abc123")`
-- => true
```

## `str-handl.is_empty`

Whether `s` is the empty string.

@param {s} - the input string

**Signature:** `str-handl.is_empty((s))`

**Examples:**

```handl
`str.is_empty("")`
-- => true
```

## `str-handl.is_numeric`

Whether every character of `s` is numeric.

**Signature:** `str-handl.is_numeric((s))`

**Examples:**

```handl
`str.is_numeric("123")`
-- => true
```

## `str-handl.join`

Joins the strings of `xs` with `sep` between each pair.

@param {xs} - the strings to join @param {sep} - the separator

**Signature:** `str-handl.join((xs, sep))`

**Examples:**

```handl
`str.join(["a", "b", "c"], "-")`
-- => "a-b-c"
```

## `str-handl.kebab_case`

Converts `s` to `kebab-case`.

**Signature:** `str-handl.kebab_case((s))`

**Examples:**

```handl
`str.kebab_case("helloWorld_again")`
-- => "hello-world-again"
```

## `str-handl.length`

The number of characters in `s`.

**Signature:** `str-handl.length((s))`

**Examples:**

```handl
`str.length("hello")`
-- => 5
```

## `str-handl.levenshtein`

The Levenshtein edit distance between `a` and `b`.

**Signature:** `str-handl.levenshtein((a, b))`

**Examples:**

```handl
`str.levenshtein("kitten", "sitting")`
-- => 3
```

## `str-handl.lines`

Splits `s` into lines.

**Signature:** `str-handl.lines((s))`

**Examples:**

```handl
`str.lines("a\nb\n")`
-- => ["a", "b"]
```

## `str-handl.lower`

Lowercases every character of `s`.

**Signature:** `str-handl.lower((s))`

**Examples:**

```handl
`str.lower("Hello")`
-- => "hello"
```

## `str-handl.pad_left`

Left-pads `s` to `n` chars by cycling the chars of `p`.

@param {s} - the input string @param {n} - the target length @param {p} - the pad pattern (empty `p` is a no-op)

**Signature:** `str-handl.pad_left((s, n, p))`

**Examples:**

```handl
`str.pad_left("ab", 5, "0")`
-- => "000ab"
```

## `str-handl.pad_right`

Right-pads `s` to `n` chars by cycling the chars of `p`.

@param {s} - the input string @param {n} - the target length @param {p} - the pad pattern (empty `p` is a no-op)

**Signature:** `str-handl.pad_right((s, n, p))`

**Examples:**

```handl
`str.pad_right("ab", 5, "0")`
-- => "ab000"
```

## `str-handl.pascal_case`

Converts `s` to `PascalCase`.

**Signature:** `str-handl.pascal_case((s))`

**Examples:**

```handl
`str.pascal_case("hello_world-again")`
-- => "HelloWorldAgain"
```

## `str-handl.repeat`

`s` concatenated with itself `n` times.

**Signature:** `str-handl.repeat((s, n))`

**Examples:**

```handl
`str.repeat("ab", 3)`
-- => "ababab"
```

## `str-handl.replace`

Replaces every non-overlapping occurrence of `old` in `s` with `to`.

**Signature:** `str-handl.replace((s, old, to))`

**Examples:**

```handl
`str.replace("aXbXc", "X", "-")`
-- => "a-b-c"
```

## `str-handl.replace_first`

Replaces the first occurrence of `old` in `s` with `to`.

**Signature:** `str-handl.replace_first((s, old, to))`

**Examples:**

```handl
`str.replace_first("aXbXc", "X", "-")`
-- => "a-bXc"
```

## `str-handl.reverse`

Reverses `s` by character.

@param {s} - the input string

**Signature:** `str-handl.reverse((s))`

**Examples:**

```handl
`str.reverse("abc")`
-- => "cba"
```

## `str-handl.rfind`

The char index of the last occurrence of `pat` in `s`, or `-1`.

**Signature:** `str-handl.rfind((s, pat))`

**Examples:**

```handl
`str.rfind("aXbXc", "X")`
-- => 3
```

## `str-handl.similarity`

A similarity score between `a` and `b` in `[0.0, 1.0]`.

**Signature:** `str-handl.similarity((a, b))`

**Examples:**

```handl
`str.similarity("kitten", "sitting")`
-- => 0.5714...
```

## `str-handl.slice`

The substring of `s` between char indices `a` (inclusive) and `b`

(exclusive).

**Signature:** `str-handl.slice((s, a, b))`

**Examples:**

```handl
`str.slice("hello", 1, 4)`
-- => "ell"
```

## `str-handl.slugify`

Converts `s` to a URL-safe slug.

**Signature:** `str-handl.slugify((s))`

**Examples:**

```handl
`str.slugify("Hello, World!")`
-- => "hello-world"
```

## `str-handl.snake_case`

Converts `s` to `snake_case`.

**Signature:** `str-handl.snake_case((s))`

**Examples:**

```handl
`str.snake_case("helloWorld-again")`
-- => "hello_world_again"
```

## `str-handl.split`

Splits `s` on every non-overlapping occurrence of `sep`.

**Signature:** `str-handl.split((s, sep))`

**Examples:**

```handl
`str.split("a,b,c", ",")`
-- => ["a", "b", "c"]
```

## `str-handl.split_at`

Splits `s` at char index `i` into `[head, tail]`.

**Signature:** `str-handl.split_at((s, i))`

**Examples:**

```handl
`str.split_at("hello", 2)`
-- => ["he", "llo"]
```

## `str-handl.split_whitespace`

Splits `s` on whitespace runs.

**Signature:** `str-handl.split_whitespace((s))`

**Examples:**

```handl
`str.split_whitespace("  a  b \n c ")`
-- => ["a", "b", "c"]
```

## `str-handl.starts_with`

Whether `s` starts with `pat`.

@param {s} - the input string @param {pat} - the prefix to test

**Signature:** `str-handl.starts_with((s, pat))`

**Examples:**

```handl
`str.starts_with("hello", "he")`
-- => true
```

## `str-handl.strip_prefix`

Removes the prefix `p` from `s` when present.

@param {s} - the input string @param {p} - the prefix to strip

**Signature:** `str-handl.strip_prefix((s, p))`

**Examples:**

```handl
`str.strip_prefix("hello", "he")`
-- => "llo"
```

## `str-handl.strip_suffix`

Removes the suffix `p` from `s` when present.

@param {s} - the input string @param {p} - the suffix to strip

**Signature:** `str-handl.strip_suffix((s, p))`

**Examples:**

```handl
`str.strip_suffix("hello", "lo")`
-- => "hel"
```

## `str-handl.title_case`

Titlecases `s`: uppercase after whitespace, lowercase elsewhere.

@param {s} - the input string

**Signature:** `str-handl.title_case((s))`

**Examples:**

```handl
`str.title_case("hello world")`
-- => "Hello World"
```

## `str-handl.trim`

Removes leading and trailing whitespace.

@param {s} - the input string

**Signature:** `str-handl.trim((s))`

**Examples:**

```handl
`str.trim("  hi  ")`
-- => "hi"
```

## `str-handl.trim_end`

Removes trailing whitespace.

@param {s} - the input string

**Signature:** `str-handl.trim_end((s))`

**Examples:**

```handl
`str.trim_end("  hi  ")`
-- => "  hi"
```

## `str-handl.trim_matches`

Removes leading and trailing characters that appear in `set`.

**Signature:** `str-handl.trim_matches((s, set))`

**Examples:**

```handl
`str.trim_matches("xxhixx", "x")`
-- => "hi"
```

## `str-handl.trim_start`

Removes leading whitespace.

@param {s} - the input string

**Signature:** `str-handl.trim_start((s))`

**Examples:**

```handl
`str.trim_start("  hi  ")`
-- => "hi  "
```

## `str-handl.truncate`

Truncates `s` to at most `m` chars, appending `"..."` when cut.

**Signature:** `str-handl.truncate((s, m))`

**Examples:**

```handl
`str.truncate("hello world", 8)`
-- => "hello..."
```

## `str-handl.upper`

Uppercases every character of `s`.

**Signature:** `str-handl.upper((s))`

**Examples:**

```handl
`str.upper("Hello")`
-- => "HELLO"
```

## `str-handl.word_wrap`

Wraps `s` to lines of at most `w` chars on word boundaries.

**Signature:** `str-handl.word_wrap((s, w))`

**Examples:**

```handl
`str.word_wrap("the quick brown fox", 9)`
-- => "the quick\nbrown fox"
```
