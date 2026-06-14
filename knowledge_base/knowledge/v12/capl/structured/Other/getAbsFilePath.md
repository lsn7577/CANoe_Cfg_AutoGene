# getAbsFilePath

> Category: `Other` | Type: `function`

## Syntax

```c
long getAbsFilePath(char relPath[], char absPath[], long absPathLen)
```

## Description

Gets the absolute path of a file.

As parameter the file should be defined with the relative path to the current configuration.

## Return Values

On success this function returns length of the full path name, otherwise -1.

## Example

```c
on key 'x'
{
   char absPath[256];
   getAbsFilePath("Nodes\\Test.can", absPath, 256);
   write ("absPath: %s ", absPath);
}
```

## Availability

| Since Version |
|---|
