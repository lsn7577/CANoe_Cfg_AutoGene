# strstr_regex, strstr_regex_off

> Category: `Other` | Type: `function`

## Syntax

```c
long strstr_regex(char s[], char pattern[]);
long strstr_regex_off(char s[], long offset, char pattern[]);
```

## Description

Searches for a regular expression pattern in a string.

## Parameters

| Name | Description |
|---|---|
| s | String to be searched. |
| offset | Offset in s at which the search shall be started. |
| pattern | Regular expression which is searched. For the regular expression, the same syntax is used as in the Perl programming language. |

## Return Values

The position in s where the pattern was found, or -1 if it wasn’t found.

## Example

```c
char buffer[70] = "Vector Informatik";
long res;
res = strstr_regex(buffer, "Inf[a-z]*"); // 7
res = strstr_regex_off(buffer, res + 1, "Inf[a-z]*"); // -1
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
