# GBT27930IL_BlockRxMessage

> Category: `J1939` | Type: `function`

## Syntax

```c
long GBT27930IL_BlockRxMessage(dword pgn, dword sourceAddress, qword filterMask, qword filterValue); // form 1
```

## Description

Prevents processing of a received message by the interaction layer.

The message to block is specified by PGN, destination source address and a part of the first eight data bytes.

To revert this command you can use GBT27930IL_ResetBlockedRxMessage or GBT27930IL_ResetAllBlockedTxMessages.

## Return Values

0: Manipulation is set successfully

## Example

```c
—
```

## Availability

| Since Version |
|---|
