# linResetMasterNode

> Category: `LIN` | Type: `function`

## Syntax

```c
long linResetMasterNode()
```

## Description

Calling this function reverses the effect of linSetMasterNode. Sending LIN headers (by calling linTransmitHeader or similar functions) is no longer restricted to the currently assigned LIN master node. If a node is assigned as LDF master node, the LIN scheduler will be reset to its state before linSetMasterNode was called.

## Return Values

Node ID of the previous master node. If the return value is 0 (zero), the function failed, or there was no previous LIN master node.

## Availability

| Since Version |
|---|
