# SecurityLocalStartControlSimulationNode

> Category: `Security` | Type: `function`

## Syntax

```c
long SecurityLocalStartControlSimulationNode(char nodeName[], char networkName[], dword orderNumber)
```

## Description

Registers the calling node to a node in the simulation setup. Both nodes require the SecMgrCANoeClient Nodelayer.

After a successful registration, the calling node can use all SecurityOfNode…() Functions to control the simulation node.

The calling node receives all OnSecurityOfNode… callbacks from the specified node on the specified network.

You have to call SecurityLocalStopControlSimulationNode to unregister.

## Return Values

1: SuccessA Value of 1 means that the action was successful. A value less than or equal to 0 means error. A value larger than 1 means warning.

## Availability

| Since Version |
|---|
