# sysGetVariableMax

> Category: `SystemVariables` | Type: `function`

## Syntax

```c
long sysGetVariableMax(SysVarName, long& maxValue); // form 1
long sysGetVariableMax(SysVarName, double& maxValue); // form 2
long sysGetVariableMax(char namespace[], char variable[], long& maxValue); // form 3
long sysGetVariableMax(char namespace[], char variable[], double& maxValue); // form 4
long sysGetVariableMax(SysVarName, dword& maxValue); // form 5
long sysGetVariableMax(char namespace[], char variable[], dword& maxValue); // form 6
long sysGetVariableMax(SysVarName, int64& maxValue); // form 7
long sysGetVariableMax(char namespace[], char variable[], int64& maxValue); // form 8
long sysGetVariableMax(SysVarName, qword& maxValue); // form 9
long sysGetVariableMax(char namespace[], char variable[], qword& maxValue); // form 10
```

## Description

Retrieves the maximum of a variable.

## Parameters

| Name | Description |
|---|---|
| SysVarName | Name of the fully qualified name of the system variable, including all name spaces, separated by "::".The name must be preceded by "sysVar::". |
| namespace | Name of the namespace. |
| variable | Name of the variable. |
| maxValue | Receives the maximum of the variable if no errors occur (reference parameter). Must be the correct type for the system variable. |

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
