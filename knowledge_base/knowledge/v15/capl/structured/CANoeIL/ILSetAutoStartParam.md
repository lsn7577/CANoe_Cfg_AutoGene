# ILSetAutoStartParam

> Category: `CANoeIL` | Type: `function`

## Syntax

```c
long ILSetAutoStartParam(dword autoStartParam)
```

## Description

Defines the behavior of the interaction layer at measurement start.

If used at all, the function must be called within the on preStart event handler of a CAPL program.

## Parameters

| Name | Description |
|---|---|
| Note The default behavior (i.e. when ILSetAutoStartParam is omitted) is analogous to ILSetAutoStartParam(2). |  |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.1 | 14 | 14 | — | — |
| Restricted To | — | CAN | CAN | CAN | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | — | N/A |
