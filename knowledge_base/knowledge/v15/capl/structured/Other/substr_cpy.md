# substr_cpy

> Category: `Other` | Type: `function`

## Syntax

```c
void substr_cpy(char dest[], char src[], long srcStart, long len, long max);
```

## Description

This function copies a substring of src to dest. max indicates the size of dest in bytes. The function ensures that there is a terminating '\0'. Thus, a maximum of max-1 bytes are copied.

## Parameters

| Name | Description |
|---|---|
| dest | Destination buffer |
| src | Source string |
| srcStart | Start index in bytes in src of substring |
| len | Length of the substring in bytes, or -1 to copy the string until the end |
| max | Size of dest in bytes |

## Return Values

—

## Example

```c
char s1[7];
char s2[18] = "Vector Informatik";
substr_cpy(s1, s2, 0, 6, elcount(s1)); // s1: Vector
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
