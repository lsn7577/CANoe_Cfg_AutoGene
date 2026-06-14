# VTIL_ResetManipulatedMessage

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_ResetManipulatedMessage( dword pgn, dword destinationAddress, qword filterMask, qword filterValue ); // form 1
```

## Description

Resets the change of a single ISO11783VTIL_ManipulateMessage call. The corresponding message is specified by PGN, destination address and a part of the first eight data bytes.

## Return Values

-1: There is no matching entry made by ISO11783VTIL_ManipulateMessage

## Availability

| Since Version |
|---|
