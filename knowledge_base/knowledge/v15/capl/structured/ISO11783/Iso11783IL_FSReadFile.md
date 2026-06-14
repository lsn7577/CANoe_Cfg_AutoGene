# Iso11783IL_FSReadFile

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_FSReadFile( dword fileHandle, dword bufferSize, char buffer[] );
long Iso11783IL_FSReadFile( dword fileHandle, dword bufferSize, byte buffer[] );
long Iso11783IL_FSReadFile( dword fileHandle, dword bufferSize, char buffer[], long flags);
long Iso11783IL_FSReadFile( dword fileHandle, dword bufferSize, byte buffer[], long flags);
```

## Description

The function reads data from an open file and directory entries from an open directory respectively.

Whenever reading directory entries, ensure that handle consists of at least (n * 22 + 2) bytes (n = the number of directory entries to read passed in size. 22 bytes is a maximum length directory entry when the file name length is 12 characters (subject to the 8.3 naming convention). Two bytes are used for the word in buffer[0] and buffer[1] with the number of directory entries actually read).

## Parameters

| Name | Description |
|---|---|
| fileHandle | File or directory handle, see also Iso11783IL_FSOpenFile |
| bufferSize | Size of buffer in Bytes (handle references file) or number of directory entries to read (handle references directory) |
| Structure of a Directory Entry |  |
| Byte 1 | Length (bytes) of the file or directory name |
| Byte 2-n | File or directory name |
| Byte n+1 | Attributes (see Iso11783IL_GetFileInfo) |
| Bytes n+2, n+3 | Date bits 1..5: day bits 6..9: month bits 10..16: year-1939 |
| Bytes m+4, n+5 | Time bits 1..5: seconds/2 bits 6..11: minutes bits 12..16: hours |
| Bytes n+6..n+9 | Size of the file/directory |
| flags | Bit 0: if this bit is set hidden files are listed during reading directories |

## Example

```c
// Read data from file
LONG handle;
char data[200];

handle = Iso11783IL_FSOpenFile( "\test.TXT", 0x00 );
if (handle > 0) {
   Iso11783IL_FSReadFile( handle, elCount(data), data );
  Iso11783IL_FSCloseFile( handle );
} 

                                
// Read directory entries:
LONG handle;
char data[200];

handle = Iso11783IL_FSOpenFile( "\DIR1", 0x03 );
if (handle > 0) {
   Iso11783IL_FSReadFile( handle, (elCount(data)-2)/22, data );
  Iso11783IL_FSCloseFile( handle );
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
