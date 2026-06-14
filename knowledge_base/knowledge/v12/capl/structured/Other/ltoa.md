# ltoa

> Category: `Other` | Type: `function`

## Syntax

```c
void ltoa(long val, char s[], long base);
```

## Description

The number val is converted to a string s. In this case, base indicates a number base between 2 and 36. s must be large enough to accept the converted number!

## Return Values

—

## Example

Result:

```c
char s1[9];
char s2[9];
ltoa(z,s1,2);
ltoa(z,s2,10);
write("z: %d s1= %s",z, s1);
write("z: %d s2= %s",z, s2);
...
z: 255 s1= 11111111
z: 255 s2= 255
```

## Availability

| Since Version |
|---|
