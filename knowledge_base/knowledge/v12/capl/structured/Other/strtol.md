# strtol

> Category: `Other` | Type: `function`

## Syntax

```c
int strtol(char s[], long& result);
```

## Description

Converts the string s to a 32bit integer.The number base is

Whitespace (spaces or tabs) at the start of the string is ignored.

## Return Values

-2: If s is empty or startIndex is larger than strlen(s).

## Example

```c
char s[20] = "123 0xFF";
long number1, number2;
int res;
res = strtol(s, number1);
write("number1: %d, res: %d", number1, res); // output: number1: 123, res: 3
res = strtol(s, res, number2);
write("number2: %d, res: %d", number2, res); // output: number2: 255, res: 8
```

## Availability

| Since Version |
|---|
