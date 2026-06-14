# CANstressSetContinuousDisturbanceUntilStop

> Category: `CANstress` | Type: `function`

## Syntax

```c
void CANstressSetContinuousDisturbanceUntilStop (dword type);
```

## Description

Sets the Continuous disturbance (until stop) mode. Once the trigger has been activated, the continuous disturbance will prevail until the CANstress device is deactivated (e.g. by means of the CANstressStop function) and/or the measurement or test module is terminated.

## Parameters

| Name | Description |
|---|---|
| type | Defines the type of continuous disturbance. The disturbance can be associated with dominant or recessive bits or it can be an analog disturbance. 2 indicates a dominant disturbance, 3 a recessive disturbance and 4 an analog disturbance (only in conjunction with CANstress DR). |

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
