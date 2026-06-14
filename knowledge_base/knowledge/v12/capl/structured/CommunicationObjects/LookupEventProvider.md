# LookupEventProvider

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
eventProviderRef * LookupEventProvider(char[] path)
```

## Description

Searches for the specified event provider. The path must be complete including namespaces, endpoint and event: (Namespace::)+Service[provider].Event.

You can downcast the result to a concrete type, see the example.

## Return Values

The event provider. An uninitialized object if the event provider is not found, which will also be reported in the Write Window or as an error in test system (if the function is called in a test routine).

## Example

```c
eventProviderRef MirrorAdjustment.Position positionEvent;
char path[200];
char service[50] = "Mirrors::MirrorAdjustment";
char provider[20] = "LeftMirror";
char eventName[20] = "Position";

snprintf(path, elcount(path), "%s[%s].%s", service, provider, eventName);
positionEvent = (eventProviderRef MirrorAdjustment.Position) lookupEventProvider(path);
```

## Availability

| Since Version |
|---|
