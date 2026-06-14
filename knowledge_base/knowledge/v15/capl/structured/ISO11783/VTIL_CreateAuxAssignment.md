# VTIL_CreateAuxAssignment

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_CreateAuxAssignment(dbNode auxiliaryFunctionWSM, dbNode auxiliaryInputWSM, word auxiliaryFunctionId, word auxiliaryInputId); // form 1
long VTIL_CreateAuxAssignment(dword addressAuxiliaryFunctionWSM, dword addressAuxiliaryInputWSM, word auxiliaryFunctionId, word auxiliaryInputId); // form 2
long VTIL_CreateAuxAssignment(dbNode vt, dbNode auxiliaryFunctionWSM, dbNode auxiliaryInputWSM, word auxiliaryFunctionId, word auxiliaryInputId); // form 3
long VTIL_CreateAuxAssignment(dbNode vt, dword addressAuxiliaryFunctionWSM, dword addressAuxiliaryInputWSM, word auxiliaryFunctionId, word auxiliaryInputId); // form 4
```

## Description

Assigns an Auxiliary Input to an Auxiliary Function.

As a result the Auxiliary Input Status Type 2 Enable command is sent to the Auxiliary Input (if not already enabled) and the Auxiliary Assignment Type 2 command is sent to the Auxiliary Function Working Set Master.

If the participants are using VT Version 0, 1 or 2 only an Auxiliary Assignment Type 1 command is sent to the Auxiliary Input.

## Parameters

| Name | Description |
|---|---|
| Vt | VT simulation node to apply the function |
| auxiliaryFunctionWSM | Working Set Master which provides the Auxiliary Function |
| addressAuxiliaryFunctionWSM | Address of the Working Set Master which provides the Auxiliary Function |
| auxiliaryInputWSM | Working Set Master which provides the Auxiliary Input |
| addressAuxiliaryInputWSM | Address of the Working Set Master which provides the Auxiliary Input |
| auxiliaryFunctionId | Object ID of the Auxiliary Function |
| auxiliaryInputId | Object ID of the Auxiliary Input |

## Example

```c
long result;
result = VTIL_CreateAuxAssignment(VT, Loader, AuxInput, 1001, 1003);
switch (result)
{
  case 0: TestStepPass(); break;
  case -2109: TestStepFail("A Working Set is not available!"); break;
  case -2118: TestStepFail("An object is not suitable!"); break;
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
