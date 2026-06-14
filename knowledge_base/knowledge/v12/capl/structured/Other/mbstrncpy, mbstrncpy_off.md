# mbstrncpy, mbstrncpy_off

> Category: `Other` | Type: `function`

## Syntax

```c
void mbstrncpy(char dest[], char src[], long len);
```

## Description

mbstrncpy function copies src to dest. len indicates the number of characters that shall be copied; use -1 to indicate that as much shall be copied into dest as will fit (maximum until the end of src). The function ensures that there is a terminating 0 byte; but in contrast to strncpy, that byte is not counted into len.

mbstrncpy_off overwrites characters in the destination buffer starting at the character offset destOffset.

## Return Values

—

## Example

```c
char s1[50] = "eine grüne "; // german for 'a green'
char s2[10] = "Türen"; // german for 'doors'
mbstrncpy_off(s1, 11, s2, 3);
write("%s", s1); // eine grüne Tür (german for 'a green door')
```

## Availability

| Since Version |
|---|
