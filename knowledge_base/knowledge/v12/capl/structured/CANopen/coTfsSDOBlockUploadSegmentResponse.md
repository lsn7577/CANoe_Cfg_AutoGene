# coTfsSDOBlockUploadSegmentResponse

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsSDOBlockUploadSegmentResponse( dword ccs, dword cs, dword ackSeq, dword blkSize, dword expMsgNumber, dword startSeqNumber );
```

## Description

This function waits for a SDO segmented upload request and sends the corresponding response. Before the call of this function, no time-delay functions should be inserted in order to prevent a loss of the request message.

## Return Values

Error code

## Example

```c
see example of coTfsSDOBlockInit
```
