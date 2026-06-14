# SCC_CreateChargeParameterDiscoveryResAC_ISO

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_CreateChargeParameterDiscoveryResAC_ISO ( byte SessionID[], char ResponseCode[], long NotificationMaxDelay, byte StatusFlags[], char Notification[], long EVSEProcessing, float NominalVoltage, float MaxCurrent )
```

## Description

Creates a Charge Parameter Discovery Response message for sending, using the AC syntax.

## Parameters

| Name | Description |
|---|---|
| SessionID | 8-byte long SessionID of SCC connection, range: 0 - 0xFF FF FF FF FF FF FF FF. |
| ResponseCode | Acknowledgement status of the message. |
| NotificationMaxDelay | Time until the vehicle is expected to react on the notification (for AC_EVSEStatus). |
| StatusFlags | Flags for AC_EVSEStatus: StatusFlags[0] = PowerSwitchClosed StatusFlags[1] = RCD |
| Notification | Notification about an action that the charge point wants the vehicle to perform (for AC_EVSEStatus). |
| EVSEProcessing | 0 if Finished 1 if Ongoing 2 if Ongoing_WaitingForCustomerInteraction (ISO 15118) |
| NominalVoltage | Line voltage supported by the EVSE. |
| MaxCurrent | EVSEMaxCurrent |
| Index | Name Type Description |
| 0 | SAScheduleList long Schedule / tariff list from secondary actor |

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
