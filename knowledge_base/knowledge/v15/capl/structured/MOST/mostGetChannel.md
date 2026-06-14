# mostGetChannel

> Category: `MOST` | Type: `function`

## Syntax

```c
mostGetChannel ();
```

## Description

This query returns the number of the MOST channel to which the CAPL node is connected in the Simulation Setup.

This query is especially useful with nodes that are only connected to one MOST channel in the Simulation Setup. The return value can be used directly as a parameter for all CAPL functions that expect specification of a channel, e.g. in driving the hardware interface.

With the help of this function CAPL programs can be created such that they are independent of channel numbers. By proper configuration of the Simulation Setup the user can choose the MOST interface over which the node should be operated.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.0 | — | — | — | —✔ |
| Restricted To | — | MOST25 MOST50 MOST150 | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | — | ✔ | — | N/A | — | —✔ |
| 64-Bit | — | ✔ | — | — | — | —✔ |
