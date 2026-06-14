# TestWaitForLinETFSingleResponse

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForLinETFSingleResponse (dword aETFFrameId, dword aAssocFrameId, dword aTimeout);
```

## Description

Waits for the occurrence of a LIN Event-triggered frame with a single response for the specified associated frame. Should the event-triggered frame not occur before the expiration of the specified timeout, the wait condition is resolved nevertheless.

Consider to set always the appropriate bus context in a multibus environment before the function is called.

Further information on site MultiBus Environment.

## Return Values

-2: Resume due to constraint violation

## Example

```c
testcase tcTFS_linETFSingleResponse ()
{
   linFrame 0 linETFSingleResponseData;

   if (testWaitForLinETFSingleResponse(0x3A, 0x36, 5000) == 1)
   {
      if (testGetWaitLinETFSingleResponseData(linETFSingleResponseData) == 0)
      {
         testStep("Evaluation", "LIN Event-triggered frame with a single response occurred for FrameId=0x%X", linETFSingleResponseData.ID);
      }
   }
}
```

## Availability

| Since Version |
|---|
