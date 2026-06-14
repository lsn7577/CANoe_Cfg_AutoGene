# seqFileClose

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long seqFileClose(long file);
```

## Description

The function closes the file specified by handle file. All System-allocated buffers are freed upon closing.

## Return Values

The function returns zero on success. If the operation fails, it returns an non-zero error code.

## Availability

| Up to Version |
|---|
