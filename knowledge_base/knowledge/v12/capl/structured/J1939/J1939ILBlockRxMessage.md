# J1939ILBlockRxMessage

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939ILBlockRxMessage(dword pgn, dword sourceAddress, qword filterMask, qword filterValue); // form 1
```

## Description

Prevents processing of a received message by the interaction layer.

The message to block is specified by PGN, destination source address and a part of the first eight data bytes.

To revert this command you can use J1939ILResetBlockedRxMessage or J1939ILResetAllBlockedRxMessages.

## Return Values

0: Manipulation is set successfully

## Example

```c
—
```

## Availability

| Since Version |
|---|
