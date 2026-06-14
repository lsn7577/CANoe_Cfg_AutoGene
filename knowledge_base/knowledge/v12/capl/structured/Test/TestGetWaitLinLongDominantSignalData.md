# TestGetWaitLinLongDominantSignalData

> Category: `Test` | Type: `function`

## Syntax

```c
long TestGetWaitLinLongDominantSignalData (linLongDominantSignal apEvent);
```

## Description

If LIN LongDominantSignal is the last event that triggers a wait instruction, the frame content can be called up with the first function.

The second function can only be used for joined events. The number of the joined event (return value of testJoin...) is here being used as an index.

## Return Values

0: Data access successful

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
