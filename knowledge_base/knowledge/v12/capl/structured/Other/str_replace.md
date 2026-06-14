# str_replace

> Category: `Other` | Type: `function`

## Syntax

```c
long str_replace(char s[], char searched[], char replacement[]); // form 1
```

## Description

Form 1: Replaces all occurrences of a text in a string with another string.

Form 2: Replaces a part of a string with another string.

## Return Values

1 if successful, 0 if the resulting string would be too long for the buffer s.

## Example

```c
char buffer[70] = "Vector Informatik";
str_replace(buffer, "Informatik", "CANoe");
write(buffer);
str_replace(buffer, 7, "CANalyzer", 10);
write(buffer);
```

## Availability

| Since Version |
|---|
