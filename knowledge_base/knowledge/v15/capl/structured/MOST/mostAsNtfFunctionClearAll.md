# mostAsNtfFunctionClearAll

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostAsNtfFunctionClearAll(long deviceID, long fblockID, long instID;
```

## Description

Clears notification client entries from the notification matrix (deviceID >= 0). Functionality is similar to command message FBlock.Notification.Set(ClearAll, deviceID).

The notification matrix can be written with the function without sending a respective message.

## Parameters

| Name | Description |
|---|---|
| deviceID | Address of the notification client Exception: -1 clears the entire notification matrix |
| fblockID | Function block ID |
| instID | Instance ID |

## Return Values

See error codes

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.2 | — | — | — | —✔ |
| Restricted To | — | MOST25 MOST50 MOST150 While Application Socket is active | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | — | ✔ | — | N/A | — | —✔ |
| 64-Bit | — | ✔ | — | — | — | —✔ |
