# getProfileString

> Category: `Other` | Type: `function`

## Syntax

```c
long getProfileString(char section[], char entry[], char def[], char buff[], long buffsize, char filename[]); // form 1
long getProfileString(char section[], char entry[], char def[], char buff[], long buffsize, char filename[], dword utf16); // form 2
```

## Description

Searches the file filename under section section for the variable entry. Its contents (value) are written to the buffer buff. Its length must be passed correctly in buffsize.

If the file or entry is not found, the default value def is copied to buffer.

If the read string length is longer than the buffer, the string will be cut to the buffer length.

## Parameters

| Name | Description |
|---|---|
| section | Section of the file as a string. |
| entry | Variable name as a string. |
| def | Default value in case of error as a string. |
| buff | Buffer for the read-in character as a string. |
| buffersize | Size of buff in bytes (max. 1022 characters). |
| filename | File name as a string. |
| utf16 | If this flag is set the file will be interpreted as UTF-16LE encoded, if the corresponding BOM is also present. The string written to buff will be converted to the CAPL encoding. |

## Return Values

Length of the read string.
Length of the default string: Fault Key not found
-1: Fault File not found

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
