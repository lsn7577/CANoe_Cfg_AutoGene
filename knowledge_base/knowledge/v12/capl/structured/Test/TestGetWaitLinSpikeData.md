# TestGetWaitLinSpikeData

> Category: `Test` | Type: `function`

## Syntax

```c
long TestGetWaitLinSpikeData (linSpikeEvent apEvent);
```

## Description

If LIN Spike is the last event that triggers a wait instruction, the frame content can be called up with the first function.

The second function can only be used for joined events. The number of the joined event (return value of testJoin...) is here being used as an index.

## Return Values

0: Data access successful

## Example

```c
testcase tcTFS_linSpikeEvent ()
{
   linSpikeEvent linSpikeEventData;
   if (testWaitForLinSpike (5000) == 1)
   {
   if (testGetWaitLinSpikeData(linSpikeEventData) == 0)
      {
      testStep("Evaluation", "LIN Spike event occurred. Signal length is %d ns", linSpikeEventData.length_ns);
      }
   }
}
```

## Availability

| Since Version |
|---|
