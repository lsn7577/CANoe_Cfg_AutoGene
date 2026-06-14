# graphicsWindowClear

> Category: `Other` | Type: `function`

## Syntax

```c
void graphicsWindowClear (char[] windowName);
```

## Description

Temporarily deletes the contents of the CANoe Graphics Window. E.g. with TestReportAddWindowCapture a screenshot is created that contains only the data of a certain period of time.

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
