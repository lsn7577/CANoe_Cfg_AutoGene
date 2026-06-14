# Iso11783IL_FSOpenFile

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_FSOpenFile( char path[], dword flags );
```

## Description

This function opens a file or directory.

## Return Values

>0: File handle

## Example

```c
LONG handle;
char data[200];

handle = Iso11783IL_FSOpenFile( 
 "\test.TXT", 0x00 );
if (handle > 0) 
 {
  Iso11783IL_FSReadData( 
 handle, elCount(data), data );
  Iso11783IL_FSCloseFile( 
 handle );
}
```

## Availability

| Since Version |
|---|
