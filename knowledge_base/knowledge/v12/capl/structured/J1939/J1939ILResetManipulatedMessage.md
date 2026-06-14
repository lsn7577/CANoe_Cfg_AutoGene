# J1939ILResetManipulatedMessage

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939ILResetManipulatedMessage( dword pgn, dword destinationAddress, qword filterMask, qword filterValue ); // form 1
```

## Description

Resets the change of a single J1939ILManipulateMessage call. The corresponding message is specified by PGN, destination address and a part of the first eight data bytes.

## Return Values

-1: There is no matching entry made by J1939ILManipulateMessage

## Availability

| Since Version |
|---|
