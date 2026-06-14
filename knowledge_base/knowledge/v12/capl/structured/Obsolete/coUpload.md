# coUpload

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void coUpload( dword nodeId, dword index, dword subIndex, dword flags, dword errCode[] );
```

## Description

Reading of an entry from the object dictionary of another node.

The function triggers a SDO upload. The response of the node is returned in the event function coOnUploadResponse or coOnError.

## Return Values

—

## Example

```c
dword errCode[1];

coUpload( 1, 0x1000, 0x00, 0, errCode );
if (errCode[0] == 0) {
  write( "SDO Upload successfully initiated" ); 
}
```

## Availability

| Up to Version |
|---|
