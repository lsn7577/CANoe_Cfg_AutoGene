# SCC_SetOptionalParameter

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_SetOptionalParameter ( dword Parameter, long ParameterValue ) // form 1
long SCC_SetOptionalParameter ( dword Parameter, float ParameterValue ) // form 2
long SCC_SetOptionalParameter ( dword Parameter, char ParameterValue[] ) // form 3
long SCC_SetOptionalParameter ( dword Parameter, byte ParameterValue[] ) // form 4
```

## Description

Sets an optional parameter after creating a message.

## Parameters

| Name | Description |
|---|---|
| Parameter | ID number of the parameter, as denoted in the lists of optional parameters below each Create-function. |
| ParameterValue | Desired value of the parameter in the matching data type. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 SP3: 1, 2, 3, 4 | — | — | — | 3.0 SP3: form 1, 2, 3, 4 |
| Restricted To | — | Ethernet .SmartCharging | — | — | — | Ethernet .SmartCharging |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
