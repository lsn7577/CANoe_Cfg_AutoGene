# mostWriteReg

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostWriteReg(long channel, long chip, dword offset, long regdatalen, byte regdata[]);
```

## Description

Writes to one or more registers of a MOST hardware chip.

## Parameters

| Name | Description |
|---|---|
| channel | Channel to which the hardware is connected |
| chip | Number of the MOST hardware chip (1 = OS8104; other chips cannot be accessed yet) |
| offset | Address of the first register |
| regdatalen | Number of registers to be written (maximum 16) |
| regdata[] | A byte buffer at least regdatalen in size with the data to be written |

## Return Values

See error codes

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.0 | 5.0 | — | — | — | —✔ |
| Restricted To | MOST25 After measurement start Not in StopMeasurement | MOST25 After measurement start Not in StopMeasurement | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
