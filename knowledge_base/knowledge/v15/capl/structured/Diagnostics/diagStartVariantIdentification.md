# diagStartVariantIdentification

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagStartVariantIdentification();
long diagStartVariantIdentification(char ecuQualifier[]);
```

## Description

Start the automatic variant identification algorithm for the given target, or the currently selected one if none is given. The algorithm will communicate via the built-in diagnostic channel, i.e. the CAPL callback functions are not used for the identification.

A tester module may wait for the completion of the algorithm with testWaitForDiagVariantIdentificationCompleted, or query the status of the identification with diagGetIdentifiedVariant.

## Parameters

| Name | Description |
|---|---|
| ecuQualifier | ECU the identification algorithm should run for, not the currently selected one. If given, diagSetTarget does not have to be called. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.0 | 7.1 SP3 | — | — | — | 1.0 |
| Restricted To | Online mode | Online mode | — | — | — | Online mode |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
