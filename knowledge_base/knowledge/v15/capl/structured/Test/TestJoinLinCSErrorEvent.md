# TestJoinLinCSErrorEvent

> Category: `Test` | Type: `function`

## Syntax

```c
long TestJoinLinCSErrorEvent()
long TestJoinLinCSErrorEvent(dbMsg apDBMsg)
long TestJoinLinCSErrorEvent(dword aFrameId)
```

## Description

Adds an event of type checksum error to the set of joined events. This is a non-blocking function.

## Parameters

| Name | Description |
|---|---|
| apDBMsg | Symbolic message |
| aFrameId | Frame identifier |

## Example

```c
testcase tcTFS_waitForLINResponse(int frameId)
{
   long eventIndex;

   testJoinMessageEvent(frameId);
   testJoinLinReceiveErrorEvent(frameId);
   testJoinLinCSErrorEvent(frameId);
   testJoinLinTransmErrorEvent(frameId);

   eventIndex = testWaitForAnyJoinedEvent(5000);
   switch (eventIndex)
   {
      case 1: // valid frame
         testStepPass("Validation", "IUT has responded correctly");
      break;

      case 2:  // receive error
         testStepFail("Validation", "IUT has responded with wrong number of data bytes");
      break;

      case 3: // checksum error
         testStepFail("Validation", "IUT has responded with wrong checksum");
      break;

      case 4: // transmission error
         testStepFail("Validation", "IUT has not responded");
      break;

      default:
      testStepFail("Validation", "Internal error! Unexpected event (return code %d) on waiting for response", eventIndex);
   }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.2 | 13.0 | — | — | 1.0 |
| Restricted To | — | LIN | LIN | — | — | LIN |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
