# VTIL_SelectInputObject, VTIL_SelectInputObjectMsg

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_SelectInputObject(dword objectId); // form 1
long VTIL_SelectInputObject(dbNode vt, dword objectId); // form 2
long VTIL_SelectInputObject(dword objectId, byte openMode); // form 3
long VTIL_SelectInputObject(dbNode vt, dword objectId, dword openMode); // form 4
long VTIL_SelectInputObjectMsg(dword objectId, dword objectIsSelected, dword openMode); // form 5
long VTIL_SelectInputObjectMsg(dbNode vt, dword objectId, dword objectIsSelected, dword openMode); // form 6
```

## Description

Select an input filed, Button of Key object.

The VTIL_SelectInputObject methods simulate the selection of an input field, button or key object by user. As a result:

The VTIL_SelectInputObjectMsg methods send only the VT Select Input Object message (without influencing any button or input object and without triggering any event in the Virtual Terminal). You can use it to implement fault injection.

If an input object is open for data input, the value of the object can be modified with VTIL_EditNumericValue or VTIL_EditStringValue. To close an input object which is open for data input, you have to use this command with openMode 0.

## Parameters

| Name | Description |
|---|---|
| vt | VT simulation node to apply the function |
| objectId | Object ID of an input filed, Button of Key object |
| objectIsSelected | 0: Object is deselected 1: Object is selected (has focus) |
| openMode | 0: Select object or close open object 1: Open object for data input |

## Example

Example 1: Form 2, 4 and 6

Example 2: Form 2, 4 and 6

Simulation of real time editing:

```c
//to simulate: operator navigates to the object with ID=220

long result;
result = VTIL_SelectInputObject(VT, 220);
switch (result)
{
  case 0: TestStepPass(); break;
  case -2102: TestStepFail("Invalid object!"); break;
  case -2104: TestStepFail("Currently there is no acive Working Set!"); break;
  case -2106: TestStepFail("Currently there is no active Data or Alarm mask!"); break;
  case -2112: TestStepFail("Invalid open mode!"); break;
  case -2115: TestStepFail("VT works in passiv mode therefore you cannot select objects!"); break;
  case -2116: TestStepFail("Failed to select object!"); break;
  default:    TestStepFail("Unexpected error!"); break;
}

//to simulate: Real Time Editing of the numeric object with ID=220

VTIL_SelectInputObject(VT, 220, 1); // open for editing
TestWaitForTimeout(200);
VTIL_EditNumericValue(VT, 220, 1, 0); //type „1“
TestWaitForTimeout(500);
VTIL_EditNumericValue(VT, 220, 12, 0); //type additionally „2“
TestWaitForTimeout(600);
VTIL_EditNumericValue(VT, 220, 123, 0);  //type additionally „3“
TestWaitForTimeout(400);
VTIL_SelectInputObject(VT, 220, 0);    //finish editing
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 | 13.0 | — | — | 2.1 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 2, 4, 6 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1, 3, 5) | ✔ (form 1, 3, 5) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2, 4, 6) | ✔ (form 2, 4, 6) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2, 4, 6) | ✔ (form 2, 4, 6) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
