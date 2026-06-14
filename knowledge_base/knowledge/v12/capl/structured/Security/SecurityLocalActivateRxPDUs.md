# SecurityLocalActivateRxPDUs

> Category: `Security` | Type: `function`

## Syntax

```c
long SecurityLocalActivateRxPDUs(char nodeName[])
```

## Description

Allows a node (e.g. gateway) to validate Rx secured PDUs of another node. The calling node registers to all Rx PDUs of the specified node.

You have to set the bus context before you call this method.

This method has to be executed in Pre Start callback of CAPL.

## Availability

| Since Version |
|---|
