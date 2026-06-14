# TestWaitForMostStableLock

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForMostStableLock(dword aTimeout);
```

## Description

The function waits until the expiration of the time aTimout for the occurrence of a LightLock event indicating "stable lock" state.

A LightLock event with a "stable lock" state is generated, when a "light & Lock" state lasts uninterrupted at the hardware for a period of time equal or longer than tLock (see MOST specification).

## Parameters

| Name | Description |
|---|---|
| aTimeout | Maximum wait time [ms] (Specification of 0: no timeout controlling) |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.0 | — | — | — | — |
| Restricted To | — | MOST25, MOST50, MOST150 | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
