# TestJoinMostAMSSpyReportEvent

> Category: `Test` | Type: `function`

## Syntax

```c
TestJoinMostAMSSpyReportEvent (int aFBlockId, int aInstanceId, int aFunctionId)
```

## Description

Completes the current set of "joined events" with the transmitted event, a MOST AMS spy response message (Report, OpType > 8).

This function does not wait.

The wait point can be subsequently attached with TestWaitForAllJoinedEvents and TestWaitForAnyJoinedEvent.

Consider to set always the appropriate bus context in a multibus environment before the function is called.

Further information on site MultiBus Environment.

## Parameters

| Name | Description |
|---|---|
| Note For parameters aFBlockId, aInstanceId and aFunctionId the following applies: If -1 is given, the corresponding field can get any value. This is also the standard for not explicit set values. |  |

## Return Values

-6: Parse Error; on specification of a symbolic message definition that cannot be resolved with the available XML function catalog or that is flawed

## Availability

| Since Version |
|---|
