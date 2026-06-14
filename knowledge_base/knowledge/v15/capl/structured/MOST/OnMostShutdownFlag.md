# OnMostShutdownFlag

> Category: `MOST` | Type: `function`

## Syntax

```c
OnMostShutdownFlag(long oldstate, long newstate);
```

## Description

This event procedure is called each time the state of the Shutdown flag changes.

Within this event procedure the functions mostEventChannel, mostEventTime and mostEventOrigTime can be used to call up supplemental information.

## Parameters

| Name | Description |
|---|---|
| oldstate | Old state of the Shutdown Flag. |
| newstate | New state of the Shutdown Flag. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.1 SP4 | 7.1 SP4 | — | — | — | —✔ |
| Restricted To | MOST150 | MOST150 | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
