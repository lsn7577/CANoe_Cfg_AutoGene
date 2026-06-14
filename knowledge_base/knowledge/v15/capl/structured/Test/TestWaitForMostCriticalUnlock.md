# TestWaitForMostCriticalUnlock

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForMostCriticalUnlock(dword aTimeout);
```

## Description

The function waits until the expiration of the time aTimout for the occurrence of a LightLock event indicating "critical unlock" state.

A LightLock event with a "critical unlock" state is generated, when a single "Light & no Lock" state occurs after a "stable lock" state and lasts longer than tUnlock (see MOST specification), or several "light, no lock" states occur successively and add up to a duration longer than tUnlock.

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
