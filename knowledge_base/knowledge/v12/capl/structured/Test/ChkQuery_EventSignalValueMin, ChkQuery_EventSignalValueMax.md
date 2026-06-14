# ChkQuery_EventSignalValueMin, ChkQuery_EventSignalValueMax

> Category: `Test` | Type: `function`

## Syntax

```c
long ChkQuery_EventSignalValueMin(dword checkId, int64& value);
check.QueryEventSignalValueMin(int64& value);
```

## Description

Enables access to the minimal and maximal measured values within a check.

## Parameters

| Name | Description |
|---|---|
| Note Use the int64 parameters for system variables of UInt64 and Int64 type to cover the whole value range. The int64 parameter is interpreted for system variables of UInt64 type as qword (uint64). |  |

## Return Values

<= 0: Refers the query error codes in this chapter

## Example

```c
double maxValue;
int checkId;

checkId = ChkStart_MsgSignalValueInvalid (singalToObserve, 5.5, 10.5);    TestAddCondition(checkId)
// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
ChkQuery_EventSignalValueMax(checkID, maxValue);

write("Max signal value=%f", maxValue);

TestRemoveCondition(checkId);
```

## Availability

| Since Version |
|---|
