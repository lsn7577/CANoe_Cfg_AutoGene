# TestSetVerdictModule

> Category: `Test` | Type: `function`

## Syntax

```c
void TestSetVerdictModule (Verdict aVerdict);
```

## Description

This function sets the verdict of the test module. With this function the automatic verdict propagation of test cases to the test module can be influenced later.

E.g. this function can be used within the test controlling to conduct a test case "on probe" and to reset the verdict to "pass" in case "fail".

## Parameters

| Name | Description |
|---|---|
| 0 | pass |
| 1 | fail |
| 2 | none |
| 3 | inconclusive |
| 4 | error in test sytem |

## Return Values

—

## Example

See example: TestSetVerdictModule

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.0 | 13.0 | — | 14 | — |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
