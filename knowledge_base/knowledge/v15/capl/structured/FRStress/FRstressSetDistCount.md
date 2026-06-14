# FRstressSetDistCount

> Category: `FRStress` | Type: `function`

## Syntax

```c
FRstressSetDistCount(long index, long disturbanceCount);
```

## Description

Modifies the specified frame element with bit accuracy. The disturbance is defined as a bit sequence. A complex disturbance can be configured through multiple calls.

The associated trigger condition must not overlap with the disturbance.

If the function is called in analog mode, it has no effect.

## Parameters

| Name | Description |
|---|---|
| index | Values: 1–4 |
| disturbanceCount | Values: 0–254, -1 = infinite |

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
