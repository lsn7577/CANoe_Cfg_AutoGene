# Iso11783FSMakeAbsolutePath

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783FSMakeAbsolutePath( char relPath[], char absPath[], dword mustExist, dword bufferSize, char buffer[] );
long Iso11783FSMakeAbsolutePath( char relPath[], char absPath[], dword mustExist, dword bufferSize, char buffer[], char volume[], long manufacturerCode );
```

## Description

This function converts an relative path into an absolute path including a conversion to uppercase characters. An absolute path begins with \ and refers to the root directory (see also Iso11783SetPath). A relative path could contain .. and ..

A path must follow the 8.3 format (8 character identifier with 4 character extension).

## Parameters

| Name | Description |
|---|---|
| relPath | Relative path which could contain .. and . |
| absPath | Absolute path |
| mustExist | 1: check, if path exists and return an error if the file does not exist 0: the path must not exist |
| bufferSize | Size of buffer in byte |
| buffer | New path is copied to this buffer |
| volume | Name of the volume, this information and the manufacturer code are needed to resolve the root directory in the paths |
| manufacturerCode | Manufacturer code, this information and the volume are needed to resolve the root directory in the paths |

## Return Values

0 or error code

## Example

```c
char defaultDirectory[64] = "\IMPL";
char newPath[255];

if (Iso11783FSMakeAbsolutePath( "..\DATA", defaultDirectory, 1, elCount(newPath), newPath ) == 0) {
  write( "Path '%s'", newPath );
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
