# FRSSetScopeMode

> Category: `FRStress` | Type: `function`

## Syntax

```c
long FRSSetScopeMode( float baudrate, long channel, long payloadLength);
```

## Description

Activates the Scope mode of FRstress.

Configuration functions that belong to another operating mode are ignored.

## Parameters

| Name | Description |
|---|---|
| baudrate | Values: 10, 5, 2.5, 1.25 Mbit/s |
| 1 | A |
| 2 | B |
| payloadLength | Values: 0–254 Bytes |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.2 | — | — | — | 1.1 |
| Restricted To | — | FlexRay Digital, analog, Scope mode | — | — | — | FlexRay |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
