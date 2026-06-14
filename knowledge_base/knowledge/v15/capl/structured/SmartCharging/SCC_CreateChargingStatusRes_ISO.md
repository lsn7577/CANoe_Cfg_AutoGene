# SCC_CreateChargingStatusRes_ISO

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_CreateChargingStatusRes_ISO ( byte SessionID[], char ResponseCode[], long NotificationMaxDelay, byte StatusFlags[], char Notification[], char EVSEID[], long SAScheduleTupleId )
```

## Description

Creates a Charging Status Response message for sending.

## Parameters

| Name | Description |
|---|---|
| SessionID | 8-byte long SessionID of SCC connection, range: 0 - 0xFF FF FF FF FF FF FF FF. |
| ResponseCode | Acknowledgement status of the message. |
| NotificationMaxDelay | Time until the vehicle is expected to react on the notification (for AC_EVSEStatus). |
| StatusFlags | Flags for AC_EVSEStatus: StatusFlags[0] = PowerSwitchClosed StatusFlags[1] = RCD. |
| Notification | Notification about an action that the charge point wants the vehicle to perform (for AC_EVSEStatus). |
| Caution! EVSEID is interpreted as a 64 bit number, and thus must not contain any letters. |  |
| SAScheduleTupleId | Unique ID of a SAScheduleTuple which identifies the selected Tariff. |
| Index | Name Type Description |
| 0 | MeterID char[] Unique ID of the meter. |
| 1 | MeterReading long Current meter reading in Wh. |
| 2 | SigMeterReading byte[] Signature of the meter reading (length 64). |
| 3 | MeterStatus long Current status of the meter. |
| 4 | TMeter long Timestamp of the current SECC time. |
| 5 | MaxCurrent float EVSEMaxCurrent. |
| 6 | ReceiptRequired long Indicates if the vehicle is required to sent a MeteringReceiptReq. |
| Caution! Due to the requirements of the schema, the element “MeterID” is mandatory if any of the optional meter-related parameters are to be supplied. |  |

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
