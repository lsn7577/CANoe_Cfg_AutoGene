# VTIL_GetChildObjectId

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_GetChildObjectId(dbNode workingSetMaster, dword objectId, dword index, long & childObjectId); // form 1
long VTIL_GetChildObjectId(dword addressWorkingSetMaster, dword objectId, dword index, long & childObjectId); // form 2
long VTIL_GetChildObjectId(dbNode vt, dbNode workingSetMaster, dword objectId, dword index, long & childObjectId); // form 3
long VTIL_GetChildObjectId(dbNode vt, dword addressWorkingSetMaster, dword objectId, dword index, long & childObjectId); // form 4
```

## Description

Returns the ID of an object which is contained by a parent object.

You can obtain the number of child objects with method VTIL_GetNumberOfChildObjects.

## Parameters

| Name | Description |
|---|---|
| vt | VT simulation node to apply the function. |
| workingSetMaster | Working Set Master which provides the Object Pool. |
| addressWorkingSetMaster | Address of the Working Set Master which provides the Object Pool. |
| objectId | Object ID of the parent object. |
| index | Index of the child object in the object list of the parent object. The first index is 0. |
| childObjectId | Returns the ID of the object at the specified index. If there is no child object for the specified index the value of childObjectId is set to -1. |

## Example

Example form 3, 4

```c
dword index, numberOfChildObjects;
long childObjectId;

//iterate over all children of the object with objectId = 1000
if (VTIL_GetNumberOfChildObjects(VT, Loader, 1000, numberOfChildObjects) == 0)
{
  for (index = 0; index < numberOfChildObjects; ++index)
  {
    if (VTIL_GetChildObjectId(VT, Loader, 1000, index, childObjectId) == 0)
    {
      Write("ID of child object at index %u is %i", index, childObjectId);
    }
  }
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
