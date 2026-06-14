# VTIL_GetActiveMask

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_GetActiveMask(dword & maskId); // form 1
```

## Description

Returns object ID of the active Data or Alarm Mask.

## Return Values

0: Function has been executed successfully

## Example

```c
long result;
dword maskId;
result = VTIL_GetActiveMask(VT, maskId);
switch (result)
{
  case 0:
    write("ID of current mask is %u", maskId);
    TestStepPass();
    break;
  case -2104: TestStepFail("Currently there is no active Working Set!"); break;
  case -2106: TestStepFail("Currently there is no active Data or Alarm mask!"); break;
  default:    TestStepFail("Unexpected error!"); break;
}
```

## Availability

| Since Version |
|---|
