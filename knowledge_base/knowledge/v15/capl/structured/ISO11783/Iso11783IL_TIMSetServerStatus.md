# Iso11783IL_TIMSetServerStatus

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_TIMSetServerStatus(dword cycleTime); // form 1
long Iso11783IL_TIMSetServerStatus(dword cycleTime, pg TIM12 pgWithNewContent); // form 2
long Iso11783IL_TIMSetServerStatus(dbNode server, dword cycleTime); // form 3
long Iso11783IL_TIMSetServerStatus(dbNode server, dword cycleTime, pg TIM12 pgWithNewContent); // form 4
```

## Description

Forms (1, 3): This function changes the cycle time of the TIM_ServerStatus_Msg message. The content of TIM_ServerStatus_Msg message stays unchanged.

Forms (2, 4): This function changes the content and cycle time of the TIM_ServerStatus_Msg message.

## Parameters

| Name | Description |
|---|---|
| cycleTime | Cycle time of the TIM_ServerStatus_Msg message [ms] (default: 100). |
| pgWithNewContent | Content of this message is used by the following TIM_ServerStatus_Msg messages sent by the TIM server. |
| server | TIM server node. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 | 13.0 | — | — | 3.0 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 3, 4 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1, 2) | ✔ (form 1, 2) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 3, 4) | ✔ (form 3, 4) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 3, 4) | ✔ (form 3, 4) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
