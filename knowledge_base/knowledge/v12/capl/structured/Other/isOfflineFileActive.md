# isOfflineFileActive

> Category: `Other` | Type: `function`

## Syntax

```c
long isOfflineFileActive(long index);
```

## Description

Returns whether events of an offline source file are currently replayed, i.e., the start of the source file has been reached but the end of the source file has not yet been reached.

## Return Values

-1: If error (e.g., not in offline mode)

## Example

```c
long isActive;
char buffer[256];
long numFiles;
long i;

numFiles = getNumOfflineFiles();
for (i = 0; i < numFiles; ++i)
{
  getOfflineFileName(i, buffer, 256);
  isActive = isOfflineFileActive(i);
  if (isActive)
  {
    write("Offline file %s is active", buffer);
  }
  else
  {
    write("Offline file %s is inactive", buffer);
  }
}
```

## Availability

| Since Version |
|---|
