# mostReadReg

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostReadReg(long channel, long chip, dword offset, long regdatalen);
```

## Description

Initiates read-out of the registers of a MOST hardware chip.

## Parameters

| Name | Description |
|---|---|
| channel | Channel to which the hardware is connected. |
| chip | Number of the chip in the MOST hardware (1 = OS8104; other chips cannot be accessed yet). |
| offset | Address of the first register. |
| regdatalen | Number of registers to be read (1 <= regdatalen <= 16). |

## Return Values

See error codes
A read request by mostReadReg() causes the CAPL event procedure OnMostReg to be called.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.0 | 5.0 | — | — | — | —✔ |
| Restricted To | MOST25 After measurement start Not in Stopmeasurement | MOST25 After measurement start Not in Stopmeasurement | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
