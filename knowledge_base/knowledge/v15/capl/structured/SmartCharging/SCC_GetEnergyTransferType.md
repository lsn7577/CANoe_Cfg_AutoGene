# SCC_GetEnergyTransferType

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_GetEnergyTransferType ( char[] EnergyTransferType )
```

## Description

Gets the energy transfer type (DIN 70121) resp. energy transfer mode (ISO 15118) from various messages.

## Parameters

| Name | Description |
|---|---|
| EnergyTransferType | Desired charging mode. |

## Return Values

Type of requested power supply:
The EnergyTransferType resp -Mode string is additionally written to the output buffer. If this is not required, an empty string can be transferred.

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
