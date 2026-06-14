# strncpy_off

> Category: `Other` | Type: `function`

## Syntax

```c
void strncpy_off(char dest[], long destOffset, char src[], long max);
```

## Description

This function copies src to dest. max indicates the size of dest in bytes.

The function ensures that there is a terminating '\0'. Thus, a maximum of max-1-destOffset bytes are copied. Bytes are overwritten in dest starting at destOffset.

A character may need several bytes depending on the string encoding, e.g. Japanese characters in Windows ANSI (932) encoding or any special characters in UTF-8 encoding. In that case, you should use mbstrncpy_off instead.

## Return Values

—

## Example

```c
char s[6] = "Hello";
strncpy_off(s, 1, "e", elcount(s)); // s: He
```

## Availability

| Since Version |
|---|
