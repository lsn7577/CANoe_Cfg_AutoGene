# coDownload

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void coDownload( dword nodeId, dword index, dword subIndex, char data[], dword dataSize, dword flags, dword errCode[] );
```

## Description

Writing of an entry into the object dictionary of another node.

The function triggers a SDO download. The response of the node is returned in the event function coOnDownloadResponse or coOnError.

(3) If it is used with the float parameter value, it always initiates a transfer with the length 8 bytes. This corresponds to the data type Real64.

## Return Values

—

## Example

```c
dword errCode[1];
char data[256] = "coDownloadData";

coDownload( 1, 0x2000, 0x00, data, strlen(data), 0, errCode );
if (errCode[0] == 0) {
  write( "SDO Download successfully initiated" ); 
}
```

## Availability

| Up to Version |
|---|
