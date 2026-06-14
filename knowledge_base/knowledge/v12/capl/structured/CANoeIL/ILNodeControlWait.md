# ILNodeControlWait

> Category: `CANoeIL` | Type: `function`

## Syntax

```c
long ILNodeControlWait(char aNodeName[]); // form 1
```

## Description

Stops the interaction layer of the specified simulation node. Cyclical sending of messages stops but setting of signals is still possible. The specified node must be in the current bus context. In all other cases the function has no effect and will return with an error.

## Return Values

0: No error

## Availability

| Since Version |
|---|
