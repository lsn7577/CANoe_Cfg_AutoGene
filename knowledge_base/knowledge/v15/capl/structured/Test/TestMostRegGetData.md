# TestMostRegGetData

> Category: `Test` | Type: `function`

## Syntax

```c
long TestMostRegGetData(BYTE aBuffer[], long aBufferSize);
```

## Description

The TestMostRegGetData() function is used together with the TestMostReadReg and TestMostWriteReg functions.

After initiating one of these two functions, the resulting register value can be copied into a byte buffer. Ensure that the buffer size is as specified. A maximum of 16 bytes are transported with the MostReg result.

Note that the register values are only held ready for call-up until the next wait condition in the test program.

## Parameters

| Name | Description |
|---|---|
| aBuffer[] | Data buffer in which the register values are written |
| aBufferSize | Size of the given data buffer (max. 16 bytes) |

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
