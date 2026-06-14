# Open

> Category: `Other` | Type: `function`

## Syntax

```c
file(char [] filename, dword access, dword mode); // form 1
```

## Description

This function opens the file named filename.

If access = 0, the file is opened for write access; if access = 1 the file is opened for read access.

If mode = 0 the file is opened in text mode; if mode = 1 the file is opened in binary mode.

## Return Values

— (constructor)

## Availability

| Since Version |
|---|
