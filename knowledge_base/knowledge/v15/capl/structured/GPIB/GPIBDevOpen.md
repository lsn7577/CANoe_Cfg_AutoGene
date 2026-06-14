# GPIBDevOpen

> Category: `GPIB` | Type: `function`

## Syntax

```c
long GPIBDevOpen (long boardIdx, long primAddr, long secAddr, long timeout, long eot, long eos);
```

## Description

Opens a GPIB device and returns a device ID.

## Parameters

| Name | Description |
|---|---|
| boardIdx | Index of the GPIB board (e.g.0) |
| primAddr | Primary address of the GPIB device (0..30) |
| secAddr | Secondary address of the GPIB device (96..126, typical: 0) |
| 0 | Timeout disabled. Do not use! |
| 1 | Timeout = 10 us |
| 2 | Timeout = 30 us |
| 3 | Timeout = 100 us |
| 4 | Timeout = 300 us |
| 5 | Timeout = 1 ms |
| 6 | Timeout = 3 ms |
| 7 | Timeout = 10 ms |
| 8 | Timeout = 30 ms |
| 9 | Timeout = 100 ms |
| 10 | Timeout = 300 ms |
| 11 | Timeout = 1 s |
| 12 | Timeout = 3 s |
| 13 | Timeout = 10 s |
| 14 | Timeout = 30 s |
| 15 | Timeout = 100 s |
| 16 | Timeout = 300 s |
| 17 | Timeout = 1000 s |
| eot | Indicates whether the GPIB EOI line should be set at the end of a write operation. Values: 0, 1 (typical: 1) |
| eos | Configuration of "end-of-string" behavior. For further information please refer to documentation for your GPIB controller. Typical value: 0 |

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
