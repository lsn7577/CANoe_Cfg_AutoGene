# Iso11783IL_BlockRxMessage

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_BlockRxMessage(dword pgn, dword sourceAddress, qword filterMask, qword filterValue); // form 1
```

## Description

Prevents processing of a received message by the interaction layer.

The message to block is specified by PGN, destination source address and a part of the first eight data bytes.

To revert this command you can use Iso11783IL_ResetBlockedRxMessage or Iso11783IL_ResetAllBlockedRxMessages.

## Return Values

0: Manipulation is set successfully

## Example

```c
—
```

## Availability

| Since Version |
|---|
