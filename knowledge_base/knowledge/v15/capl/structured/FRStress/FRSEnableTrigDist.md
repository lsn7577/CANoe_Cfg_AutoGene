# FRSEnableTrigDist

> Category: `FRStress` | Type: `function`

## Syntax

```c
long FRSEnableTrigDist(long triggerCondition, long iEnable);
```

## Description

Activates a trigger/disturbance page of FRstress. This function can be called out of a measurement session.

## Parameters

| Name | Description |
|---|---|
| triggerCondition | Values: 1–4 |
| 0 | Enable |
| 1 | Disable |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.0 | — | — | — | 1.1 |
| Restricted To | — | FlexRay | — | — | — | FlexRay |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
