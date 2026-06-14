# atodbl

> Category: `Other` | Type: `function`

## Syntax

```c
double atodbl(char s[]);
```

## Description

The function converts the string s into a double number. Normally, the base is decimal and must have the following format:

String parsing ceases at the first non-compliant character.

If the string cannot be converted into a number, 0.0 is returned.

If the string starts with 0x, the base used is 16. Only integer numbers can be read in.

## Return Values

Double number, the converted string.

## Example

```c
double d;
d = atodbl("  -3.7");    // -3.7
d = atodbl("0x1F");      // 31.0
d = atodbl("1.3E2");     // 130.0
```

## Availability

| Since Version |
|---|
