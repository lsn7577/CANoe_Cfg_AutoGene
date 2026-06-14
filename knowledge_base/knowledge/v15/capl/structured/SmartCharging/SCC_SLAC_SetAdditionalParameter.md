# SCC_SLAC_SetAdditionalParameter

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_SLAC_SetAdditionalParameter ( dword Parameter, dword ParameterValue ) // form 1
long SCC_SLAC_SetAdditionalParameter ( dword Parameter, byte ParameterValues[] ) // form 2
```

## Description

Sets an additional parameter after creating a message, thus overwriting a value predefined by the specification (DIN 70121:2014-12).

## Parameters

| Name | Description |
|---|---|
| Parameter | ID number of the parameter, as denoted in the lists of optional parameters below each Create-function. |
| ParameterValue | Desired value of the parameter in the matching data type. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 SP3: form 1, 2 | — | — | — | 3.0 SP3: form 1, 2 |
| Restricted To | — | Ethernet .SmartCharging | — | — | — | Ethernet .SmartCharging |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
