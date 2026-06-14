# GBT27930IL_ResetDelayedRxMessage

> Category: `J1939` | Type: `function`

## Syntax

```c
long GBT27930IL_ResetDelayedRxMessage(dword pgn, dword sourceAddress, qword filterMask, qword filterValue, dword behavior); // form 1
```

## Description

Resets the change of a single GBT27930IL_DelayRxMessage call. The corresponding message is specified by PGN, source address, destination address and a part of the first eight data bytes.

## Return Values

0: Function has been executed successfully

## Example

```c
—
```

## Availability

| Since Version |
|---|
