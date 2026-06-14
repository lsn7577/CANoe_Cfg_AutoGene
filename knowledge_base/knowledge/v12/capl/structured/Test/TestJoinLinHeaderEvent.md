# TestJoinLinHeaderEvent

> Category: `Test` | Type: `function`

## Syntax

```c
long TestJoinLinHeaderEvent (dbMessage aFrame)
```

## Description

Completes the current set of "joined events" with the transmitted event. This function does not wait.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Return Values

-3: Join error

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
