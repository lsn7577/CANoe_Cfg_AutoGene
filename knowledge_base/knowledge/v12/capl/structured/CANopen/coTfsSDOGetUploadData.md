# coTfsSDOGetUploadData

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsSDOGetUploadData( byte outValueBuf[], dword valueBufSize );
```

## Description

This function makes available the data of the last successful SDO upload procedure. This can be an expedited, segmented or block transfer.

The data field outValueBuf must always be able to accommodate the received data.

## Example

```c
see example of coTfsSDOInit
```
