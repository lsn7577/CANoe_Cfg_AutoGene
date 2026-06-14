# VTIL_GetDisplayedValue

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_GetDisplayedValue(dbNode workingSetMaster, dword objectId, double & value); // form 1
```

## Description

Returns the displayed value of an object.

If the object supports scaling/offset then the displayed value is

displayed value = (value + offset) * scaling factor

If the object uses a variable reference then the value of this reference is used to calculate the displayed value.

For Input String and Output String objects you can use form 3 and 4.

## Return Values

0: Function has been executed successfully

## Example

```c
long result;
double value;
result = VTIL_GetDisplayedValue(VT, 206, value);
switch (result)
{
  case 0:
    write("Displayed value of object 206 is '%f'", value);
    TestStepPass();
    break;
  case -2102: TestStepFail("Invalid object!"); break;
  case -2104: TestStepFail("Currently there is no active Working Set!"); break;
  case -2108: TestStepFail("Invalid variable reference!"); break;
  default:    TestStepFail("Unexpected error!"); break;
}
```

## Availability

| Since Version |
|---|
