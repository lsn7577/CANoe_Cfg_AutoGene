# strtod

> Category: `Other` | Type: `function`

## Syntax

```c
int strtod(char s[], double& result);
```

## Description

Converts the string s to a floating point number. The string must have the format [whitespace][sign][digits][.digits][{d|D|e|E}[sign]digits].

Whitespace: may consist of space and tab characters, which are ignoredsign: is either plus (+) or minus (-)digits: are one or more decimal digits.If no digits appear before the radix character, at least one must appear after the radix character. The decimal digits can be followed by an exponent, which consists of an introductory letter (d, D, e, or E) and an optionally signed integer. If neither an exponent part nor a radix character appears, a radix character is assumed to follow the last digit in the string.

## Return Values

-2: If s is empty or startIndex is larger than strlen(s).

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

| Since Version |
|---|
