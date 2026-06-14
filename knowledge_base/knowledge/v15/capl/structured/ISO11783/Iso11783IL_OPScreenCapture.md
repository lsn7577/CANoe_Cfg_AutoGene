# Iso11783IL_OPScreenCapture

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPScreenCapture( dword itemRequested, dword path ); // form 1
long Iso11783IL_OPScreenCapture( dbNode implement, dword itemRequested, dword path ); // form 2
```

## Description

Sends a Screen Capture command to the Virtual Terminal to request a screen capture of the current screen image.

## Parameters

| Name | Description |
|---|---|
| implement | Simulation node to apply the function. |
| itemRequested | Requested item 0: Screen Image 240-255: Manufacturer Proprietary |
| path | Path of the request 1: VT accessible storage/removable media 240-255: Manufacturer Proprietary |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 14 | 13.0 | — | — | 5.0 SP3 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 2 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
