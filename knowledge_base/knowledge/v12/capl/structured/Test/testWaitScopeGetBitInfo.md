# testWaitScopeGetBitInfo

> Category: `Test` | Type: `function`

## Syntax

```c
long testWaitScopeGetBitInfo(ScopeAnalyseHandle handle, dword msgFieldStart,long startBitNo, dword msgFieldEnd, long EndBitNo, ScopeMaskViolationData data);
```

## Description

After a signal was analyzed with the function testWaitScopeAnalyseSignal, the average values of the voltages of CAN_H, CAN_L, and CAN_Diff are calculated for a defined bit range.

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
