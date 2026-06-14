# ILSetSignalRawField

> Category: `CANoeIL` | Type: `function`

## Syntax

```c
long ILSetSignalRawField (dbSignal sig, const char *pData, long aDataLen)
```

## Description

Sets the transferred signal to the provided value.

Use for integer signals > 32 bit.

## Parameters

| Name | Description |
|---|---|
| sig | Signal that should be set. Specify as follows 'Message::Signal'. |
| pData | Byte array, which contains the raw data. |
| aDataLen | Length of the byte array. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.1 | 14 | 14 | — | — |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | — | N/A |
