# sysSetAnalysisOnlyVariable

> Category: `SystemVariables` | Type: `function`

## Syntax

```c
void sysSetAnalysisOnlyVariable(SysVarName, long anlyzLocal);
```

## Description

Determines whether the variable is meant to be used for analysis purposes.

If this is true (anlyzLocal is set to 1), and the variable is changed in a CAPL program in the Measurement setup, the value change is not transmitted to the real time part of CANoe, but used immediately in the analysis part. This is the default.

If it is false (anlyzLocal is set to 0), value changes are always transmitted to the real time part.

## Parameters

| Name | Description |
|---|---|
| anlyzLocal | Defines whether the variable shall be used only in the analysis part of CANoe. |
| SysVarName | Name of the fully qualified name of the system variable, including all name spaces, separated by "::". |

## Return Values

—

## Example

```c
sysSetAnalysisOnlyVariable(sysvar::MyNamespace::StringVar, 1);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.2 SP3 | 7.0 | 13.0 | — | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | — | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | ✔ | N/A |
