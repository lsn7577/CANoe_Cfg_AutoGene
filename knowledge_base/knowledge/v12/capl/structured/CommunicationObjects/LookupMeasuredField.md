# LookupMeasuredField

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
measuredFieldRef * LookupMeasuredField(char[] path)
```

## Description

Searches for the specified measured field. The path must be complete including namespaces and both endpoints: (Namespace::)+Service.measure[consumer,provider].Field.

You can downcast the result to a concrete type, see the example.

## Return Values

The measured field. An uninitialized object if the field is not found, which will also be reported in the Write Window or as an error in test system (if the function is called in a test routine).

## Example

```c
measuredFieldRef MirrorAdjustment.Position positionField;
char path[200];
char service[50] = "Mirrors::MirrorAdjustment";
char consumer[20] = "CANoe";
char provider[20] = "LeftMirror";
char field[20] = "Position";

snprintf(path, elcount(path), "%s.measure[%s,%s].%s", service, consumer, provider, field);
positionField = (measuredFieldRef MirrorAdjustment.Position) lookupMeasuredField(path);
```

## Availability

| Since Version |
|---|
