# diagGetTesterPresentState

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
diagGetTesterPresentState(char ecuQualifier[])
diagGetTesterPresentState()
```

## Description

Returns the state of autonomous/cyclical Tester Present requests from CANoe to the specified or current ECU.

Status:

0: sending Tester Present disabled for target ECU1: sending Tester Present enabled for target ECU

## Parameters

| Name | Description |
|---|---|
| ecuQualifier | Qualifier of the ECU as specified in the diagnostic configuration dialog, for which the Tester Present state shall be queried. If no parameter is provided, the state of the current diagnostic target (set by diagSetTarget(char ecuQualifier[]) is returned. |

## Return Values

Error code or status

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.5 SP2 | 7.0 | — | — | — | 1.0 |
| Restricted To | Online mode | Online mode | — | — | — | Online mode |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
