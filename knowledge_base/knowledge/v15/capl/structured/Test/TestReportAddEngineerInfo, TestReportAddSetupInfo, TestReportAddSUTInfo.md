# TestReportAddEngineerInfo, TestReportAddSetupInfo, TestReportAddSUTInfo

> Category: `Test` | Type: `function`

## Syntax

```c
TestReportAddEngineerInfo (char name[], char description[], ...);
TestReportAddSetupInfo (char name[], char description[], ...);
TestReportAddSUTInfo (char name[], char description[], ...);
```

## Description

With these functions, information pairs of name and description (e.g. "serial number" and "S012345AB") can be taken up into the report in the areas TestEngineer, TestSetUp, and device (SUT) to be tested. The three areas named must not be created; they are automatically available in the report. In the course of the test execution, any number of information pairs can be written.

## Parameters

| Name | Description |
|---|---|
| name | Information pair of name and description. |
| description | Information pair of name and description. |

## Return Values

—

## Example

See example: TestReportAdd* Functions

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.0 | 13.0 | — | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
