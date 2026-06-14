# coODCreateArray

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void coODCreateArray( dword index, dword dataType, dword accessSub0, dword access, dword elementCount, dword errCode[] );
```

## Description

Generates a new field object in the local object dictionary. If the object already exists, then it is replaced by the new object.

## Return Values

—

## Example

```c
dword errCode[1];

coODCreateArray( 0x1f81, 0x7, 0, 1, 127, errCode );
if (errCode[0] == 0) {
  write( "Array [0x1f81] created" );
}
```

## Availability

| Up to Version |
|---|
