# CANstressSetLimitedDisturbanceNumber

> Category: `CANstress` | Type: `function`

## Syntax

```c
void CANstressSetLimitedDisturbanceNumber (dword cycles, dword distPerCycle, dword cyclePause);
```

## Description

Sets the Limited number of disturbances disturbance mode. In this mode, the number n of disturbances in a disturbance cycle is limited. n disturbances will be followed by a configurable pause p as long as this is not a single disturbance cycle.

## Parameters

| Name | Description |
|---|---|
| cycles | Defines the number of disturbance cycles. Values from 1 to 65,535 are valid. |
| distPerCycles | Defines the number of disturbances per disturbance cycle. Values from 1 to 255 are valid. |
| cyclePause | Defines the length of the pause between two disturbance cycles. The length is defined in ms and may be between 1 and 65,535. |

## Return Values

—

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.0 | — | — | — | 1.1 |
| Restricted To | — | CAN CANstress | — | — | — | CAN CANstress |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
