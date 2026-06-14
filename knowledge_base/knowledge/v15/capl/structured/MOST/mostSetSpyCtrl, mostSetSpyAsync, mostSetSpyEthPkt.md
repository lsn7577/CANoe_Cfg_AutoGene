# mostSetSpyCtrl, mostSetSpyAsync, mostSetSpyEthPkt

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostSetSpyCtrl(long channel, long mode);
long mostSetSpyAsync(long channel, long mode);
MOST150: long mostSetSpyEthPkt(long channel, long mode);
```

## Description

Spy mode is activated (mode = 1) or deactivated (mode = 0) for the Control, Asynchronous or Ethernet transmission channel using these functions.

## Parameters

| Name | Description |
|---|---|
| channel | Channel of the connected interface |
| 0 | Spy inactive |
| 1 | Spy active |

## Return Values

See error codes
For MOST hardware interfaces that do not support a Spy mode the error code kMostWrongHWType is returned.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.0: form 1-2 7.6 SP2: 3 | 5.0: form 1-2 7.6 SP2: form 3 | — | — | — | —✔ |
| Restricted To | MOST150 (since version 7.6 SP2) Not in StopMeasurement | MOST150 (since version 7.6 SP2) Not in StopMeasurement | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
