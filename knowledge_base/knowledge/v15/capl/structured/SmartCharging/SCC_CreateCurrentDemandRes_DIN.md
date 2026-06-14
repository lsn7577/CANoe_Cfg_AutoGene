# SCC_CreateCurrentDemandRes_DIN

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_CreateCurrentDemandRes_DIN ( byte SessionID[], char ResponseCode[], long NotificationMaxDelay, char StatusCode[], char Notification[], float PresentVoltage, float PresentCurrent, byte LimitAchievedFlags[] )
```

## Description

Creates a Current Demand Request message for sending.

## Parameters

| Name | Description |
|---|---|
| SessionID | 8-byte long SessionID of SCC connection range: 0 - 0xFF FF FF FF FF FF FF FF. |
| ResponseCode | Acknowledgement status of the message. |
| NotificationMaxDelay | Time until the vehicle is expected to react on the notification (for DC_EVSEStatus). |
| StatusCode | Internal state of the EVSE (for DC_EVSEStatus). |
| Notification | Notification about an action that the charge point wants the vehicle to perform (for DC_EVSEStatus). |
| PresentVoltage | EVSEPresentVoltage |
| PresentCurrent | EVSEPresentCurrent |
| LimitAchievedFlags | Flags that indicate if any limit is achieved: LimitAchievedFlags [0] = EVSECurrentLimitAchieved LimitAchievedFlags [1] = EVSEVoltageLimitAchieved LimitAchievedFlags [2] = EVSEPowerLimitAchieved |
| Index | Name Type Description |
| 0 | IsolationStatus char[] Current isolation condition. |
| 1 | MaxVoltage float EVSEMaximumVoltageLimit |
| 2 | MaxCurrent float EVSEMaximumCurrentLimit |
| 3 | MaxPower float EVSEMaximumPowerLimit |

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
