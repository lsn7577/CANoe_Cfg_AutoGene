# CANstressWaitForIdle

> Category: `CANstress` | Type: `function`

## Syntax

```c
long CANstressWaitForIdle( dword timeout );
```

## Description

Waits until the CANstress hardware is in the state Idle.

## Parameters

| Name | Description |
|---|---|
| Note With timeout = 0 an infinite time is waited until the state Idle occurs. Thus the additional test procedure is blocked if the state Idle is not reached. |  |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.0 | — | — | — | 1.1 |
| Restricted To | — | CAN CANstress | — | — | — | CAN CANstress |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
