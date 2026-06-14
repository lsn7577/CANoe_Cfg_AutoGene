# SCC_CreatePowerDeliveryResDC_ISO

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_CreatePowerDeliveryResDC_ISO ( byte SessionID[], char ResponseCode[], long NotificationMaxDelay, char StatusCode[], char Notification[] )
```

## Description

Creates a Power Delivery Response message for sending, using the DC syntax.

## Parameters

| Name | Description |
|---|---|
| SessionID | 8-byte long SessionID of SCC connection, range: 0 - 0xFF FF FF FF FF FF FF FF. |
| ResponseCode | Acknowledgement status of the message. |
| NotificationMaxDelay | Time until the vehicle is expected to react on the notification (for DC_EVSEStatus). |
| StatusCode | Internal state of the EVSE (for DC_EVSEStatus). |
| Notification | Notification about an action that the charge point wants the vehicle to perform (for DC_EVSEStatus). |
| Index | Name Type Description |
| 0 | IsolationStatus char[] Current isolation condition. |

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
