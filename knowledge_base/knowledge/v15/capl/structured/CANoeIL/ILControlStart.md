# ILControlStart

> Category: `CANoeIL` | Type: `function`

## Syntax

```c
long ILControlStart ()
```

## Description

Cyclical sending starts; setting signals is now possible. Signal changes that occurred while the interaction layer was switched off (by ILControlStop or ILControlSimulationOff) are not considered on its activation.

## Parameters

| Name | Description |
|---|---|
| 0 | No error. |
| -1 | Momentary state of the IL does not permit this query. |
| -50 | Node layer is inactive — possibly deactivated in the node's configuration dialog. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.1 | 14 | 14 | — | — |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | — | N/A |
