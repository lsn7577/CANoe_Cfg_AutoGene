# LookupConsumedField

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
consumedFieldRef * LookupConsumedField(char[] path)
```

## Description

Searches for the specified consumed field. The path must be complete including namespaces and both endpoints: (Namespace::)+Service.consumerSide[consumer,provider].Field.

You can downcast the result to a concrete type, see the example.

## Return Values

The consumed field. An uninitialized object if the field is not found, which will also be reported in the Write Window or as an error in test system (if the function is called in a test routine).

## Example

```c
consumedFieldRef MirrorAdjustment.Position positionField;
char path[200];
char service[50] = "Mirrors::MirrorAdjustment";
char consumer[20] = "CANoe";
char provider[20] = "LeftMirror";
char field[20] = "Position";

snprintf(path, elcount(path), "%s.consumerSide[%s,%s].%s", service, consumer, provider, field);
positionField = (consumedFieldRef MirrorAdjustment.Position) lookupConsumedField(path);
```

## Availability

| Since Version |
|---|
