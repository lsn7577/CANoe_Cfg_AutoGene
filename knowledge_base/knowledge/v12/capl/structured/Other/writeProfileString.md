# writeProfileString

> Category: `Other` | Type: `function`

## Syntax

```c
long writeProfileString(char section[], char entry[], char value[], char filename[]); form 1
```

## Description

Opens the file filename, searches the section section and writes the variable entry with the value value. If entry already exists the old value is overwritten. The functional result is the number of characters written or 0 in case of an error.

## Return Values

0: Write error

## Availability

| Since Version |
|---|
