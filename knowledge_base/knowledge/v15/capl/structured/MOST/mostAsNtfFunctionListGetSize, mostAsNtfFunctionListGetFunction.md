# mostAsNtfFunctionListGetSize, mostAsNtfFunctionListGetFunction

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostAsNtfFunctionListGetSize(long deviceID, long fblockID, long instID);
long mostAsNtfFunctionListGetFunction(long deviceID, long fblockID, long instid, long index);
```

## Description

The function makes it possible to output the list of all functions in which the notification client (deviceID) is registered. Functionality is similar to command message FBlock.NotificationCheck.Get(deviceID).

The notification matrix can be read out with the function without sending a respective message.

## Parameters

| Name | Description |
|---|---|
| deviceID | Address of the notification client. Exception: -1 outputs a list of all enabled functions. |
| fblockID | Function block ID |
| instID | Instance ID |
| index | Index in the function list |

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
