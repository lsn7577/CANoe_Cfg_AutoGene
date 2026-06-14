# coODGetBitSize

> Category: `Obsolete` | Type: `function`

## Syntax

```c
dwordcoODGetBitSize( dword index, dword subIndex, dword errCode[] );
```

## Description

The function returns the size of an object in the local object dictionary in bits.

## Return Values

Size of the object in bits

## Example

```c
dword errCode[1];
dword size;

size = coODGetBitSize( 0x1000, 0x0, errCode );
if(errCode[0] == 0) {
  write( "Object size: %d bit", size);
}
```

## Availability

| Up to Version |
|---|
