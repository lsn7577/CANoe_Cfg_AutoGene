# TestEnableUpdateBit

> Category: `Test` | Type: `function`

## Syntax

```c
long TestEnableUpdateBit (dbSignal aSignal);
```

## Description

Re-enables the standard behaviour of the update bit, after it has been disabled with TestDisableUpdateBit.

This function influences a simulation node with an assigned CANoe Interaction Layer.

## Parameters

| Name | Description |
|---|---|
| aSignal | Signal that should be reset to update bit standard behavior. |

## Example

```c
// disables the update bit of signal ‘DoorStatus_UB’ for 1000 ms
TestDisableUpdateBit(DoorStatus_UB, 0);
TestWaitForTimeout(1000);
TestEnableUpdateBit(DoorStatus_UB);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.2 | 13.0 | — | — | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
