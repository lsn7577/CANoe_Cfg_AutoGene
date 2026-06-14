# LookupFieldConsumer

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
fieldConsumerRef * LookupFieldConsumer(char[] path)
```

## Description

Searches for the specified field consumer. The path must be complete including namespaces, endpoint and field: (Namespace::)+Service[consumer].Field.

You can downcast the result to a concrete type, see the example.

## Return Values

The field consumer. An uninitialized object if the field consumer is not found, which will also be reported in the Write Window or as an error in test system (if the function is called in a test routine).

## Example

```c
fieldConsumerRef MirrorAdjustment.Position positionField;
char path[200];
char service[50] = "Mirrors::MirrorAdjustment";
char consumer[20] = "CANoe";
char fieldName[20] = "Position";

snprintf(path, elcount(path), "%s[%s].%s", service, consumer, fieldName);
positionField = (fieldConsumerRef MirrorAdjustment.Position) lookupFieldConsumer(path);
```

## Availability

| Since Version |
|---|
