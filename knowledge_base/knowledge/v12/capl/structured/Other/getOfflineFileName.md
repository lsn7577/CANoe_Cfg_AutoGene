# getOfflineFileName

> Category: `Other` | Type: `function`

## Syntax

```c
long getOfflineFileName(char[] buffer, dword bufferSize); //form 1
```

## Description

Returns the complete path of one file of the currently used offline source files. If form 1 is used, the first file is returned, otherwise the index of the file to return is passed as parameter.

## Return Values

0: If no error

## Example

```c
long isActive;
char buffer[256];
long numFiles;
long i;

write("Offline source files:");
numFiles = getNumOfflineFiles();
for (i = 0; i < numFiles; ++i)
{
  getOfflineFileName(i, buffer, 256);
  write("%s", buffer);
}
```

## Availability

| Since Version |
|---|
