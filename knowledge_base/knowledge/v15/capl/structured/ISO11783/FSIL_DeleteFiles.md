# FSIL_DeleteFiles

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long FSIL_DeleteFiles( char path[], byte options); // form 1
long FSIL_DeleteFiles( dbNode fs, char path[], byte options); // form 2
```

## Description

Deletes a file or directory of the File Server.

## Parameters

| Name | Description |
|---|---|
| fs | FS simulation node to apply the function |
| path | Path of a file or directory to delete. The path is absolute or relative to the root directory of the File Server. If the path is an empty string then all directories and files of the root directory are deleted. |
| options | Bit 0 = 0: The specified file or directory is deleted Bit 0 = 1: Only the content of the specified directory is deleted (this value is only valid if parameter path is a directory) |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 12.0 | 13.0 | — | — | 4.0 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 2 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
