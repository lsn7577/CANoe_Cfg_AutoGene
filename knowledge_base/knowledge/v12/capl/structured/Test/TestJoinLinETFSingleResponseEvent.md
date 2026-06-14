# TestJoinLinETFSingleResponseEvent

> Category: `Test` | Type: `function`

## Syntax

```c
long TestJoinLinETFSingleResponseEvent (dword aETFFrameId, dword aAssocFrameId)
```

## Description

Adds an event of type LIN Event-triggered Frame Single Response to the set of joined events. This is a non-blocking function.

Consider to set always the appropriate bus context in a multibus environment before the function is called.

Further information on site MultiBus Environment.

## Return Values

-3: Join error

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

| Since Version |
|---|
