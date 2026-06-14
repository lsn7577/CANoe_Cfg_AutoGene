# TestJoinLinCSErrorEvent

> Category: `Test` | Type: `function`

## Syntax

```c
long TestJoinLinCSErrorEvent()
```

## Description

Adds an event of type checksum error to the set of joined events. This is a non-blocking function.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Return Values

-3: Error while adding the specified event to the set of joined events

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
