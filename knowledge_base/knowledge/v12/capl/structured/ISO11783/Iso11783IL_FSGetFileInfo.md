# Iso11783IL_FSGetFileInfo

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_FSGetFileInfo( dword fileHandle, dword infoCount, dword retInfo[] );
```

## Description

This function retrieves information about a file or directory.

In the entry of the array, the following information is returned:

0

Bit-field with valid entries, bit 1 set = index 1 is valid, ...

1

Attributes of the file:

2

Year

3

Month

4

Day

5

Hour

6

Minute

7

Second

## Return Values

= 0: Function has been executed successfully

## Example

```c
LONG handle;
dword info[8];

handle = Iso11783IL_FSOpenFile( "\TEST.TXT", 0x00 );
if (handle > 0) {
  if (Iso11783IL_FSGetFileInfo( handle, elCount(info), info ) == 0) {
    write( "Date %d-%d-%d'", info[2], info[3], info[4] );
  }
  Iso11783IL_FSCloseFile( handle );
}
```

## Availability

| Since Version |
|---|
