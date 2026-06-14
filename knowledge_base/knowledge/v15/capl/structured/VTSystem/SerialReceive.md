# SerialReceive

> Category: `VTSystem` | Type: `method`

## Syntax

```c
long SysVarNamespace.SerialReceive( byte buffer[], dword size);
```

## Description

Starts receiving blocks of bytes from the serial port of the specified VT7001 channel. Received data is copied to the specified buffer. The data can only be accessed in the OnSerialReceive callback.

The used serial port has to be opened first.

## Parameters

| Name | Description |
|---|---|
| buffer | An array of bytes where received data is copied to. The buffer is only valid within the OnSerialReceive callback. |
| number | Maximum number of Bytes which can be received at a time. Must have a value > 0 and < 65. |

## Example

See example SerialConfigure

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.2 SP3 | 13.0 | — | — | 1.0 |
| Restricted To | — | — | VT offline | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
