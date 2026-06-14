# TestWaitForLinTransmError

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForLinTransmError (dword aFrameId, dword aTimeout);
```

## Description

Waits for the occurrence of LIN Transmission Error event. Should the event not occur before the expiration of the time aTimeout, the wait condition is resolved nevertheless.

Consider to set always the appropriate bus context in a multibus environment before the function is called.

Further information on site MultiBus Environment.

## Return Values

-2: Resume due to constraint violation

## Example

```c
testcase tcTFS_linNoResponseEvent ()
{
   linTransmError linTransmErrorData;

   if (testWaitForLinTransmError(5000) == 1)
   {
      if (testGetWaitLinTransmErrData(linTransmErrorData) == 0)
      {
         testStep("Evaluation", "LIN No-Response event occurred for FrameId=0x%X", linTransmErrorData.ID);
      }
   }
}
```

## Availability

| Since Version |
|---|
