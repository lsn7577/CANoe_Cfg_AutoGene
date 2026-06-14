# SCC_CreateChargeParameterDiscoveryReqDC_DIN

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_CreateChargeParameterDiscoveryReqDC_DIN ( byte SessionID[], byte StatusFlags[], char ErrorCode[], char EnergyTransferType[], float MaxCurrent, float MaxVoltage)
```

## Description

Creates a Charge Parameter Discovery Request message for sending, using the DC syntax.

## Parameters

| Name | Description |
|---|---|
| SessionID | 8-byte long SessionID of SCC connection, range: 0 - 0xFF FF FF FF FF FF FF FF. |
| StatusFlags | Flags for DC_EVStatus: StatusFlags[0] = EVReady StatusFlags[1] = EVCabinConditioning StatusFlags[2] = EVRESSConditioning StatusFlags[3] = EVRESSSOC |
| ErrorCode | EVErrorCode for DC_EVStatus. |
| EnergyTransferType | Desired charging mode. |
| MaxCurrent | EVMaxCurrent |
| MaxVoltage | EVMaxVoltage |
| Index | Name Type Description |
| 0 | MaxPower float EVMaximumPowerLimit |
| 1 | EnergyCapacity float Maximum supported power capacity in Wh. |
| 2 | EnergyRequest float Amount of requested energy in Wh. |
| 3 | FullSOC long Charge percentage to be considered as fully charged. |
| 4 | BulkSOC long Charge percentage to be considered as the end of a fast charge process. |

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
