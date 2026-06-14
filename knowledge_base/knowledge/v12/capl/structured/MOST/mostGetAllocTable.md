# mostGetAllocTable

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostGetAllocTable(long channel, byte buffer[], long buffersize)
```

## Description

The mostGetAllocTable() function copies the MOST Allocation Table (max. 60 bytes) to a local CAPL buffer. It must be verified that the buffer has the required size (buffersize).

The Allocation Table contains the reservation status of the synchronous MOST channels.

## Return Values

See error codes

## Example

```c
byte allocTable[60];
// copy allocation table to local buffer
mostGetAllocTable(mostGetChannel(), allocTable, elcount(allocTable));
```

## Availability

| Since Version |
|---|
