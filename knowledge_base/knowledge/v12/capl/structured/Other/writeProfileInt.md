# writeProfileInt

> Category: `Other` | Type: `function`

## Syntax

```c
long writeProfileInt(char section[], char entry[], long value, char filename[]); // form 1
```

## Description

Opens the file filename, searches the section section and writes the variable entry with the value value. If entry already exists the old value is overwritten.

## Return Values

The functional result is 0 in case of an error.

## Availability

| Since Version |
|---|
