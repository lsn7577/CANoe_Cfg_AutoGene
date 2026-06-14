# str_replace_regex

> Category: `Other` | Type: `function`

## Syntax

```c
long str_replace_regex(char s[], char pattern[], char replacement[]);
```

## Description

Replaces all occurrences of pattern in a string with another string.

## Parameters

| Name | Description |
|---|---|
| s | String to be modified. |
| pattern | Regular expression which determines the parts in s which shall be replaced. For the regular expression, the same syntax is used as in the Perl programming language. |
| replacement | Replacement for the parts which match the pattern. |

## Return Values

1 if successful, 0 if the resulting string would be too long for the buffer s.

## Example

```c
char buffer[70] = "Vector Informatik";
str_replace_regex(buffer, "Inf[a-z]*", "CANoe");
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
