# MediaEnumVideoCapturers

> Category: `Media` | Type: `function`

## Syntax

```c
dword MediaEnumVideoCapturers(dword[] retVideoCapturerHandles, dword &retCount);
```

## Description

Enumerates a list of video capture devices.

## Parameters

| Name | Description |
|---|---|
| retCount | Count of elements provided in videoCapturerHandles.Caller: Set to elCount(videoCapturerHandles). On successful return of the function this parameter contains the number of valid handles in the videoCapturerHandles array. |
| retVideoCapturerHandles | Array in which this function returns the video capturer handles of all video capture devices that are available. After its use the caller must release each audio capturer returned in the array by calling MediaReleaseVideoCapturer. |

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
