# strtod

> Category: `Other` | Type: `function`

## Syntax

```c
int strtod(char s[], double& result); // from 1
int strtod(char s[], dword startIndex, double& result); // form 2
```

## Description

Converts the string s to a floating point number. The string must have the format [whitespace][sign][digits][.digits][{d|D|e|E}[sign]digits].

Whitespace: may consist of space and tab characters, which are ignoredsign: is either plus (+) or minus (-)digits: are one or more decimal digits.If no digits appear before the radix character, at least one must appear after the radix character. The decimal digits can be followed by an exponent, which consists of an introductory letter (d, D, e, or E) and an optionally signed integer. If neither an exponent part nor a radix character appears, a radix character is assumed to follow the last digit in the string.

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
char s[20] = "-1.23 2.4E3";
double number1, number2;
int res;
res = strtod(s, number1);
write("number1: %g, res: %d", number1, res); // output: number1: -1.23, res: 5
res = strtod(s, res, number2);
write("number2: %g, res: %d", number2, res); // output: number2: 2400, res: 11
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
