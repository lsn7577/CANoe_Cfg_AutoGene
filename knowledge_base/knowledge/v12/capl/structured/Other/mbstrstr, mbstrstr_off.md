# mbstrstr, mbstrstr_off

> Category: `Other` | Type: `function`

## Syntax

```c
long mbstrstr(char s1[], char s2[]);
```

## Description

Searches in s1 for s2.

## Return Values

First position in characters of s2 in s1, or -1 if s2 is not found in s1.

## Example

```c
long pos;
char s[50] = "'Tür' is german for 'door'";
pos = mbstrstr(s, "german");
write("%d", pos); // 9
```

## Availability

| Since Version |
|---|
