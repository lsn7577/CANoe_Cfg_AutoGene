# LookupTxSignal

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
txSignalRef * LookupTxSignal(char[] path)
```

## Description

Searches for the specified tx signal. The path must be complete including namespaces and endpoint(s):

You can downcast the result to a concrete type, see the example.

## Return Values

The tx signal. An uninitialized object if the signal is not found, which will also be reported in the Write Window or as an error in test system (if the function is called in a test routine).

## Example

```c
txSignalRef long errorSignal;
char path[200];
char signalName[50] = "Mirrors::ErrorSignal";
char sender[20] = "LeftMirror";

snprintf(path, elcount(path), "%s[%s]", signalName, sender);
errorSignal = (txSignalRef long) lookupTxSignal(path);
```

## Availability

| Since Version |
|---|
