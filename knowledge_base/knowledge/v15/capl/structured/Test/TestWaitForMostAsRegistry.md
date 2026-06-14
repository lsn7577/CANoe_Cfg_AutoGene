# TestWaitForMostAsRegistry

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForMostAsRegistry(long aRegistry, unsigned long aTimeout);
```

## Description

The function waits for the specified time period for any change to a registry in the application socket.

## Parameters

| Name | Description |
|---|---|
| 1 | Wait for changes in the local registry |
| 2 | Wait for changes in the global registry |
| -1 | Wait for changes in all registries |
| aTimeout | Maximum time that should be waited [ms] (Transmission of 0: no timeout monitoring; test module waits infinitely long) |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.2 | — | — | — | — |
| Restricted To | — | MOST | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
