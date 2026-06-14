# str_match_regex

> Category: `Other` | Type: `function`

## Syntax

```c
long str_match_regex(char s[], char pattern[]);
```

## Description

Checks whether a string completely matches a regular expression pattern.

## Parameters

| Name | Description |
|---|---|
| s | String to be checked. |
| pattern | Regular expression against which the string is matched. For the regular expression, the same syntax is used as in the Perl programming language. |

## Return Values

1 if the string matches the pattern, 0 if it doesn’t match the pattern.

## Example

```c
char buffer[70] = "Vector Informatik";
long res;
res = str_match_regex(buffer, "Vector [A-Za-z]*"); // 1
res = str_match_regex(buffer, "Inf[a-z]*"); // 0
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
