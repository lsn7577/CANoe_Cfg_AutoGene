# SCC_CreatePowerDeliveryReqDC_DIN

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_CreatePowerDeliveryReqDC_DIN ( byte SessionID[], byte StatusFlags[], char ErrorCode[], long ReadyToChargeState, long ChargingComplete )
```

## Description

Creates a Power Delivery Request message for sending, using the DC syntax.

## Parameters

| Name | Description |
|---|---|
| SessionID | 8-byte long SessionID of SCC connection, range: 0 - 0xFF FF FF FF FF FF FF FF. |
| StatusFlags | Flags for DC_EVStatus: StatusFlags[0] = EVReady StatusFlags[1] = EVCabinConditioning StatusFlags[2] = EVRESSConditioning StatusFlags[3] = EVRESSSOC |
| ErrorCode | EVErrorCode for DC_EVStatus: |
| ReadyToChargeState | 1 if start of charging is requested, 0 if stop of charging is requested. |
| ChargingComplete | 1, if the battery is completely charged; otherwise 0. |
| Index | Name Type Description |
| 0 | ChargingProfile complex Desired charging profile for the current charging session (i.e. maximum amount of power drawn over time). |
| 1 | BulkChargingComplete long 1, if the bulk charging operation is complete; otherwise 0. |

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
