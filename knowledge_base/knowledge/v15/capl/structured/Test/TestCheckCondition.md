# TestCheckCondition

> Category: `Test` | Type: `function`

## Syntax

```c
long TestCheckCondition (dword aAuxHandle);
long TestCheckCondition (char aEventText[]);
```

## Description

Checks whether the specified condition was already injured.

This function can be used both within a test case and also on test module level.

## Parameters

| Name | Description |
|---|---|
| aAuxHandle | Event object, for example a check from the TestService Library. Specified is the handle that is returned on creation of a check. This function can be used both within a test case and also on the test module level. |
| aEventText | Textual name of an event whose occurrence should be monitored. This event can be triggered with the function TestSupplyTextEvent. |

## Example

Example 1

Add check as condition

Example 2

Add text event as condition

```c
// checks the maximum duration of a sequence of actions
checkId = ChkStart_Timeout (1000);
TestAddCondition(checkId);
TestWaitForTimeout(1500);
result = TestCheckCondition(checkId);
if (result == 1)
   TestStepFail("Timeout already occurred after 1500 ms.");
// sequence of different actions and waiting conditions
TestRemoveCondition(checkId);
// test case to check if Error Frames occur
testcase CheckErrorFrameReceived ()
{
   TestAddCondition("ErrorFrameReceived");
   TestWaitForTimeout(1000);
   result = TestCheckCondition("ErrorFrameReceived");
   if (result == 1)
      TestStepFail("Error Frame already occurred after 1000 ms.");
   // sequence of different actions and waiting conditions
   TestRemoveCondition("ErrorFrameReceived");
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
| Since Version | — | 5.1 | 13.0 | — | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
