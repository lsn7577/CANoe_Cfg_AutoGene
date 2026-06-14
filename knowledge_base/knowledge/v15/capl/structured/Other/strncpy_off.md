# strncpy_off

> Category: `Other` | Type: `function`

## Syntax

```c
void strncpy_off(char dest[], long destOffset, char src[], long max);
```

## Description

This function copies src to dest. max indicates the size of dest in bytes.

The function ensures that there is a terminating '\0'. Thus, a maximum of max-1-destOffset bytes are copied. Bytes are overwritten in dest starting at destOffset.

## Parameters

| Name | Description |
|---|---|
| dest | Destination buffer |
| destOffset | Offset in destination buffer |
| src | Source string |
| max | Is used to determine the maximum number of copied bytes.Must not be larger than the size of dest. A maximum of max-1-destOffset bytes are copied.If src is shorter than that, bytes are only copied until a terminating '\0' is encountered. |

## Return Values

—

## Example

```c
char s[6] = "Hello";
strncpy_off(s, 1, "e", elcount(s)); // s: He
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
