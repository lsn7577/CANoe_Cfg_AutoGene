# mostSyncDealloc

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostSyncDealloc(long label)
```

## Description

MOST25:

This function releases reserved bandwidth for synchronous channels by sending a Dealloc system message to the TimingMaster.

The result is reported by means of the callback function OnMostSyncDeallocResult. This requires defining OnMostSyncDeallocResult in the CAPL program using the following signature: OnMostSyncDeallocResult(long deallocResult, long label)

Most150:

Deallocates synchronous bandwidth on MOST150.

In contrast to MOST25 the callback function OnMostSyncDeallocResult (see below) will not be called on completion. mostAllocTableGetCL can be applied to check the de-allocation result.

## Return Values

See error codes

## Availability

| Since Version |
|---|
