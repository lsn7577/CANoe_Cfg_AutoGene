# SetVideoOfflineSource

> Category: `Other` | Type: `function`

## Syntax

```c
SetVideoOfflineSource(char windowName[], long sourceType, char sourcePath[]);
```

## Description

Sets the offline source (type and path) for a CANoeVideo Window.

## Parameters

| Name | Description |
|---|---|
| windowName | The name of the Video Window. |
| sourceType | The type of offline source: 0\|cNoVideoInput 1\|cVideoFile 2\|cImageFolder For details see the Offline Source in the CANoeVideo Configuration dialog. |
| sourcePath | The corresponding source path: For cNoVideoInput the path will be ignored. For cVideoFile this must be a existing video file. For cImageFolder this must be a existing folder. |

## Return Values

—

## Example

```c
on preStart
{
  //Configure offline source (video file)
  SetVideoOfflineSource("Video Window", 1, "MyVideoFile.avi");
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 10.0 SP3 | 13.0 | — | 14 | 2.2 SP2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | — | — | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
