# VTIL_GetDisplayedValue

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_GetDisplayedValue(dbNode workingSetMaster, dword objectId, double & value); // form 1
long VTIL_GetDisplayedValue(dword addressWorkingSetMaster, dword objectId, double & value); // form 2
long VTIL_GetDisplayedValue(dbNode vt, dbNode workingSetMaster, dword objectId, double & value); // form 3
long VTIL_GetDisplayedValue(dbNode vt, dword addressWorkingSetMaster, dword objectId, double & value); // form 4
long VTIL_GetDisplayedValue(dbNode workingSetMaster, dword objectId, char* buffer, dword bufferLength); // form 5: deprecated with 13
long VTIL_GetDisplayedValue(dbNode vt, dbNode workingSetMaster, dword objectId, char* buffer, dword bufferLength); // form 6: deprecated with 13
long VTIL_GetDisplayedValue(dbNode workingSetMaster, dword objectId, char* buffer); // form 7
long VTIL_GetDisplayedValue(dword addressWorkingSetMaster, dword objectId, char* buffer); // form 8
long VTIL_GetDisplayedValue(dbNode vt, dbNode workingSetMaster, dword objectId, char* buffer); // form 9
long VTIL_GetDisplayedValue(dbNode vt, dword addressWorkingSetMaster, dword objectId, char* buffer); // form 10
```

## Description

Returns the displayed value of an object.

If the object supports scaling/offset then the displayed value is

displayed value = (value + offset) * scaling factor

If the object uses a variable reference then the value of this reference is used to calculate the displayed value.

For Input String and Output String objects you can use form 7 and 9.

## Parameters

| Name | Description |
|---|---|
| vt | VT simulation node to apply the function |
| workingSetMaster | Working Set Master which provides the object pool. |
| addressWorkingSetMaster | Address of the Working Set Master which provides the object pool. |
| objectId | Object ID. |
| value | Returns the value of the object. |
| buffer | After execution, this parameter contains the displayed string of an Input String or Output String object. |
| bufferLength | Length of the buffer parameter in bytes. |

## Example

Example form 3, 4, 9, 10

```c
long result;
double value;
result = VTIL_GetDisplayedValue(VT, 128, 206, value) );  //Form 4 is used
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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0: form 1, 3 13.0: form 2, 4, 7, 9, 10 | 13.0 | — | — | 2.1: form 3 5.0: form 4, 9, 10 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 3, 4, 9, 10 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1, 3, 7, 8) | ✔ (form 1, 3, 7, 8) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 3, 4, 9, 10) | ✔ (form 3, 4, 9, 10) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 3, 4, 9, 10) | ✔ (form 3, 4, 9, 10) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
