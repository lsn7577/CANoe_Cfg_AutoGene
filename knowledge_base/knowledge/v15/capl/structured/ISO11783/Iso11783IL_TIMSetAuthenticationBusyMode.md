# Iso11783IL_TIMSetAuthenticationBusyMode

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_TIMSetAuthenticationBusyMode(dword activate); // form 1
long Iso11783IL_TIMSetAuthenticationBusyMode(dbNode* timParticipant, dword activate); // form 2
```

## Description

Activates or deactivates the authentication busy mode.

If the busy mode is activated:

## Parameters

| Name | Description |
|---|---|
| activate | 0: Busy mode is deactivated 1: Busy mode is activated |
| participant | TIM participant (TIM server or TIM client). |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 12.0 SP3 | 13.0 | — | — | 4.0 SP3 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 2 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
