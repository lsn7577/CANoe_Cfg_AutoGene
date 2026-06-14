# strlen

> Category: `Other` | Type: `function`

## Syntax

```c
long strlen(char s[]);
```

## Description

The functional result is the length of the string s in bytes.

A character may need several bytes depending on the string encoding, e.g. Japanese characters in Windows ANSI (932) encoding or any special characters in UTF-8 encoding. In that case, you may want to use mbstrlen instead.

## Return Values

Length of the string in bytes.

## Example

Result:

```c
long length;
char buffer[100] = "CANalyzer";
length = strlen(buffer);
```

## Availability

| Since Version |
|---|
