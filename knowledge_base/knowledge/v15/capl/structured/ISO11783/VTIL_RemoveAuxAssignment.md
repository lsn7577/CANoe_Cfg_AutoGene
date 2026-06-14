# VTIL_RemoveAuxAssignment

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_RemoveAuxAssignment(dbNode auxiliaryFunctionWSM, word auxiliaryFunctionId); // form 1
long VTIL_RemoveAuxAssignment(dword addressAuxiliaryFunctionWSM, word auxiliaryFunctionId); // form 2
long VTIL_RemoveAuxAssignment(dbNode vt, dbNode auxiliaryFunctionWSM, word auxiliaryFunctionId); // form 3
long VTIL_RemoveAuxAssignment(dbNode vt, dword addressAuxiliaryFunctionWSM, word auxiliaryFunctionId); // form 4
```

## Description

Removes an auxiliary assignment. As a result the Auxiliary Assignment Type 2 command is sent to the Auxiliary Function Working Set Master. If there are no assignments for the Auxiliary Input an Auxiliary Input Status Type 2 Enable command (Disable) is sent to the Auxiliary Input Working Set Master.

If the participants are using VT Version 0, 1 or 2 only an Auxiliary Assignment Type 1 command is sent to the Auxiliary Input.

## Parameters

| Name | Description |
|---|---|
| vt | VT simulation node to apply the function |
| auxiliaryFunctionWSM | Working Set Master which provides the Auxiliary Function |
| addressAuxiliaryFunctionWSM | Address of the Working Set Master which provides the Auxiliary Function |
| auxiliaryFunctionId | Object ID of the Auxiliary Function. For value 0xFFFF all assigned functions are removed |

## Example

```c
long result;
result = VTIL_RemoveAuxAssignment (VT, Loader, 1001);
switch (result)
{
  case 0: TestStepPass(); break;
  case -2109: TestStepFail("The Working Set is not available!"); break;
  case -2118: TestStepFail("Object is not Auxiliary Function!"); break;
  case -2119: TestStepFail("The assignment failed!"); break;
  default: TestStepFail("Unexpected error!"); break;
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
