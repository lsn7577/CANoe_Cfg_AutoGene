# coODGetData

> Category: `Obsolete` | Type: `function`

## Syntax

```c
dword coODGetData( dword index, dword subIndex, char buffer[], dword bufferSize, dword errCode[] );
```

## Description

Returns the data of an object in the local object dictionary. This function can be applied to all objects. For objects with a size up to 32 bits or floating point objects, however, the functions coODGetSigned, coODGetUnsigned, and coODGetFloat are recommended.

For the use of this function, a note on handling should be considered.

## Return Values

Number of read data bytes

## Example

```c
dword errCode[1];
char buffer[128];
dword count;

count = coODGetData( 0x1008, 0x0, buffer, elCount(buffer), errCode );
if (errCode[0] == 0) {
  write( "Object size %d, object data %s", count, buffer);
}
```

## Availability

| Up to Version |
|---|
