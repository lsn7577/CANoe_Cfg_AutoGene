# SetPWMRepeats

> Category: `VTSystem` | Type: `method`

## Syntax

```c
long SysVarNamespace.SetPWMRepeats (dword numOfRepeats);
```

## Description

This function sets the number of stimulated PWM periods after the start of stimulation. If the number of cycles output is not limited, numOfRepeats must be set to 0.

## Parameters

| Name | Description |
|---|---|
| numOfRepeats | Number of PWM periods to be stimulated.Valid values: 0…65535. |

## Example

See example SetStimulationMode

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.1 SP3 | 13.0 | — | — | 1.0 |
| Restricted To | — | — | VT offline | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
