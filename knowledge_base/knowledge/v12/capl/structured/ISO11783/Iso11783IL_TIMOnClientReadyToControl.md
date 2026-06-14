# Iso11783IL_TIMOnClientReadyToControl

> Category: `ISO11783` | Type: `function`

## Syntax

```c
void Iso11783IL_TIMOnClientReadyToControl(dword functionID, dword clientAddress)
```

## Description

This callback function is called if the TIM Client is ready to control a TIM function.

Within this callback you can call Iso11783IL_TIMOperatorAcknowledge to acknowledge the request.

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
