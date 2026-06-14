# VTIL_SaveAsImage

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_SaveAsImage(dbNode workingSetMaster, dword maskOrSoftkey, char imagePath[]); // form 1
long VTIL_SaveAsImage(dword addressWorkingSetMaster, dword maskOrSoftkey, char imagePath[]); // form 2
long VTIL_SaveAsImage(dbNode vt, dbNode workingSetMaster, dword maskOrSoftkey, char imagePath[]); // form 3
long VTIL_SaveAsImage(dbNode vt, dword addressWorkingSetMaster, dword maskOrSoftkey, char imagePath[]); // form 4
```

## Description

Saves the current Data/Alarm Mask or one of the current Soft Keys as an image. An existing file is overwritten.

## Parameters

| Name | Description |
|---|---|
| vt | VT simulation node to apply the function |
| workingSetMaster | Working Set Master which Data/Alarm Mask or Soft Key is saved as an image (must not be the active Working Set) |
| addressWorkingSetMaster | Address of the Working Set Master which Data/Alarm Mask or Soft Key is saved as an image (must not be the active Working Set) |
| maskOrSoftkey | 0: Current active Data or Alarm Mask 1-64: A current active Soft Key |
| imagePath | Saves the current Data/Alarm Mask of soft key in this file (*.bmp, *.png, *.jpg or *.gif). Path has to be absolute or relative relating to the folder of the CANoe configuration. |

## Example

Example form 3

```c
long result;
result = VTIL_SaveAsImage(VT, Loader, 0, "BMP\\DataMask.bmp");
switch (result)
{
  case 0: TestStepPass(); break;
  case -2113: TestStepFail("Invalid parameter!"); break;
  case -2122: TestStepFail("Failed to save active Data Mask to file!"); break;
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
