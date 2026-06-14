# coTfsSDOUpload

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsSDOUpload( dword index, dword subIndex ); // form 1
```

## Description

This function executes a complete SDO upload. Depending on the number of data, this is either an expedited upload (up to 4 bytes) or a segmented transfer. After a successful upload, the data received can be called up with the command coTfsGetSdoUploadData. (form 1)

Alternatively the function can return the received data automatically. (form 2)

This function syntax can only be used for expedited uploads. (form 3)

## Return Values

Error code

## Example

```c
dword dataLength, i;
byte pReceiveData[2048];

if ( coTfsSDOUpload(0x2000, 2) != 1) {
  write("SDO upload failed");
  return;
} // if

if ((dataLength = coTfsSDOGetUploadData( pReceiveData, 2048)) > 0) {
  write("datalength = %d",dataLength);
  for (i = 0; i< dataLength; i++) {
    write("data %i = 0x%X",i,pReceiveData[i]);
  } // for
} // if
else {
  write("no data available");
} // else
```
