# mostAsRgGetRxTxLog

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostAsRgGetRxTxLog(long regsel, long i)
```

## Description

The first one returns the logical device address (node address) at position i of the registry. Indexing starts at 0.

The second one returns the logical device address (node address) of the function block. If there is no entry with the given FBlockId and InstId, an error code <0 is returned.

## Return Values

>=0: Logical device address

## Availability

| Since Version |
|---|
