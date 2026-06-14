# TestWaitForLinReceiveError

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForLinReceiveError (dword aFrameId, dword aTimeout);
```

## Description

Waits for the occurrence of LIN Receive Error event. Should the event not occur before the expiration of the time aTimeout, the wait condition is resolved nevertheless.

Consider to set always the appropriate bus context in a multibus environment before the function is called.

Further information on site MultiBus Environment.

## Return Values

-2: Resume due to constraint violation

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
