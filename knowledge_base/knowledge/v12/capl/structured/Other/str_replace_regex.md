# str_replace_regex

> Category: `Other` | Type: `function`

## Syntax

```c
long str_replace_regex(char s[], char pattern[], char replacement[])
```

## Description

Replaces all occurrences of pattern in a string with another string.

## Return Values

1 if successful, 0 if the resulting string would be too long for the buffer s.

## Example

```c
char buffer[70] = "Vector Informatik";
str_replace_regex(buffer, "Inf[a-z]*", "CANoe");
write(buffer);
```

## Availability

| Since Version |
|---|
