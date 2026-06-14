# VTIL_ConnectSysVar

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_ConnectSysVar(dbNode workingSetMaster, dword objectId, char[] sysVarNameWithPath); // form 1
long VTIL_ConnectSysVar(dword addressWorkingSetMaster, dword objectId, char[] sysVarNameWithPath); // form 2
long VTIL_ConnectSysVar(dbNode vt, dbNode workingSetMaster, dword objectId, char[] sysVarNameWithPath); // form 3
long VTIL_ConnectSysVar(dbNode vt, dword addressWorkingSetMaster, dword objectId, char[] sysVarNameWithPath); // form 4
```

## Description

Connects an object from the object pool to a system variable. Valid objects are variables, objects representing values or string, buttons and soft keys.

If a variable object or an object representing a values or a string is changed, the new value is put into the system variable.

To release connection between the system variable and an object, just call the same method again, but with the empty string instead of the name of system variable.

## Parameters

| Name | Description |
|---|---|
| vt | VT simulation node to apply the function |
| workingSetMaster | Working Set Master which provides the Object Pool |
| addressWorkingSetMaster | Address of the Working Set Master which provides the Object Pool |
| sysVarNameWithPath | Name of the system variable, all name spaces inclusive |
| objectId | Identifier of the object in the object pool |

## Example

Example for 3, 4

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0: form 1, 3 13.0: form 2, 4 | 13.0 | — | — | 2.1: form 3 5.0: form 4 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 3, 4 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1, 2) | ✔ (form 1, 2) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 3, 4) | ✔ (form 3, 4) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 3, 4) | ✔ (form 3, 4) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
