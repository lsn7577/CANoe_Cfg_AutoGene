# coODSetFloat

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void coODSetFloat( dword index, dword subIndex, float value, dword errCode[] );
```

## Description

Sets the floating point value of an object in the local object dictionary. This function can only be applied to objects with the data types 0x8 and 0x11.

For the use of this function, a note on handling should be considered.

## Return Values

—

## Example

```c
dword errCode[1];

coODSetFloat( 0x2000, 0x0, 123.456789, errCode );
if (errCode[0] == 0) {
  write( "New object value successfully set");
}
```

## Availability

| Up to Version |
|---|
