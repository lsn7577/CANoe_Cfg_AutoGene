# mostSetNodeAdr, mostSetGroupAdr, mostSetAltPktAdr, mostSetOwnAdr

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostSetNodeAdr(long channel, long nodeadr);
long mostSetGroupAdr(long channel, long grpadr);
long mostSetAltPktAdr(long channel, long altpktadr);
long mostSetOwnAdr(long channel, long grpadr, long nodeadr);
```

## Description

These functions set the node address, group address or alternative packet address of the MOST hardware to the specified values.

## Parameters

| Name | Description |
|---|---|
| channel | Channel of the connected interface |
| nodeadr | Logical node address |
| groupadr | Group address |
| altpktadr | Alternative packet address |
| nodeposadr | Node position address |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 3.2: form 1-2 5.0: form 3 5.0: form 4 | 3.2: form 1-2 5.0: form 3 5.0: form 4 | — | — | — | —✔ |
| Restricted To | MOST25 (form 1-4) MOST50 (form 1-2) MOST150 (1, 2, 4) Not in StopMeasurement | MOST25 (form 1-4) MOST50 (form 1-2) MOST150 (1, 2, 4) Not in StopMeasurement | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
