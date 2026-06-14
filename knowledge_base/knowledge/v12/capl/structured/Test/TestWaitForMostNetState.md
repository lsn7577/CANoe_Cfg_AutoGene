# TestWaitForMostNetState

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForMostNetState(long aOldState, long aNewState, unsigned long aTimeout);
```

## Description

The function waits until the expiration of the time aTimeout for a transfer of the MOST NetState from the state aOldState into the state aNewState.

Consider to set always the appropriate bus context in a multibus environment before the function is called.

Further information on site MultiBus Environment.

## Parameters

| Name | Description |
|---|---|
| 0 | MostNetState_Undefined |
| 2 | MostNetState_PowerOff |
| 3 | MostNetState_NetInterfaceInit |
| 4 | MostNetState_ConfigNotOk |
| 5 | MostNetState_ConfigOk |
| -1 | Wildcard, any NetState state |

## Return Values

-2: Resume based on Constraint Violation

## Availability

| Since Version |
|---|
