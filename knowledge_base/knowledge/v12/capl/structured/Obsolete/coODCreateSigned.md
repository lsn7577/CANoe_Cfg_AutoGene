# coODCreateSigned

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void coODCreateSigned( dword index, dword subIndex, dword dataType, dword access, long initValue, dword errCode[] );
```

## Description

Generates a new object in the local object dictionary of the specified type and with a start value provided with leading sign. If the length of the available start value (maximum 32 bits) is smaller than the size of the object, the remaining part is initialized with null.

If the object already exists, then it is replaced by the new object.

## Return Values

—

## Example

```c
dword errCode[1];

coODCreateSigned( 0x2000, 0x0, 0x4, 1, -255, errCode );
if (errCode[0] == 0) {
  write( "Object [0x2000,0] created" );
}
```

## Availability

| Up to Version |
|---|
