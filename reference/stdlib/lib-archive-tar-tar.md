# Tar

## `tar.pack`

pack an array of {path, contents} objects into a base64 tar archive string.

**Signature:** `tar.pack : Array -&gt; String`

## `tar.unpack`

unpack a base64 tar archive string into an array of {path, contents} objects.

**Signature:** `tar.unpack : String -&gt; Array`
