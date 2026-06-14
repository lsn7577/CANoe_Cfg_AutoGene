# Iso11783IL_TIMContinueConnection

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_TIMContinueConnection(dbNode counterpart); // form 1
long Iso11783IL_TIMContinueConnection(dbNode counterpart, dword nextState); // form 2
long Iso11783IL_TIMContinueConnection(byte counterpartAddress); // form 3
long Iso11783IL_TIMContinueConnection(byte counterpartAddress, dword nextState); // form 4
long Iso11783IL_TIMContinueConnection(dbNode participant, dbNode counterpart); // form 5
long Iso11783IL_TIMContinueConnection(dbNode participant, dbNode counterpart, dword nextState); // form 6
long Iso11783IL_TIMContinueConnection(dbNode participant, byte counterpartAddress); // form 7
long Iso11783IL_TIMContinueConnection(dbNode participant, byte counterpartAddress, dword nextState); // form 8
```

## Description

Continues a connection which has been frozen by Iso11783IL_TIMFreezeConnection.

Form 1, 3, 5, and 7 continues the state of the currently frozen connection by execution the action of this state.

Form 2, 4, 6 and 8 continues with the specified state and executes the action of this state.

## Parameters

| Name | Description |
|---|---|
| counterpart | TIM counterpart of the client/server connection. |
| counterpartAddress | Address of TIM counterpart of the client/server connection. |
| nextState | ID of the next state. |
| participant | TIM participant (TIM server or TIM client). |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0: form 1, 2, 5, 6 11.0 SP2: form 3, 4, 7, 8 | 13.0 | — | — | 3.0: form 5, 6 3.0 SP2: form 7, 8 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 5, 6, 7, 8 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1, 2, 3, 4) | ✔ (form 1, 2, 3, 4) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 5, 6, 7, 8) | ✔ (form 5, 6, 7, 8) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 5, 6, 7, 8) | ✔ (form 5, 6, 7, 8) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
