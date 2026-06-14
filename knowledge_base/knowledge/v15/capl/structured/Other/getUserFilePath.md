# getUserFilePath

> Category: `Other` | Type: `function`

## Syntax

```c
long getUserFilePath(char fileName[], char absPath[], long absPathLen);
```

## Description

Gets the absolute path of a user file.

In case of execution in a distributed environment the absolute user file path (including file name) on the remote device (e.g. VN8900) is returned if the user file was pre-defined. If the file was not pre-defined an error code is returned.

In case of a single Computer environment the registered absolute file path (including file name) of the user file is returned if the user file was pre-defined. If the file was not pre-defined the function returns the same result as getAbsFilePath (converting a path relative to the configuration directory to an absolute path).

## Parameters

| Name | Description |
|---|---|
| fileName | A file name potentially containing a path. If the file name is pre-defined the path is ignored. Otherwise the path is interpreted as relative to the current configuration path in a single Computer environment. |
| absPath | Buffer to which the full path name should be copied. |
| absPathLen | Size of the buffer [in bytes] for the full path name. |

## Return Values

On success this function returns the length of the full path name. Otherwise the function returns -1 if parameters do not fit or buffer size is too small or -2 if no user file with the given name was registered in case of a distributed environment.

## Example

```c
on preStart
{
   char absPath[256];
   VgetUserFilePath("MyCAPLDll.INI", absPath, 256);
   MyCAPLDllFunction(absPath);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.6 SP4 | 13.0 | — | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
