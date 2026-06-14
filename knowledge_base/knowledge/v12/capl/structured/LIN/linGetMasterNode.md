# linGetMasterNode

> Category: `LIN` | Type: `function`

## Syntax

```c
long linGetMasterNode()
```

## Description

This function returns a unique internal ID for the current LIN master node of the channel given by the current bus context. See SetBusContext for how to change the current bus context.

The return value may be used as input parameter to a call to linSetMasterNode(long nodeId).

The return value must not be used between measurements, as these will be newly generated each time the measurement is started.

## Return Values

Node ID of the current master node. If the return value is 0 (zero), the function failed, or there is currently no LIN master node assigned.

## Availability

| Since Version |
|---|
