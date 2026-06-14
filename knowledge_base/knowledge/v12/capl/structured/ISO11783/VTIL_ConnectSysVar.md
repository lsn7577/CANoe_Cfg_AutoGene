# VTIL_ConnectSysVar

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_ConnectSysVar(dbNode workingSetMaster, dword objectId, char[] sysVarNameWithPath); // form 1
```

## Description

Connects an object from the object pool to a system variable. Valid objects are variables, objects representing values or string, buttons and soft keys.

If a variable object or an object representing a values or a string is changed, the new value is put into the system variable.

To release connection between the system variable and an object, just call the same method again, but with the empty string instead of the name of system variable.

## Return Values

0: Function has been executed successfully

## Example

```c
long result;
result = VTIL_ConnectSysVar(VT, Sprayer, 221, "VT::svValueInt32");
switch (result)
{
  case 0:
    write("Object 12 is successfully connected with svValueInt32");
    TestStepPass();
    break;
  case -2109: TestStepFail("Working Set is not available!"); break;
  case -2113: TestStepFail("Invalid Parameter!"); break;
  case -2114: TestStepFail("Invalid system variable path!"); break;
  default:    TestStepFail("Unexpected error!"); break;
}
```

## Availability

| Since Version |
|---|
