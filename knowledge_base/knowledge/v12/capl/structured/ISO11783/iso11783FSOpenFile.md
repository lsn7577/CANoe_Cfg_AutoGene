# iso11783FSOpenFile

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long iso11783FSOpenFile( char path[], dword flags );
```

## Description

This function opens a file or directory.

## Example

```c
LONG handle;
char data[200];

handle = iso11783FSOpenFile( 
 "\test.TXT", 0x00 );
if (handle > 0) 
 {
  Iso11783FSReadData( 
 handle, elCount(data), data );
  Iso11783FSCloseFile( 
 handle );
}
```

## Availability

| Since Version |
|---|
