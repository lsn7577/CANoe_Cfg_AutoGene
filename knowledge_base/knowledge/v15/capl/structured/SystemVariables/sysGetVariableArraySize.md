# sysGetVariableArraySize

> Category: `SystemVariables` | Type: `function`

## Syntax

```c
dword sysGetVariableArraySize(sysvar variable) // form 1
long sysGetVariableArraySize(char namespace[], char variable[], dword& arraySize) // form 2
```

## Description

Retrieves the current array size of a system variable which has a generic array data type.

## Parameters

| Name | Description |
|---|---|
| variable (form 1) | Name of the fully qualified name of the system variable, including all name spaces, separated by "::". The name must be preceded by "sysVar::". |
| namespace (form 2) | Name of the namespace |
| variable (form 2) | Name of the variable |
| arraySize (form 2) | current size of the array (out-parameter) |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 9.0 | 9.0 | 13.0 | — | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | ✔ | N/A |
