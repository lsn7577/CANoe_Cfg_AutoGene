# Iso11783IL_FSWriteFile

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_FSWriteFile( dword fileHandle, dword bufferSize, char buffer[] );
```

## Description

This function writes data to an open file.

Contrary to the other file operations, this function does not provide any functionality for a passed directory handle.

## Return Values

0: Function has been executed successfully

## Example

```c
LONG handle;
char data[200];

handle = Iso11783IL_FSOpenFile( "\test.TXT", 0x02 );
if (handle > 0) {
  Iso11783IL_FSWriteFile( handle, 12, "Hello World!" );
  Iso11783IL_FSCloseFile( handle );
}
```

## Availability

| Since Version |
|---|
