# FSIL_ImportFiles

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long FSIL_ImportFiles( char targetPath[], char sourcePath[]); // form 1
```

## Description

Imports files into the File Server.

Adds a file or the content of a local directory to the File Server. Existing directories and files are replaced if they are not write protected.

## Return Values

0: Property has been set successfully

## Example

```c
FSIL_ImportFiles(“Volume1\MSM1861\VT1”, “VT1_Pools”);

FSIL_ImportFiles(“Volume1\MSM1861\VT1”, “VT1_Pools\2FB3AAE801840CA0_SprayV0.iop”);

FSIL_ImportFiles(“”, “Volume1\MSM1861\VT1\VT1_Pools”);
```

## Availability

| Since Version |
|---|
