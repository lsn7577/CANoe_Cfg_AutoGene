# Iso11783IL_BlockTxMessage

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_BlockTxMessage(dword pgn, dword destinationAddress, qword filterMask, qword filterValue); // form 1
```

## Description

Prevents transmitting of a message generated and sent by the interaction layer.

The message to block is specified by PGN, destination address and a part of the first eight data bytes.

To revert this command you can use Iso11783IL_ResetBlockedTxMessage or Iso11783IL_ResetAllBlockedTxMessages.

## Return Values

0: Manipulation is set successfully

## Example

```c
—
```

## Availability

| Since Version |
|---|
