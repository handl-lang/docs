# Command

## `command.Command`

**Signature:** `command.Command(sym())`

## `command.command`

user-space command registration and invocation algebra.

**Signature:** `command.command : (String, Array) ~[1]~&gt; Value`

## `command.default_handler`

the default `Command` handler: an ordinary arrow returning a record of operations.

**Signature:** `command.default_handler((registry))`

## `command.has`

**Signature:** `command.has : (String) ~[1]~&gt; Bool`

## `command.names`

**Signature:** `command.names : () ~[1]~&gt; Array`

## `command.register`

**Signature:** `command.register : (String, (Array) ~[1]~&gt; Value) ~[1]~&gt; ()`

## `command.unregister`

**Signature:** `command.unregister : (String) ~[1]~&gt; ()`
