# ILConfigureNMNotifications

> Category: `CANoeIL` | Type: `function`

## Syntax

```c
dword ILConfigureNMNotifications (dword direction, dword mode);
```

## Description

The function allows manipulating the coupling between IL and NM module.

The function can be called at any time.

## Parameters

| Name | Description |
|---|---|
| direction | 0: IL->NM 1: NM -> IL Other values are reserved. |
| mode | 0: notifications are off 1: notifications are done always (regardless of existing callback functions) 2 and 3: notifications are done only in absence of certain callback functions (default) Other values are reserved. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 SP3 | 14 | 14 | — | — |
| Restricted To | — | CAN | CAN | CAN | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | — | N/A |
