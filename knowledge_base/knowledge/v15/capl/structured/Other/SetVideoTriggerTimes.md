# SetVideoTriggerTimes

> Category: `Other` | Type: `function`

## Syntax

```c
SetVideoTriggerTimes(char windowName[], dword preTriggerTime, dword postTriggerTime);
```

## Description

Sets the trigger times for a CANoeVideo Window.

## Parameters

| Name | Description |
|---|---|
| windowName | The name of the Video Window. |
| preTriggerTime | The pre trigger time (in ms). For details see the pre trigger time in the CANoeVideo Configuration dialog. |
| postTriggerTime | The pre trigger time (in ms). For details see the pre trigger time in the CANoeVideo Configuration dialog. |

## Return Values

—

## Example

```c
// set trigger times for "VideoWindow"
SetVideoTriggerTimes("VideoWindow", 0, 2500);
```

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
