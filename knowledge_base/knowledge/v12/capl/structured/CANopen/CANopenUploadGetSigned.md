# CANopenUploadGetSigned

> Category: `CANopen` | Type: `function`

## Syntax

```c
Int64 CANopenUploadGetSigned(dword errCode[] );
```

## Description

Returns the data of a CANopen upload in a callback function as a signed value.

## Return Values

The data as Int64.

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
  Int64 value;
  value = CANopenUploadGetSigned(errCode );
  write( "Upload response data: %I64d", value );
}
```

## Availability

| Since Version |
|---|
