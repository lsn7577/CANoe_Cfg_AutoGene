# TestJoinLinHeaderEvent

> Category: `Test` | Type: `function`

## Syntax

```c
long TestJoinLinHeaderEvent (dbMsg aFrame)
long TestJoinLinHeaderEvent (dword aFrameId)
```

## Description

Completes the current set of "joined events" with the transmitted event. This function does not wait.

## Parameters

| Name | Description |
|---|---|
| aFrame | Frame whose header should be awaited. |
| aFrameId | Numeric ID of a frame whose header should be awaited. |

## Example

```c
testcase tcTFS_waitForLINHeader(int frameId)
{
   long eventIndex;

   testJoinLinHeaderEvent(frameId);
   testJoinLinWakeupEvent();
   testJoinLinSyncErrorEvent();

   eventIndex = testWaitForAnyJoinedEvent(5000);
   switch (eventIndex)
   {
      case 1:
         testStepPass("Validation", "LIN Header for FrameId=0x%X occurred", frameId);
      break;

      case 2:
         testStepFail("Validation", "LIN Wakeup signal occurred");
      break;

      case 3:
         testStepFail("Validation", "LIN Sync error occurred");
      break;

      default:
         testStepFail("Validation", "Internal error! Unexpected event (return code %d) on waiting for any LIN event", eventIndex);
   }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.1 | 13.0 | — | — | 1.0 |
| Restricted To | — | LIN | LIN | — | — | LIN |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
