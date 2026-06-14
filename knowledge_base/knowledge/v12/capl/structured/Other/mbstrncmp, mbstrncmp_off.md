# mbstrncmp, mbstrncmp_off

> Category: `Other` | Type: `function`

## Syntax

```c
long mbstrncmp(char s1[], char s2[], long len); // form 1
```

## Description

This function compares s1 with s2 for a maximum of len characters.

If they are identical the functional result is 0. If s1 is less than s2 the result is -1, else +1.

Comparison starts in s1 at s1offset (form 3) and in s2 at s2offset (form 2 and form 3).

## Return Values

-1 if s1 is less than s2.

## Example

```c
char s[50] = "'Tür' is the german word for 'door'.";
write("%d", mbstrncmp_off(s, 13, "german", 0, 6)); // 0
```

## Availability

| Since Version |
|---|
