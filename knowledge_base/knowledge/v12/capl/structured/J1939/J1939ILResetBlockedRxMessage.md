# J1939ILResetBlockedRxMessage

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939ILResetBlockedRxMessage(dword pgn, dword sourceAddress, qword filterMask, qword filterValue); // form 1
```

## Description

Resets the change of a single J1939ILBlockRxMessage call. The message to unblock is specified by PGN, source address and a part of the first eight data bytes.

## Return Values

0: Blocking has been stopped successfully

## Example

```c
—
```

## Availability

| Since Version |
|---|
