# Iso11783FSGetFileInfo

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783FSGetFileInfo( dword fileHandle, dword infoCount, dword retInfo[] );
long Iso11783FSGetFileInfo( char fileName[], dword infoCount, dword retInfo[] );
```

## Description

This function retrieves information about a file or directory. In the entry of the array, the following information is returned:

## Parameters

| Name | Description |
|---|---|
| fileHandle | File or directory handle, see also Iso11783FSOpenFile |
| fileName | Name of file or directory |
| infoCount | Number of elements in retInfo |
| retInfo | Contains the information about the file or directory |

## Return Values

0 or error code

## Example

```c
LONG handle;
dword info[8];

handle = Iso11783FSOpenFile( "\TEST.TXT", 0x00 );
if (handle > 0) {
  if (Iso11783FSGetFileInfo( handle, elCount(info), info ) == 0) {
    write( "Date %d-%d-%d'", info[2], info[3], info[4] );
  }
  Iso11783FSCloseFile( handle );
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.1 | 13.0 | — | — | — |
| Restricted To | — | ISO11783 | ISO11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
