# GBT27930IL_ResetBlockedTxMessage

> Category: `J1939` | Type: `function`

## Syntax

```c
long GBT27930IL_ResetBlockedTxMessage(dword pgn, dword destinationAddress, qword filterMask, qword filterValue); // form 1
```

## Description

Resets the change of a single GBT27930IL_BlockTxMessage call.

The message to unblock is specified by PGN, destination address and a part of the first eight data bytes.

## Return Values

0: Blocking has been stopped successfully

## Example

```c
—
```

## Availability

| Since Version |
|---|
