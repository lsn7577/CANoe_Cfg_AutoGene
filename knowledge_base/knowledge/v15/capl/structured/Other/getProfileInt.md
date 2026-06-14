# getProfileInt

> Category: `Other` | Type: `function`

## Syntax

```c
long getProfileInt(char section[], char entry[], long def, char filename[]); // form 1
long getProfileInt(char section[], char entry[], long def, char filename[], dword utf16); // form 2
```

## Description

Searches the file filename under section section for the variable entry. If its value is a number, this number is returned as the functional result. If the file or entry is not found, or if entry does not contain a valid number, the default value def is returned as the functional result.

## Parameters

| Name | Description |
|---|---|
| section | Section of the file as a string. |
| entry | Variable name as a string. |
| def | Default value in case of error as an integer. |
| filename | File path as a string. |
| utf16 | If this flag is set the file will be interpreted as UTF-16LE encoded, if the corresponding BOM is also present. |

## Return Values

Integer that was read in.

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
