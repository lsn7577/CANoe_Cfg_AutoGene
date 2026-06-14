# FRSSetTrigOutput

> Category: `FRStress` | Type: `function`

## Syntax

```c
FRSSetTrigOutput(long triggermask, long triggerlevel);
```

## Description

Activates the trigger output of FRstress. The trigger output can react to individual trigger lowerings or to a combination of sources.

## Parameters

| Name | Description |
|---|---|
| 1 | Trigger1 |
| 2 | Trigger2 |
| 4 | Trigger3 |
| 8 | Trigger4 |
| 16 | SW Trigger |
| 32 | External Trigger |
| 0 | Low |
| 1 | High |

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
