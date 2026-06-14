# mostGetFBlockID, mostGetFunctionID, mostGetOpType

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long mostGetFBlockID(mostMessage msg)
```

## Description

These functions return the FBlockID, FunctionID or OpType of the message.

## Return Values

FblockId, FunctionId, OpType
Note
These values are determined independent of the message type and if applicable independent of the TelId. The Values are only valid if the message is out of the function catalog.

## Availability

| Up to Version |
|---|
