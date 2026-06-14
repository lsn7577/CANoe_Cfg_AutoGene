# TestJoinLinETFSingleResponseEvent

> Category: `Test` | Type: `function`

## Syntax

```c
long TestJoinLinETFSingleResponseEvent (dword aETFFrameId, dword aAssocFrameId)
```

## Description

Adds an event of type LIN Event-triggered Frame Single Response to the set of joined events. This is a non-blocking function.

## Parameters

| Name | Description |
|---|---|
| aETFFrameId | Frame identifier of LIN event-triggered frame to be awaited. |
| aAssocFrameId | Frame identifier of a LIN unconditional frame associated with the awaited event-triggered frame. |

## Example

```c
testcase tcTFS_waitForLinETFSingleResponse(int etfFrameId)
{
   long eventIndex;
   testJoinLinETFSingleResponseEvent(etfFrameId, linGetProtectedID(0x36));
   testJoinLinETFSingleResponseEvent(etfFrameId, linGetProtectedID(0x34));

   eventIndex = testWaitForAnyJoinedEvent(5000);
   switch (eventIndex)
   {
      case 1:
         testStepPass("Validation", "ETF single frame response occurred. FrameId=0x36");
      break;

      case 2:
         testStepPass("Validation", "ETF single frame response occurred. FrameId=0x34");
      break;

      default:
         testStepFail("Validation", "ETF single frame response not occurred");
   }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.0 | 13.0 | — | — | 1.0 |
| Restricted To | — | LIN | LIN | — | — | LIN |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
