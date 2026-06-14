# Iso11783FSWriteFile

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783FSWriteFile( dword fileHandle, dword bufferSize, char buffer[] );
```

## Description

This function writes data to an open file.

Contrary to the other file operations, this function does not provide any functionality for a passed directory handle.

## Example

```c
LONG handle;
char data[200];

handle = Iso11783FSOpenFile( "\test.TXT", 0x02 );
if (handle > 0) {
 Iso11783FSWriteFile( handle, 12, "Hello World!" );
  Iso11783FSCloseFile( handle );
}
```

## Availability

| Since Version |
|---|
