# SetVideoRecordFile

> Category: `Other` | Type: `function`

## Syntax

```c
SetVideoRecordFile(char windowName[], char recordFile[]);
```

## Description

Sets the record file for a CANoeVideo Window.

## Parameters

| Name | Description |
|---|---|
| windowName | The name of the Video Window. |
| Note If a valid path is provided the recorder will automatically be activated, even if it is deactivated in the CANoeVideo Configuration dialog. If an empty string (" ") is provided as path, the recorder will automatically be deactivated, even if it is activated in the CANoeVideo Configuration dialog. Within a string literal a second backslash has to be set (see example betow). |  |

## Return Values

—

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.5 SP4 | 13.0 | — | 14 | 2.0 SP3 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | — | — | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
