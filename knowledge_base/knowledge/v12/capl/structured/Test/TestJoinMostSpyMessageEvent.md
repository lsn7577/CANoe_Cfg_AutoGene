# TestJoinMostSpyMessageEvent

> Category: `Test` | Type: `function`

## Syntax

```c
TestJoinMostSpyMessageEvent(dbMessage aDBMsg, int aInstanceId)
```

## Description

Completes the current set of "joined events" with the transmitted event, a MOST Spy message.

The first arriving control message, which fulfills the specified conditions, resolves the wait point, irregardless of whether it is part of a segmented transmission. TelId is not included in this process.

This function does not wait.

The wait point can be subsequently attached with TestWaitForAllJoinedEvents and TestWaitForAnyJoinedEvent.

Consider to set always the appropriate bus context in a multibus environment before the function is called.

Further information on site MultiBus Environment.

## Parameters

| Name | Description |
|---|---|
| Note For parameters aSourceAddress, aDestinationAddress, aFBlockId, aInstanceId, aFunctionId and aOpType the following applies: If -1 is given, the corresponding field can get any value. This is also the standard for not explicit set values. |  |

## Return Values

-6: Parse Error; on specification of a symbolic message definition that cannot be resolved with the available XML function catalog or that is flawed

## Availability

| Since Version |
|---|
