# coTfsSDODownload

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsSDODownload( dword index, dword subIndex, dword size, byte inValueBuf[], dword valueBufSize ); // form 1
```

## Description

This function makes available the complete SDO download functionality. It can be used in order to transfer data to the desired CANopen® device easily.

Form 1: Depending on the data length, either an expedited or segmented download is executed.

Form 2: This function syntax can only be used for expedited download.

## Return Values

Error code

## Example

```c
coTfsSDODownload ( 0x1017, 0, 2, pdata, 2);
```
