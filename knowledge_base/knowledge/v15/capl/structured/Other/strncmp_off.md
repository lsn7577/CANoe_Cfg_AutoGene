# strncmp_off

> Category: `Other` | Type: `function`

## Syntax

```c
long strncmp_off(char s1[], long s1offset, char s2[], long s2offset, long len);
```

## Description

This function compares s1 with s2 for a maximum of len bytes.

If they are identical the functional result is 0. If s1 is less than s2 the result is -1, else +1. Comparison starts in s1 at s1offset and in s2 at s2offset.

## Parameters

| Name | Description |
|---|---|
| s1 | First string |
| s2 | Second string |
| s1offset | Offset in s1 in bytes |
| s2offset | Offset in s2 in bytes |
| len | Maximum number of bytes to compare |

## Example

```c
char s1[18] = "Vector Informatik";
char s2[11] = "Informatik";
if (strncmp_off(s1, 7, s2, 0, strlen(s2)) == 0)
   write("Equal!");
else
   write("Unequal!");
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
