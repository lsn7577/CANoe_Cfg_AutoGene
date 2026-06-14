# TestJoinLinSyncErrorEvent

> Category: `Test` | Type: `function`

## Syntax

```c
long TestJoinLinSyncErrorEvent()
```

## Description

Adds an event of type synchronisation error to the set of joined events. This is a non-blocking function.

Consider to set always the appropriate bus context in a multibus environment before the function is called.

Further information on site MultiBus Environment.

## Return Values

-3: error while adding the specified event to the set of joined events

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

| Since Version |
|---|
