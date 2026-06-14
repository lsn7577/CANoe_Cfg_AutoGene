# Iso11783IL_OPSelectActiveWorkingSet

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPSelectActiveWorkingSet( dword workingSetAddress ); // form 1
long Iso11783IL_OPSelectActiveWorkingSet( dbNode implement, dword workingSetAddress ); // form 2
```

## Description

Sends a Select Active Working Set command to the Virtual Terminal to select a new active Working Set. The necessary device name for this command is determined by means of parameter workingSetAddress.

## Parameters

| Name | Description |
|---|---|
| implement | Simulation node to apply the function. |
| workingSetAddress | Address of the new active Working Set, 0..253. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 14 | 13.0 | — | — | 5.0 SP3 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 2 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
