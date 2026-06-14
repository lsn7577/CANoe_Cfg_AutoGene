# writeProfileFloat

> Category: `Other` | Type: `function`

## Syntax

```c
long writeProfileFloat(char section[], char entry[], float value, char filename[]); // form 1
long writeProfileFloat(char section[], char entry[], float value, char filename[], dword utf16); // form 2
```

## Description

Opens the file filename, searches the section section and writes the variable entry with the value value. If entry already exists the old value is overwritten.

## Parameters

| Name | Description |
|---|---|
| section | Section of the file as a string. |
| entry | Variable name as a string. |
| value | Value as a float. |
| filename | File path as a string. |
| utf16 | If this flag is set the file will be UTF-16LE encoded if it is newly written, or interpreted as such, if the corresponding BOM is also present. |

## Return Values

The functional result is 0 in case of an error.

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
