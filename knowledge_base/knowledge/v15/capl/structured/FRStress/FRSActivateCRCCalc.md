# FRSActivateCRCCalc

> Category: `FRStress` | Type: `function`

## Syntax

```c
FRSActivateCRCCalc(long index, long calculateCRC);
```

## Description

Activates the automatic CRC computation based on the disturbance data (FRSSetDist, FRSSetDistElem, FRSSetDistPayload) and the real frame.

## Parameters

| Name | Description |
|---|---|
| index | Values: 1–4 |
| 0 | No calculation |
| 1 | Calculate header crc |
| 2 | Calculate frame crc |
| 3 | Calculate header and frame crc |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.2 | — | — | — | 1.1 |
| Restricted To | — | FlexRay Digital mode | — | — | — | FlexRay |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
