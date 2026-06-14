# sysSetVariableDescriptionForValue

> Category: `SystemVariables` | Type: `function`

## Syntax

```c
long sysSetVariableDescriptionForValue(char namespace[], char variable[], long value, char description[]);
```

## Description

Sets a description for a particular value of a system variable of type Integer or Integer Array

## Parameters

| Name | Description |
|---|---|
| namespace | Name of the name space. |
| variable | Name of the variable. |
| value | Value for which the description shall be set. |
| description | New description for the value. |

## Example

```c
sysSetVariableDescriptionForValue("Dynamic", "IntVar", 0, "Zero");
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
