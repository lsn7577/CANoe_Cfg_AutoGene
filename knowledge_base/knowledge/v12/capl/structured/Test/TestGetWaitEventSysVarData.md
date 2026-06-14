# TestGetWaitEventSysVarData

> Category: `Test` | Type: `function`

## Syntax

```c
long testGetWaitEventSysVarData(dword index, float & value); // form 1
```

## Description

Retrieves the system variable value that has led to the resume of a joined wait statement.

## Parameters

| Name | Description |
|---|---|
| Note Use the int64 parameters for system variables of UInt64 and Int64 type to cover the whole value range. The int64 parameter is interpreted for system variables of UInt64 type as qword (uint64). |  |

## Return Values

0: Data access successful

## Example

```c
// add sysVar event to the current set of “joined events” and get the sysVar value
dword index = 0;
float sysValue = 0;
TestJoinSysVarEvent(MySysVar);
// ... other join events
index = TestWaitForAnyJoinedEvent(2000);

TestGetWaitEventSysVarData(index, sysValue);
```

## Availability

| Since Version |
|---|
