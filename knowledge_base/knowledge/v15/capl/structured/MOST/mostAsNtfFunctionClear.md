# mostAsNtfFunctionClear

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostAsNtfFunctionClear(long deviceID, long fblockID, long instID, long functionID);
```

## Description

Clears a notification client entry from the notification matrix. Functionality is similar to command message FBlock.Notification.Set(Clear, deviceID, functionID).

The notification matrix can be written with the function without sending a respective message.

## Parameters

| Name | Description |
|---|---|
| deviceID | Addess of the notification client |
| fblockID | Function block ID |
| instID | Instance ID |
| functionID | Function ID |

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
