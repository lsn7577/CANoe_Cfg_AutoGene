# vtsLoadWFResistance

> Category: `VTSystem` | Type: `function`

## Syntax

```c
long vtsLoadWFResistance (char Target[], char filepath[]);
```

## Description

This function loads a resistance curve for a VT2004 channel from the specified file.

## Parameters

| Name | Description |
|---|---|
| Target | Name of the system variable/namespace that will be affected by this function call. |
| filepath | Path of the file containing the resistance curve. The path can be given absolute or relative to the CANoe configuration. |

## Example

See example vtsSetWFParams

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.5 SP2 | 13.0 | — | — | 1.0 |
| Restricted To | — | Main method | Main method VT offline | — | — | Main method |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
