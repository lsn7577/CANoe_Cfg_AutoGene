# diagGetIdentifiedVariant

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetIdentifiedVariant(char identifiedVariantOut[], dword bufferLen);
long diagGetIdentifiedVariant(char ecuQualifier[], char identifiedVariantOut[], dword bufferLen);
```

## Description

Retrieve the qualifier of the variant that has been identified by the last successful run of the automatic variant identification algorithm for given target, or the current target if no target is given. The function can also be used to determine whether the algorithm has finished.

## Parameters

| Name | Description |
|---|---|
| ecuQualifier | ECU the identification algorithm should run for, not the currently selected one. If given, diagSetTarget does not have to be called. |
| identifiedVariantOut | Buffer for the qualifier |
| bufferLen | Length of the buffer |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.0 | 7.1 SP3 | — | — | — | 1.0 |
| Restricted To | Online mode | Online mode | — | — | — | Online mode |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
