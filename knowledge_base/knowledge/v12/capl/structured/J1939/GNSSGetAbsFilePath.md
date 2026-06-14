# GNSSGetAbsFilePath

> Category: `J1939` | Type: `function`

## Syntax

```c
long GNSSGetAbsFilePath( char file [], char fileNameWithAbsPath[], long absPathLen )
```

## Description

This function gets the absolute path of a file.

Functionality

## Return Values

Error code

## Example

```c
on key 'x'
{
  char absPath[256];

  GNSSGetAbsFilePath("Test.can", absPath, 256);
  write ("absPath 1: %s ", absPath);

  GNSSGetAbsFilePath("Nodes\\Test.can", absPath, 256);
  write ("absPath 1: %s ", absPath);

  GNSSGetAbsFilePath("C:\\Nodes\\Test.can", absPath, 256);
  write ("absPath 1: %s ", absPath);
}
```

## Availability

| Since Version |
|---|
