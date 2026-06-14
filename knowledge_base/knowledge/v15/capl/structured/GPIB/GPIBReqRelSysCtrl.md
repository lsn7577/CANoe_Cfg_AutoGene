# GPIBReqRelSysCtrl

> Category: `GPIB` | Type: `function`

## Syntax

```c
long GPIBReqRelSysCtrl (long boardIdx, long mode);
```

## Description

Sets or deletes the permission to send interface clear (IFC) or remote enable (REN). If mode is "0," the GPIB board surrenders system control and all controller-specific commands are not allowed. If mode = "1," then controller-specific commands are allowed.

## Parameters

| Name | Description |
|---|---|
| boardIdx | GPIB Board ID |
| mode | (0..1) |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.0 | — | — | — | 1.1 SP2 |
| Restricted To | — | GPIB | — | — | — | GPIB |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
