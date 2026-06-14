# coOnDownloadResponse

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void coOnDownloadResponse( dword nodeId, dword index, dword subIndex );
```

## Description

This function is called if the response to a SDO download was received (see coDownload and coDownloadExpedited ).

## Return Values

—

## Example

```c
void coOnDownloadResponse( dword nodeId, dword index, dword subIndex ){
  write( "Download response of [0x%.4x,0x%.2x] from node %d received", index, subIndex, nodeId );
}
```

## Availability

| Up to Version |
|---|
