# TestReportAddWindowCapture

> Category: `Test` | Type: `function`

## Syntax

```c
TestReportAddWindowCapture(char[] window, char[] data, char[] title, char[] file); //form 1: deprecated
```

## Description

Creates a screen capture of CANoe window and panels.

Can only be used within test cases (test case function).

The test case verdict is not affected. Errors that occur during window capture are logged in the report as warnings, but do not affect the test case verdict.

The test case verdict is not affected. Window capture is not allowed in CANoe standalone mode. Errors on creating the window capture are reported as a warning in the test report.

## Return Values

—

## Example

```c
TestReportAddWindowCapture("Graphics", "ABSdata::CarSpeed;Gear", "Screenshot of Graphic window");
```

## Availability

| Since Version |
|---|
