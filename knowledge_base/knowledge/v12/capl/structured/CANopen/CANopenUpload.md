# CANopenUpload

> Category: `CANopen` | Type: `function`

## Syntax

```c
void CANopenUpload( dword nodeId, dword index, dword subIndex, dword blockMode, dword errCode[] ); // form 1
```

## Description

Reads an entry from the object dictionary of another node using the SDO protocol. When the node responds with the requested data, the callback OnCANopenUploadResponse is called. If the data transfer is aborted, the callback OnCANopenAbort is called.

## Return Values

—

## Example

```c
dword errCode[1];
CANopenUpload ( 1, 0x1000, 0x00, 0, errCode );

if (errCode[0] == 0)
{
  write( "SDO Upload successfully initiated" );
}

void OnCANopenUploadResponse ( dword nodeId, dword index, dword subIndex, dword size 
{
  dword errCode[1];
  dword value;
  value = CANopenUploadGetUnsigned ( errCode );
  write( "Upload response data: 0x%X", value );
}
```

## Availability

| Since Version |
|---|
