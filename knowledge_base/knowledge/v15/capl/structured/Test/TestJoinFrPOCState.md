# TestJoinFrPOCState

> Category: `Test` | Type: `function`

## Syntax

```c
long TestJoinFrPOCState () // form 1
long TestJoinFrPOCState (dword aPOCState) // form 2
long TestJoinFrPOCState (dword aPOCState, dword aWUState) // form 3
```

## Description

Completes the current set of "joined events" with the transmitted event.

This function does not wait.

## Parameters

| Name | Description |
|---|---|
| aPOCState | The POC state the function will wait for (see selector 'FR_POCState' in event procedure on FrPOCState). If set to '-1' in combination with a 'WUState' the function will wait only for a Wakeup state (any POC state will be accepted). Available from CANoe 7.2. |
| aWUState | The Wakeup state the function will wait for (see selector 'FR_Info2' in event procedure on FrPOCState). Available from CANoe 7.2. |

## Example

For an example see function TestWaitForFrPOCState.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.0 SP4: form 1 7.2: form 2, 3 | 13.0 | — | — | 1.0 |
| Restricted To | — | FlexRay | FlexRay | — | — | FlexRay |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
