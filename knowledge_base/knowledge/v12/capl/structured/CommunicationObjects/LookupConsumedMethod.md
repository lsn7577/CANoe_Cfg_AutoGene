# LookupConsumedMethod

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
consumedMethodRef * LookupConsumedMethod(char[] path)
```

## Description

Searches for the specified consumed method. The path must be complete including namespaces and both endpoints: (Namespace::)+Service.consumerSide[consumer,provider].Method.

You can downcast the result to a concrete type, see the example.

## Return Values

The consumed method. An uninitialized object if the method is not found, which will also be reported in the Write Window or as an error in test system (if the function is called in a test routine).

## Example

```c
consumedMethodRef MirrorAdjustment.Adjust adjustMethod;
char path[200];
char service[50] = "Mirrors::MirrorAdjustment";
char consumer[20] = "CANoe";
char provider[20] = "LeftMirror";
char method[20] = "Adjust";

snprintf(path, elcount(path), "%s.consumerSide[%s,%s].%s", service, consumer, provider, method);
adjustMethod = (consumedMethodRef MirrorAdjustment.Adjust) lookupConsumedMethod(path);
```

## Availability

| Since Version |
|---|
