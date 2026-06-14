# ARILResetPDUTimingCyclic

> Category: `AUTOSARpduIL` | Type: `function`

## Syntax

```c
long ARILResetPDUTimingCyclic (dbMsg dbMessage, long TrueOrFalse);
```

## Description

Resets the cyclic-timing to the values from the database. Possibly two timings (False and True) exist in parallel and are selected upon the current transmission mode of the PDU.

## Parameters

| Name | Description |
|---|---|
| dbMessage | The symbolic name of a PDU in the database. |
| TrueOrFalse | 0: denotes the False timing 1: denotes the True timing 3: denotes the True and the False timing. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 SP2 | 14 | 14 | — | — |
| Restricted To | — | CAN Ethernet FlexRay | CAN Ethernet FlexRay | CAN Ethernet FlexRay | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | — | N/A |
