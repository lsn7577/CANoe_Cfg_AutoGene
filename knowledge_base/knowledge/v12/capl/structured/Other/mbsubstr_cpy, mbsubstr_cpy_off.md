# mbsubstr_cpy, mbsubstr_cpy_off

> Category: `Other` | Type: `function`

## Syntax

```c
void mbsubstr_cpy(char dest[], char src[], long srcStart, long len);
```

## Description

mbsubstr_cpy copies a substring of src to dest. len indicates the number of characters that shall be copied; use -1 to indicate that as much shall be copied into dest as will fit (maximum until the end of src). The function ensures that there is a terminating 0 byte; but in contrast to substr_cpy/substr_cpy_off, that byte is not counted into len.

mbsubstr_cpy_off overwrites characters in the destination buffer starting at the character offset destOffset.

## Return Values

—

## Example

```c
char s1[50] = "eine grüne "; // german for 'a green'
char s2[20] = "schöne Türen"; // german for 'beautiful doors'
mbsubstr_cpy_off(s1, 11, s2, 7, 3);
write("%s", s1); // eine grüne Tür (german for 'a green door')
```

## Availability

| Since Version |
|---|
