# Iso11783TxAbort

> Category: `ISO11783` | Type: `function`

## Syntax

```c
dword Iso11783TxAbort( dword ecuHandle, dword pgn );
```

## Description

Interrupt of a transfer that has previously been started with Iso11783TxReqPG(). Please note in this regard that for technical reasons, it is only possible to interrupt PGs that are fragmented.

## Return Values

0 on success or error code

## Example

```c
Iso11783TxAbort(ecuHdl, 
 0xFE09)
```

## Availability

| Since Version |
|---|
