# getUserFilePath

> Category: `Other` | Type: `function`

## Syntax

```c
long getUserFilePath(char fileName[], char absPath[], long absPathLen)
```

## Description

Gets the absolute path of a user file.

In case of execution in a distributed environment the absolute user file path (including file name) on the remote device (e.g. VN8900) is returned if the user file was pre-defined. If the file was not pre-defined an error code is returned.

In case of a single PC environment the registered absolute file path (including file name) of the user file is returned if the user file was pre-defined. If the file was not pre-defined the function returns the same result as getAbsFilePath (converting a path relative to the configuration directory to an absolute path).

## Return Values

On success this function returns the length of the full path name. Otherwise the function returns -1 if parameters do not fit or buffer size is too small or -2 if no user file with the given name was registered in case of a distributed environment.

## Example

```c
on preStart
{
   char absPath[256];
   VgetUserFilePath("MyCAPLDll.INI", absPath, 256);
   MyCAPLDllFunction(absPath);
}
```

## Availability

| Since Version |
|---|
