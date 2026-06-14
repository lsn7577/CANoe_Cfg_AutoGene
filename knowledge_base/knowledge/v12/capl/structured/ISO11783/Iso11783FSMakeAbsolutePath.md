# Iso11783FSMakeAbsolutePath

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783FSMakeAbsolutePath( char relPath[], char absPath[], dword mustExist, dword bufferSize, char buffer[] );
```

## Description

This function converts an relative path into an absolute path including a conversion to uppercase characters. An absolute path begins with \ and refers to the root directory (see also Iso11783SetPath). A relative path could contain .. and ..

A path must follow the 8.3 format (8 character identifier with 4 character extension).

## Return Values

0 or error code

## Example

```c
char defaultDirectory[64] = "\IMPL";
char newPath[255];

if (Iso11783FSMakeAbsolutePath( "..\DATA", defaultDirectory, 1, elCount(newPath), newPath ) == 0) {
  write( "Path '%s'", newPath );
}
```

## Availability

| Since Version |
|---|
