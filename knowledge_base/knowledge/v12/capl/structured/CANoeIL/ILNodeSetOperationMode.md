# ILNodeSetOperationMode

> Category: `CANoeIL` | Type: `function`

## Syntax

```c
long ILNodeSetOperationMode(char aNodeName[], long mode, long param); // form 1
```

## Description

Form 1:Sets specific operation mode in the interaction layer of the specified simulation node. The specified node must be in the current bus context. In all other cases the function has no effect and will return with an error.

Form 2:Sets specific operation mode in the interaction layer for the specified signal group of the specified message.

Form 3:Sets specific operation mode in the interaction layer for the specified signal.

## Return Values

0: No error

## Availability

| Since Version |
|---|
