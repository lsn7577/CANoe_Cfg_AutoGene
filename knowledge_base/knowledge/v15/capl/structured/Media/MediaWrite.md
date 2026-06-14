# MediaWrite

> Category: `Media` | Type: `function`

## Syntax

```c
long MediaWrite(dword sinkWriterHandle, dword streamIndex, int64 timestamp, byte buffer[], dword length);
long MediaWrite(dword sinkWriterHandle, dword streamIndex, int64 timestamp, int buffer[], dword length);
long MediaWrite(dword sinkWriterHandle, dword streamIndex, int64 timestamp, long buffer[], dword length);
```

## Description

Delivers sample data to the sink writer. The buffer can be reused immediately after the function returns.

## Parameters

| Name | Description |
|---|---|
| sinkWriterHandle | The sink writer handle. |
| streamIndex | The zero-based index of the stream. |
| buffer | The buffer used to store the sample data. |
| length | The length of the data buffer. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.5 | 13.0 | — | — | — |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | — |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | — |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | — |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | — |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | — |
| 32-Bit | — | ✔ | ✔ | N/A | — | — |
| 64-Bit | — | ✔ | ✔ | — | — | — |
