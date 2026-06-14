# OnMostSyncSpdif

> Category: `MOST` | Type: `function`

## Syntax

```c
OnMostSyncSpdif(long label, long device, long mode);
```

## Description

The event procedure OnMostSyncSpdif will be called after routing of S/PDIF input or output of the bus interface (see mostSetSyncSpdif).

## Parameters

| Name | Description |
|---|---|
| label | Connection label. |
| device | 0: S/PDIF-In: Audio input signals are put on synchronous channels. 1: S/PDIF-Out: Synchronous channel signals are grabbed for audio output. |
| mode | 0: Routing cancelled. 1: Routing executed. |

## Return Values

—

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.1 SP4 | 7.1 SP4 | — | — | — | —✔ |
| Restricted To | MOST25 MOST150 | MOST25 MOST150 | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
