# coODGetType

> Category: `Obsolete` | Type: `function`

## Syntax

```c
dword coODGetType( dword index, dword subIndex, dword errCode[] );
```

## Description

The function returns the data type of an object in the local object dictionary.

For the special file objects that are generated with the function coODCreate in order to read or write on the file system, internally the data type Domain is assumed.

## Return Values

Data type of the object

## Example

```c
dword errCode[1];
dword datatype;

datatype= coODGetType( 0x1000, 0x0, errCode );
if (errCode[0] == 0) {
  write( "Object data type: %d", datatype);
}
```

## Availability

| Up to Version |
|---|
