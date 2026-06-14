# TestReportAddMiscInfoBlock

> Category: `Test` | Type: `function`

## Syntax

```c
TestReportAddMiscInfoBlock (char title[]);
```

## Description

The function generates a new information block for additional information pairs in the report. With the function TestReportAddMiscInfo information pairs can be taken up into this block. This is possible until a new information block is opened with TestReportAddMiscInfoBlock, the current test case is ended (if the information block was opened within the test case) or a test case is called (if the information block was called in the test module).

## Parameters

| Name | Description |
|---|---|
| title | Title of the information block. |

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
