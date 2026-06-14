# Iso11783IL_FSSeekFile

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_FSSeekFile( dword fileHandle, dword mode, dword offset );
```

## Description

This function moves the current write/read position of an open file or the read position of directory entries within a directory.

## Parameters

| Name | Description |
|---|---|
| fileHandle | File or directory handle, see also Iso11783IL_FSOpenFile |
| mode | 0: from the beginning of the file/from the first directory entry 1: from the current pointer position 2: from the end of the file/from the last directory entry |
| offset | Number of bytes to move the file pointer or the number of directory entries to move the directory pointer |

## Example

```c
Iso11783IL_FSSeekFile( handle, 0, 10 );
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
