# VTIL_RemoveAuxAssignment

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_RemoveAuxAssignment(dbNode auxiliaryFunctionWSM, word auxiliaryFunctionId); // form 1
```

## Description

Removes an auxiliary assignment. As a result the Auxiliary Assignment Type 2 command is sent to the Auxiliary Function Working Set Master. If there are no assignments for the Auxiliary Input an Auxiliary Input Status Type 2 Enable command (Disable) is sent to the Auxiliary Input Working Set Master.

If the participants are using VT Version 0, 1 or 2 only an Auxiliary Assignment Type 1 command is sent to the Auxiliary Input.

## Return Values

0: Function has been executed successfully

## Example

```c
long result;
result = VTIL_RemoveAuxAssignment (VT, Loader, 1001);
switch (result)
{
  case 0: TestStepPass(); break;
  case -2109: TestStepFail("The Working Set is not available!"); break;
  case -2118: TestStepFail("Object is not Auxiliary Function!"); break;
  case -2119: TestStepFail("The assignment failed!"); break;
  default: TestStepFail("Unexpected error!"); break;
}
```

## Availability

| Since Version |
|---|
