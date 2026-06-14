# OnMediaRead

> Category: `Media` | Type: `function`

## Syntax

```c
void OnMediaRead(dword sourceReaderHandle, long result, dword streamIndex, dword streamFlags, int64 timestamp, byte buffer[], dword length);
void OnMediaRead(dword sourceReaderHandle, long result, dword streamIndex, dword streamFlags, int64 timestamp, int buffer[], dword length);
void OnMediaRead(dword sourceReaderHandle, long result, dword streamIndex, dword streamFlags, int64 timestamp, long buffer[], dword length);
```

## Description

This callback is dispatched when an asynchronous read operation on a source reader completes.

## Parameters

| Name | Description |
|---|---|
| sourceReaderHandle | The source reader handle. |
| result | The specific result code of the operation. If the operation completed success-fully the value is zero. Otherwise the value is non-zero. |
| streamIndex | The zero-based index of the stream that delivered the sample. |
| Value | Description |
| SOURCE_READERF_ERROR0x00000001 | An error occurred. If you receive this flag, do not make any further calls to SourceReader methods. |
| SOURCE_READERF_ENDOFSTREAM0x00000002 | The source reader reached the end of the stream. |
| SOURCE_READERF_NEWSTREAM0x00000004 | One or more new streams were created. Respond to this flag by doing at least one of the following: Set the output types on the new streams. Update the stream selection by selecting or deselecting streams. |
| SOURCE_READERF_NATIVEMEDIATYPECHANGED0x00000010 | The native format has changed for one or more streams. The native format is the format delivered by the media source before any decoders are inserted. |
| SOURCE_READERF_CURRENTMEDIATYPECHANGED0x00000020 | The current media has type changed for one or more streams. To get the current media type, call the source reader’s GetMediaType method. |
| MF_SOURCE_READERF_STREAMTICK0x00000100 | There is a gap in the stream. |
| SOURCE_READERF_ALLEFFECTSREMOVED0x00000200 | All transforms inserted by the application have been removed for a particular stream. This could be due to a dynamic format change from a source or decoder that prevents custom transforms from being used because they cannot handle the new media type. |
| buffer | The buffer into which the data was stored. |
| length | The length of the received data. |

## Return Values

—

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
