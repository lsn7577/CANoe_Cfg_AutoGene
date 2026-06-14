# ILNodeControlResume

> Category: `CANoeIL` | Type: `function`

## Syntax

```c
long ILNodeControlResume(char aNodeName[]); // form 1
```

## Description

Restarts the interaction layer of the specified simulation node. Cyclical sending of messages is restarted. The specified node must be in the current bus context. In all other cases the function has no effect and will return with an error.

## Return Values

0: No error

## Availability

| Since Version |
|---|
