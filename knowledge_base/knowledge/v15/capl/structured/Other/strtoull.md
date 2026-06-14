# strtoull

> Category: `Other` | Type: `function`

## Syntax

```c
int strtoull(char s[], qword& result); // from 1
int strtoull(char s[], dword startIndex, qword& result); // from 2
```

## Description

Converts the string s to an unsigned 64bit integer.The number base is

Whitespace (spaces or tabs) at the start of the string is ignored.

## Parameters

| Name | Description |
|---|---|
| s | String to be converted. |
| result | Contains the converted value after the call. The value is 0 if the string can’t be converted to a number. It is the largest possible positive/negative number in case of overflow. |
| startIndex | Position in s where the conversion shall begin. |

## Return Values

Otherwise, returns the index of the first character after the number.

## Example

```c
char s[20] = "123 0xFF";
qword number1, number2;
int res;
res = strtoull(s, number1);
write("number1: %I64u, res: %d", number1, res); // output: number1: 123, res: 3
res = strtoull(s, res, number2);
write("number2: %I64u, res: %d", number2, res); // output: number2: 255, res: 8
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.2 | 8.2 | 13.0 | 13.0 | 14 | 1.1 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | ✔ | N/A |
