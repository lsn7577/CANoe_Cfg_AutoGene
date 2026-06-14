# Iso11783IL_OPSaveAuxAssignment

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPSaveAuxAssignment( char filename[] ); // form 1
long Iso11783IL_OPSaveAuxAssignment( dbNode implement, char filename[] ); // form 2
```

## Description

The function saves the current auxiliary input assignment as Preferred Auxiliary Input Assignment in an INI file.

With the function Iso11783IL_OPLoadAuxAssignment the Preferred Assignment can be load and used again.

## Parameters

| Name | Description |
|---|---|
| filename | File name of an INI file (*.ini) |
| implement | Simulation node to apply the function. |

## Example

```c
Iso11783IL_OPSaveAuxAssignment( "Sprayer.INI");
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0: form 1 9.0: form 2 | 13.0 | — | — | 2.1 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 2 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
