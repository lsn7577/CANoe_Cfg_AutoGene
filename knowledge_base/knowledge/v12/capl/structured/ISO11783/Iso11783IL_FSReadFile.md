# Iso11783IL_FSReadFile

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_FSReadFile( dword fileHandle, dword bufferSize, char buffer[] );
```

## Description

The function reads data from an open file and directory entries from an open directory respectively.

Whenever reading directory entries, ensure that handle consists of at least (n * 22 + 2) bytes (n = the number of directory entries to read passed in size. 22 bytes is a maximum length directory entry when the file name length is 12 characters (subject to the 8.3 naming convention). Two bytes are used for the word in buffer[0] and buffer[1] with the number of directory entries actually read).

## Return Values

>=0: Number of bytes written to buffer

## Example

```c
// Read data from file
LONG handle;
char data[200];

handle = Iso11783IL_FSOpenFile( "\test.TXT", 0x00 );
if (handle > 0) {
   Iso11783IL_FSReadFile( handle, elCount(data), data );
  Iso11783IL_FSCloseFile( handle );
} 

                        
// Read directory entries:
LONG handle;
char data[200];

handle = Iso11783IL_FSOpenFile( "\DIR1", 0x03 );
if (handle > 0) {
   Iso11783IL_FSReadFile( handle, (elCount(data)-2)/22, data );
  Iso11783IL_FSCloseFile( handle );
}
```

## Availability

| Since Version |
|---|
