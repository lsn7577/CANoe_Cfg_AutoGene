# VTIL_SaveAsImage

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_SaveAsImage(dbNode workingSetMaster, dword maskOrSoftkey, char imagePath[]); // form 1
```

## Description

Saves the current Data/Alarm Mask or one of the current Soft Keys as an image. An existing file is overwritten.

## Return Values

0: Function has been executed successfully

## Example

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

| Since Version |
|---|
