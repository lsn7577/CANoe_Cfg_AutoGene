# mostAllocTableGetCL

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostAllocTableGetCL(long channel, long idx);
```

## Description

Returns the connection label of the respective entry in the allocation table.

## Parameters

| Name | Description |
|---|---|
| channel | Application channel number. |
| idx | Index of the entry in the allocation table. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.1 SP4: form 1 7.2 SP3: form 1 | 7.1 SP4: form 1 7.2 SP3: form 1 | — | — | — | —✔ |
| Restricted To | MOST150 After measurement start Not in Stopmeasurement | MOST150 After measurement start Not in Stopmeasurement | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
