# coODCreateFromFile

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void coODCreateFromFile( char filename[], dword nodeId, dword defaults, dword errCode[] );
```

## Description

The function loads an EDS or DCF file and generates the local object dictionary from it. The given file have to match the format described in /7/. Already existing objects will be deleted on call of that function.

All errors that occur and indications about this procedure are reported to the write window.

## Return Values

—

## Example

```c
dword errCode[1];

coODCreateFromFile( "NMTMaster.eds", 120, 1, errCode );
if (errCode[0] == 0) {
  write( "Object dictionary successfully created" );
}
```

## Availability

| Up to Version |
|---|
