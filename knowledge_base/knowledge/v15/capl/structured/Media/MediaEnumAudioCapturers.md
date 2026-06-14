# MediaEnumAudioCapturers

> Category: `Media` | Type: `function`

## Syntax

```c
dword MediaEnumAudioCapturers(dword& count, dword audioCapturerHandles[]);
```

## Description

Enumerates a list of audio capture devices.

## Parameters

| Name | Description |
|---|---|
| count | Count of elements provided in audioCapturerHandles.Caller: Set to elCount(audioCapturerHandles). On successful return of the function this parameter contains the number of valid handles in the audioCapturerHandles array. |
| audioCapturerHandles | Array in which this function returns the audio capturer handles of all audio capture devices that are available. After its use the caller must release each audio capturer returned in the array by calling MediaReleaseAudioCapturer. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 10.0 | 13.0 | — | — | — |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | — |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | — |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | — |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | — |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | — |
| 32-Bit | — | ✔ | ✔ | N/A | — | — |
| 64-Bit | — | ✔ | ✔ | — | — | — |
