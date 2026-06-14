# CANopenUploadGetData

> Category: `CANopen` | Type: `function`

## Syntax

```c
void CANopenUploadGetData( char[] buffer, dword bufferSize, dword errCode[] ); //form 1
void CANopenUploadGetData( byte[] buffer, dword bufferSize, dword errCode[] ); //form 2
```

## Description

Returns the data of a CANopen upload in a callback function as char or byte array.

## Parameters

| Name | Description |
|---|---|
| buffer | Char (form 1) or byte (form 2) array buffer for the data. |
| bufferSize | Size of the buffer in bytes. |
| errCode | Error code buffer (is entered in index 0 of the field). 0: Value was retrieved 1: Value not available |

## Return Values

—

## Example

```c
dword errCode[1];
CANopenUpload ( 1, 0x2000, 0x00, 0, errCode );
if (errCode[0] == 0)
{
  write( "SDO Upload successfully initiated" );
}

void OnCANopenUploadResponse ( dword nodeId, dword index, dword subIndex, dword size )
{
  dword errCode[1];
  char value[100];
  CANopenUploadGetData ( value, elcount(value), errCode );
  write( "Upload response data: %s", value );
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 10.0 | 13.0 | — | — | 2.2 |
| Restricted To | — | CANopen | CANopen | — | — | CANopen |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
