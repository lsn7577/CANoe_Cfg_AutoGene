# TestGetWaitLinWakeupData

> Category: `Test` | Type: `function`

## Syntax

```c
long TestGetWaitLinWakeupData (linWakeupFrame apEvent);
```

## Description

If LIN Wakeup frame is the last event that triggers a wait instruction, the frame content can be called up with the first function.The second function can only be used for "joined events". The number of the "joined event" (return value of "testJoin...") is here being used as an index.

## Return Values

0: Data access successful

## Example

```c
testcase tcTFS_linWakeupEvent ()
{
   linWakeupFrame linWakeupData;
   if (testWaitForLinWakeupFrame(5000) == 1)
   {
      if (testGetWaitLinWakeupData(linWakeupData) == 0)
      {
         testStep("Evaluation", "LIN Wakeup event occurred. Signal length is %d ns", linWakeupData.length_ns);
      }
   }
}
```

## Availability

| Since Version |
|---|
