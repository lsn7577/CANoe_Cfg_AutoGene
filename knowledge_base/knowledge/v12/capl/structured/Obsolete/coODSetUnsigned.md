# coODSetUnsigned

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void coODSetUnsigned( dword index, dword subIndex, dword value, dword errCode[] );
```

## Description

Sets the value of an object in the local object dictionary with no leading sign. This function can be applied to all objects with a length up to 32 bits. Exceptions are the data type 0x8, 0x9, 0xA, 0xF, and 0x11.

For the use of this function, a note on handling should be considered.

## Return Values

—

## Example

```c
dword errCode[1];

coODSetUnsigned( 0x2000, 0x0, 6656, errCode );
if (errCode[0] == 0) {
  write( "New object value successfully set");
}
```

## Availability

| Up to Version |
|---|
