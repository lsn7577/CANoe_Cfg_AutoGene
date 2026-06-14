# TestReportAddMiscInfo

> Category: `Test` | Type: `function`

## Syntax

```c
TestReportAddMiscInfo (char name[], char description[], ...);
```

## Description

With these functions, information pairs of name and description (e.g. "parameter value V0" and "3.7 V") can be taken up into an additional information area in the report. The additional information area must be created previously with TestReportAddMiscInfoBlock. If this function is used and there is no corresponding information area, then a warning will be generated in the Write Window and a new information area will be created automatically. In this information area, any number of information pairs can be written with this function.

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
