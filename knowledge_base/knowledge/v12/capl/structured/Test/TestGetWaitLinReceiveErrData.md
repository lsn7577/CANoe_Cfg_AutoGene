# TestGetWaitLinReceiveErrData

> Category: `Test` | Type: `function`

## Syntax

```c
long TestGetWaitLinReceiveErrData (linReceiveError apEvent);
```

## Description

If LIN Receive Error event is the last event that triggers a wait instruction, the error content can be called up with the first function.The second function can only be used for "joined events". The number of the "joined event" (return value of "testJoin...") is here being used as an index.

## Return Values

0: Data access successful

## Example

```c
testcase tcTFS_linReceiveErrorEvent ()
{
   linReceiveError linReceiveErrorData;
   if (testWaitForLinReceiveError(5000) == 1)
   {
      if (TestGetWaitLinReceiveErrData(linReceiveErrorData) == 0)
      {
         testStep("Evaluation", "LIN Receive Error event occurred for FrameId=0x%X", linReceiveErrorData.ID);
      }
   }
}
```

## Availability

| Since Version |
|---|
