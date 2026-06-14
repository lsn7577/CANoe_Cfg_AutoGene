# substr_cpy_off

> Category: `Other` | Type: `function`

## Syntax

```c
void substr_cpy_off(char dest[], long destOffset, char src[], long srcStart, long len, long max)
```

## Description

This function copies a substring of src to dest. max indicates the the size of dest in bytes. The function ensures that there is a terminating ‘\0’. Thus, a maximum of max-1-destOffset bytes are copied.

A character may need several bytes depending on the string encoding, e.g. Japanese characters in Windows ANSI (932) encoding or any special characters in UTF-8 encoding. In that case, you should use mbsubstr_cpy_off instead.

## Return Values

—

## Example

```c
char s1[9] = "New CAPL";
char s2[18] = "Vector Informatik";
substr_cpy_off(s2, 7, s1, 4, -1, elcount(s2)); // s2: Vector CAPL
```

## Availability

| Since Version |
|---|
