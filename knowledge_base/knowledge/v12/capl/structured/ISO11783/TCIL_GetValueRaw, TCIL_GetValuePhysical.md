# TCIL_GetValueRaw, TCIL_GetValuePhysical

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_GetValueRaw(dbNode client, dword ddi, dword elementNumber, long & value); // form 1
```

## Description

These functions return the current value of a data entity of the Task Controller. No Request Value command is sent.

## Return Values

0: Function has been executed successfully

## Example

```c
void CheckValue(double referenceValue)
{
  long result;
  double value;
  result = TCIL_GetValuePhysical(TC, Sprayer, 6, 1, value);
  if (result == 0)
  {
    if (value == referenceValue)
    {
      TestStepPass();
    }
    else
    {
      TestStepFail("CheckValue", "Value of data entity (DDI 6 , element number 1) is different (Expected value: %f)", referenceValue);
    }
  }
  else
  {
    TestStepFail("CheckValue", "Failed to get value of data entity (DDI 6 , element number 1). Error %i", result);
  }
}
```

## Availability

| Since Version |
|---|
