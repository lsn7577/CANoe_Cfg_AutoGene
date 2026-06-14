# mbstrlen

> Category: `Other` | Type: `function`

## Syntax

```c
long mbstrlen(char s[]);
```

## Description

The functional result is the length of the string s in characters.

## Return Values

Length of the string in characters.

## Example

```c
long length;
char s1[10] = "door";
char s2[10] = "Tür";
write("%d %d", mbstrlen(s1), strlen(s1)); // 4 4
write("%d %d", mbstrlen(s2), strlen(s2)); // 3 [3 or 4 depending on file encoding]
```

## Availability

| Since Version |
|---|
