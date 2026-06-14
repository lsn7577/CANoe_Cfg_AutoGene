# fileGetString

> Category: `Other` | Type: `function`

## Syntax

```c
long fileGetString (char buff[], long buffsize, dword fileHandle);
```

## Description

The function reads a string from the specified file into the buffer buff.

Characters are read until the end of line is reached or the number of read characters is equal to buffsize -1.The end of line is marked either

The end of line in the buffer is represented by a line feed. See also fileGetStringSZ.

If the end of a line was encountered, the returned string contains a new line character. Else, the next call to fileGetString will start reading in the last line starting with the first character which didn't fit into the buffer on the previous call.

## Parameters

| Name | Description |
|---|---|
| buff | Buffer for the read-out string. |
| buffsize | Length of the string. |
| fileHandle | Handle to the file. |

## Return Values

If an error occurs, the return value is 0, else 1.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 3.0 7.0 SP5: method | 3.0 7.0 SP5: method | 13.0 | — | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | ✔ | N/A |
