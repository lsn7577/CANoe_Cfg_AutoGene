# TestJoinSysVarEvent

> Category: `Test` | Type: `function`

## Syntax

```c
long TestJoinSysVarEvent(sysvar aSysVar)
```

## Description

Completes the current set of "joined events" with the transmitted event. This function does not wait.

## Parameters

| Name | Description |
|---|---|
| Note Not available for a single element of a double or integer array. |  |

## Return Values

-3: Join error.

## Example

```c
// add sysVar event to the current set of “joined events” and get the sysVar value
dword index = 0;
float sysValue = 0;
TestJoinSysVarEvent(MySysVar);
// … other join events
TestJoinEnvVarEvent(MyEnvVar);
TestJoinSignalInRange(Velocity, 80, 100);
TestJoinTextEvent("ErrorFrame occurred!");
index = TestWaitForAnyJoinedEvent(2000);

TestGetWaitEventSysVarData(index, sysValue);
```

## Availability

| Since Version |
|---|
