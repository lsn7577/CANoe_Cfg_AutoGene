# LookupEventConsumer

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
eventConsumerRef * LookupEventConsumer(char[] path)
```

## Description

Searches for the specified event consumer. The path must be complete including namespaces, endpoint and event: (Namespace::)+Service[consumer].Event.

You can downcast the result to a concrete type, see the example.

## Return Values

The event consumer. An uninitialized object if the event consumer is not found, which will also be reported in the Write Window or as an error in test system (if the function is called in a test routine).

## Example

```c
eventConsumerRef MirrorAdjustment.Position positionEvent;
char path[200];
char service[50] = "Mirrors::MirrorAdjustment";
char consumer[20] = "CANoe";
char eventName[20] = "Position";

snprintf(path, elcount(path), "%s[%s].%s", service, consumer, eventName);
positionEvent = (eventConsumerRef MirrorAdjustment.Position) lookupEventConsumer(path);
```

## Availability

| Since Version |
|---|
