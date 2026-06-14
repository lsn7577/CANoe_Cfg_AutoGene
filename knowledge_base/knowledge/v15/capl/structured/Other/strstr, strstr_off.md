# strstr, strstr_off

> Category: `Other` | Type: `function`

## Syntax

```c
long strstr(char s1[], char s2[]);
long strstr_off(char s1[], long offset, char s2[]);
```

## Description

Searches in s1 for s2.

## Parameters

| Name | Description |
|---|---|
| s1 | First string |
| offset | Offset in s1 in bytes at which the search shall be started |
| s2 | Second string |

## Return Values

First position in bytes of s2 in s1, or -1 if s2 is not found in s1.

## Example

```c
long pos;
char s1[18] = "Vector Informatik";
char s2[11] = "Informatik";
pos = strstr(s1, s2); // pos = 7
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.0 | 7.0 | 13.0 | 13.0 | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | ✔ | N/A |
