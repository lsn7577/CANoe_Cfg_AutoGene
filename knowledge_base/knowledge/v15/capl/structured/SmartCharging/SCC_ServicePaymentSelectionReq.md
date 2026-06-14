# SCC_ServicePaymentSelectionReq

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_ServicePaymentSelectionReq ( byte SessionID[], char SelectedPaymentOption[], long ServiceListCount )
```

## Description

The callback is called as soon as a Service Payment Selection Request is received. The Request contains the selected services and the chosen method of payment. Further details that are transmitted in this request can be queried with the following functions:

## Parameters

| Name | Description |
|---|---|
| SessionID | 8-byte long SessionID of SCC connection, range: 0 – 0xFF FF FF FF FF FF FF FF. |
| SelectedPaymentOption | The selected payment option in form of a string. |
| ServiceListCount | Number of selected services: Up to 8 entries are contained in the list. The list entries must be queried via separate help functions. |

## Return Values

—

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
