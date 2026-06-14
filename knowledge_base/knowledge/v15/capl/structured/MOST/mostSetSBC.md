# mostSetSBC

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostSetSBC (long channel, long sbcvalue);
```

## Description

This function sets the "Synchronous Bandwidth Control (SBC) Register" of the MOST hardware chip to the given value.

The function is only practically applicable if the hardware connected to the channel is in master mode.

The newly set value is only accepted once a "DeAllocate" message re-releases all synchronous channel assignments.

## Parameters

| Name | Description |
|---|---|
| channel | Channel of the connected MOST hardware |
| sbcvalue | New SBC register value. Values between 0 and 15 are permitted. |

## Return Values

—

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.2 | 5.2 | — | — | — | —✔ |
| Restricted To | MOST25 MOST50 MOST150 Not in StopMeasurement | MOST25 MOST50 MOST150 Not in StopMeasurement | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
