# frSetPOCState

> Category: `FlexRay` | Type: `function`

## Syntax

```c
long frSetPOCState( long channel, long ccNumber, long pocState );
```

## Description

This function puts the FlexRay Communication Controller (CC) into the desired Protocol Operation Mode (POC state). The function is non-blocking. That means, the function will return before the CC has reached the desired POC-state.

All E-Ray POC-state changes can be monitored with the status- or POC-state-events. A status event is generated as soon as the second CC has reached the desired POC-state.

The diagram shows the several states and the corresponding transitions in the protocol operation control process:

## Parameters

| Name | Description |
|---|---|
| Channel | FlexRay channel (cluster number). |
| ccNumber | 1: E-Ray2: Second Startup Controller/Coldstart helper (Fujitsu) |
| POC State | Meaning |
| 0 | wakeup |
| 1 | normal active |
| 2 | halt |
| 3 | ready |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.1 | 7.1 | 13.0 | — | — | 1.0 |
| Restricted To | FlexRay | FlexRay | FlexRay | — | — | FlexRay |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
