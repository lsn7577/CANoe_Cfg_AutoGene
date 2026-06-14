# MediaProcessOutput

> Category: `Media` | Type: `function`

## Syntax

```c
long MediaProcessOutput(dword multiplexerHandle, dword outputStreamIndex, int64& retTimestamp, byte buffer[], dword& length, dword& retStatus)
```

## Description

Generates output from the current input data.

## Parameters

| Name | Description |
|---|---|
| multiplexerHandle | The multiplexer handle returned previously by a call to MediaCreateMultiplexer. |
| outputStreamIndex | The index of the output stream the media type should be retrieved for. For multiplexers set to 0. |
| retTimestamp | The (presentation) timestamp in nanoseconds returned from this function. This time is relative to the start of the stream (not the absolute gPTP time). |
| buffer | The sample data for the input stream that should be processed. |
| length | In/Out parameter. Set to elCount(buffer) before calling this function. After the return of the function it contains the length of the sample data in the buffer array in bytes. |
| retStatus | Before calling MediaProcessOutput, set this member to zero. When the method returns, the multiplexer might set additional status flags. Otherwise, the multiplexer leaves this member equal to zero. |

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
