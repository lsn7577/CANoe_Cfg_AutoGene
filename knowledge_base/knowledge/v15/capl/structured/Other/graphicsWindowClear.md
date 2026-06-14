# graphicsWindowClear

> Category: `Other` | Type: `function`

## Syntax

```c
void graphicsWindowClear (char[] windowName);
```

## Description

Temporarily deletes the contents of the CANoeGraphics Window. E.g. with TestReportAddWindowCapture a screenshot is created that contains only the data of a certain period of time.

## Parameters

| Name | Description |
|---|---|
| windowName | The name of the Graphics Window. |

## Return Values

—

## Example

```c
//Clear the Graphics Window to show only data from this test case
graphicsWindowClear("Graphics");
testWaitForTimeout(2000);

//Fit all signal values
graphicsWindowFit("Graphics", 1);

//Take a capture of the window and add it to the test report
TestReportAddWindowCapture("Graphics", "", "Screenshot of Graphic window");
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 10.0 SP3 | 10.0 SP3 | 13.0 | — | 14 | 2.2 SP2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | ✔ | N/A |
