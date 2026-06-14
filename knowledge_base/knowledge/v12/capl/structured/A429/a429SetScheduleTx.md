# a429SetScheduleTx

> Category: `A429` | Type: `function`

## Syntax

```c
dword a429SetScheduleTx( a429word myA429word, dword myCycle );
```

## Description

Prepare an ARINC word to be transmitted cyclically by means of the hardware scheduling support. Calling this function modifies the selectors TxCycle and TxCtrl.

Note: This modifies the ARINC word attributes only. For transmission call the function output.

## Availability

| Since Version |
|---|
