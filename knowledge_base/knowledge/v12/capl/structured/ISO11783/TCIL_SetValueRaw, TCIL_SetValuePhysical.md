# TCIL_SetValueRaw, TCIL_SetValuePhysical

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_SetValueRaw(dbNode client, dword ddi, dword elementNumber, long value); // form 1
```

## Description

These functions set the value of a data entity without sending any command.

## Return Values

0: Function has been executed successfully

## Example

```c
void SetSetpointMassPerAreaApplicationRate(double value)
{
  long result;
  result = TCIL_SetValuePhysical(TC, Sprayer, 6, 1, value);
  switch (result)
  {
    case     0: TestStepPass(); break;
    case -2202: TestStepFail("Function is not available in passive mode of the TC IL!"); break;
    case -2204: TestStepFail("Node 'Sprayer' is no client device!"); break;
    default:    TestStepFail("Unexpected error"); break;
  }
}
```

## Availability

| Since Version |
|---|
