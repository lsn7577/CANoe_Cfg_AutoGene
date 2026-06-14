# coTfsODRunUserDownloadUploadAndCompareTest

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsODRunUserDownloadUploadAndCompareTest( void );
```

## Description

This function executes a SDO Download and a SDO Upload for all objects that are defined in the internal list of test objects (see coTfsODAddEntry). It checks if the written data are conform to the stored data as well as the read data.

## Return Values

Error code

## Example

```c
see example of coTfsODAddEntryIndexRange
```
