# TestGetWaitFrNullFrameData

> Category: `Test` | Type: `function`

## Syntax

```c
long TestGetWaitFrNullFrameData (frNullFrame aNullFrame);
long TestGetWaitFrNullFrameData (dword index, frNullFrame aNullFrame);
```

## Description

If a FlexRay Null Frame is the last event that triggers a wait instruction, the frame’s content can be called up with the first function.

The second function can only be used for "joined events". The number of the "joined event" (return value of "testJoin...") is here being used as an index.

## Parameters

| Name | Description |
|---|---|
| aNullFrame | Null Frame variable that should be filled in with this function. |
| Index | Number of the "joined event" corresponds with the return value of "testJoin...". |

## Example

For an example see function TestWaitForFrFrame and replace all FrFrame by FrNullFrame.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.0 SP4 | 13.0 | — | — | 1.0 |
| Restricted To | — | FlexRay | FlexRay | — | — | FlexRay |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
