# Event

## `event.default_handler`

the default `Event` handler: an ordinary arrow returning a record of operations.

**Signature:** `event.default_handler((registry))`

## `event.emit`

emit a named event with a payload.

**Signature:** `event.emit : (String, Value) ~[1]~&gt; ()`

## `event.Event`

**Signature:** `event.Event(sym())`

## `event.has`

test whether a named event has any listener registered.

**Signature:** `event.has : (String) ~[1]~&gt; Bool`

## `event.names`

list the names of registered events.

**Signature:** `event.names : () ~[1]~&gt; Array`

## `event.on`

register a natural-arrow listener for a named event.

**Signature:** `event.on : (String, (String, Value) ~[1]~&gt; ()) ~[1]~&gt; ()`

## `event.unregister`

remove all listeners for a named event.

**Signature:** `event.unregister : (String) ~[1]~&gt; ()`
