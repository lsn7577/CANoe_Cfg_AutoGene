# VTIL_CreateAuxAssignment

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_CreateAuxAssignment(dbNode auxiliaryFunctionWSM, dbNode auxiliaryInputWSM, word auxiliaryFunctionId, word auxiliaryInputId); // form 1
```

## Description

Assigns an Auxiliary Input to an Auxiliary Function.

As a result the Auxiliary Input Status Type 2 Enable command is sent to the Auxiliary Input (if not already enabled) and the Auxiliary Assignment Type 2 command is sent to the Auxiliary Function Working Set Master.

If the participants are using VT Version 0, 1 or 2 only an Auxiliary Assignment Type 1 command is sent to the Auxiliary Input.

## Return Values

0: Function has been executed successfully

## Example

```c
long result;
result = VTIL_CreateAuxAssignment(VT, Loader, AuxInput, 1001, 1003);
switch (result)
{
  case 0: TestStepPass(); break;
  case -2109: TestStepFail("A Working Set is not available!"); break;
  case -2118: TestStepFail("An object is not suitable!"); break;
  case -2119: TestStepFail("The assignment failed!"); break;
  default: TestStepFail("Unexpected error!"); break;
}
```

## Availability

| Since Version |
|---|
