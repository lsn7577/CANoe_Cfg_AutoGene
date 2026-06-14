# atol

> Category: `Other` | Type: `function`

## Syntax

```c
long atol(char s[]);
```

## Description

This function converts the string s to a LONG number. The number base is decimal. Starting with string 0x, base 16 is used. Leading blanks are not read.

## Return Values

long integer

## Example

Result:

```c
...
long z1;
long z2;
z1 = atol("200");
z2 = atol("0xFF");
...
```

## Availability

| Since Version |
|---|
