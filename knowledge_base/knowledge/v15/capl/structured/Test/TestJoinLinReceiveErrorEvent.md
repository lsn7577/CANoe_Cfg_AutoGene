# TestJoinLinReceiveErrorEvent

> Category: `Test` | Type: `function`

## Syntax

```c
long TestJoinLinReceiveErrorEvent (dword aFrameId)
long TestJoinLinReceiveErrorEvent ()
```

## Description

Completes the current set of "joined events" with the transmitted event. This function does not wait.

## Parameters

| Name | Description |
|---|---|
| aFrameId | Numeric ID of a frame whose Receive Error should be awaited. Default value: wait for any ID. |

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
