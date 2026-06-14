# VTIL_ExportObjectPool

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_ExportObjectPool(dbNode workingSetMaster, char objectPoolFilePath[]); // form 1
```

## Description

Exports the current object pool of the Working Set Master into a file (*.iop). An existing file is overwritten.

## Return Values

0: Function has been executed successfully

## Example

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

| Since Version |
|---|
