# Iso11783FSSetFileInfo

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783FSSetFileInfo( dword fileHandle, dword infoCount, dword info[] );
```

## Description

This function sets file or directory attributes.

## Return Values

0 or error code

## Example

```c
LONG handle;
dword info[2];

handle = Iso11783FSSetFileInfo( "\TEST.TXT", 0x00 );
if (handle > 0) {
  info[0] = 0x01; // Entry 1 is valid
  info[1] = 0x04; // Hide file
  if (Iso11783FSSetFileInfo( handle, elCount(info), info ) == 0) {
    write( "Changed attributes successfully" );
  }
  Iso11783FSCloseFile( handle );
}
```

## Availability

| Since Version |
|---|
