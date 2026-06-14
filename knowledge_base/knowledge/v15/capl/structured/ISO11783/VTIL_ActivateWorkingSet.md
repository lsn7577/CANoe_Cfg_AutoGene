# VTIL_ActivateWorkingSet

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_ActivateWorkingSet(dbNode workingSetMaster); // form 1
long VTIL_ActivateWorkingSet(byte workingSetMasterAddress); // form 2
long VTIL_ActivateWorkingSet(dbNode vt, dbNode workingSetMaster); // form 3
long VTIL_ActivateWorkingSet(dbNode vt, byte workingSetMasterAddress); // form 4
```

## Description

Activates a corresponding Working Set in the Virtual Terminal: As a result, the VT Status message is sent with the source address of newly activated Working Set as well as its active Data/Alarm and Soft Key Mask.

## Parameters

| Name | Description |
|---|---|
| vt | VT simulation node to apply the function |
| workingSetMaster | Working Set Master node |
| workingSetMasterAddress | Address of the Working Set Master |

## Example

Example for test node

```c
long result;
result = VTIL_ActivateWorkingSet(VT, Sprayer);
switch (result)
{
  case 0: TestStepPass(); break;
  case -2109: TestStepFail ("Working Set 'Sprayer' is not available!"); break;
  case -2110: TestStepFail ("Failed to activate Working Set 'Sprayer'!"); break;
  default:    TestStepFail ("Unexpected error"); break;
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 | 13.0 | — | — | 2.1 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 3, 4 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1, 2) | ✔ (form 1, 2) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 3, 4) | ✔ (form 3, 4) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 3, 4) | ✔ (form 3, 4) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
