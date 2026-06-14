# mostSyncAlloc

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostSyncAlloc(long numChannels)
```

## Description

MOST25:

This function reserves synchronous bandwidth by sending an Alloc system message to the MOST TimingMaster.

The result is reported by means of the callback function OnMostSyncAllocResult(). This requires defining OnMostSyncAllocResult() in the CAPL program using the following signature: OnMostSyncAllocResult(long allocResult, long numChannels, long channels[])

The service can only process one request at a time. After mostSyncAlloc() or mostSyncDealloc() is called, the next request cannot be made until the result of the current request is returned – asynchronously.

MOST150:

Allocates synchronous bandwidth on MOST150.

## Return Values

See error codes

## Availability

| Since Version |
|---|
