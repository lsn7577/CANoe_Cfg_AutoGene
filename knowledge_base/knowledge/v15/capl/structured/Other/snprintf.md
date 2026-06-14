# snprintf

> Category: `Other` | Type: `function`

## Syntax

```c
long snprintf(char dest[], long len, char format[], ...);
```

## Description

This function corresponds to the C function sprintf. Supplementally, the parameter len indicates the maximum length of the array dest.

The format string has the same meaning as with the function write and is described there.

## Parameters

| Name | Description |
|---|---|
| dest | Character buffer to print to. |
| len | Maximum number of characters printed to buffer including terminating '\0'.Must be at most the size of the buffer. |
| format | Formatted string printed to buffer. |

## Return Values

The number of characters written.

## Example

```c
char buffer[100], str[7] = "Vector";
long i;
i = snprintf(buffer,elcount(buffer),"String: %s\n", str);
write("Output:\n%s : Character count = %d\n", buffer, i);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | All | All | 13.0 | 13.0 | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | ✔ | N/A |
