# memcpy_off

> Category: `StructByteAccess` | Type: `function`

## Syntax

```c
void memcpy_off( struct type dest, dword destOffset, byte source[], dword sourceOffset, dword length); // form 1
```

## Description

Copies bytes from a source to destination, giving a destination start offset. The size of the destination must be at least destOffset + length.

## Return Values

—

## Availability

| Since Version |
|---|
