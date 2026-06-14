# strstr_regex, strstr_regex_off

> Category: `Other` | Type: `function`

## Syntax

```c
long strstr_regex(char s[], char pattern[])
```

## Description

Searches for a regular expression pattern in a string.

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

| Since Version |
|---|
