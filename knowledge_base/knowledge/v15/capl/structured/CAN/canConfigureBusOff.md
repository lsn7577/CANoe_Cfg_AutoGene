# canConfigureBusOff

> Category: `CAN` | Type: `function`

## Syntax

```c
long canConfigureBusOff(long channel, long canId, long flags);
```

## Description

Uses the defined ID of a message to set the bus state to BusOff.

## Parameters

| Name | Description |
|---|---|
| Channel | The CAN channel. |
| canId | Message ID that is used to set the bus state to BusOff. |
| flags | 0 = Switches off the disturbance1 = Switches on the disturbance |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.5 SP4 | 8.5 SP4 | 13.0 | — | — | 2.0 SP3 |
| Restricted To | CAN | CAN | CAN | — | — | CAN |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
