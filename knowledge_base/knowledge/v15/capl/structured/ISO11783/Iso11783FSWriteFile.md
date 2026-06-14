# Iso11783FSWriteFile

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783FSWriteFile( dword fileHandle, dword bufferSize, char buffer[] );
long Iso11783FSWriteFile( dword fileHandle, dword bufferSize, byte buffer[] );
```

## Description

This function writes data to an open file.

## Parameters

| Name | Description |
|---|---|
| fileHandle | File handle, see also Iso11783FSOpenFile |
| bufferSize | Number of bytes to write |
| buffer | Data to write |

## Example

```c
LONG handle;
char data[200];

handle = Iso11783FSOpenFile( "\test.TXT", 0x02 );
if (handle > 0) {
Iso11783FSWriteFile( handle, 12, "Hello World!" );
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
