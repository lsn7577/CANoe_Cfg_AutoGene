# getAbsFilePath

> Category: `Other` | Type: `function`

## Syntax

```c
long getAbsFilePath(char relPath[], char absPath[], long absPathLen);
```

## Description

Gets the absolute path of a file.

As parameter the file should be defined with the relative path to the current configuration.

## Parameters

| Name | Description |
|---|---|
| relPath | A path (with or without a file name) defined relative to the current configuration. If this parameter is empty, then the full path of the current configuration will simply be returned. |
| absPath | Buffer to which the full path name should be copied. |
| absPathLen | Size of the buffer [in bytes] for the full path name. |

## Return Values

On success this function returns length of the full path name, otherwise -1.

## Example

```c
on key 'x'
{
   char absPath[256];
   getAbsFilePath("Nodes\\Test.can", absPath, 256);
   write ("absPath: %s ", absPath);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.1 | 5.1 | 13.0 | — | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | ✔ | N/A |
