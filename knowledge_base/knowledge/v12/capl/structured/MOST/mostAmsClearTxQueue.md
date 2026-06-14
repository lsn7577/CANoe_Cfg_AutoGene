# mostAmsClearTxQueue

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostAmsClearTxQueue(long channel)
```

## Description

Clears all entries in the AMS send buffer.

This command can be used to stop further sending of AMS messages in case of errors (e.g. critical unlock or light off) or if the system state changes to "NotOk".

## Return Values

<= 0: See error codes

## Availability

| Since Version |
|---|
