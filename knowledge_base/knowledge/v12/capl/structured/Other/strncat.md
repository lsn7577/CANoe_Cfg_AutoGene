# strncat

> Category: `Other` | Type: `function`

## Syntax

```c
void strncat(char dest[], char src[], long len);
```

## Description

This function appends src to dest. len indicates the maximum length of the composite string. The function ensures that there is a terminating "\0". Thus, a maximum of len - strlen(dest) - 1 characters are copied.

Unlike the strncat C-function, rather than the number of characters to be appended, len indicates the maximum length of the composite string, including the terminating "\0".

## Return Values

—

## Example

```c
char s[20];
strncpy(s, "Vector", 10); // s is "Vector"
strncat(s, " CANoe", 19); // s is "Vector CANoe"
strncpy(s, "Vector", 10); // s is "Vector"
strncat(s, " CANoe", 11); // s is "Vector CAN"
```

## Availability

| Since Version |
|---|
