# strncpy

> Category: `Other` | Type: `function`

## Syntax

```c
void strncpy(char dest[], char src[], long max);
```

## Description

This function copies src to dest. max indicates the size of dest in bytes. The function ensures that there is a terminating '\0'. Thus, a maximum of max-1 bytes are copied.

A character may need several bytes depending on the string encoding, e.g. Japanese characters in Windows ANSI (932) encoding or any special characters in UTF-8 encoding. In that case, you should use mbstrncpy instead.

## Return Values

—

## Example

```c
variables {
   char s1[7] = "Vector";
   char s2 [32];
}
on key 'z'
{                                 Output to the Write-Window:
   strncpy (s2,s1,elcount(s2));
   write ("Result: %s",s2);       Result: Vector
}
```

## Availability

| Since Version |
|---|
