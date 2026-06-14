# SecurityLocalActivateTxPDUs

> Category: `Security` | Type: `function`

## Syntax

```c
long SecurityLocalActivateTxPDUs(char nodeName[])
```

## Description

Allows a node (e.g. gateway) to do a MAC calculation for Tx secured PDUs of another node. The calling node registers to all Tx PDUs of the specified node.

You have to set the bus context before you call this method.

This method has to be executed in Pre Start callback of CAPL.

## Return Values

1: Activation successful

## Availability

| Since Version |
|---|
