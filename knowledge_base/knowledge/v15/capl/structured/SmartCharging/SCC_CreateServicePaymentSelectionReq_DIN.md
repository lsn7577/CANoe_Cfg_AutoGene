# SCC_CreateServicePaymentSelectionReq_DIN

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_CreateServicePaymentSelectionReq_DIN ( byte SessionID[], char SelectedPaymentOption[], byte SelectedServiceIDs[], byte SelectedParameterSetIDs[], dword ServiceIDCount )
```

## Description

Creates a Service Payment Selection Request message for sending.

## Parameters

| Name | Description |
|---|---|
| SessionID | 8-byte long SessionID of SCC connection, range: 0 - 0xFF FF FF FF FF FF FF FF. |
| SelectedPaymentOption | Contract or ExternalPayment. |
| SelectedServiceIDs | IDs of the selected services. Must contain at least one entry. |
| SelectedParameterSetIDs | Parameter set IDs corresponding to the SelectedServiceIDs. Array must be the same size as SelectedServiceIDs, you can use -1 to omit a parameter set ID. |
| ServiceIDCount | Size of the array SelectedServiceIDs. |

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
