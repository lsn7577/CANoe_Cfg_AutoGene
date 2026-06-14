# Iso11783IL_TIMGetFunctionState

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_TIMGetFunctionState(dword functionID, dword& currentState); // form 1
long Iso11783IL_TIMGetFunctionState(dword functionID, dword& currentState, dword& counterpartAddress); // form 2
long Iso11783IL_TIMGetFunctionState(dbNode participant, dword functionID, dword& currentState); // form 3
long Iso11783IL_TIMGetFunctionState(dbNode participant, dword functionID, dword& currentState, dword& counterpartAddress); // form 4
```

## Description

Returns the current state of a TIM function.

If this function is called for a TIM client the function returns state 0 (Automation unavailable) if the TIM function is not assigned by the client.

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
| State | Description |
| 0 | Automation unavailable |
| 1 | Automation not ready |
| 2 | Automation ready to enable |
| 3 | Automation enabled |
| 4 | Automation pending |
| 5 | Active, not limited |
| 6 | Active, limited high |
| 7 | Active, limited low |
| 14 | Non-recoverable fault |
| 15 | Not available (parameter not supported or not configured for TIM) |
| counterpartAddress | Returns the address of the TIM counterpart. |
| participant | TIM participant (TIM server or TIM client). |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 12.0 SP3 | 13.0 | — | — | 4.0 SP3 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 3, 4 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1, 2) | ✔ (form 1, 2) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 3, 4) | ✔ (form 3, 4) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 3, 4) | ✔ (form 3, 4) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
