# Ffi

## `ffi.bind`

Bind a foreign function to a Handl function.

@param lib The name of the foreign library to load. @param sym The name of the foreign symbol to bind. @param arg_types An array of types corresponding to the arguments. @param ret_type The return type of the foreign function. @param is_variadic A boolean indicating whether the function is variadic. @return The bound function.

**Signature:** `ffi.bind : (String, String, Array, Array, String, Bool) ~[1]~&gt; Value`

## `ffi.call`

Call a foreign function.

@param lib The name of the foreign library to load. @param sym The name of the foreign symbol to call. @param args An array of arguments to pass to the foreign function. @param arg_types An array of types corresponding to the arguments. @param ret_type The return type of the foreign function. @param is_variadic A boolean indicating whether the function is variadic. @return The value returned by the foreign function.

**Signature:** `ffi.call : (String, String, Array, Array, String, Bool) ~[1]~&gt; Value`

## `ffi.Errno`

C `errno` value as a Handl Int.

## `ffi.errno`

Return the current value of the C `errno` variable.

@return The current value of the C `errno` variable.

**Signature:** `ffi.errno : () ~[1]~&gt; Errno`

## `ffi.Handle`

Opaque foreign handle (file descriptor, socket, pointer, etc.).

## `ffi.load`

Probe a library for availability without raising.

@param lib The name of the foreign library to load. @return A result tag: `{__tag__: "ok"}` on success, or

**Signature:** `ffi.load : (String) ~[1]~&gt; Value`

## `ffi.read`

Read memory through a foreign pointer.

@param ptr A raw address (Int) or opaque handle (`__resource__`). @param descriptor A marshal descriptor: scalar (`i8`..`u64`, `isize`, `usize`), `ptr`, `bytes:N`, `arr:N:T`, `rec:{...}`, `cstr`. @return The decoded value at the pointer.

**Signature:** `ffi.read : (Value, String) ~[1]~&gt; Value`

## `ffi.sym`

Probe a symbol in a library without raising.

@param lib The name of the foreign library to load. @param probe The name of the foreign symbol to probe. @return A result tag: `{__tag__: "ok", value: addr}` on success, or

**Signature:** `ffi.sym : (String, String) ~[1]~&gt; Value`
