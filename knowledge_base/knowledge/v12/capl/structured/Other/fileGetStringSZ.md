# fileGetStringSZ

> Category: `Other` | Type: `function`

## Syntax

```c
long fileGetStringSZ(char buff[], long buffsize, dword fileHandle);
```

## Description

The function reads a string from the specified file.

Characters are read until the end of line is reached or the number of read characters is equal to buffsize -1.The end of line is marked either

No line feed character will be contained in the buffer. See also fileGetString.

## Return Values

If an error occurs, the return value is 0, else 1.

## Availability

| Since Version |
|---|
