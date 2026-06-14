# TestJoinMostAMSReportEvent

> Category: `Test` | Type: `function`

## Syntax

```c
long TestJoinMostAMSReportEvent (int aFBlockId, int aInstanceId, int aFunctionId)
long TestJoinMostAMSReportEvent (char[] aSymbolicMessage, int aInstanceId)
long TestJoinMostAMSReportEvent (char[] aSymbolicMessage)
```

## Description

Completes the current set of "joined events" with the transmitted event, a MOST AMS response message (Report, OpType > 8). This function does not wait.

## Parameters

| Name | Description |
|---|---|
| Note For parameters aFBlockId, aInstanceId and aFunctionId the following applies: If -1 is given, the corresponding field can get any value. This is also the standard for not explicit set values. |  |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.0 | — | — | — | — |
| Restricted To | — | MOST25, MOST50, MOST150 | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
