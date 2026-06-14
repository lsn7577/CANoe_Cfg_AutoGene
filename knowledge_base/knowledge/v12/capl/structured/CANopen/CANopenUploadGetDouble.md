# CANopenUploadGetDouble

> Category: `CANopen` | Type: `function`

## Syntax

```c
float CANopenUploadGetDouble(dword errCode[] );
```

## Description

Returns the data of a CANopen upload in a callback function as double.

## Return Values

The data as float.

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
  float value;
  value = CANopenUploadGetDouble (errCode );
  write( "Upload response data: %f", value );
}
```

## Availability

| Since Version |
|---|
