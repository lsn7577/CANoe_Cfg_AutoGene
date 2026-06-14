# TestGetWaitLinTransmErrData

> Category: `Test` | Type: `function`

## Syntax

```c
long TestGetWaitLinTransmErrData (linTransmError apEvent);
```

## Description

If LIN Transmission Error event is the last event that triggers a wait instruction, the error content can be called up with the first function.The second function can only be used for "joined events". The number of the "joined event" (return value of "testJoin...") is here being used as an index.

## Return Values

0: Data access successful

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
