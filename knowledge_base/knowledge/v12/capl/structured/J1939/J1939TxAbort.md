# J1939TxAbort

> Category: `J1939` | Type: `function`

## Syntax

```c
dword J1939TxAbort( dword ecuHandle, dword pgn );
```

## Description

Interrupt of a transfer that has previously been started with J1939TxReqPG(). Please note in this regard that for technical reasons, it is only possible to interrupt PGs that are fragmented.

## Return Values

0 on success or error code

## Example

```c
J1939TxAbort(ecuHdl, 
 0xFE09)
```

## Availability

| Since Version |
|---|
