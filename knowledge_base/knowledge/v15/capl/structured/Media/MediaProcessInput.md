# MediaProcessInput

> Category: `Media` | Type: `function`

## Syntax

```c
long MediaProcessInput(dword multiplexerHandle, dword inputStreamIndex, int64 timestamp, byte buffer[], dword length)
```

## Description

Delivers data to an input stream on this multiplexer.

## Parameters

| Name | Description |
|---|---|
| multiplexerHandle | The multiplexer handle returned previously by a call to MediaCreateMultiplexer. |
| inputStreamIndex | The index of the input stream the media type should be set for. Currently only 1 input stream per multiplex stream is supported, so set this parameter to 0. |
| timestamp | The (presentation) timestamp in nanoseconds. This time is relative to the start of the stream (not the absolute gPTP time). |
| buffer | The sample data for the input stream that should be processed. |
| length | The length of the sample data in the buffer array in bytes. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 13.0 | 13.0 | — | — | — |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | — |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | — |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | — |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | — |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | — |
| 32-Bit | — | ✔ | ✔ | N/A | — | — |
| 64-Bit | — | ✔ | ✔ | — | — | — |
