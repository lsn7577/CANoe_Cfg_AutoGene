# VTIL_ActivateWorkingSet

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_ActivateWorkingSet(dbNode workingSetMaster); // form 1
```

## Description

Activates a corresponding Working Set in the Virtual Terminal: As a result, the VT Status message is sent with the source address of newly activated Working Set as well as its active Data/Alarm and Soft Key Mask.

## Return Values

0: Function has been executed successfully

## Example

```c
long result;
result = VTIL_ActivateWorkingSet(VT, Sprayer);
switch (result)
{
  case 0: TestStepPass(); break;
  case -2109: TestStepFail ("Working Set 'Sprayer' is not available!"); break;
  case -2110: TestStepFail ("Failed to activate Working Set 'Sprayer'!"); break;
  default:    TestStepFail ("Unexpected error"); break;
}
```

## Availability

| Since Version |
|---|
