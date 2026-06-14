# ILNodeSetPDUAsrTxMode

> Category: `CANoeIL` | Type: `function`

## Syntax

```c
long ILNodeSetPDUAsrTxMode (dbMsg dbMessage, long mode, long disturbanceCount, long flags)
```

## Description

Overrides the current valid transmission mode of the PDU. The transmission mode can be False or True. The current transmission mode is defined by or-ing the current data filter condition value of all signal values of the PDU.

## Parameters

| Name | Description |
|---|---|
| dbMessage | The symbolic name of a PDU in the database. |
| mode | Sets the True timing (1) or the False timing (0) to be active (regardless of the signal values). |
| disturbanceCount | Reserved/unused; should be set to -1 (“infinite”). |
| flags | Reserved; should be set to 0. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 SP4 | 14 | 14 | — | — |
| Restricted To | — | CAN FlexRay Ethernet | CAN FlexRay Ethernet | CAN FlexRay Ethernet | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | — | N/A |
