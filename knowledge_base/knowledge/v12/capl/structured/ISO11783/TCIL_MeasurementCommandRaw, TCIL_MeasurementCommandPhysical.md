# TCIL_MeasurementCommandRaw, TCIL_MeasurementCommandPhysical

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_MeasurementCommandRaw(dbNode client, dword ddi, dword elementNumber, char[] logTriggerType, long triggerValue); // form 1
```

## Description

These functions send a trigger definition to the client.

## Return Values

0: Function has been executed successfully

## Example

```c
void StopMinWithinThresholdTrigger(dword ddi, dword elementNumber)
{
  long result;
  result = TCIL_MeasurementCommandRaw(TC, Sprayer, ddi, elementNumber, "min_within_threshold", 0x7FFFFFFF);
  switch (result)
  {
    case 0 : TestStepPass(); break;
    default: TestStepFail("StopMinWithinThresholdTrigger", "Unexpected error (error code %i)", result); break;
  }
}
```

## Availability

| Since Version |
|---|
