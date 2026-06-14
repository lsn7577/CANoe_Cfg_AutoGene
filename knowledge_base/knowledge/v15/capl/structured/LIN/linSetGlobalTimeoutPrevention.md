# linSetGlobalTimeoutPrevention

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linSetGlobalTimeoutPrevention(dword on);
```

## Description

Activates/deactivates the global timeout prevention for transceivers with a dominant timeout. If active, the cab/piggy will use an inbuilt transistor to keep the bus signal at a dominant level after the dominant timeout stopped the transceiver from transmitting a dominant signal.

## Parameters

| Name | Description |
|---|---|
| on | 0: Disable 1: Enable |

## Return Values

On success, a value unequal to zero, otherwise zero.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.5 | — | — | — | 1.0 |
| Restricted To | — | LIN Real bus mode | — | — | — | LIN Real bus mode |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
