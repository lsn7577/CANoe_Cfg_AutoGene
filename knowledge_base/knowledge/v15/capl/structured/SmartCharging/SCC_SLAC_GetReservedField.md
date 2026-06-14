# SCC_SLAC_GetReservedField

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_SLAC_GetReservedField ( dword Index, byte Data[], dword& DataSize )
```

## Description

Queries one of the reserved fields of the message. For a valid message, these fields must contain only zeroes.

## Parameters

| Name | Description |
|---|---|
| Index | Number of the reserved field (0 or 1). |
| Data | Output buffer for the field. |
| DataSize | Output of the byte length of the returned data. |

## Return Values

Data and length of the reserved field.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 SP3 | — | — | — | 3.0 SP3 |
| Restricted To | — | Ethernet .SmartCharging | — | — | — | Ethernet .SmartCharging |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
