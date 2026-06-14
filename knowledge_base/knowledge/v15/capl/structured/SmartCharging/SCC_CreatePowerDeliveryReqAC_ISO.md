# SCC_CreatePowerDeliveryReqAC_ISO

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_CreatePowerDeliveryReqAC_ISO ( byte SessionID[], char ChargeProgress[], long SAScheduleTupleId )
```

## Description

Creates a Power Delivery Request message for sending, using the AC syntax.

## Parameters

| Name | Description |
|---|---|
| SessionID | 8-byte long SessionID of SCC connection, range: 0 - 0xFF FF FF FF FF FF FF FF. |
| ChargeProgress | Type of action: “Start”, “Stop” or “Renegotiate”. |
| SAScheduleTupleId | Unique ID of a SAScheduleTuple which identifies the selected Tariff. |
| Index | Name Type Description |
| 0 | ChargingProfile complex Desired charging profile for the current charging session (i.e. maximum amount of power drawn over time). |

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
