# TestWaitForDiagVariantIdentificationCompleted, TestWaitForDiagEcuVariantIdentificationCompleted

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForDiagVariantIdentificationCompleted(); // form 1
long TestWaitForDiagVariantIdentificationCompleted( char expectedVariant[]); // form 2
long TestWaitForDiagVariantIdentificationCompleted( char ecuQualifier[], char expectedVariant[]); // form 3
long TestWaitForDiagEcuVariantIdentificationCompleted( char ecuQualifier[]); // form 4
```

## Description

Waits for the completion of the automatic variant identification algorithm. If the qualifier of an expected variant is given, an error is returned if a different variant is identified.

## Parameters

| Name | Description |
|---|---|
| expectedVariant | Qualifier of the variant that should be identified. |
| ecuQualifier | Wait for the completion of the variant identification for this diagnostic ECU. No call to DiagSetTarget is necessary if this parameter is given. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.1 SP3: form 1-2 10.0 SP3: form 3-4 | — | — | — | 1.0: form 1-2 2.2 SP2: form 3-4 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
