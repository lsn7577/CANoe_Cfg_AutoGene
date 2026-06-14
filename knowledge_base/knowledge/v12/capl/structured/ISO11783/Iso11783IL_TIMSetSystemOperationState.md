# Iso11783IL_TIMSetSystemOperationState

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_TIMSetSystemOperationState(dword state) // form 1
```

## Description

Sets the current system operation state of a TIM Server.

This state is transmitted in the TIM_ServerStatus_Msg message. But it does not influence the functionality of the TIM server.

## Parameters

| Name | Description |
|---|---|
| State | Description |
| 0 | Requirements for TIM operation are not fulfilled |
| 1 | Requirements for normal operation are fulfilled |
| 2 | Requirements for standstill operation are fulfilled |
| 3 | Requirements for stationary operation are fulfilled |
| 4-13 | Reserved |
| 14 | Error |
| 15 | Not available |

## Return Values

0: Property has been set successfully

## Availability

| Since Version |
|---|
