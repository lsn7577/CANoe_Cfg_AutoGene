# MediaRead

> Category: `Media` | Type: `function`

## Syntax

```c
long MediaRead(dword sourceReaderHandle, dword streamIndex, byte buffer[], dword length, char onReadCallback[]);
long MediaRead(dword sourceReaderHandle, dword streamIndex, int buffer[], dword length, char onReadCallback[]);
long MediaRead(dword sourceReaderHandle, dword streamIndex, long buffer[], dword length, char onReadCallback[]);
```

## Description

Reads sample data from the media source.

## Parameters

| Name | Description |
|---|---|
| sourceReaderHandle | The source reader handle. |
| Name | Description |
| 0–0xFFFFFFFB | The zero-based index of a stream. |
| SOURCE_READER_FIRST_VIDEO_STREAM 0xFFFFFFFC | The first video stream. |
| SOURCE_READER_FIRST_AUDIO_STREAM 0xFFFFFFFD | The first audio stream. |
| SOURCE_READER_ANY_STREAM 0xFFFFFFFE | Get the next available sample, regardless of which stream. |
| buffer | The buffer used to store the incoming data. |
| length | The length of the data buffer. |
| onReadCallback | The name of the CAPL callback function (see OnMediaRead). |

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
