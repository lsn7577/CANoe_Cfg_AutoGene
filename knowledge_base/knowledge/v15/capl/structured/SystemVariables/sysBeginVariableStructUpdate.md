# sysBeginVariableStructUpdate

> Category: `SystemVariables` | Type: `function`

## Syntax

```c
long sysBeginVariableStructUpdate(char namespace[], char variable[]); // form 1
long sysBeginVariableStructUpdate(sysvarName); // form 2
```

## Description

Starts the update of several elements of a system variable of type struct or generic array.

Use this function and the corresponding sysEndVariableStructUpdate to change several elements at the same time without the variable having an intermediate value where only some elements are changed. Each call must be followed by a call to sysEndVariableStructUpdate, else the variable value will not change.

## Parameters

| Name | Description |
|---|---|
| namespace | Name of the name space. |
| variable | Name of the variable SysVarName: Name of the fully qualified name of the system variable, including all name spaces, separated by "::". The name must be preceded by "sysVar::". |
| SysVarName | Name of the fully qualified name of the system variable, including all name spaces, separated by "::". The name must be preceded by "sysVar::". |

## Example

```c
sysBeginVariableStructUpdate(sysvar::XCP::ECU_2::KL2);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.0 SP4 | 8.0 SP4 | 13.0 | 13.0: form 2 | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | ✔ | N/A |
