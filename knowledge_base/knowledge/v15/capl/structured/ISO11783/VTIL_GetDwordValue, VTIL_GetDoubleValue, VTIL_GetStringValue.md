# VTIL_GetDwordValue, VTIL_GetDoubleValue, VTIL_GetStringValue

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_GetDwordValue(dbNode workingSetMaster, dword objectId, dword & value); // form 1
long VTIL_GetDwordValue(dword addressWorkingSetMaster, dword objectId, dword & value); // form 2
long VTIL_GetDwordValue(dbNode workingSetMaster, dword objectId, dword attributeID, dword & value); // form 3
long VTIL_GetDwordValue(dword addressWorkingSetMaster, dword objectId, dword attributeID, dword & value); // form 4
long VTIL_GetDwordValue(dbNode vt, dbNode workingSetMaster, dword objectId, dword & value); // form 5
long VTIL_GetDwordValue(dbNode vt, dword addressWorkingSetMaster, dword objectId, dword & value); // form 6
long VTIL_GetDwordValue(dbNode vt, dbNode workingSetMaster, dword objectId, dword attributeID, dword & value); // form 7
long VTIL_GetDwordValue(dbNode vt, dword addressWorkingSetMaster, dword objectId, dword attributeID, dword & value); // form 8
long VTIL_GetDoubleValue(dbNode workingSetMaster, dword objectId, dword attributeID, double & value); // form 9
long VTIL_GetDoubleValue(dword addressWorkingSetMaster, dword objectId, dword attributeID, double & value); // form 10
long VTIL_GetDoubleValue(dbNode vt, dbNode workingSetMaster, dword objectId, dword attributeID, double & value); // form 11
long VTIL_GetDoubleValue(dbNode vt, dword addressWorkingSetMaster, dword objectId, dword attributeID, double & value); // form 12
long VTIL_GetStringValue(dbNode workingSetMaster, dword objectId, char* value, dword bufferLength); // form 13
long VTIL_GetStringValue(dword addressWorkingSetMaster, dword objectId, char* value, dword bufferLength); // form 14
long VTIL_GetStringValue(dbNode vt, dbNode workingSetMaster, dword objectId, char* value, dword bufferLength); // form 15
long VTIL_GetStringValue(dbNode vt, dword addressWorkingSetMaster, dword objectId, char* value, dword bufferLength); // form 16
long VTIL_GetStringValue(dbNode workingSetMaster, dword objectId, char* value); // form 17
long VTIL_GetStringValue(dword addressWorkingSetMaster, dword objectId, char* value); // form 18
long VTIL_GetStringValue(dbNode vt, dbNode workingSetMaster, dword objectId, char* value); // form 19
long VTIL_GetStringValue(dbNode vt, dword addressWorkingSetMaster, dword objectId, char* value); // form 20
```

## Description

Returns the value of an object or of an object attribute.

You can use VTIL_GetDoubleValue or VTIL_GetDwordValue without attribute ID to get the numeric value of a Key object, Button object or an object that supports the Change Numeric Value command. You can use VTIL_GetStringValue the get the string value of a Input String, Output String, String Variable or a Input Attribute object.

## Parameters

| Name | Description |
|---|---|
| vt | VT simulation node to apply the function |
| workingSetMaster | Working Set Master which provides the Object Pool |
| addressWorkingSetMaster | Address of the Working Set Master which provides the Object Pool |
| objectId | Object ID the attribute belongs to |
| attributeID | Identifies the necessary attribute (correlate to the AIDcolumn of corresponding object definitions from Annex B (Iso11783-6) |
| value | Returns the value of the object or attribute |

## Example

Example forms 5, 6,7, 8, 11, 12, 15, 16, 19, 20

```c
long result;
char buf[100];
result = VTIL_GetStringValue(VT, 128, 205, buf);  //Form 20 is used
switch (result)
{
  case 0:
    write("Current value of object 205 is '%s'", buf);
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
| Since Version | — | 9.0: form 1, 3, 5, 7, 9, 11, 13, 15, 17, 19 13.0: form 2, 4, 6, 8, 10, 12, 14, 16 18, 20 | 13.0 | — | — | 2.1: form 5, 7, 11, 15, 19 5.0: form 6, 8, 12, 16, 20 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 5, 6,7, 8, 11, 12, 15, 16, 19, 20 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1, 2, 3, 4, 9, 10, 13, 14, 17, 18) | ✔ (form 1, 2, 3, 4, 9, 10, 13, 14, 17, 18) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 5, 6,7, 8, 11, 12, 15, 16, 19, 20) | ✔ (form 5, 6,7, 8, 11, 12, 15, 16, 19, 20) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 5, 6,7, 8, 11, 12, 15, 16, 19, 20) | ✔ (form 5, 6,7, 8, 11, 12, 15, 16, 19, 20) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
