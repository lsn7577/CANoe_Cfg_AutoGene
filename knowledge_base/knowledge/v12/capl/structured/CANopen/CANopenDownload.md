# CANopenDownload

> Category: `CANopen` | Type: `function`

## Syntax

```c
void CANopenDownload( dword nodeId, dword index, dword subIndex, qword data, dword dataSize, dword blockMode, dword errCode[] ); // form 1
```

## Description

Writes an entry in the object dictionary of another node using the SDO protocol. If the data transfer is aborted, the callback OnCANopenAbort is called.

## Return Values

—

## Example

```c
dword errCode[1];
char data[256] = "DownloadData";

CANopenDownload( 1, 0x2000, 0x00, data, strlen(data), 0, errCode );
if (errCode[0] == 0)
{
  write( "SDO Download successfully initiated" );
}
```

## Availability

| Since Version |
|---|
