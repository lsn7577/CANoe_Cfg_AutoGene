# getNumOfflineFiles

> Category: `Other` | Type: `function`

## Syntax

```c
long getNumOfflineFiles();
```

## Description

Returns the number of configured offline source files.

## Return Values

-1: If error (e.g., not in offline mode)

## Example

```c
long numFiles;

numFiles = getNumOfflineFiles();
write("Number of configured offline source files: %d", numFiles);
```

## Availability

| Since Version |
|---|
