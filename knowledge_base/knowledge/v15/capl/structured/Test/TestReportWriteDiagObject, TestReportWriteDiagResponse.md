# TestReportWriteDiagObject, TestReportWriteDiagResponse

> Category: `Test` | Type: `function`

## Syntax

```c
TestReportWriteDiagObject (diagRequest req);
TestReportWriteDiagObject (diagResponse resp);
TestReportWriteDiagResponse (diagRequest req);
```

## Description

TestReportWriteDiagObject writes a test step with a textual interpretation of the specified request or response object into the test report.

TestReportWriteDiagResponse writes a test step with a textual interpretation of the received response for the specified request object into the test report.

These test steps are subject to the common test step report filtering as configured in the Test Module Configuration dialog.

## Parameters

| Name | Description |
|---|---|
| req | Request |
| resp | Response |

## Return Values

Error code

## Example

Using Diagnostics Functions in Test Cases

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.1 | — | — | — | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
