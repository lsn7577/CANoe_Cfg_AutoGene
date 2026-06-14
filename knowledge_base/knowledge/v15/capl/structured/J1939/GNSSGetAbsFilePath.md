# GNSSGetAbsFilePath

> Category: `J1939` | Type: `function`

## Syntax

```c
long GNSSGetAbsFilePath( char file [], char fileNameWithAbsPath[], long absPathLen )
```

## Description

This function gets the absolute path of a file.

Functionality

## Parameters

| Name | Description |
|---|---|
| file | The file can be defined: with the file name only with the file name and relative path to the current configuration with the absolute path |
| fileNameWithAbsPath | buffer to which the full path name should be copied |
| absPathLen | size of the buffer in bytes for the full path name. |

## Return Values

Error code

## Example

```c
on key 'x'
{
  char absPath[256];

  GNSSGetAbsFilePath("Test.can", absPath, 256);
  write ("absPath 1: %s ", absPath);

  GNSSGetAbsFilePath("Nodes\\Test.can", absPath, 256);
  write ("absPath 1: %s ", absPath);

  GNSSGetAbsFilePath("C:\\Nodes\\Test.can", absPath, 256);
  write ("absPath 1: %s ", absPath);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.6 SP3 | 13.0 | — | — | — |
| Restricted To | — | J1939 ISO11783 | J1939 ISO11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
