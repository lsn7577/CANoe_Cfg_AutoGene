# LookupProvidedEvent

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
providedEventRef * LookupProvidedEvent(char[] path)
```

## Description

Searches for the specified provided event. The path must be complete including namespaces and both endpoints: (Namespace::)+Service.providerSide[consumer,provider].Event.

You can downcast the result to a concrete type, see the example.

## Return Values

The provided event. An uninitialized object if the event is not found, which will also be reported in the Write Window or as an error in test system (if the function is called in a test routine).

## Example

```c
providedEventRef MirrorAdjustment.Position positionEvent;
char path[200];
char service[50] = "Mirrors::MirrorAdjustment";
char consumer[20] = "CANoe";
char provider[20] = "LeftMirror";
char event[20] = "Position";

snprintf(path, elcount(path), "%s.providerSide[%s,%s].%s", service, consumer, provider, event);
positionEvent = (providedEventRef MirrorAdjustment.Position) lookupProvidedEvent(path);
```

## Availability

| Since Version |
|---|
