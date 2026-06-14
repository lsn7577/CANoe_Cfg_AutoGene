# coTfsSDODownload

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsSDODownload( dword index, dword subIndex, dword size, byte inValueBuf[], dword valueBufSize ); // form 1
long coTfsSDODownload( dword index, dword subIndex, dword size, qword inValue); // form 2
```

## Description

This function makes available the complete SDO download functionality. It can be used in order to transfer data to the desired CANopen® device easily.

Form 1: Depending on the data length, either an expedited or segmented download is executed.

Form 2: This function syntax can only be used for expedited download.

## Parameters

| Name | Description |
|---|---|
| index | Object index |
| subIndex | Object sub index |
| size | Number of bytes to be transmitted. |
| inValueBuf[] | Data field for transfer data. |
| valueBufSize | Buffer size in byte of inValueBuf. |
| inValue | Data to be transmitted. |

## Return Values

Error code

## Example

```c
coTfsSDODownload ( 0x1017, 0, 2, pdata, 2);
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
