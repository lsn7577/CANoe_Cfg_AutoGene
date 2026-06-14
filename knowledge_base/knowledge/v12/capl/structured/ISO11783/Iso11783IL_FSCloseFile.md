# Iso11783IL_FSCloseFile

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_FSCloseFile( dword fileHandle );
```

## Description

This function closes an opened file or directory.

## Return Values

0: Function has been executed successfully

## Example

```c
// handle references a file
LONG handle;
char data[200];

handle = Iso11783IL_FSOpenFile( 
 "\test.TXT", 0x00 );
if (handle > 0) 
 {
  Iso11783IL_FSReadFile( 
 handle, elCount(data), data );
 Iso11783IL_FSCloseFile( handle );
}
// handle references a directory
LONG dirHandle;
char data[200];

dirHandle = Iso11783IL_FSOpenFile( 
 "\dir1", 0x03 );
if (dirHandle > 
 0) {
  Iso11783IL_FSReadFile( 
 dirHandle, (elCount(data)-2)/22, data);
 Iso11783IL_FSCloseFile( dirHandle );
}
```

## Availability

| Since Version |
|---|
