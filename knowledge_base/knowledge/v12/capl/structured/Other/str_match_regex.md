# str_match_regex

> Category: `Other` | Type: `function`

## Syntax

```c
long str_match_regex(char s[], char pattern[])
```

## Description

Checks whether a string completely matches a regular expression pattern.

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

| Since Version |
|---|
