# ILNodeControlStop

> Category: `CANoeIL` | Type: `function`

## Syntax

```c
long ILNodeControlStop(char aNodeName[])
```

## Description

Stops the interaction layer of the specified simulation node. Cyclical sending of messages is stopped and setting of signals is not possible anymore. The specified node must be in the current bus context. In all other cases the function has no effect and will return with an error.

## Return Values

0: No error

## Availability

| Since Version |
|---|
