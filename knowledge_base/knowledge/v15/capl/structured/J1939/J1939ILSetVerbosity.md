# J1939ILSetVerbosity

> Category: `J1939` | Type: `function`

## Syntax

```c
dword J1939ILSetVerbosity( dword verbosityLevel); // form 1
dword J1939ILSetVerbosity( dbNode fs, dword verbosityLevel); // form 2
```

## Description

Sets verbosity for writing in Write Window.

## Parameters

| Name | Description |
|---|---|
| verbosityLevel | 0: do not write messages to the Write Window 1: write only error messages 2: write warning and error messages (default) 3: write information, warning and error messages |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 12.0 SP3 | 13.0 | — | — | 4.0 SP3 |
| Restricted To | — | J1939 | J1939 | — | — | form 2 J1939 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
