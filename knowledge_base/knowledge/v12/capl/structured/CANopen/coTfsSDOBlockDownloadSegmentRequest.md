# coTfsSDOBlockDownloadSegmentRequest

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsSDOBlockDownloadSegmentRequest( dword cont, dword seqNumber, byte inValueBuf[], dword valueBufSize, dword isLastSegment );
```

## Description

This function sends a single segmented SDO block download message and waits for the corresponding response.

## Return Values

Error code
