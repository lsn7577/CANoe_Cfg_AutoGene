# graphicsWindowFit

> Category: `Other` | Type: `function`

## Syntax

```c
void graphicsWindowFit(char[] windowName, byte mode);
```

## Description

Scales symbols in a CANoe Graphics Window.

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

| Since Version |
|---|
