# mostGetSpyCtrl, mostGetSpyAsync, mostGetSpyEthPkt

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostGetSpyCtrl(long channel); // form 1
long mostGetSpyAsync(long channel); // form 2
MOST150: long mostGetSpyEthPkt(long channel); // form 3
```

## Description

Determines whether Spy mode for the Control, Asynchronous or Ethernet transmission channel is activated (Return value = 1) or deactivated (Return value = 0).

## Parameters

| Name | Description |
|---|---|
| channel | Channel of the connected interface. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.0: form 1-2 (MOST25) 7.6 SP2: form 3 | 5.0: form 1-2 (MOST25) 7.6 SP2: form 3 | — | — | — | —✔ |
| Restricted To | MOST150 Not in StopMeasurement | MOST150 Not in StopMeasurement | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
