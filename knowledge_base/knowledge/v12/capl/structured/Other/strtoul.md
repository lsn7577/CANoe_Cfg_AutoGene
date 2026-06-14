# strtoul

> Category: `Other` | Type: `function`

## Syntax

```c
int strtoul(char s[], dword& result);
```

## Description

Converts the string s to an unsigned 32bit integer.The number base is

Whitespace (spaces or tabs) at the start of the string is ignored.

## Return Values

-2: If s is empty or startIndex is larger than strlen(s).

## Example

```c
char s[20] = "123 0xFF";
dword number1, number2;
int res;
res = strtoul(s, number1);
write("number1: %u, res: %d", number1, res); // output: number1: 123, res: 3
res = strtoul(s, res, number2);
write("number2: %u, res: %d", number2, res); // output: number2: 255, res: 8
```

## Availability

| Since Version |
|---|
