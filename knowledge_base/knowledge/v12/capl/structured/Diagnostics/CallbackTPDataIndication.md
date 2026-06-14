# CallbackTPDataIndication

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long CallbackTPDataIndication( dword timeStart, dword timeFinish, WORD channel, dword CanIdTx, dword additionalTx, dword CanIdRx, BYTE data[], char source[], char target[])
```

## Description

Indicates the transmission of an ISO TP data packet on a CAN channel where the ISO TP Observer is configured to supervise the communication.

## Return Values

1: Forward the event further down the measurement branch.

## Availability

| Since Version |
|---|
