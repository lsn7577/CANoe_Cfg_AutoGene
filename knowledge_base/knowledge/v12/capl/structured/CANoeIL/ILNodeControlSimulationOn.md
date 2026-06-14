# ILNodeControlSimulationOn

> Category: `CANoeIL` | Type: `function`

## Syntax

```c
long ILNodeControlSimulationOn(char aNodeName[])
```

## Description

Start the simulation of the interaction layer of the specified simulation node. The IL is in the same state as it was before stopping. The specified node must be in the current bus context. In all other cases the function has no effect and will return with an error.

## Return Values

0: No error

## Availability

| Since Version |
|---|
