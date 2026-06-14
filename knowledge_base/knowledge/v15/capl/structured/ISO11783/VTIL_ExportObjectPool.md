# VTIL_ExportObjectPool

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_ExportObjectPool(dbNode workingSetMaster, char objectPoolFilePath[]); // form 1
long VTIL_ExportObjectPool(dword addressWorkingSetMaster, char objectPoolFilePath[]); // form 2
long VTIL_ ExportObjectPool (dbNode vt, dbNode workingSetMaster, char objectPoolFilePath []); // form 3
long VTIL_ ExportObjectPool (dbNode vt, dword addressWorkingSetMaster, char objectPoolFilePath []); // form 4
```

## Description

Exports the current object pool of the Working Set Master into a file (*.iop). An existing file is overwritten.

## Parameters

| Name | Description |
|---|---|
| vt | VT simulation node to apply the function |
| workingSetMaster | Working Set Master which object pool is exported (must not be the active Working Set). |
| addressWorkingSetMaster | Address of the Working Set Master which object pool is exported (must not be the active Working Set). |
| objectPoolPath | Path to the *.iop file the object pool has be exported to. Path has to be absolute or relative relating to the folder of the CANoe configuration. |
| versionLabel | The Virtual Terminal IL stores the object pool with this label |

## Example

Example form 3

```c
long result;
result = VTIL_ExportObjectPool(VT, Loader, "c:\\temp\\Loader.iop");
switch (result)
{
  case 0: TestStepPass(); break;
  case -2113: TestStepFail("Invalid parameter!"); break;
  case -2122: TestStepFail("Failed to export object pool to file!"); break;
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
