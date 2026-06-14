# TestGroupBegin

> Category: `Test` | Type: `function`

## Syntax

```c
TestGroupBegin (char title[], char description[]); // form 1
TestGroupBegin (char ident[], char title[], char description[]); // form 2
```

## Description

A test group is opened with this function. It may only be called in a test module, but not in a test case. All test cases and test groups that are executed before call of the corresponding function TestGroupEnd are part of this test group. If a test group is not closed with TestGroupEnd, then at the end of the test module, a warning is written in the Write Window and the test group is closed automatically.

To obtain line breaks (in form of <br /> tags) in the test report, "\n" may be inserted at any place.

## Parameters

| Name | Description |
|---|---|
| ident | E.g. a test group number) of the test group. |
| title | Title for the test group. |
| description | Description text for the test group. |

## Return Values

—

## Example

See example: TestGroupBegin, TestGroupEnd

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.0: form 1 7.0 SP4: form 2 | 13.0 | — | 14 | — |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
