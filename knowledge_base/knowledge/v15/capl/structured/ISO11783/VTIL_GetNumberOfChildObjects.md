# VTIL_GetNumberOfChildObjects

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_GetNumberOfChildObjects(dbNode workingSetMaster, dword objectId, dword & numberOfChildObjects); // form 1
long VTIL_GetNumberOfChildObjects(dword addressWorkingSetMaster, dword objectId, dword & numberOfChildObjects); // form 2
long VTIL_GetNumberOfChildObjects(dbNode vt, dbNode workingSetMaster, dword objectId, dword & numberOfChildObjects); // form 3
long VTIL_GetNumberOfChildObjects(dbNode vt, dword addressWorkingSetMaster, dword objectId, dword & numberOfChildObjects); // form 4
```

## Description

Returns the number of child objects which are contained in an object.

## Parameters

| Name | Description |
|---|---|
| vt | VT simulation node to apply the function. |
| workingSetMaster | Working Set Master which provides the Object Pool. |
| addressWorkingSetMaster | Address of the Working Set Master which provides the Object Pool. |
| objectId | Object ID of the parent object. |
| numberOfChildObjects | Returns the number of child objects contained in the parent object. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 SP5: form 1, 3 13.0: form 2, 4 | 13.0 | — | — | 2.2: form 3 5.0: form 4 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 3, 4 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1, 2) | ✔ (form 1, 2) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 3, 4) | ✔ (form 3, 4) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 3, 4) | ✔ (form 3, 4) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
