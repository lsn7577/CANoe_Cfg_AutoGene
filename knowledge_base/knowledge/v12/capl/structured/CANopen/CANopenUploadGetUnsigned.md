# CANopenUploadGetUnsigned

> Category: `CANopen` | Type: `function`

## Syntax

```c
qword CANopenUploadGetUnsigned(dword errCode[] );
```

## Description

Returns the data of a CANopen upload in a callback function as an unsigned value.

## Return Values

The data as qword.

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
  qword value;
  value = CANopenUploadGetUnsigned(errCode );
  write( "Upload response data: %I64u", value );
}
```

## Availability

| Since Version |
|---|
