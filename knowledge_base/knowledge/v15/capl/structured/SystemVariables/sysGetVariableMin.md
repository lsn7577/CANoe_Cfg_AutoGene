# sysGetVariableMin

> Category: `SystemVariables` | Type: `function`

## Syntax

```c
long sysGetVariableMin(SysVarName, long& minValue); // form 1
long sysGetVariableMin(SysVarName, double& minValue); // form 2
long sysGetVariableMin(char namespace[], char variable[], long& minValue); // form 3
long sysGetVariableMin(char namespace[], char variable[], double& minValue); // form 4
long sysGetVariableMin(SysVarName, dword& minValue); // form 5
long sysGetVariableMin(char namespace[], char variable[], dword& minValue); // form 6
long sysGetVariableMin(SysVarName, int64& minValue); // form 7
long sysGetVariableMin(char namespace[], char variable[], int64& minValue); // form 8
long sysGetVariableMin(SysVarName, qword& minValue); // form 9
long sysGetVariableMin(char namespace[], char variable[], qword& minValue); // form 10
```

## Description

Retrieves the minimum of a variable of type integer or integer array.

## Parameters

| Name | Description |
|---|---|
| SysVarName | Name of the fully qualified name of the system variable, including all name spaces, separated by "::".The name must be preceded by "sysVar::". |
| namespace | Name of the namespace. |
| variable | Name of the variable. |
| minValue | Receives the minimum of the variable if no errors occur (reference parameter). Must be the correct type for the system variable. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.2 SP3: form 1-4 11.0 SP2: form 5-10 | 7.2: form 1-4 11.0 SP2: form 5-10 | 13.0 | — | 14 | 1.0: form 1-4 3.0 SP2: form 5-10 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | ✔ | N/A |
