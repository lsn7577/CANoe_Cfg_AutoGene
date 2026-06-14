# getProfileInt

> Category: `Other` | Type: `function`

## Syntax

```c
long getProfileInt(char section[], char entry[], long def, char filename[]); // form 1
```

## Description

Searches the file filename under section section for the variable entry. If its value is a number, this number is returned as the functional result. If the file or entry is not found, or if entry does not contain a valid number, the default value def is returned as the functional result.

## Return Values

Integer that was read in.

## Availability

| Since Version |
|---|
