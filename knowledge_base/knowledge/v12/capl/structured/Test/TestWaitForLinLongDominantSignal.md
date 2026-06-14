# TestWaitForLinLongDominantSignal

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForLinLongDominantSignal (dword aTimeout);
```

## Description

Waits for the occurrence of a LIN long dominant signal. Should the frame not occur before the expiration of the time aTimeout, the wait condition is resolved nevertheless.

Consider to set always the appropriate bus context in a multibus environment before the function is called.

Further information on site MultiBus Environment.

## Return Values

-2: Resume due to constraint violation

## Example

```c
testcase tcTFS_linLongDominantSignal ()
{
   linLongDominantSignal linLongDominantSignal;
   if (testWaitForLinLongDominantSignal (5000) == 1)
   {
      if (testGetWaitLinLongDominantSignalData(linLongDominantSignal) == 0)
      {
         testStep("Evaluation", "LIN LongDominantSignal event occurred. Signal length is %d ns", linLongDominantSignalData.length_ns);
      }
   }
}
```

## Availability

| Since Version |
|---|
