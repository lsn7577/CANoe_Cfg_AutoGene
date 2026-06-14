# coTfsSDODownloadUploadAndCompare

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsSDODownloadUploadAndCompare( dword index, dword subIndex, dword size, qword downloadValue ); // form 1
long coTfsSDODownloadUploadAndCompare( dword index, dword subIndex, dword size, byte downloadValueBuf[], dword valueBufSize ); // form 2
```

## Description

This function executes a complete SDO download to write the object value and after that a SDO upload to read the written value. Depending on the number of data, this is either an expedited upload (up to 4 bytes) or a segmented transfer. Afterwards the received data is compared against the data supplied.

It is not possible to fetch the received data using coTfsGetSdoUploadData after this function was called.

(2) can be used for maximum 4 byte objects only.

## Parameters

| Name | Description |
|---|---|
| index | Object index |
| subIndex | Object sub index |
| size | Expected data length. |
| downloadValue | Value that is to be written. |
| downloadValueBuf[] | Data pointer for data to be written. |
| valueBufSize | Buffer size in byte of downloadValueBuf. |

## Return Values

error code or

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
