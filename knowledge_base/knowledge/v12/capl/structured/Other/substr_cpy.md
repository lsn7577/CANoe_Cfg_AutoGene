# substr_cpy

> Category: `Other` | Type: `function`

## Syntax

```c
void substr_cpy(char dest[], char src[], long srcStart, long len, long max);
```

## Description

This function copies a substring of src to dest. max indicates the size of dest in bytes. The function ensures that there is a terminating '\0'. Thus, a maximum of max-1 bytes are copied.

A character may need several bytes depending on the string encoding, e.g. Japanese characters in Windows ANSI (932) encoding or any special characters in UTF-8 encoding. In that case, you should use mbsubstr_cpy instead.

## Return Values

—

## Example

```c
char s1[7];
char s2[18] = "Vector Informatik";
substr_cpy(s1, s2, 0, 6, elcount(s1)); // s1: Vector
```

## Availability

| Since Version |
|---|
