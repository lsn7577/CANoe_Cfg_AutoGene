# TestWaitForLinSpike

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForLinSpike (dword aTimeout);
```

## Description

Waits for the occurrence of a LIN Spike event. Should the event not occur before the expiration of the time aTimeout, the wait condition is resolved nevertheless.

Consider to set always the appropriate bus context in a multibus environment before the function is called.

Further information on site MultiBus Environment.

## Return Values

-2: Resume due to constraint violation

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
