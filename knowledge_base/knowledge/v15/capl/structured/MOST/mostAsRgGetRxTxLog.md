# mostAsRgGetRxTxLog

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostAsRgGetRxTxLog(long regsel, long i); // form 1
long mostAsRgGetRxTxLog(long regsel, long fblockId, long instId); // form 2
```

## Description

The first one returns the logical device address (node address) at position i of the registry. Indexing starts at 0.

The second one returns the logical device address (node address) of the function block. If there is no entry with the given FBlockId and InstId, an error code <0 is returned.

## Parameters

| Name | Description |
|---|---|
| regsel | 1: Local FBlockList2: Bus registry |
| i | Position of the registry entry. |
| fblockId | Function block ID |
| instId | Instance ID |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.0 | — | — | — | —✔ |
| Restricted To | — | MOST25 MOST50 MOST150 While Application Socket is active | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | — | ✔ | — | N/A | — | —✔ |
| 64-Bit | — | ✔ | — | — | — | —✔ |
