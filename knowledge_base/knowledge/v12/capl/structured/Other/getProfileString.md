# getProfileString

> Category: `Other` | Type: `function`

## Syntax

```c
long getProfileString(char section[], char entry[], char def[], char buff[], long buffsize, char filename[]); // form 1
```

## Description

Searches the file filename under section section for the variable entry. Its contents (value) are written to the buffer buff. Its length must be passed correctly in buffsize.

If the file or entry is not found, the default value def is copied to buffer.

If the read string length is longer than the buffer, the string will be cut to the buffer length.

## Return Values

Length of the read string.

## Availability

| Since Version |
|---|
