# substr_cpy_off

> Category: `Other` | Type: `function`

## Syntax

```c
void substr_cpy_off(char dest[], long destOffset, char src[], long srcStart, long len, long max);
```

## Description

This function copies a substring of src to dest. max indicates the the size of dest in bytes. The function ensures that there is a terminating ‘\0’. Thus, a maximum of max-1-destOffset bytes are copied.

## Parameters

| Name | Description |
|---|---|
| dest | Destination buffer |
| destOffset | Offset in bytes in destination buffer |
| src | Source string |
| srcStart | Start index in bytes in src of substring |
| len | Length of the substring in bytes, or -1 to copy the string until the end |
| max | Size of dest in bytes |

## Return Values

—

## Example

```c
char s1[9] = "New CAPL";
char s2[18] = "Vector Informatik";
substr_cpy_off(s2, 7, s1, 4, -1, elcount(s2)); // s2: Vector CAPL
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
