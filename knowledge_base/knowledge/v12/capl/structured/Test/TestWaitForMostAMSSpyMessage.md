# TestWaitForMostAMSSpyMessage

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForMostAMSSpyMessage(dbMessage aDBMsg, int aInstanceId, unsigned long aTimeout);
```

## Description

Waits for the occurrence of the specified MOST AMS spy message.

This may deal with transmission of individual frames (TelID=0) or segmented transmissions. In the case of segmented transmission, the last control message of a correct transmission resolves the wait conditions.

If the message does not occur by the time the aTimeout expires, the wait condition is still resolved.

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
