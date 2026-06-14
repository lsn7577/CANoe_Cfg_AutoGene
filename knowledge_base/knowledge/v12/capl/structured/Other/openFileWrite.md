# openFileWrite

> Category: `Other` | Type: `function`

## Syntax

```c
dword openFileWrite (char filename[], dword mode); // form 1
```

## Description

This function opens the file named filename for the write access.

If mode=0 writing can be executed in text mode; if mode=1 writing can be executed in binary mode. An already existing file will be overwritten.

mode=2 to append data at the end of the file use for text mode.mode=3 to append data at the end of the file for binary mode.

## Return Values

The return value is the file handle that must be used for write operations.
If an error occurs, the return value is 0.

## Availability

| Since Version |
|---|
