# LookupConsumedEvent

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
consumedEventRef * LookupConsumedEvent(char[] path)
```

## Description

Searches for the specified consumed event. The path must be complete including namespaces and both endpoints: (Namespace::)+Service.consumerSide[consumer,provider].Event.

You can downcast the result to a concrete type, see the example.

## Return Values

The consumed event. An uninitialized object if the event is not found, which will also be reported in the Write Window or as an error in test system (if the function is called in a test routine).

## Example

```c
consumedEventRef MirrorAdjustment.Position positionEvent;
char path[200];
char service[50] = "Mirrors::MirrorAdjustment";
char consumer[20] = "CANoe";
char provider[20] = "LeftMirror";
char event[20] = "Position";

snprintf(path, elcount(path), "%s.consumerSide[%s,%s].%s", service, consumer, provider, event);
positionEvent = (consumedEventRef MirrorAdjustment.Position) lookupConsumedEvent(path);
```

## Availability

| Since Version |
|---|
