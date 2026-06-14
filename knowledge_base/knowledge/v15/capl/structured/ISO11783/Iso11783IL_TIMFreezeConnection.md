# Iso11783IL_TIMFreezeConnection

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_TIMFreezeConnection(dbNode counterpart, dword runToState); // form 1
long Iso11783IL_TIMFreezeConnection(dbNode counterpart, dword runToState, char sysVarNameWithPath[]); // form 2
long Iso11783IL_TIMFreezeConnection(byte counterpartAddress, dword runToState); // form 3
long Iso11783IL_TIMFreezeConnection(byte counterpartAddress, dword runToState, char sysVarNameWithPath[]); // form 4
long Iso11783IL_TIMFreezeConnection(dbNode participant, dbNode counterpart, dword runToState); // form 5
long Iso11783IL_TIMFreezeConnection(dbNode participant, dbNode counterpart, dword runToState, char sysVarNameWithPath[]); // form 6
long Iso11783IL_TIMFreezeConnection(dbNode participant, byte counterpartAddress, dword runToState); // form 7
long Iso11783IL_TIMFreezeConnection(dbNode participant, dword runToState, char sysVarNameWithPath[]); // form 8
```

## Description

After calling this function the TIM client or TIM server runs until the specified state is reached. In this state the node still sends the cyclic status messages.

You find the possible states in the tables of Client States (TIM Component - ISO11783) or Server States (TIM Component - ISO11783).

To continue the standard process you can call Iso11783IL_TIMContinueConnection.

For form 2, 4, 6 and 8 you can specify an additional system variable which is set to value 1 if the specified state is reached.

## Parameters

| Name | Description |
|---|---|
| counterpart | TIM counterpart of the client/server connection. |
| runToState | The simulated TIM participant runs to this state and freezes this state. |
| counterpartAddress | Address of the TIM counterpart of the client/server connection. |
| sysVarNameWithPath | Name of a system variable (all name spaces inclusive) which is set to 1 if the state is reached. |
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
