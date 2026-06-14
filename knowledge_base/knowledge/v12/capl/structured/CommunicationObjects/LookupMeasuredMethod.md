# LookupMeasuredMethod

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
measuredMethodRef * LookupMeasuredMethod(char[] path)
```

## Description

Searches for the specified measured method. The path must be complete including namespaces and both endpoints: (Namespace::)+Service.measure[consumer,provider].Method.

You can downcast the result to a concrete type, see the example.

## Return Values

The measured method. An uninitialized object if the method is not found, which will also be reported in the Write Window or as an error in test system (if the function is called in a test routine).

## Example

```c
measuredMethodRef MirrorAdjustment.Adjust adjustMethod;
char path[200];
char service[50] = "Mirrors::MirrorAdjustment";
char consumer[20] = "CANoe";
char provider[20] = "LeftMirror";
char method[20] = "Adjust";

snprintf(path, elcount(path), "%s.measure[%s,%s].%s", service, consumer, provider, method);
adjustMethod = (measuredMethodRef MirrorAdjustment.Adjust) lookupMeasuredMethod(path);
```

## Availability

| Since Version |
|---|
