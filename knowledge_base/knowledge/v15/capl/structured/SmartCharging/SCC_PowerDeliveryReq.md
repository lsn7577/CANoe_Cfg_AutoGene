# SCC_PowerDeliveryReq

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_PowerDeliveryReq ( byte SessionId[], long ChargeProfileCount, long ChargeState, long ScheduleID)
```

## Description

The callback is called as soon as a Power Delivery Request is received.

With this request, the vehicle requests the charge point to switch on the current and to send the charging profile.

Further details that are transmitted in this request can be queried with the following functions:

## Parameters

| Name | Description |
|---|---|
| SessionID | 8-byte long SessionID of SCC connection, range: 0 – 0xFF FF FF FF FF FF FF FF. |
| ChargingProfileCount | Number of received charging profiles. |
| ChargeState | 1 if start of charging is requested, 0 if stop of charging is requested, 2 if ReNegotiation is requested (only ISO 15118). Corresponds to ReadyToChargeState in DIN 70121. |
| ScheduleID | ID of the chosen SAScheduleTuple. |

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
