# StandardFrameCount

> Category: `CAN` | Type: `function`

## Syntax

```c
long StandardFrameCount ()
```

## Description

Returns the number of standard CAN messages on channel x since start of measurement.

Valid x values: 1…32

## Return Values

Number of standard CAN messages on channel x since start of measurement.

## Example

```c
write ("Number of standard frames on CAN1 = %d", CAN1.StandardFrameCount);
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
