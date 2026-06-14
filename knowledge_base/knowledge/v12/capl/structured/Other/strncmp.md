# strncmp

> Category: `Other` | Type: `function`

## Syntax

```c
long strncmp(char s1[], char s2[], long len);
```

## Description

This function compares s1 with s2 for a maximum of len bytes.

If they are identical the functional result is 0. If s1 is less than s2 the result is -1, else +1.

Form 2 starts the comparison in s2 at the specified offset.

A character may need several bytes depending on the string encoding, e.g. Japanese characters in Windows ANSI (932) encoding or any special characters in UTF-8 encoding. In that case, you should use mbstrncmp instead.

## Return Values

-1 if s1 is less than s2.

## Example

```c
on key 's'
{
char s1[7] = "Vector";
char s2[7] = "Vector";
if(strncmp(s1,s2,strlen(s1)))
write("not equal");
else
write("equal");
}
```

## Availability

| Since Version |
|---|
