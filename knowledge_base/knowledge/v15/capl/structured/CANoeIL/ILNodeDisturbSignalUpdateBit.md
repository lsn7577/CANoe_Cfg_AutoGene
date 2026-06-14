# ILNodeDisturbSignalUpdateBit

> Category: `CANoeIL` | Type: `function`

## Syntax

```c
long ILNodeDisturbSignalUpdateBit(dbSignal aSignal, long disturbanceMode, long disturbanceCount, long disturbanceValue);
long ILNodeDisturbSignalUpdateBit(char aMessageName[], char aSignalName[], long disturbanceMode, long disturbanceCount, long disturbanceValue);
```

## Description

This function modifies the update bit of a signal. Different fault injections are possible.This function influences a simulation node with an assigned CANoe interaction layer.

## Parameters

| Name | Type | Description |
|---|---|---|
| aMessageName |  | Name of the message or PDU that should be modified. |
| aSignalName |  | Name of the update bit signal. |
| aSignal |  | Update bit signal. |
| 0 | Value | The disturbance uses the value in disturbanceValue as update bit. |
| 1 | Freeze | The current update bit value is transmitted. |
| 2 | Random | A random value is transmitted as update bit. |
| -1 |  | Infinite. |
| 0 |  | Stops the disturbance, e.g.a infinite disturbance. |
| n |  | Number of disturbances. |
| disturbanceValue |  | This value is used in combination with the disturbanceMode. |

## Example

```c
// Sets the Signal Update Bit to 0

variables {
  long disturbanceMode  = 0; // The disturbance uses the value in disturbanceValue as Update Bit.
  int disturbanceCount  = 100;
  long disturbanceValue = 0;
}

on key 'a'{
  ILNodeDisturbSignalUpdateBit("PDU_A", "Signal_A", disturbanceMode, disturbanceCount, disturbanceValue);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 SP4 | 14 | 14 | — | — |
| Restricted To | — | CAN FlexRay | CAN FlexRay | CAN FlexRay | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | — | N/A |
