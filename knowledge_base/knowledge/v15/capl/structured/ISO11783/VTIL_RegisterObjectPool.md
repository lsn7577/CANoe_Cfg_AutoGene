# VTIL_RegisterObjectPool

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_RegisterObjectPool(dbNode workingSetMaster, char[] objectPoolPath[], char[] versionLabel); // form 1
long VTIL_RegisterObjectPool(dword addressWorkingSetMaster, char[] objectPoolPath[], char[] versionLabel); // form 2
long VTIL_RegisterObjectPool(dbNode vt, dbNode workingSetMaster, char[] objectPoolPath[], char[] versionLabel); // form 3
long VTIL_RegisterObjectPool(dbNode vt, dword addressWorkingSetMaster, char[] objectPoolPath[], char[] versionLabel); // form 4
```

## Description

Registers an object pool file (iop).

A registered object pool can be loaded via the Load Version command.

For more information see chapter Save Object Pools in VT Storage.

## Parameters

| Name | Description |
|---|---|
| vt | VT simulation node to apply the function |
| workingSetMaster | Working Set Master to which the Object Pool belongs |
| addressWorkingSetMaster | Address of the Working Set Master to which the Object Pool belongs |
| objectPoolPath | Path of an object pool file (*.iop). Path has to be absolute or relative relating to the folder of the CANoe configuration. |
| versionLabel | The Virtual Terminal IL stores the object pool with this label |

## Example

Example form 3, 4

```c
long result;
result = VTIL_RegisterObjectPool( VT, Sprayer, "iop\\sprayerV1.iop", "sprayV1");
if (result < 0)
{
  TestStepFail("Failed to register file!");
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
