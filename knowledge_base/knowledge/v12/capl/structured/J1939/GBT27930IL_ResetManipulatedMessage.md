# GBT27930IL_ResetManipulatedMessage

> Category: `J1939` | Type: `function`

## Syntax

```c
long GBT27930IL_ResetManipulatedMessage( dword pgn, dword destinationAddress, qword filterMask, qword filterValue ); // form 1
```

## Description

Resets the change of a single GBT27930IL_ManipulateMessage call. The corresponding message is specified by PGN, destination address and a part of the first eight data bytes.

## Return Values

-1: There is no matching entry made by GBT27930IL_ManipulateMessage

## Availability

| Since Version |
|---|
