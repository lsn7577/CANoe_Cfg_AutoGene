# coODGetUnsigned

> Category: `Obsolete` | Type: `function`

## Syntax

```c
dwordcoODGetUnsigned( dword index, dword subIndex, dword errCode[] );
```

## Description

Returns the value of an object in the local object dictionary without a leading sign. This function can be applied to all objects with a length up to 32 bits. Exceptions are the data type 0x8, 0x9, 0xA, 0xF, and 0x11.

For the use of this function, a note on handling should be considered.

## Return Values

Value of the object

## Example

```c
dword errCode[1];
dword value;

value = coODGetUnsigned( 0x2000, 0x0, errCode );
if (errCode[0] == 0) {
  write( "Read value %d", value);
}
```

## Availability

| Up to Version |
|---|
