# TestWaitForMostMessage

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForMostMessage(dbMessage aDBMsg, int aInstanceId, dword aTimeout);
```

## Description

Waits for the occurrence of the specified MOST message (MOST control message or MOST spy message). Should the message not occur before the expiration of the time aTimeout, the wait condition is resolved nevertheless.

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
