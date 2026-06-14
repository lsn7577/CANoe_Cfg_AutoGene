# VTIL_IsObjectVisible

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_IsObjectVisible(dbNode workingSetMaster, dword typeOfActiveMask, dword objectId, dword & isVisible); // form 1
long VTIL_IsObjectVisible(dword addressWorkingSetMaster, dword typeOfActiveMask, dword objectId, dword & isVisible); // form 2
long VTIL_IsObjectVisible(dbNode vt, dbNode workingSetMaster, dword typeOfActiveMask, dword objectId, dword & isVisible); // form 3
long VTIL_IsObjectVisible(dbNode vt, dword addressWorkingSetMaster, dword typeOfActiveMask, dword objectId, dword & isVisible); // form 4
```

## Description

Checks if an object is visible in the current Data Mask or Soft Key Mask.

## Parameters

| Name | Description |
|---|---|
| vt | VT simulation node to apply the function. |
| workingSetMaster | Working Set Master which provides the Object Pool |
| addressWorkingSetMaster | Address of the Working Set Master which provides the Object Pool |
| typeOfActiveMask | This parameter specifies if function checks the visibility of the object in the active Data Mask or in the active Soft Key Mask. 0: Data mask 1: Soft Key mask |
| objectId | Object ID of visible Data Mask or Alarm Mask. |
| isVisible | Returns the visibility of the object. 0: Object is not visible 1: Object is visible |

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
