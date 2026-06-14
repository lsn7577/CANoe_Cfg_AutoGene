# TCIL_ConnectSysVarWithSection

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_ConnectSysVarWithSection(dbNode client, dword ddiOfCondensedState, dword elementNumber, dword sectionNumber, char[] sysVarNameWithPath); // form 1
```

## Description

This function connects a single section state to a system variable.

If a section state is changed the new value is put into the system variable. To release connection between the system variable and the condensed state, just call the same method again, but with the empty string instead of the name of system variable.

## Return Values

0: Function has been executed successfully

## Example

```c
long result;
result = TCIL_ConnectSysVarWithSection(TC, Sprayer, 162, 1, 20,
Sprayer::svActualCondensedWorkStateSection20");
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
