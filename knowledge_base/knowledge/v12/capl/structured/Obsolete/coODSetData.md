# coODSetData

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void coODSetData( dword index, dword subIndex, char data[], dword dataSize, dword errCode[] );
```

## Description

Sets the data of an object in the local object dictionary. This function can be applied to all objects. For objects with a size up to 32 bits or floating point objects, however, the functions coODSetSigned, coODSetUnsigned, and coODSetFloat are recommended.

For the use of this function, a note on handling should be considered.

## Return Values

—

## Example

```c
dword errCode[1];
char data[6] = { 1, 2, 3, 4, 5, 6 };

coODSetData( 0x2000, 0x0, data, elCount(data), errCode );
if (errCode[0] == 0) {
  write( "Object data successfully written");
}
```

## Availability

| Up to Version |
|---|
