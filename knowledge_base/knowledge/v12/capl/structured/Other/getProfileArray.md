# getProfileArray

> Category: `Other` | Type: `function`

## Syntax

```c
long getProfileArray(char section[], char entry[],char buff[], long buffsize, char filename[]); // form 1
```

## Description

Searches the file under section section for the variable entry. Entry is interpreted as a list of numerical values, separated by comma, tab, space, semicolon or slash. A 0x prefix indicates hex values.

## Return Values

Number of numerical values read in.

## Availability

| Since Version |
|---|
