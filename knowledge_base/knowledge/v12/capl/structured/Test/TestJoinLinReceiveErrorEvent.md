# TestJoinLinReceiveErrorEvent

> Category: `Test` | Type: `function`

## Syntax

```c
long TestJoinLinReceiveErrorEvent (dword aFrameId)
```

## Description

Completes the current set of "joined events" with the transmitted event. This function does not wait.

Consider to set always the appropriate bus context in a multibus environment before the function is called.

Further information on site MultiBus Environment.

## Return Values

-3: Join error

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

| Since Version |
|---|
