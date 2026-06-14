# testWaitForDiagChangedActiveVariant

> Category: `Test` | Type: `function`

## Syntax

```c
long testWaitForDiagChangedActiveVariant(char variantQualifier[]); // form 1
long testWaitForDiagChangedActiveVariant(char ecuQualifier[] , char variantQualifier[]); // form 2
```

## Description

Changes the active variant for the current target.

## Parameters

| Name | Description |
|---|---|
| variantQualifier | The variant to be used. |
| ecuQualifier | Qualifier of the ECU or target as set in the diagnostic configuration dialog for the respective diagnostic description. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.5 form 1 9.0 SP3 form 2 | — | — | — | 2.0 form 1 2.1 SP3 form 2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
