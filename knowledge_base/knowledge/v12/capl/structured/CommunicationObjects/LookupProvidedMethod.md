# LookupProvidedMethod

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
providedMethodRef * LookupProvidedMethod(char[] path)
```

## Description

Searches for the specified provided method. The path must be complete including namespaces and both endpoints: (Namespace::)+Service.providerSide[consumer,provider].Method.

You can downcast the result to a concrete type, see the example.

## Return Values

The provided method. An uninitialized object if the method is not found, which will also be reported in the Write Window or as an error in test system (if the function is called in a test routine).

## Example

```c
providedMethodRef MirrorAdjustment.Adjust adjustMethod;
char path[200];
char service[50] = "Mirrors::MirrorAdjustment";
char consumer[20] = "CANoe";
char provider[20] = "LeftMirror";
char method[20] = "Adjust";

snprintf(path, elcount(path), "%s.providerSide[%s,%s].%s", service, consumer, provider, method);
adjustMethod = (providedMethodRef MirrorAdjustment.Adjust) lookupProvidedMethod(path);
```

## Availability

| Since Version |
|---|
