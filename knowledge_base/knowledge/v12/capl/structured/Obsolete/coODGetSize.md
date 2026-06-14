# coODGetSize

> Category: `Obsolete` | Type: `function`

## Syntax

```c
dword coODGetSize( dword index, dword subIndex, dword errCode[] );
```

## Description

The function returns the size of an object in the local object dictionary in bytes.

## Return Values

Size of the object in bytes

## Example

```c
dword errCode[1];
dword size;

size = coODGetSize( 0x1000, 0x0, errCode );
if (errCode[0] == 0) {
  write( "Object size: %d byte", size);
}
```

## Availability

| Up to Version |
|---|
