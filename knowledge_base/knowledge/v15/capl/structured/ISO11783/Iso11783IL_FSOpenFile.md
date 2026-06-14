# Iso11783IL_FSOpenFile

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_FSOpenFile( char path[], dword flags );
```

## Description

This function opens a file or directory.

## Parameters

| Name | Description |
|---|---|
| path | Absolute path of the file |
| Bit | Description |
| 1-2 | 0: Read only 1: Write only 2: Read and write 3: Open directory for reading |
| 3 | 0: Open an existing file or directory 1: Create a new file or directory if not yet existing |
| 4 | 0: Random access 1: Append |
| 5 | 0: Shared access 1: Exclusive access |

## Example

```c
LONG handle;
char data[200];

handle = Iso11783IL_FSOpenFile( 
 "\test.TXT", 0x00 );
if (handle > 0) 
 {
  Iso11783IL_FSReadData( 
 handle, elCount(data), data );
  Iso11783IL_FSCloseFile( 
 handle );
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0 | 13.0 | — | — | — |
| Restricted To | — | ISO11783 | ISO11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
