# sysGetVariableValueForDescription

> Category: `SystemVariables` | Type: `function`

## Syntax

```c
long sysGetVariableValueForDescription(SysVarName, char description[], long& value); // form 1
long sysGetVariableValueForDescription(char namespace[], char variable[], char description[], long& value); // form 2
```

## Description

Retrieves the value for a value description of a system variable of type long or long array. In this way, you can access the value table of the system variable.

## Parameters

| Name | Description |
|---|---|
| namespace | Name of the name space. |
| variable | Name of the variable. |
| description | Description for which the value shall be retrieved. |
| value | Receives the value for the description. |
| SysVarName | Name of the fully qualified name of the system variable, including all name spaces, separated by "::".The name must be preceded by "sysVar::". |

## Example

```c
long val;
sysGetVariableValueForDescription("Dynamic", "IntVar", "Zero", val);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.0 SP4 | 8.0 SP4 | 13.0 | — | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | ✔ | N/A |
