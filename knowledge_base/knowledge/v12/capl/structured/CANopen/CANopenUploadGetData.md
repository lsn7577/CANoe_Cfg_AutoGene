# CANopenUploadGetData

> Category: `CANopen` | Type: `function`

## Syntax

```c
void CANopenUploadGetData( char[] buffer, dword bufferSize, dword errCode[] ); //form 1
```

## Description

Returns the data of a CANopen upload in a callback function as char or byte array.

## Return Values

—

## Example

```c
dword errCode[1];
CANopenUpload ( 1, 0x2000, 0x00, 0, errCode );
if (errCode[0] == 0)
{
  write( "SDO Upload successfully initiated" );
}

void OnCANopenUploadResponse ( dword nodeId, dword index, dword subIndex, dword size )
{
  dword errCode[1];
  char value[100];
  CANopenUploadGetData ( value, elcount(value), errCode );
  write( "Upload response data: %s", value );
}
```

## Availability

| Since Version |
|---|
