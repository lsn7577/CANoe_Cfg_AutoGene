# linIsMasterNode

> Category: `LIN` | Type: `function`

## Syntax

```c
long linIsMasterNode()
```

## Description

This function returns 1 if the calling node is the current LIN master node of the network given by the current bus context. This will be the node assigned to the LIN master from the LDF if linSetMasterNode has not been called before, or the node referred to by the previous call of linSetMasterNode.

See SetBusContext for how to change the current bus context.

## Return Values

1 if the calling node is the current LIN master node, 0 otherwise.

## Availability

| Since Version |
|---|
