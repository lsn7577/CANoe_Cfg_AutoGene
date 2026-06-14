# strncmp_off

> Category: `Other` | Type: `function`

## Syntax

```c
long strncmp_off(char s1[], long s1offset, char s2[], long s2offset, long len);
```

## Description

This function compares s1 with s2 for a maximum of len bytes.

If they are identical the functional result is 0. If s1 is less than s2 the result is -1, else +1. Comparison starts in s1 at s1offset and in s2 at s2offset.

A character may need several bytes depending on the string encoding, e.g. Japanese characters in Windows ANSI (932) encoding or any special characters in UTF-8 encoding. In that case, you should use mbstrncmp_off instead.

## Return Values

-1 if s1 is less than s2.

## Example

```c
char s1[18] = "Vector Informatik";
char s2[11] = "Informatik";
if (strncmp_off(s1, 7, s2, 0, strlen(s2)) == 0)
   write("Equal!");
else
   write("Unequal!");
```

## Availability

| Since Version |
|---|
