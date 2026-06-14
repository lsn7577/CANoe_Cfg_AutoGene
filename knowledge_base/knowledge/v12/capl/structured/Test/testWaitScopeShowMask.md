# testWaitScopeShowMask

> Category: `Test` | Type: `function`

## Syntax

```c
long testWaitScopeShowMask (ScopeAnalyseHandle handle, dword msgFieldStart, long startBitNo, long bitCount); // form 1
```

## Description

The defined frame cutout of the previously analyzed frame together with the bit mask is shown in the scope's Diagram view. The enlarged area is automatically scaled in time direction. Only the differential signal will be displayed.

Form 1: Can only be used for CAN bit mask analysis.

Form 2: Can only be used for FlexRay bit mask analysis.

## Parameters

| Name | Type | Description |
|---|---|---|
| Keyword | Description | Type |
| handle | A unique ID | long |

## Return Values

1 = Success

## Availability

| Since Version |
|---|
