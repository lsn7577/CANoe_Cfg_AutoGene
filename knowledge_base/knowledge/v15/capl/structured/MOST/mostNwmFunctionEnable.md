# mostNwmFunctionEnable

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostNwmFunctionEnable(long functionId, long opTypes);
```

## Description

Registers and unregisters a function and its operations with the NetworkMaster.

## Parameters

| Name | Description |
|---|---|
| functionId | Function ID. |
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

## Return Values

See error codes

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.1 | — | — | — | —✔ |
| Restricted To | — | MOST25 MOST50 MOST150 | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | — | ✔ | — | N/A | — | —✔ |
| 64-Bit | — | ✔ | — | — | — | —✔ |
