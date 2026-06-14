# Iso11783IL_TIMConnectSysVarToState

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_TIMConnectSysVarToState(dbNode counterpart, char[] sysVarNameWithPath); // form 1
long Iso11783IL_TIMConnectSysVarToState(byte counterpartAddress, char[] sysVarNameWithPath); // form 2
long Iso11783IL_TIMConnectSysVarToState(dbNode participant, dbNode counterpart, char[] sysVarNameWithPath); // form 3
long Iso11783IL_TIMConnectSysVarToState(dbNode participant, byte counterpartAddress, char[] sysVarNameWithPath); // form 4
```

## Description

Connects the state of a TIM client/server connection to a system variable.

You find the possible states in the tables of Client States (TIM Component - ISO11783) or Server States (TIM Component - ISO11783).

By means of the function you can wait for a specific state (e.g. using TestWaitForSignalMatch) and with Iso11783IL_TIMFreezeConnection you can stay in this state.

To release connection between the system variable and a state, just call the same method again, but with the empty string instead of the name of system variable.

## Parameters

| Name | Description |
|---|---|
| counterpart | TIM counterpart of the client/server connection. |
| counterpartAddress | Address of the TIM counterpart of the client/server connection. Value range: 0..253 |
| sysVarNameWithPath | Name of the system variable, all name spaces inclusive. |
| participant | TIM participant (TIM server or TIM client). |

## Example

```c
Iso11783IL_TIMConnectSysVarToState(TIMClient, "sysvarTIMClientState");
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0: form 1, 3 11.0 SP2: form 2, 4 | 13.0 | — | — | 3.0: form 2 3.0 SP2: form 4 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 3, 4 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1, 2) | ✔ (form 1, 2) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 3, 4) | ✔ (form 3, 4) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 3, 4) | ✔ (form 3, 4) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
