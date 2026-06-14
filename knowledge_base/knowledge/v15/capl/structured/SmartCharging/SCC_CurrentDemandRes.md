# SCC_CurrentDemandRes

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_CurrentDemandRes ( byte SessionId[], long ResponseCode, float EVSEPresentVoltage, float EVSEPresentCurrent, byte LimitAchievedFlags[], char EVSEID[], long SAScheduleTupleID, long ReceiptRequired)
```

## Description

The callback is called as soon as a Current Demand Response is received. Further details that are transmitted in this message can be queried with the following functions:

## Parameters

| Name | Description |
|---|---|
| SessionID | 8-byte long SessionID of SCC connection, range: 0 – 0xFF FF FF FF FF FF FF FF. |
| ResponseCode | 1 if OK, 0 if FAILED |
| EVSEPresentVoltage | Present voltage value of charge point. |
| EVSEPresentCurrent | Present current of charge point. |
| LimitAchievedFlags (ISO 15118) | Array of three flags which correspond to current \| voltage \| power limit achieved, in this order. |
| EVSEID (ISO 15118) | ID of charge point. |
| SAScheduleTupleID (ISO 15118) | ID of the selected SAScheduleTuple. |
| ReceiptRequired (ISO 15118) | Indicates if the vehicle is required to send a MeteringReceiptReq. |

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
