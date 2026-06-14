# TestAddConstraint

> Category: `Test` | Type: `function`

## Syntax

```c
long TestAddConstraint (dword aAuxHandle);
long TestAddConstraint (dword aAuxHandle, long aBehavior);
long TestAddConstraint (char aEventText[]);
long TestAddConstraint (char aEventText[], long aBehavior);
```

## Description

Adds an event object or an event text as a constraint. Checks from the Test Service Library are suitable as event objects.

This function can be used within a test case and also on the main test level.

## Parameters

| Name | Description |
|---|---|
| aAuxHandle | Event object, for example a check from the TestService Library. Specified is the handle that is returned when a check is created. |
| aEventText | Textual name of an event whose occurrence should be monitored. This event can be triggered with the function TestSupplyTextEvent. |
| 0 | Default behavior, entry in test report and setting of the verdict to "fail" |
| 1 | Only an entry in the test report is made, the verdict remains unchanged |
| 2, 3 | reserved |
| 4 | In addition to the entry in the test report and the setting of the verdict to "fail," the current waiting point is also aborted. This behavior was introduced for reasons of compatibility with Version 5.0 and should only be selected in exceptional cases since here after each waiting point a corresponding query must be inserted. |

## Example

Example 1

Add check as constraint

Example 2

```c
dword checkId;
dword numCheckEvents;

// start the Error Frame observation
checkId = ChkStart_ErrorFramesOccured();
// Add check as constraint,
// that means that check violations are reported and
// the verdict of the test case is set to "failed"
TestAddConstraint(checkId);
// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
// Remove check as constrait
TestRemoveConstraint(checkId);

// stop the check
ChkControl_Stop(checkId);
// reset stored values of the check
ChkControl_Reset(checkId);

// start the check again without adding as constraint,
// that means that Error Frames are observed, but violations
// are not reported and do not set the test case verdict to "failed"
ChkControl_Start(checkId);
// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
// stop the check
ChkControl_Stop(checkId);

// analysis of check
numCheckEvents = ChkQuery_NumEvents(checkId);
if (numCheckEvents > 0)
TestStepFail("Error Frame occurred!");

// destroy check
ChkControl_Destroy(checkId);
// test case to check if Error Frames occur
testcase CheckErrorFrameReceived ()
{
  TestAddConstraint("ErrorFrameReceived");
  // sequence of different actions and waiting conditions
  TestWaitForTimeout(1000);
  TestRemoveConstraint("ErrorFrameReceived");
}

// handler to supply text event
on errorFrame
{
  TestSupplyTextEvent("ErrorFrameReceived");
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.0 | 13.0 | — | 14 | 1.0 |
| Restricted To | — | Test nodes | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
