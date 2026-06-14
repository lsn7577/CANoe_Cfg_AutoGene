# linSimulateETFCollision

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linSimulateETFCollision (dword etfId); // form 1
dword linSimulateETFCollision (dword etfId, dword respLength, dword numCollisions, byte dataBytes[]); // form 2
```

## Description

This function can be used to cause collisions for next coming header(s) of an event-triggered frame.

## Parameters

| Name | Description |
|---|---|
| etfId | LIN frame identifier in the range 0 .. 59 |
| respLength | Number of databytes to be sent as the response on the header of the event-triggered frame. Value range: 1..9. Default: 1 |
| numCollisions | Number of times the specified response has to be applied. Value range: 1..255. Default: 1 |
| Databytes | Array of databytes to be sent as the response. The size of the array shall correspond to the respLength parameter. Default: NULL |

## Return Values

On success, a value unequal to zero, otherwise zero.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 6.0 | 6.0 | — | — | — | 1.0 |
| Restricted To | LIN Real bus mode | LIN Real bus mode | — | — | — | LIN Real bus mode |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
