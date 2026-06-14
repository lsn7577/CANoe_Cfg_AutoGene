# openFileWrite

> Category: `Other` | Type: `function`

## Syntax

```c
dword openFileWrite (char filename[], dword mode); // form 1
dword openFileWrite (char filename[], dword mode, dword fileEncoding); // form 2
```

## Description

This function opens the file named filename for the write access.

If mode=0 writing can be executed in text mode; if mode=1 writing can be executed in binary mode. An already existing file will be overwritten.

mode=2 to append data at the end of the file use for text mode.mode=3 to append data at the end of the file for binary mode.

## Parameters

| Name | Description |
|---|---|
| filename | file name |
| mode |  |
| fileEncoding | Identifier of the Microsoft code page that is used to encode the file. |

## Return Values

The return value is the file handle that must be used for write operations.
If an error occurs, the return value is 0.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 3.0: form 1 12.0: form 2 | 3.0: form 1 12.0: form 2 | 13.0 | — | 14 | 1.0: form 1 4.0: form 2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | ✔ | N/A |
