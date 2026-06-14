# coODCreateFloat

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void coODCreateFloat( dword index, dword subIndex, dword dataType, dword access, float initValue, dword errCode[] );
```

## Description

Generates a new object in the local object dictionary of the specified type and with a floating point start value. If the size of the object (type 0x8 - 32 bit) is smaller than the length of the start value (64 bits), a conversion is undertaken. This can cause lower precision or value falsification.

If the object already exists, then it is replaced by the new object.

## Return Values

—

## Example

```c
dword errCode[1];

coODCreateFloat( 0x2000, 0x0, 0x8, 1, 2.5894, errCode );
if (errCode[0] == 0) {
  write( "Object [0x2000,0] created" );
}
```

## Availability

| Up to Version |
|---|
