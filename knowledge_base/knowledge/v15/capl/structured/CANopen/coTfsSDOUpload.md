# coTfsSDOUpload

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsSDOUpload( dword index, dword subIndex ); // form 1
long coTfsSDOUpload( dword index, dword subIndex, dword outSize[1], byte outValueBuf[], dword valueBufSize ); // form 2
long coTfsSDOUpload( dword index, dword subIndex, dword outSize, qword outValueBuf); // form 3
```

## Description

This function executes a complete SDO upload. Depending on the number of data, this is either an expedited upload (up to 4 bytes) or a segmented transfer. After a successful upload, the data received can be called up with the command coTfsGetSdoUploadData. (form 1)

Alternatively the function can return the received data automatically. (form 2)

This function syntax can only be used for expedited uploads. (form 3)

## Parameters

| Name | Description |
|---|---|
| index | Object index |
| subIndex | Object sub index |
| outSize[1] | Data length pointer |
| outValueBuf[] | Received data pointer |
| valueBufSize | Buffer size in byte of outValueBuf. |
| outSize | Size of the data to be transmitted. |
| outValueBuf | Data to be transmitted. |

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

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 | 13.0 | — | — | 2.1 SP3 |
| Restricted To | — | CANopen | CANopen | — | — | CANopen |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
