# openFileRead

> Category: `Other` | Type: `function`

## Syntax

```c
dword openFileRead (char filename[], dword mode); // form 1
```

## Description

This function opens the file named filename for the read access.

If mode=0 the file is opened in text mode; if mode=1 the file is opened in binary mode.

## Return Values

The return value is the file handle that must be used for read operations.
If an error occurs, the return value is 0.

## Availability

| Since Version |
|---|
