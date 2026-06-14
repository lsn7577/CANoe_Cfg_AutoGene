# LookupProvidedService

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
providedServiceRef * LookupProvidedService(char[] path)
```

## Description

Searches for the specified provided service. The path must be complete including namespaces and both endpoints: (Namespace::)+Service.providerSide[consumer,provider].

You can downcast the result to a concrete type, see the example.

## Return Values

The provided service. An uninitialized object if the service is not found, which will also be reported in the Write Window or as an error in test system (if the function is called in a test routine).

## Example

```c
providedServiceRef MirrorAdjustment mirrorSvc;
char path[200];
char service[50] = "Mirrors::MirrorAdjustment";
char consumer[20] = "CANoe";
char provider[20] = "LeftMirror";

snprintf(path, elcount(path), "%s.providerSide[%s,%s]", service, consumer, provider);
mirrorSvc = (providedServiceRef MirrorAdjustment) lookupProvidedService(path);
```

## Availability

| Since Version |
|---|
