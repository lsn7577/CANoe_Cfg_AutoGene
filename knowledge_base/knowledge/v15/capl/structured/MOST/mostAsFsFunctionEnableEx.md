# mostAsFsFunctionEnableEx

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostAsFsFunctionEnableEx(long fblockId, long instId, long functionId, long opTypes); // form 1
long mostAsFsFunctionEnableEx(long fblockId, long instId, long functionId, long opTypes, char cbSendStatus[]); // form 2
```

## Description

mostAsFsFunctionEnableEx() registers a function and its operations with the function service. The service must have been previously enabled for the function block with mostAsFsEnableEx.

The second option registers a function with the notification service simultaneously. For this to be achieved, the function must be of the "Property" type and the notification service of the function block must have been previously enabled with mostAsNtfEnableEx.

Database support

The special value functionID=-1 triggers the execution of the CAPL function for all MOST functions and operations of the function block from the function catalog.

## Parameters

| Name | Description |
|---|---|
| fblockId | Function block ID |
| instId | Instance ID |
| functionId | Function ID or -1 for all functions of the function block from the database. |
| cbSendStatus[] | Name of the CAPL function that generates and sends the status message. If functionID=-1, cbSendStatus designates the prefix of the CAPL send functions to be defined. If an empty character string is specified, the default prefix "SendStatus_" is used. |
| Bit 0 | OpType = 0x0 (Set/Start) |
| Bit 1 | OpType = 0x1 (Get/Abort) |
| Bit 2 | OpType = 0x2 (SetGet/StartResult) |
| Bit 3 | OpType = 0x3 (Increment/-) |
| Bit 4 | OpType = 0x4 (Decrement/-) |
| Bit 5 | OpType = 0x5 (GetInterface/GetInterface) |
| Bit 6 | OpType = 0x6 (-/StartResultAck) |
| Bit 7 | OpType = 0x7 (-/AbortAck) |
| Bit 8 | OpType = 0x8 (-/StartAck) |
| Bit 9 | OpType = 0x9 (-/ErrorAck) |
| Bit 10 | OpType = 0xA (-/ProcessingAck) |
| Bit 11 | OpType = 0xB (-/Processing) |
| Bit 12 | OpType = 0xC (Status/Result) |
| Bit 13 | OpType = 0xD (-/ResultAck) |
| Bit 14 | OpType = 0xE (Interface/Interface) |
| Bit 15 | OpType = 0xF (Error) |
| Bit 16 | All OpTypes corresponding to 0-15, if they are defined in the XML function catalog. |

## Return Values

See error codes

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.0 | — | — | — | —✔ |
| Restricted To | — | MOST25 MOST50 MOST150 While Application Socket is active | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | — | ✔ | — | N/A | — | —✔ |
| 64-Bit | — | ✔ | — | — | — | —✔ |
