# coODSetSigned

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void coODSetSigned( dword index, dword subIndex, long value, dword errCode[] );
```

## Description

Sets the value of an object in the local object dictionary with a leading sign. This function can only be applied to objects with the data types 0x2, 0x3, 0x10, and 0x4.

For the use of this function, a note on handling should be considered.

## Return Values

—

## Example

```c
dword errCode[1];

coODSetSigned( 0x2000, 0x0, -789, errCode );
if (errCode[0] == 0) {
  write( "New object value successfully set");
}
```

## Availability

| Up to Version |
|---|
