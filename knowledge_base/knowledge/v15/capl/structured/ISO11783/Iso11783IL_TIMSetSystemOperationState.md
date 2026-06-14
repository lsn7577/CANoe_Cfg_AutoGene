# Iso11783IL_TIMSetSystemOperationState

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_TIMSetSystemOperationState(dword state) // form 1
long Iso11783IL_TIMSetSystemOperationState(dbNode server, dword state) // form 2
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
| server | TIM server simulation node to apply the function. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 12.0 | 13.0 | — | — | 4.0 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 2 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
