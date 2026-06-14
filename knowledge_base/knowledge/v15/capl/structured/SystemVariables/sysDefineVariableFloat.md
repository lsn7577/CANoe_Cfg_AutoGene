# sysDefineVariableFloat

> Category: `SystemVariables` | Type: `function`

## Syntax

```c
long sysDefineVariableFloat(char namespace[], char variable[], double initialValue); // form 1
long sysDefineVariableFloat(char namespace[], char variable[], double initialValue, double minimum, double maximum); // form 2
```

## Description

Defines a variable of the float type.

## Parameters

| Name | Description |
|---|---|
| namespace | Name of the name space. |
| variable | Name of the variable. |
| initialValue | Initial value of the variable. |
| minimum | The minimum value of the variable. |
| maximum | The maximum value of the variable. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.1/5.2: form 1 7.2 SP3: form 2 | 5.1/5.2: form 1 7.2: form 2 | 13.0 | — | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | ✔ | N/A |
