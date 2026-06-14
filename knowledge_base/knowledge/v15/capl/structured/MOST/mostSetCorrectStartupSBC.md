# mostSetCorrectStartupSBC

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostSetCorrectStartupSBC (long channel, long mode);
```

## Description

During the next start-up phase of the ring, this function activates or deactivates the correct setting of the "Synchronous Bandwidth Control" register (SBC) in the MOST chip (e.g. at the next wake-up of the ring).

## Parameters

| Name | Description |
|---|---|
| channel | Channel of the connected MOST interface. |
| 0 | inactive |
| 1 | active |

## Return Values

—

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.0 SP2 | 7.0 SP2 | — | — | — | —✔ |
| Restricted To | MOST25 | MOST25 | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
