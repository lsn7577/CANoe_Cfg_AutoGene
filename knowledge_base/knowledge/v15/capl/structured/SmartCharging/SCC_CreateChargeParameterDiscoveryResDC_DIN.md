# SCC_CreateChargeParameterDiscoveryResDC_DIN

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_CreateChargeParameterDiscoveryResDC_DIN ( byte SessionID[], char ResponseCode[], long NotificationMaxDelay, char StatusCode[], char Notification[], long EVSEProcessing, float CurrentAndVoltageLimits[], float PeakCurrentRipple)
```

## Description

Creates a Charge Parameter Discovery Response message for sending, using the DC syntax.

## Parameters

| Name | Description |
|---|---|
| SessionID | 8-byte long SessionID of SCC connection, range: 0 - 0xFF FF FF FF FF FF FF FF. |
| ResponseCode | Acknowledgement status of the message. |
| NotificationMaxDelay | Time until the vehicle is expected to react on the notification (for DC_EVSEStatus). |
| StatusCode | Internal state of the EVSE (for DC_EVSEStatus). |
| Notification | Notification about an action that the charge point wants the vehicle to perform (for DC_EVSEStatus). |
| EVSEProcessing | 0 if Finished 1 if Ongoing 2 if Ongoing_WaitingForCustomerInteraction (ISO 15118) |
| CurrentAndVoltageLimits | Electrical limit values CurrentAndVoltageLimits[0] = EVSEMaximumCurrentLimit CurrentAndVoltageLimits[1] = EVSEMaximumVoltageLimit CurrentAndVoltageLimits[2] = EVSEMinimumCurrentLimit CurrentAndVoltageLimits[3] = EVSEMinimumVoltageLimit Only for ISO 15118 CurrentAndVoltageLimits[4] = EVSEMaximumPowerLimit |
| PeakCurrentRipple | Peak-to-peak magnitude of the current ripple. |
| Index | Name Type Description |
| 0 | MaxPower float EVSEMaximumPowerLimit |
| 1 | CurrentRegulation- Tolerance float Absolute magnitude of the regulation tolerance. |
| 2 | EnergyToBeDelivered float Amount of energy to be delivered in Wh. |
| 3 | SAScheduleList long Schedule / tariff list from secondary actor. |
| 4 | EVSEIsolationStatus char[] Indicates the isolation condition. |

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
