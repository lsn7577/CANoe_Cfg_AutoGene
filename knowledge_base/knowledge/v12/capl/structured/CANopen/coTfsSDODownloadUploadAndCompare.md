# coTfsSDODownloadUploadAndCompare

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsSDODownloadUploadAndCompare( dword index, dword subIndex, dword size, qword downloadValue ); // form 1
```

## Description

This function executes a complete SDO download to write the object value and after that a SDO upload to read the written value. Depending on the number of data, this is either an expedited upload (up to 4 bytes) or a segmented transfer. Afterwards the received data is compared against the data supplied.

It is not possible to fetch the received data using coTfsGetSdoUploadData after this function was called.

(2) can be used for maximum 4 byte objects only.

## Return Values

error code or
