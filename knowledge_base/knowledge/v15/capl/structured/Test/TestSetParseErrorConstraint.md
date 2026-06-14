# TestSetParseErrorConstraint

> Category: `Test` | Type: `function`

## Syntax

```c
void TestSetParseErrorConstraint (long mode);
```

## Description

The function sets the behavior of the symbolic variants of TestWaitForMost... and TestJoinMost... functions on the occurrence of errors during the parsing of the message definitions.

Depending on whether the function is called within or outside of a test case, the setting either has an effect on only all subsequent TestWaitForMost... and TestJoinMost... function calls within the test case or generally on all subsequent calls. Therefore, the behavior specified within a test case loses its validity with the end of the test case and will be, if necessary, replaced by a previously externally-set behavior.

## Parameters

| Name | Description |
|---|---|
| 0 | The return value of the relevant function call indicates the problem that has occurred and a corresponding note is entered in the report. This is the pre-set default behavior. |
| 1 | The relevant test case is aborted and the verdict set to "fail". The aborting of the test case is noted with the error in the report. |
| 2 | Measurement will be stopped. The relevant test case is aborted and the verdict set to "fail". The aborting of the test case is noted with the error in the report. |

## Return Values

—

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.1 | 13.0 | — | — | — |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
