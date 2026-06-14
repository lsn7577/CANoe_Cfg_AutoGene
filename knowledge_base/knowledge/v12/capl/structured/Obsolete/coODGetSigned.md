# coODGetSigned

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long coODGetSigned( dword index, dword subIndex, dword errCode[] );
```

## Description

Returns the value of an object in the local object dictionary with a leading sign. This function can only be applied to objects with the data types 0x2, 0x3, 0x10, and 0x4.

For the use of this function, a note on handling should be considered.

## Return Values

Value of the object

## Example

```c
dword errCode[1];
long value;

value = coODGetSigned( 0x2000, 0x0, errCode );
if (errCode[0] == 0) {
  write( "Read value %d", value);
}
```

## Availability

| Up to Version |
|---|
