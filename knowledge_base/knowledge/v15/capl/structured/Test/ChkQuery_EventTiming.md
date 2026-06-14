# ChkQuery_EventTiming

> Category: `Test` | Type: `function`

## Syntax

```c
float ChkQuery_EventTiming (dword checkId);
```

## Description

Retrieves the timing value that has been violated in the LIN specific check.

## Parameters

| Name | Description |
|---|---|
| checkId | Identifier of the queried Check. |

## Example

```c
testcase tcTSL_LINSyncBreak()
{
   dword checkId;
   float lastMeasuredSyncBreakLength;

   checkId = ChkStart_LINSyncBreakTimingViolation (18, 20);
   testWaitForTimeout(5000);
   ChkControl_Stop(checkId);

   lastMeasuredSyncBreakLength = ChkQuery_EventTiming(checkId);
   testStep("Evaluation", "Last measured sync break length is %.2f bits", lastMeasuredSyncBreakLength);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.2 7.0 SP5: method | 13.0 | — | 14 | 1.0 |
| Restricted To | — | LIN | LIN | — | LIN | LIN |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
