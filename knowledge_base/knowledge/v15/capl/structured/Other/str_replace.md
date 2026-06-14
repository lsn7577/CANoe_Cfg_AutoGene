# str_replace

> Category: `Other` | Type: `function`

## Syntax

```c
long str_replace(char s[], char searched[], char replacement[]); // form 1
long str_replace(char s[], long startoffset, char replacement[], long length); // form 2
```

## Description

Form 1: Replaces all occurrences of a text in a string with another string.

Form 2: Replaces a part of a string with another string.

## Parameters

| Name | Description |
|---|---|
| s | String to be modified. |
| searched | Text which shall be replaced. |
| startoffset | Offset at which to start replacing characters. |
| replacement | Text which replaces the original characters. |
| length | Maximum number of characters to replace. |

## Return Values

1 if successful, 0 if the resulting string would be too long for the buffer s.

## Example

```c
char buffer[70] = "Vector Informatik";
str_replace(buffer, "Informatik", "CANoe");
write(buffer);
str_replace(buffer, 7, "CANalyzer", 10);
write(buffer);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.5 SP2 | 7.5 SP2 | 13.0 | 13.0 | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | ✔ | N/A |
