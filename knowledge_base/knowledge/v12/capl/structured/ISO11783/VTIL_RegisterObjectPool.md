# VTIL_RegisterObjectPool

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_RegisterObjectPool(dbNode workingSetMaster, char[] objectPoolPath[], char[] versionLabel); // form 1
```

## Description

Registers an object pool file (iop).

A registered object pool can be loaded via the Load Version command.

For more information see chapter Save Object Pools in VT Storage.

## Return Values

0: Function has been executed successfully

## Example

```c
long result;
result = VTIL_RegisterObjectPool( VT, Sprayer, "iop\\sprayerV1.iop", "sprayV1");
if (result < 0)
{
  TestStepFail("Failed to register file!");
}
```

## Availability

| Since Version |
|---|
