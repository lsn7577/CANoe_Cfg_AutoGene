# SCC_CreateMeteringReceiptReq_ISO

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_CreateMeteringReceiptReq_ISO ( byte SessionID[], long SAScheduleTupleId, char MeterID[], char ReceiptID[] )
```

## Description

Creates a Metering Receipt Request message for sending.

## Parameters

| Name | Description |
|---|---|
| SessionID | 8-byte long SessionID of SCC connection, range: 0 - 0xFF FF FF FF FF FF FF FF. |
| SAScheduleTupleId | Unique ID of a SAScheduleTuple which identifies the selected Tariff. |
| MeterID | Unique ID of the meter. |
| ReceiptID | Unique ID of the MeteringReceiptReq message. |
| Index | Name Type Description |
| 0 | MeterReading long Current meter reading in Wh |
| 1 | SigMeterReading byte [] Signature of the meter reading (length 64) |
| 2 | MeterStatus long Current status of the meter |
| 3 | TMeter long Timestamp of the current SECC time |

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
