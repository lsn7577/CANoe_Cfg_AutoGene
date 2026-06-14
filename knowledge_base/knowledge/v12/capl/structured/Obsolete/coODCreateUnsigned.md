# coODCreateUnsigned

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void coODCreateUnsigned( dword index, dword subIndex, dword dataType, dword access, dword initValue, dword errCode[] );
```

## Description

Generates a new object in the local object dictionary of the specified type and with a start value with no leading sign. If the length of the available start value (maximum 32 bits) is smaller than the size of the object, the remaining part is initialized with null.

If the object already exists, then it is replaced by the new object.

## Return Values

—

## Example

```c
dword errCode[1];

coODCreateUnsigned( 0x1000, 0x0, 0x7, 0, 401, errCode );
if (errCode[0] == 0) {
  write( "Object [0x1000,0] created" );
}
```

## Availability

| Up to Version |
|---|
