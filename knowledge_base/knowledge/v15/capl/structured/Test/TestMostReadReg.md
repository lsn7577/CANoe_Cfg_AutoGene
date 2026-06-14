# TestMostReadReg

> Category: `Test` | Type: `function`

## Syntax

```c
long TestMostReadReg(long aChannel, long aChip, dword aOffset, dword aRegDataLen, unsigned long aTimeout);
```

## Description

Reads one or several chip registers in the MOST hardware and waits for the result. If the operation is successful, the written register values can be read out using TestMostRegGetData.

## Parameters

| Name | Description |
|---|---|
| aChannel | Channel connected to the hardware. |
| aChip | MOST hardware chip ID. Possible values are: 1 : OS814 (other chips cannot be accessed as of yet) |
| aOffset | First register address. |
| aRegDataLen | Number of registers to be read. Values between 1 and 16 are possible. |
| aTimeout | Maximum time that should be waited [ms] (Transmission of 0: no timeout monitoring; test module waits infinitely long) |

## Return Values

Resume based on occurred event

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.2 | — | — | — | — |
| Restricted To | — | MOST25 | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
