# ChipState

> Category: `CAN` | Type: `function`

## Syntax

```c
long ChipState ()
```

## Description

Returns the current chip state of the CAN x controller.

Valid x values: 1…32

## Return Values

Chip state of the CAN x controller. See the following table for a description of the return values.
A description of the chip states can also be found here: Bus Statistics Window of option CAN.

## Example

```c
write ("Chip state of CAN1 = %d", CAN1.ChipState);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.1 | 7.1 | 13.0 | — | — | 1.0 |
| Restricted To | CAN | CAN | CAN | — | — | CAN |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — (since version 8.0) (deprecated, replaced by predefined system variable sysvar::_Statistics::CANn::,for details see system variables for statistics.) | — (since version 8.0) (deprecated, replaced by predefined system variable sysvar::_Statistics::CANn::,for details see system variables for statistics.) | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
