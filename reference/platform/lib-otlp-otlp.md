# Otlp

## `otlp.add_event`

add a named event to a span.

**Signature:** `otlp.add_event : String -&gt; Value`

## `otlp.configure`

set endpoint, service name, headers and resource attributes.

**Signature:** `otlp.configure : Value -&gt; Value`

## `otlp.end_span`

end a span by id.

**Signature:** `otlp.end_span : String -&gt; Value`

## `otlp.flush`

export all buffered telemetry.

**Signature:** `otlp.flush : -&gt; Value`

## `otlp.record_log`

record a log entry.

**Signature:** `otlp.record_log : String -&gt; Value`

## `otlp.record_metric`

record a numeric metric.

**Signature:** `otlp.record_metric : String -&gt; Value`

## `otlp.set_attribute`

set a span attribute.

**Signature:** `otlp.set_attribute : String -&gt; Value`

## `otlp.shutdown`

end all spans, flush and release the exporter.

**Signature:** `otlp.shutdown : -&gt; Value`

## `otlp.start_span`

start a span and return its id.

**Signature:** `otlp.start_span : String -&gt; String`
