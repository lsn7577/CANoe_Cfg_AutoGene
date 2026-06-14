# snprintf

> Category: `Other` | Type: `function`

## Syntax

```c
long snprintf(char dest[], long len, char format[], ...);
```

## Description

This function corresponds to the C function sprintf. Supplementally, the parameter len indicates the maximum length of the array dest.

The format string has the same meaning as with the function write and is described there.

CAPL supports a function call with maximum 64 parameters.

## Return Values

The number of characters written.

## Example

```c
char buffer[100], str[7] = "Vector";
long i;
i = snprintf(buffer,elcount(buffer),"String: %s\n", str);
write("Output:\n%s : Character count = %d\n", buffer, i);
```

## Availability

| Since Version |
|---|
