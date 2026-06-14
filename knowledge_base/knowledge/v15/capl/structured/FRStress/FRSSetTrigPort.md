# FRSSetTrigPort

> Category: `FRStress` | Type: `function`

## Syntax

```c
long FRSSetTrigPort(long triggerCondition, long portMask);
```

## Description

Adds a bit sequence to the respective trigger condition as a trigger value. A complex trigger condition can be created through multiple calls.

## Parameters

| Name | Description |
|---|---|
| triggerCondition | Values: 1–4 |
| 3 | Both ports |
| 1 | Port A (Channel1) |
| 2 | Port B (Channel2) |

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
