# fileGetStringSZ

> Category: `Other` | Type: `function`

## Syntax

```c
long fileGetStringSZ(char buff[], long buffsize, dword fileHandle);
```

## Description

The function reads a string from the specified file.

Characters are read until the end of line is reached or the number of read characters is equal to buffsize -1.The end of line is marked either

No line feed character will be contained in the buffer. See also fileGetString.

## Parameters

| Name | Description |
|---|---|
| buff | Buffer for the read-out string |
| buffsize | Length of the string |
| fileHandle | Handle to the file |

## Return Values

If an error occurs, the return value is 0, else 1.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 3.0 7.0 SP5: method | 3.0 7.0 SP5: method | 13.0 | 13.0 | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | ✔ | N/A |
