# ILNodeControlSimulationOff

> Category: `CANoeIL` | Type: `function`

## Syntax

```c
long ILNodeControlSimulationOff(char aNodeName[])
```

## Description

Stops the simulation of the interaction layer of the specified simulation node. In this state the interaction layer does not react on any function besides turning the simulation on again. The specified node must be in the current bus context. In all other cases the function has no effect and will return with an error.

## Return Values

0: No error

## Availability

| Since Version |
|---|
