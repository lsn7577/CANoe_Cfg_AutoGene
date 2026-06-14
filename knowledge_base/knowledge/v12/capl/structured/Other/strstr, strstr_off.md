# strstr, strstr_off

> Category: `Other` | Type: `function`

## Syntax

```c
long strstr(char s1[], char s2[]);
```

## Description

Searches in s1 for s2.

A character may need several bytes depending on the string encoding, e.g. Japanese characters in Windows ANSI (932) encoding or any special characters in UTF-8 encoding. In that case, you should use mbstrstr/mbstrstr_off instead.

## Return Values

First position in bytes of s2 in s1, or -1 if s2 is not found in s1.

## Example

```c
long pos;
char s1[18] = "Vector Informatik";
char s2[11] = "Informatik";
pos = strstr(s1, s2); // pos = 7
```

## Availability

| Since Version |
|---|
