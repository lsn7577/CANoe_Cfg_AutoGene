# LookupRxSignal

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
rxSignalRef * LookupRxSignal(char[] path)
```

## Description

Searches for the specified rx signal. The path must be complete including namespaces and endpoint(s):

You can downcast the result to a concrete type, see the example.

## Return Values

The rx signal. An uninitialized object if the signal is not found, which will also be reported in the Write Window or as an error in test system (if the function is called in a test routine).

## Example

```c
rxSignalRef long errorSignal;
char path[200];
char signalName[50] = "Mirrors::ErrorSignal";
char receiver[20] = "CANoe";

snprintf(path, elcount(path), "%s[%s]", signalName, receiver);
errorSignal = (rxSignalRef long) lookupRxSignal(path);
```

## Availability

| Since Version |
|---|
