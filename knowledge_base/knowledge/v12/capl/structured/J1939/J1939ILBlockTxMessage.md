# J1939ILBlockTxMessage

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939ILBlockTxMessage(dword pgn, dword destinationAddress, qword filterMask, qword filterValue); // form 1
```

## Description

Prevents transmitting of a message generated and sent by the interaction layer.

The message to block is specified by PGN, destination address and a part of the first eight data bytes.

To revert this command you can use J1939ILResetBlockedTxMessage or J1939ILResetAllBlockedTxMessages.

## Return Values

0: Manipulation is set successfully

## Example

```c
—
```

## Availability

| Since Version |
|---|
