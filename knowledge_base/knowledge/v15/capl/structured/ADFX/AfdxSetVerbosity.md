# AfdxSetVerbosity

> Category: `ADFX` | Type: `function`

## Syntax

```c
long AfdxSetVerbosity( long verbosity );
```

## Description

This function sets the verbosity level of the AFDX IL.

The default setting is that only error messages are written to the Write Window of CANoe.

## Parameters

| Name | Description |
|---|---|
| verbosity | verbosity level 0: do not write messages to the Write Window 1: write only error messages (default) 2: write warning and error messages 3: write information, warning and error messages |

## Example

```c
// do not print AFDX IL messages to Write Window
AfdxSetVerbosity( 0 );
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0 | — | — | — | — |
| Restricted To | — | AFDX | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
