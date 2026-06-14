# Iso11783IL_TIMOnFunctionStateChanged

> Category: `ISO11783` | Type: `function`

## Syntax

```c
void Iso11783IL_TIMOnFunctionStateChanged(dword functionID, dword newState)
```

## Description

This callback function is called if the state of a TIM function has been changed. If this callback function is used by a TIM client the function is only called if the TIM function is assigned by the client.

You can also use the function Iso11783IL_TIMConnectSysVarToFunctionState if you are interested in the state of a function.

## Parameters

| Name | Description |
|---|---|
| Function ID | Description |
| 1-32 (1h-20h) | Auxiliary Value 1 – 32 |
| 64 (40h) | Front PTO |
| 65 (41h) | Rear PTO |
| 66 (42h) | Front hitch |
| 67 (43h) | Rear hitch |
| 68 (44h) | Vehicle speed |
| 70 (46h) | External guidance |

## Return Values

—

## Availability

| Since Version |
|---|
