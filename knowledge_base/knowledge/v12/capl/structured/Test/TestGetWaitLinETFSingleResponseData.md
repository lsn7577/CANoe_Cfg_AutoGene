# TestGetWaitLinETFSingleResponseData

> Category: `Test` | Type: `function`

## Syntax

```c
long TestGetWaitLinETFSingleResponseData (linFrame apEvent);
```

## Description

If LIN Event-triggered frame with a single response for the specified associated frame is the last event that triggers a wait instruction, the event content can be called up with this function.

When the triggering event is a part of a wait instruction for joined events, the index parameter has to correspond to the return value of "testJoin..." function.

## Return Values

0: Data access successful

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
