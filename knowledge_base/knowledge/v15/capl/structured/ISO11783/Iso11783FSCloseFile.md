# Iso11783FSCloseFile

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783FSCloseFile( dword fileHandle );
```

## Description

This function closes an opened file or directory.

## Parameters

| Name | Description |
|---|---|
| fileHandle | Handle of the file or directory, which was opened with Iso11783FSOpenFile |

## Return Values

0 or error code

## Example

```c
// handle references a 
 file
LONG handle;
char data[200];

handle = Iso11783FSOpenFile( 
 "\test.TXT", 0x00 );
if (handle > 0) 
 {
  Iso11783FSReadFile( 
 handle, elCount(data), data );
Iso11783FSCloseFile( handle );
}
// handle references a 
 directory
LONG dirHandle;
char data[200];

dirHandle = Iso11783FSOpenFile( 
 "\dir1", 0x03 );
if (dirHandle > 
 0) {
  Iso11783FSReadFile( 
 dirHandle, (elCount(data)-2)/22, data);
Iso11783FSCloseFile( dirHandle );
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
