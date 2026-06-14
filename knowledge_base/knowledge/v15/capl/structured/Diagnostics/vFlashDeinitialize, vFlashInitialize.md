# vFlashDeinitialize, vFlashInitialize

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void vFlashInitialize();
void vFlashDeinitialize();
```

## Description

Initializes (deinitializes) vFlash. Further API calls are only allowed after the CAPL callback vFlashInitializeCompleted (or vFlashDeinitializeCompleted) was called!

Note: This event-driven API is only needed outside of test modules or test units.

## Return Values

—

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.5 SP3 + DLL 2.7.3100 | — | — | — | 2.0 SP2 + DLL 2.7.3100 |
| Restricted To | — | Online mode | — | — | — | Online mode |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
