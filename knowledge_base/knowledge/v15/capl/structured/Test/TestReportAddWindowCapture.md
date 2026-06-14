# TestReportAddWindowCapture

> Category: `Test` | Type: `function`

## Syntax

```c
TestReportAddWindowCapture(char[] window, char[] data, char[] title, char[] file); //form 1: deprecated
TestReportAddWindowCapture(char[] window, char[] data, char[] title); // form 2
```

## Description

Creates a screen capture of CANoe window and panels.

Can only be used within test cases (test case function).

The test case verdict is not affected. Errors that occur during window capture are logged in the report as warnings, but do not affect the test case verdict.

The test case verdict is not affected. Window capture is not allowed in CANoestandalone mode. Errors on creating the window capture are reported as a warning in the test report.

## Parameters

| Name | Description |
|---|---|
| window | Name of the window to be captured. |
| data (optional, otherwise "") | Additional CANoewindow specific parameter (see example 2). |
| title | Text heading that precedes the captured window image in the test report. |
| Note The parameter file should not be used because in combination with the function testReportFileName or with the test reporting field codes it may produce path collisions or undefined behavior. Without usage of file parameter, the capture files will be created and managed automatically. |  |

## Return Values

—

## Example

Example 1

Example 2

```c
testcase tc_1_1()
{
   TestCaseTitle("tc_1_1",  "Test Case  1.1");
   TestReportAddWindowCapture("Trace - Report", "",  
                              "Trace  before execution of test case:",  
                              "tc-1.1-trace-before");

      ...  execute Test Pattern(s) ...

      if  (TestGetVerdictLastTestCase() != 0) {
          TestReportAddWindowCapture("Trace - Report", "",  
                                     "Testfall  failed. Trace am  Ende:",
                                     "tc-1.1-trace-after");
   }
}
TestReportAddWindowCapture("Graphics", "ABSdata::CarSpeed;Gear", "Screenshot of Graphic window");
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.1: form 1 9.0: form 2, form 1 deprecated | 13.0 | — | 14 | 1.0: form 1 2.1: form 2, form 1 deprecated |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
