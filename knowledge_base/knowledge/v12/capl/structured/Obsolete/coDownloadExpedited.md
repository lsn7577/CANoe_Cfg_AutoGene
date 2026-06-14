# coDownloadExpedited

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void coDownloadExpedited( dword nodeId, dword index, dword subIndex, dword value, dword valueSize, dword flags, dword errCode[] );
```

## Description

Writing of an entry into the object dictionary of another node.

The function triggers a SDO download. The response of the node is returned in the event function coOnDownloadResponse or coOnError.

(2) If it is used with the float parameter value, this function always initiates a transfer with the length 4 bytes. This corresponds to the data type Real32. Since CAPL only supports 8 byte floating point numbers, it must be noted that the value range must not be left when writing to a REAL32 object.

## Return Values

—

## Example

```c
dword errCode[1];

coDownloadExpedited( 1, 0x2000, 0x00, 0x1234, 2, 0, errCode );
if (errCode[0] == 0) {
  write( "SDO Download successfully initiated" ); 
}
```

## Availability

| Up to Version |
|---|
