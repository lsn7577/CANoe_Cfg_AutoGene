# output (A429)

> Category: `A429` | Type: `function`

## Syntax

```c
void output( a429word myA429Word );
```

## Description

This function triggers the transfer of the myA429Word to the network hardware interface. When the mode Simulated bus is used a built-in simulation layer takes care of the ARINC word.

Note that the transmission behavior may be adjusted via the ARINC word selectors TxCtrl, gap and TxCycle. If TxCtrl is already set to the value 1, the function updates the ARINC word in the hardware scheduler.

For transferring multiple ARINC words in one call, use the function a429Transmit.

## Availability

| Since Version |
|---|
