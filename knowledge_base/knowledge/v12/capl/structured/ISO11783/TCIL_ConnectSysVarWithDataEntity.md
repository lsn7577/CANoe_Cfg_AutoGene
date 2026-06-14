# TCIL_ConnectSysVarWithDataEntity

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_ConnectSysVarWithDataEntity(dbNode client, dword ddi, dword elementNumber, char[]sysVarNameWithPath, dword useRawValue); // form 1
```

## Description

This function connects a data entity specified by the data dictionary identifier to a system variable.

If the value of the data entity is changed, the new value is put into the system variable. To release connection between the system variable and data entity, just call the same method again, but with the empty string instead of the name of system variable.

## Return Values

0: Function has been executed successfully

## Example

```c
result = TCIL_ConnectSysVarWithDataEntity(TC, Sprayer, 117, 1, "Sprayer::svEffectiveTotalDistance", 1);
switch (result)
{
  case     0: TestStepPass(); break;
  case -2203: TestStepFail("Invalid system variable path!"); break;
  case -2211: TestStepFail("System variable does not exist!"); break;
  default   : TestStepFail("Unexpected error!"); break;
}
```

## Availability

| Since Version |
|---|
