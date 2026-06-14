# coODGetFloat

> Category: `Obsolete` | Type: `function`

## Syntax

```c
float coODGetFloat( dword index, dword subIndex, dword errCode[] );
```

## Description

Returns the floating point value of an object in the local object dictionary. This function can only be applied to objects with the data types 0x8 and 0x11.

For the use of this function, a note on handling should be considered.

## Return Values

Value of the object

## Example

```c
dword errCode[1];
float value;

value = coODGetFloat( 0x2000, 0x0, errCode );
if (errCode[0] == 0) {
  write( "Read value %f", value);
}
```

## Availability

| Up to Version |
|---|
