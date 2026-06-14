# mostSetTimingMode

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostSetTimingMode(long channel, long mode);
```

## Description

This function configures the MOST hardware as a Timing Master (mode = 1) or Timing Slave (mode = 0).

MOST25: For further information on Master/Slave switchover functionality see also the description of the MTR bit in the Transceiver Control Register of the OS8104.

MOST50/150: Switching from Slave to non-static Master does not wake the network automatically. Use mostWakeup to start the network.

## Parameters

| Name | Description |
|---|---|
| channel | Channel of the connected interface |
| 0 | Slave |
| 1 | Master |

## Return Values

See error codes

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.0 | 5.0 | — | — | — | —✔ |
| Restricted To | MOMOST25 MOST50 MOST150ST Not in StopMeasurement | MOST25 MOST50 MOST150 Not in StopMeasurement | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
