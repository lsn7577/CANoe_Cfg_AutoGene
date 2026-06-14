# LookupMeasuredService

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
measuredServiceRef * LookupMeasuredService(char[] path)
```

## Description

Searches for the specified measured service. The path must be complete including namespaces and both endpoints: (Namespace::)+Service.measure[consumer,provider].

You can downcast the result to a concrete type, see the example.

## Return Values

The measured service. An uninitialized object if the service is not found, which will also be reported in the Write Window or as an error in test system (if the function is called in a test routine).

## Example

```c
measuredServiceRef MirrorAdjustment mirrorSvc;
char path[200];
char service[50] = "Mirrors::MirrorAdjustment";
char consumer[20] = "CANoe";
char provider[20] = "LeftMirror";

snprintf(path, elcount(path), "%s.measure[%s,%s]", service, consumer, provider);
mirrorSvc = (measuredServiceRef MirrorAdjustment) lookupMeasuredService(path);
```

## Availability

| Since Version |
|---|
