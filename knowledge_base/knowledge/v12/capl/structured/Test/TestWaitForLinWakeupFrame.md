# TestWaitForLinWakeupFrame

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForLinWakeupFrame (dword aTimeout);
```

## Description

Waits for the occurrence of LIN Wakeup frame. Should the frame not occur before the expiration of the time aTimeout, the wait condition is resolved nevertheless.

Consider to set always the appropriate bus context in a multibus environment before the function is called.

Further information on site MultiBus Environment.

## Return Values

-2: Resume due to constraint violation

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
