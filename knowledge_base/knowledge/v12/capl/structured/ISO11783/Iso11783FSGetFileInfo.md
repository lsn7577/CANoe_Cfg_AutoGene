# Iso11783FSGetFileInfo

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783FSGetFileInfo( dword fileHandle, dword infoCount, dword retInfo[] );
```

## Description

This function retrieves information about a file or directory. In the entry of the array, the following information is returned:

0

bit-field with valid entries, bit 1 set = index 1 is valid, ...

1

attributes of the file:

2

year

3

month

4

day

5

hour

6

minute

7

second

## Return Values

0 or error code

## Example

```c
LONG handle;
dword info[8];

handle = Iso11783FSOpenFile( "\TEST.TXT", 0x00 );
if (handle > 0) {
  if (Iso11783FSGetFileInfo( handle, elCount(info), info ) == 0) {
    write( "Date %d-%d-%d'", info[2], info[3], info[4] );
  }
  Iso11783FSCloseFile( handle );
}
```

## Availability

| Since Version |
|---|
